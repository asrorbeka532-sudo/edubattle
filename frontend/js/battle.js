// ========================================================
// EDUBATTLE - REAL-TIME ONLINE BATTLE ENGINE
// 1v1 (Bepul) & 3-5 Kishilik (PRO) Batl Tizimi
// ========================================================

const battleState = {
  socket: null,
  roomCode: null,
  mode: '1v1',
  maxPlayers: 2,
  questionCount: 5,
  isHost: false,
  myPlayerKey: null,
  currentQuestion: null,
  currentQIndex: 0,
  totalQuestions: 5,
  timerInterval: null,
  timeLeft: 15,
  hasAnsweredCurrent: false,
  roomPlayers: []
};

// ----------------- QUESTION COUNT SELECTOR -----------------
function selectBattleQuestionCount(count) {
  playSound('click');
  battleState.questionCount = parseInt(count) || 5;
  ['5', '15', '30'].forEach(c => {
    const el = document.getElementById(`qCount${c}Btn`);
    if (el) {
      if (parseInt(c) === battleState.questionCount) {
        el.classList.add('selected');
      } else {
        el.classList.remove('selected');
      }
    }
  });
}

// ----------------- MODE SELECTOR -----------------
function selectBattleMode(mode) {
  playSound('click');
  const card1v1 = document.getElementById('mode1v1Card');
  const cardPro = document.getElementById('modeProCard');
  const proSlider = document.getElementById('proPlayerCountBox');

  if (mode === 'pro_3_5') {
    // Check if user is PRO
    if (!state.currentUser || !state.currentUser.is_pro) {
      const pText = window.edubattleProPrice ? `${Number(window.edubattleProPrice).toLocaleString()} so'mlik ` : "";
      if (confirm(`⚡ 3-5 kishilik batllar faqat PRO obunachilar uchun! Hozir ${pText}PRO tarifiga ulanasizmi?`)) {
        openPaymentModal('student_pro');
      }
      return;
    }
    battleState.mode = 'pro_3_5';
    battleState.maxPlayers = parseInt(document.getElementById('proPlayerRange').value) || 4;
    card1v1.classList.remove('selected');
    cardPro.classList.add('selected');
    proSlider.style.display = 'block';
  } else {
    battleState.mode = '1v1';
    battleState.maxPlayers = 2;
    cardPro.classList.remove('selected');
    card1v1.classList.add('selected');
    proSlider.style.display = 'none';
  }
}

function updateProPlayerCount(val) {
  battleState.maxPlayers = parseInt(val);
  document.getElementById('proPlayerCountLabel').textContent = `${val} kishi`;
}

// ----------------- ROOM CREATION & JOINING -----------------
async function createBattleRoom() {
  playSound('click');
  const user = state.currentUser;
  if (!user) {
    alert("Iltimos, avval tizimga kiring!");
    openAuthModal();
    return;
  }

  const subjectId = parseInt(document.getElementById('battleSubjectSelect').value) || 1;

  try {
    const res = await fetch('/api/battle/create-room', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        host_id: user.id,
        host_name: user.full_name,
        subject_id: subjectId,
        mode: battleState.mode,
        max_players: battleState.maxPlayers,
        question_count: battleState.questionCount || 5
      })
    });
    const data = await res.json();
    if (data.success) {
      battleState.isHost = true;
      connectToBattleWebSocket(data.room_code);
    }
  } catch (e) {
    alert("Xona yaratishda xatolik yuz berdi!");
  }
}

function promptJoinRoom() {
  playSound('click');
  const user = state.currentUser;
  if (!user) {
    alert("Iltimos, avval tizimga kiring!");
    openAuthModal();
    return;
  }

  const code = prompt("Do'stingiz yoki o'qituvchingiz yuborgan Xona Kodini kiriting (Masalan: BATL1234):");
  if (code && code.trim()) {
    battleState.isHost = false;
    connectToBattleWebSocket(code.trim().toUpperCase());
  }
}

// ----------------- WEBSOCKET CONNECTION -----------------
function connectToBattleWebSocket(roomCode) {
  battleState.roomCode = roomCode;

  const proto = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
  const wsUrl = `${proto}//${window.location.host}/ws/battle/${roomCode}`;

  if (battleState.socket) {
    battleState.socket.close();
  }

  const ws = new WebSocket(wsUrl);
  battleState.socket = ws;

  ws.onopen = () => {
    const user = state.currentUser;
    ws.send(JSON.stringify({
      action: 'join',
      user_id: user.id,
      name: user.full_name,
      is_pro: Boolean(user.is_pro),
      avatar: user.avatar
    }));
  };

  ws.onmessage = (event) => {
    try {
      const msg = JSON.parse(event.data);
      handleBattleMessage(msg);
    } catch (e) {}
  };

  ws.onerror = () => {
    alert("Batl serveriga ulanishda xatolik yuz berdi!");
  };
}

function handleBattleMessage(msg) {
  if (msg.type === 'error') {
    alert(msg.message);
    resetBattleLobby();
    return;
  }

  if (msg.type === 'room_state') {
    battleState.roomPlayers = msg.players;
    battleState.maxPlayers = msg.max_players;
    renderWaitingRoom(msg);
  } else if (msg.type === 'question') {
    renderActiveQuestion(msg);
  } else if (msg.type === 'round_result') {
    showRoundResult(msg);
  } else if (msg.type === 'game_over') {
    showGameOver(msg);
  } else if (msg.type === 'reaction') {
    showFloatingReaction(msg);
  }
}

// ----------------- WAITING ROOM -----------------
function renderWaitingRoom(data) {
  document.getElementById('battleLobbyScreen').style.display = 'none';
  document.getElementById('battleActiveStage').style.display = 'none';
  document.getElementById('battleGameOverStage').style.display = 'none';
  document.getElementById('battleWaitingScreen').style.display = 'block';

  document.getElementById('waitingRoomCode').textContent = data.room_code;
  const qCount = data.question_count || battleState.questionCount || 5;
  document.getElementById('waitingRoomBadge').textContent = data.mode === 'pro_3_5' 
    ? `PRO BATL (${data.max_players} KISHILIK • ${qCount} TA TEST)` 
    : `1v1 DUEL (${qCount} TA TEST)`;

  const arena = document.getElementById('waitingPlayersArena');
  arena.innerHTML = '';

  for (let i = 0; i < data.max_players; i++) {
    const player = data.players[i];
    const slot = document.createElement('div');
    slot.className = 'player-slot-clean';

    if (player) {
      slot.id = `waitingSlot_${player.id || player.key}`;
      slot.innerHTML = `
        <div class="player-slot-avatar ${player.is_pro ? 'pro-player' : ''}" style="position:relative;">
          ${player.is_bot ? '🤖' : (player.avatar && player.avatar.includes('teacher') ? '👨‍🏫' : '👨‍🎓')}
        </div>
        <div style="font-size:11px; font-weight:700; color:var(--text-primary); overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${player.name}</div>
        <div style="font-size:10px; color:var(--accent-green); font-weight:600;">Tayyor</div>
      `;
    } else {
      slot.innerHTML = `
        <div class="player-slot-avatar" style="border-style:dashed; color:var(--text-muted);">+</div>
        <div style="font-size:10px; color:var(--text-muted);">Kutilmoqda</div>
      `;
    }
    arena.appendChild(slot);
  }

  const startBtn = document.getElementById('startBattleBtn');
  startBtn.disabled = !data.can_start;
}

function startBattleGame() {
  playSound('click');
  if (battleState.socket && battleState.socket.readyState === WebSocket.OPEN) {
    battleState.socket.send(JSON.stringify({ action: 'start' }));
  }
}

// ----------------- ACTIVE QUESTION -----------------
function renderActiveQuestion(msg) {
  document.getElementById('battleWaitingScreen').style.display = 'none';
  document.getElementById('battleActiveStage').style.display = 'block';

  battleState.currentQuestion = msg.question;
  battleState.currentQIndex = msg.current_index;
  battleState.totalQuestions = msg.total;
  battleState.hasAnsweredCurrent = false;

  document.getElementById('battleQCounter').textContent = `${msg.current_index + 1} / ${msg.total}`;
  document.getElementById('battleQuestionText').textContent = msg.question.question_text;

  const list = document.getElementById('battleOptionsList');
  const letters = ['A', 'B', 'C', 'D'];
  list.innerHTML = (msg.question.options || []).map((opt, idx) => `
    <button class="quiz-option-btn" id="bOpt_${idx}" onclick="submitBattleAnswer(${idx})">
      <span style="color:var(--accent-red); font-weight:800; font-size:14px;">${letters[idx]})</span>
      <span style="flex:1;">${opt}</span>
    </button>
  `).join('');

  updateLiveStandingsBar(msg.leaderboard);
  startRoundTimer(msg.question.time_limit || 15);
}

function startRoundTimer(seconds) {
  if (battleState.timerInterval) clearInterval(battleState.timerInterval);
  battleState.timeLeft = seconds;
  const timerBox = document.getElementById('battleTimerBox');
  timerBox.textContent = battleState.timeLeft;

  battleState.timerInterval = setInterval(() => {
    battleState.timeLeft -= 1;
    timerBox.textContent = Math.max(0, battleState.timeLeft);

    if (battleState.timeLeft <= 5) {
      playSound('tick');
      timerBox.style.borderColor = 'var(--accent-red)';
    }

    if (battleState.timeLeft <= 0) {
      clearInterval(battleState.timerInterval);
      if (!battleState.hasAnsweredCurrent) {
        submitBattleAnswer(-1);
      }
    }
  }, 1000);
}

function submitBattleAnswer(chosenIdx) {
  if (battleState.hasAnsweredCurrent) return;
  battleState.hasAnsweredCurrent = true;

  if (battleState.timerInterval) clearInterval(battleState.timerInterval);

  if (chosenIdx >= 0) {
    const selectedBtn = document.getElementById(`bOpt_${chosenIdx}`);
    if (selectedBtn) selectedBtn.style.borderColor = 'var(--accent-red)';
    playSound('click');
  }

  document.querySelectorAll('.quiz-option-btn').forEach(b => b.disabled = true);

  if (battleState.socket && battleState.socket.readyState === WebSocket.OPEN) {
    battleState.socket.send(JSON.stringify({
      action: 'answer',
      question_index: battleState.currentQIndex,
      selected_option: chosenIdx,
      time_left: battleState.timeLeft
    }));
  }
}

function showRoundResult(msg) {
  if (battleState.timerInterval) clearInterval(battleState.timerInterval);

  const correctIdx = msg.correct_index;
  document.querySelectorAll('.quiz-option-btn').forEach((btn, idx) => {
    if (idx === correctIdx) {
      btn.classList.add('correct');
    } else {
      btn.classList.add('wrong');
    }
  });

  updateLiveStandingsBar(msg.leaderboard);
}

function updateLiveStandingsBar(standings) {
  const container = document.getElementById('battleLiveStandings');
  if (!container || !standings) return;

  container.innerHTML = standings.map(p => `
    <div style="font-size:11px; display:flex; align-items:center; gap:4px; position:relative;" id="standingPlayer_${p.id || p.key}" class="live-standing-player">
      <span class="standing-avatar-box" style="position:relative;">${p.is_bot ? '🤖' : '👨‍🎓'}</span>
      <span style="font-weight:700;">${p.name.split(' ')[0]}</span>
      <span style="color:var(--accent-green); font-weight:800;">${p.score}</span>
    </div>
  `).join('');

  const me = standings.find(p => p.id === state.currentUser?.id);
  if (me) {
    document.getElementById('battleMyScore').textContent = me.score;
  }
}

function showGameOver(msg) {
  if (battleState.timerInterval) clearInterval(battleState.timerInterval);

  document.getElementById('battleActiveStage').style.display = 'none';
  document.getElementById('battleGameOverStage').style.display = 'block';

  playSound('victory');

  const winner = msg.winner;
  const standings = msg.standings || [];

  const isMeWinner = (winner && state.currentUser && winner.id === state.currentUser.id);
  document.getElementById('winnerTitle').textContent = isMeWinner ? '🎉 Siz G\'olibsiz!' : `🏆 G'olib: ${winner ? winner.name : 'Durang'}`;
  document.getElementById('winnerSubtitle').textContent = isMeWinner ? 'Qoyilmaqom bellashuv! +50 🪙 Tanga hisobingizga qo\'shildi.' : 'Yaxshi bellashuv bo\'ldi.';

  const listEl = document.getElementById('finalStandingsList');
  listEl.innerHTML = standings.map((p, idx) => `
    <div style="display:flex; align-items:center; justify-content:space-between; padding:8px 10px; border-radius:6px; background:var(--bg-card); border:1px solid var(--border-card); margin-bottom:6px;">
      <div style="display:flex; align-items:center; gap:8px;">
        <span style="font-size:12px; font-weight:800; color:${idx === 0 ? 'var(--accent-green)' : 'var(--text-muted)'}; width:16px;">#${idx+1}</span>
        <div>
          <div style="font-size:13px; font-weight:700; color:var(--text-primary);">${p.name}</div>
          <div style="font-size:10px; color:var(--text-muted);">${p.is_pro ? 'PRO' : 'Standart'}</div>
        </div>
      </div>
      <div style="font-size:14px; font-weight:800; color:var(--accent-green);">${p.score} ball</div>
    </div>
  `).join('');

  refreshCurrentUserData();
}

// ================= BATTLE EMOTION STICKERS SYSTEM =================

const BATTLE_STICKER_CATALOG = {
  fire: [
    { emoji: "🔥", text: "Yonamiz!", type: "fire" },
    { emoji: "🚀", text: "Kosmos!", type: "fire" },
    { emoji: "⚡", text: "Tezkor!", type: "fire" },
    { emoji: "💥", text: "Bomba!", type: "fire" },
    { emoji: "🎯", text: "Aniq nishon!", type: "fire" },
    { emoji: "🌪️", text: "Shiddatli!", type: "fire" }
  ],
  flex: [
    { emoji: "😎", text: "Oson ekan!", type: "flex" },
    { emoji: "🧠", text: "Katta miya!", type: "flex" },
    { emoji: "👑", text: "Qirol!", type: "flex" },
    { emoji: "🦾", text: "Yengilmas!", type: "flex" },
    { emoji: "🥇", text: "1-o'rin!", type: "flex" },
    { emoji: "🏆", text: "Chempion!", type: "flex" }
  ],
  shock: [
    { emoji: "🤯", text: "Miya portladi!", type: "shock" },
    { emoji: "😱", text: "Adashdim-ku!", type: "shock" },
    { emoji: "⏳", text: "Vaqt yetmadi!", type: "shock" },
    { emoji: "🥶", text: "Qotib qoldim!", type: "shock" },
    { emoji: "😭", text: "Eh attang!", type: "shock" },
    { emoji: "🤦‍♂️", text: "Qanday qilib?!", type: "shock" }
  ],
  fun: [
    { emoji: "😂", text: "Voydod!", type: "fun" },
    { emoji: "😜", text: "Yetib ol-chi!", type: "fun" },
    { emoji: "🤡", text: "Voybo'o'!", type: "fun" },
    { emoji: "🥳", text: "Bayram!", type: "fun" },
    { emoji: "🍿", text: "Kuzataman!", type: "fun" },
    { emoji: "🤭", text: "Sir bo'lsin!", type: "fun" }
  ],
  friend: [
    { emoji: "👏", text: "Barakalla!", type: "friend" },
    { emoji: "🤝", text: "Zo'r o'yin!", type: "friend" },
    { emoji: "💪", text: "Bo'sh kelma!", type: "friend" },
    { emoji: "🫡", text: "Hurmat!", type: "friend" },
    { emoji: "🙌", text: "Rahmat!", type: "friend" },
    { emoji: "⭐", text: "Yulduzsan!", type: "friend" }
  ]
};

let currentStickerCategory = 'fire';
let lastStickerSentTimestamp = 0;

function openBattleStickerDrawer() {
  playSound('pop');
  const modal = document.getElementById('battleStickerModal');
  if (modal) {
    modal.classList.add('active');
    renderBattleStickers(currentStickerCategory);
  }
}

function closeBattleStickerDrawer() {
  const modal = document.getElementById('battleStickerModal');
  if (modal) {
    modal.classList.remove('active');
  }
}

function switchStickerTab(category) {
  playSound('click');
  currentStickerCategory = category;
  document.querySelectorAll('.sticker-tab-btn').forEach(btn => btn.classList.remove('active'));
  const activeBtn = document.getElementById(`stTab_${category}`);
  if (activeBtn) activeBtn.classList.add('active');
  renderBattleStickers(category);
}

function renderBattleStickers(category) {
  const container = document.getElementById('battleStickersGrid');
  if (!container) return;

  const stickers = BATTLE_STICKER_CATALOG[category] || BATTLE_STICKER_CATALOG.fire;
  container.innerHTML = stickers.map(s => `
    <div class="sticker-choice-card" onclick="sendBattleSticker('${s.emoji}', '${s.text}', '${s.type}')">
      <div class="emoji">${s.emoji}</div>
      <div class="label">${s.text}</div>
    </div>
  `).join('');
}

function sendBattleSticker(emoji, text, stickerType = 'fire') {
  const now = Date.now();
  // Anti-spam debounce: 0.7s
  if (now - lastStickerSentTimestamp < 700) {
    return;
  }
  lastStickerSentTimestamp = now;

  playSound('pop');

  if (battleState.socket && battleState.socket.readyState === WebSocket.OPEN) {
    battleState.socket.send(JSON.stringify({
      action: 'reaction',
      emoji: emoji,
      text: text || '',
      sticker_type: stickerType
    }));
  }

  closeBattleStickerDrawer();
}

function sendReaction(emoji) {
  sendBattleSticker(emoji, '', 'fire');
}

function showFloatingReaction(data) {
  let senderName = 'O\'yinchi';
  let emoji = '🔥';
  let text = '';
  let stickerType = 'fire';
  let senderId = null;
  let senderKey = null;

  if (typeof data === 'string') {
    senderName = data;
    emoji = arguments[1] || '🔥';
  } else if (data && typeof data === 'object') {
    senderName = data.sender || 'O\'yinchi';
    emoji = data.emoji || '🔥';
    text = data.text || '';
    stickerType = data.sticker_type || 'fire';
    senderId = data.sender_id;
    senderKey = data.sender_key;
  }

  // Play audio feedback
  try {
    playSound('pop');
  } catch (e) {}

  // 1. Render floating reaction bubble into the overlay
  let overlay = document.getElementById('battleFloatingStickersOverlay');
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.id = 'battleFloatingStickersOverlay';
    overlay.className = 'battle-floating-overlay';
    document.body.appendChild(overlay);
  }

  const floater = document.createElement('div');
  floater.className = `floating-sticker-item ${stickerType}`;

  // Random horizontal slight drift around center
  const offset = (Math.random() * 80 - 40); // -40px to +40px
  floater.style.left = `calc(50% + ${offset}px)`;
  floater.style.bottom = `${160 + Math.floor(Math.random() * 40)}px`;

  floater.innerHTML = `
    <div class="floating-sticker-emoji">${emoji}</div>
    <div class="floating-sticker-meta">
      <div class="floating-sticker-sender">${escapeHtml(senderName)}</div>
      <div class="floating-sticker-text">${escapeHtml(text || emoji)}</div>
    </div>
  `;

  overlay.appendChild(floater);
  setTimeout(() => {
    floater.remove();
  }, 2600);

  // 2. Also show reaction badge directly over player's avatar in scoreboard / waiting room
  const targetElement = (senderId && document.getElementById(`standingPlayer_${senderId}`)) ||
                        (senderKey && document.getElementById(`standingPlayer_${senderKey}`)) ||
                        (senderId && document.getElementById(`waitingSlot_${senderId}`)) ||
                        (senderKey && document.getElementById(`waitingSlot_${senderKey}`));

  if (targetElement) {
    const avatarBadge = document.createElement('div');
    avatarBadge.className = 'avatar-reaction-badge';
    avatarBadge.textContent = emoji;
    targetElement.appendChild(avatarBadge);
    setTimeout(() => avatarBadge.remove(), 2200);
  }
}

function resetBattleLobby() {
  if (battleState.socket) {
    battleState.socket.close();
    battleState.socket = null;
  }
  closeBattleStickerDrawer();
  document.getElementById('battleGameOverStage').style.display = 'none';
  document.getElementById('battleActiveStage').style.display = 'none';
  document.getElementById('battleWaitingScreen').style.display = 'none';
  document.getElementById('battleLobbyScreen').style.display = 'block';
}
