// ========================================================
// EDUBATTLE - MENING TESTLARIM VA MAXSUS TEST BATLLARI
// Foydalanuvchilar o'zlari test tuzishi, login-parol qo'yishi
// va shu login-parol orqali Batl qilishi uchun modul
// ========================================================

let myQuizQuestions = [];

async function loadMyQuizzesList() {
  const container = document.getElementById('myQuizzesListContainer');
  if (!container) return;

  const user = state.currentUser;
  if (!user) {
    container.innerHTML = `
      <div style="text-align:center; padding:32px 16px; color:var(--text-muted);">
        <p style="font-size:13px; margin-bottom:12px;">Testlaringizni ko'rish va yangi test tuzish uchun tizimga kiring.</p>
        <button class="btn btn-red btn-sm" onclick="openAuthModal()">Kirish / Ro'yxatdan o'tish</button>
      </div>
    `;
    return;
  }

  container.innerHTML = '<div style="text-align:center; padding:24px; color:var(--text-muted); font-size:12px;">Testlar yuklanmoqda...</div>';

  try {
    const res = await fetch(`/api/my-quizzes?user_id=${user.id}`);
    const quizzes = await res.json();

    if (!Array.isArray(quizzes) || quizzes.length === 0) {
      container.innerHTML = `
        <div class="minimal-card" style="text-align:center; padding:32px 16px; border:1px dashed var(--border-subtle);">
          <div style="font-size:32px; margin-bottom:8px;">📝</div>
          <h4 style="font-size:14px; font-weight:800; color:var(--text-primary);">Hozircha testlaringiz yo'q</h4>
          <p style="font-size:11px; color:var(--text-muted); margin:4px 0 16px;">
            O'zingiz xohlagan fandan test tuzing, maxsus login va parol o'rnating va do'stlaringiz bilan batl qiling!
          </p>
          <button class="btn btn-red btn-sm" onclick="openCreateMyQuizModal()">➕ Birinchi Testni Tuzish</button>
        </div>
      `;
      return;
    }

    container.innerHTML = quizzes.map(q => {
      const qDate = q.created_at ? q.created_at.substring(0, 10) : '';
      return `
        <div class="minimal-card highlight-purple" style="position:relative; padding:14px;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:8px;">
            <div style="min-width:0; flex:1;">
              <div style="display:flex; align-items:center; gap:6px; flex-wrap:wrap;">
                <span class="tag tag-subtle" style="font-size:10px;">${escapeHtml(q.subject_icon || '📚')} ${escapeHtml(q.subject_name || 'Fan')}</span>
                <span class="tag tag-green" style="font-size:10px;">${q.question_count} ta savol</span>
              </div>
              <h4 style="font-size:14px; font-weight:800; color:var(--text-primary); margin:8px 0 4px; overflow:hidden; text-overflow:ellipsis;">
                ${escapeHtml(q.title)}
              </h4>
              <div style="font-size:10px; color:var(--text-muted);">${qDate}</div>
            </div>
            <button onclick="deleteMyCustomQuiz(${q.id})" class="btn btn-outline btn-sm" style="color:#ef4444; border-color:rgba(239,68,68,0.25); padding:4px 8px;" title="Testni o'chirish">
              🗑️
            </button>
          </div>

          <!-- Credentials Box -->
          <div style="margin:10px 0; padding:8px 12px; background:rgba(0,0,0,0.3); border-radius:10px; border:1px solid rgba(168,85,247,0.3); display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
            <div style="display:flex; align-items:center; gap:12px; font-family:monospace; font-size:12px;">
              <div>
                <span style="color:var(--text-muted); font-size:10px; display:block;">LOGIN:</span>
                <b style="color:#a855f7; font-size:13px; letter-spacing:1px;">${escapeHtml(q.login)}</b>
              </div>
              <div style="width:1px; height:24px; background:rgba(255,255,255,0.1);"></div>
              <div>
                <span style="color:var(--text-muted); font-size:10px; display:block;">PAROL:</span>
                <b style="color:#10b981; font-size:13px; letter-spacing:1px;">${escapeHtml(q.passcode)}</b>
              </div>
            </div>

            <button onclick="copyCustomQuizCredentials('${escapeHtml(q.login)}', '${escapeHtml(q.passcode)}')" class="btn btn-outline btn-sm" style="font-size:11px; padding:4px 10px;">
              📋 Nusxalash
            </button>
          </div>

          <!-- Action buttons -->
          <div style="display:grid; grid-template-columns: 1fr; gap:6px; margin-top:8px;">
            <button onclick="launchBattleWithCustomQuiz('${escapeHtml(q.login)}', '${escapeHtml(q.passcode)}')" class="btn btn-purple btn-sm" style="font-weight:800; font-size:12px;">
              ⚔️ Ushbu Test Bilan Batl Boshlash ➜
            </button>
          </div>
        </div>
      `;
    }).join('');
  } catch (err) {
    console.error("loadMyQuizzesList error:", err);
    container.innerHTML = '<div style="text-align:center; padding:24px; color:#ef4444; font-size:12px;">Testlarni yuklashda xatolik yuz berdi.</div>';
  }
}

function copyCustomQuizCredentials(login, passcode) {
  playSound('click');
  const textToCopy = `🏆 EduBattle maxsus test to'plami:\n🔑 Test Logini: ${login}\n🔒 Test Paroli: ${passcode}\n\nEduBattle ilovasida Batl bo'limiga kiring va "🔑 Test Kodi Bilan Batl" tugmasini bosib, birga bellashing!`;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(textToCopy).then(() => {
      alert("✅ Test login va paroli nusxalandi! Do'stlaringizga yuboring.");
    }).catch(() => {
      prompt("Nusxalash uchun Ctrl+C bosing:", textToCopy);
    });
  } else {
    prompt("Nusxalash uchun Ctrl+C bosing:", textToCopy);
  }
}

async function deleteMyCustomQuiz(quizId) {
  if (!confirm("Haqiqatan ham ushbu test to'plamini o'chirmoqchimisiz?")) return;
  playSound('click');
  const user = state.currentUser;
  if (!user) return;

  try {
    const res = await fetch(`/api/my-quizzes/${quizId}?user_id=${user.id}`, { method: 'DELETE' });
    const data = await res.json();
    if (data.ok) {
      loadMyQuizzesList();
    } else {
      alert(data.detail || "O'chirishda xatolik");
    }
  } catch (e) {
    alert("Xatolik yuz berdi");
  }
}

// ----------------- TEST YARATISH FORMASI -----------------
function openCreateMyQuizModal() {
  playSound('click');
  const user = state.currentUser;
  if (!user) {
    alert("Iltimos, avval tizimga kiring!");
    openAuthModal();
    return;
  }

  // Populate subject select
  const subSelect = document.getElementById('myQuizSubjectSelect');
  if (subSelect && window.subjectsData) {
    subSelect.innerHTML = window.subjectsData.map(s => `
      <option value="${s.id}">${s.icon || '📚'} ${s.name}</option>
    `).join('');
  }

  document.getElementById('myQuizTitleInput').value = '';
  document.getElementById('myQuizLoginInput').value = `TEST-${Math.floor(1000 + Math.random() * 9000)}`;
  document.getElementById('myQuizPasscodeInput').value = `${Math.floor(1000 + Math.random() * 9000)}`;

  // Initialize with 3 questions
  myQuizQuestions = [
    { question_text: '', options: ['', '', '', ''], correct_index: 0 },
    { question_text: '', options: ['', '', '', ''], correct_index: 0 },
    { question_text: '', options: ['', '', '', ''], correct_index: 0 }
  ];
  renderMyQuizQuestionsBuilder();

  const modal = document.getElementById('createMyQuizModal');
  if (modal) modal.style.display = 'flex';
}

function closeCreateMyQuizModal() {
  const modal = document.getElementById('createMyQuizModal');
  if (modal) modal.style.display = 'none';
}

function renderMyQuizQuestionsBuilder() {
  const container = document.getElementById('myQuizQuestionsBuilder');
  if (!container) return;

  container.innerHTML = myQuizQuestions.map((q, qIdx) => `
    <div class="minimal-card" style="padding:12px; border:1px solid rgba(255,255,255,0.08); background:rgba(0,0,0,0.2);">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
        <span style="font-size:12px; font-weight:800; color:var(--accent-red);">Savol #${qIdx + 1}</span>
        ${myQuizQuestions.length > 1 ? `
          <button type="button" onclick="removeMyQuizQuestion(${qIdx})" class="btn btn-outline btn-sm" style="color:#ef4444; border-color:transparent; padding:2px 6px; font-size:11px;">
            ❌ O'chirish
          </button>
        ` : ''}
      </div>

      <textarea id="myq_text_${qIdx}" class="input-field" rows="2" placeholder="Savol matnini kiriting..." style="margin-bottom:8px; font-size:12px;" oninput="updateMyQuizQText(${qIdx}, this.value)">${escapeHtml(q.question_text || '')}</textarea>

      <div style="font-size:11px; font-weight:700; color:var(--text-muted); margin-bottom:6px;">Variantlar va to'g'ri javobni tanlang:</div>
      <div style="display:flex; flex-direction:column; gap:6px;">
        ${['A', 'B', 'C', 'D'].map((optLetter, optIdx) => `
          <div style="display:flex; align-items:center; gap:8px;">
            <input type="radio" name="myq_correct_${qIdx}" value="${optIdx}" ${q.correct_index === optIdx ? 'checked' : ''} onchange="setMyQuizCorrectOption(${qIdx}, ${optIdx})" style="cursor:pointer; accent-color:#10b981; width:16px; height:16px;">
            <span style="font-size:12px; font-weight:800; color:var(--text-muted); width:14px;">${optLetter}</span>
            <input type="text" class="input-field" placeholder="${optLetter} varianti" value="${escapeHtml(q.options[optIdx] || '')}" oninput="updateMyQuizOption(${qIdx}, ${optIdx}, this.value)" style="margin-bottom:0; font-size:12px; padding:6px 10px;">
          </div>
        `).join('')}
      </div>
    </div>
  `).join('');
}

function updateMyQuizQText(qIdx, val) {
  if (myQuizQuestions[qIdx]) myQuizQuestions[qIdx].question_text = val;
}

function updateMyQuizOption(qIdx, optIdx, val) {
  if (myQuizQuestions[qIdx] && myQuizQuestions[qIdx].options) {
    myQuizQuestions[qIdx].options[optIdx] = val;
  }
}

function setMyQuizCorrectOption(qIdx, optIdx) {
  if (myQuizQuestions[qIdx]) myQuizQuestions[qIdx].correct_index = parseInt(optIdx);
}

function addMyQuizQuestionField() {
  playSound('click');
  myQuizQuestions.push({ question_text: '', options: ['', '', '', ''], correct_index: 0 });
  renderMyQuizQuestionsBuilder();
}

function removeMyQuizQuestion(qIdx) {
  playSound('click');
  if (myQuizQuestions.length <= 1) return;
  myQuizQuestions.splice(qIdx, 1);
  renderMyQuizQuestionsBuilder();
}

async function saveMyQuiz() {
  playSound('click');
  const user = state.currentUser;
  if (!user) {
    alert("Iltimos, avval tizimga kiring!");
    return;
  }

  const subjectId = parseInt(document.getElementById('myQuizSubjectSelect')?.value) || 1;
  const title = (document.getElementById('myQuizTitleInput')?.value || '').trim();
  const login = (document.getElementById('myQuizLoginInput')?.value || '').trim();
  const passcode = (document.getElementById('myQuizPasscodeInput')?.value || '').trim();

  if (!title) {
    alert("Iltimos, test to'plami nomini kiriting!");
    return;
  }
  if (!login) {
    alert("Iltimos, test loginini kiriting!");
    return;
  }
  if (!passcode) {
    alert("Iltimos, test parolini kiriting!");
    return;
  }

  // Validate questions
  const validQuestions = [];
  for (let i = 0; i < myQuizQuestions.length; i++) {
    const q = myQuizQuestions[i];
    const text = (q.question_text || '').trim();
    const opts = (q.options || []).map(o => (o || '').trim()).filter(Boolean);
    if (!text || opts.length < 2) continue;
    validQuestions.push({
      question_text: text,
      options: q.options.map(o => (o || '').trim()),
      correct_index: q.correct_index || 0
    });
  }

  if (validQuestions.length === 0) {
    alert("Kamida bitta to'liq to'ldirilgan test savolini kiriting!");
    return;
  }

  try {
    const res = await fetch('/api/my-quizzes/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: user.id,
        subject_id: subjectId,
        title: title,
        login: login,
        passcode: passcode,
        questions: validQuestions
      })
    });
    const data = await res.json();
    if (data.ok) {
      alert(`✅ Test to'plami muvaffaqiyatli saqlandi!\nLogin: ${data.login}\nParol: ${data.passcode}`);
      closeCreateMyQuizModal();
      loadMyQuizzesList();
    } else {
      alert(data.detail || "Saqlashda xatolik yuz berdi");
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik yuz berdi");
  }
}

// ----------------- MAXSUS TEST BILAN BATL OCHISH & QO'SHILISH -----------------
function promptCustomQuizBattle() {
  playSound('click');
  const modal = document.getElementById('customQuizBattleModal');
  if (modal) {
    document.getElementById('cqbLoginInput').value = '';
    document.getElementById('cqbPasscodeInput').value = '';
    modal.style.display = 'flex';
  }
}

function closeCustomQuizBattleModal() {
  const modal = document.getElementById('customQuizBattleModal');
  if (modal) modal.style.display = 'none';
}

async function launchBattleWithCustomQuiz(login, passcode) {
  playSound('click');
  const user = state.currentUser;
  if (!user) {
    alert("Iltimos, avval tizimga kiring!");
    openAuthModal();
    return;
  }

  try {
    // 1. Verify custom quiz first
    const vRes = await fetch('/api/custom-quiz/verify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ login, passcode })
    });
    const vData = await vRes.json();
    if (!vData.ok) {
      alert(vData.detail || "Test login yoki paroli noto'g'ri!");
      return;
    }

    // 2. Create Battle Room with this custom quiz
    const createRes = await fetch('/api/battle/create-room', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        host_id: user.id,
        host_name: user.full_name,
        subject_id: 1,
        mode: battleState.mode || '1v1',
        max_players: battleState.maxPlayers || 2,
        custom_quiz_login: login,
        custom_quiz_passcode: passcode
      })
    });
    const cData = await createRes.json();
    if (cData.success) {
      battleState.isHost = true;
      battleState.customQuiz = { login, passcode, title: vData.quiz.title };
      navigateTo('battle');
      connectToBattleWebSocket(cData.room_code);
    } else {
      alert(cData.detail || "Batl xonasini ochishda xatolik");
    }
  } catch (err) {
    alert("Ulanishda xatolik yuz berdi: " + err);
  }
}

async function startCustomQuizBattleFromModal(actionType) {
  const login = (document.getElementById('cqbLoginInput')?.value || '').trim();
  const passcode = (document.getElementById('cqbPasscodeInput')?.value || '').trim();

  if (!login || !passcode) {
    alert("Iltimos, Test Logini va Parolini kiriting!");
    return;
  }

  if (actionType === 'battle') {
    closeCustomQuizBattleModal();
    launchBattleWithCustomQuiz(login, passcode);
  } else if (actionType === 'practice') {
    closeCustomQuizBattleModal();
    // Verify and start solo test
    try {
      const vRes = await fetch('/api/custom-quiz/verify', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ login, passcode })
      });
      const vData = await vRes.json();
      if (!vData.ok) {
        alert(vData.detail || "Test login yoki paroli noto'g'ri!");
        return;
      }
      // Start test session with custom questions
      if (typeof startCustomSoloQuiz === 'function') {
        startCustomSoloQuiz(vData.quiz);
      } else {
        alert(`Test topildi: "${vData.quiz.title}" (${vData.quiz.question_count} ta savol). Batl bo'limida bellashishingiz mumkin!`);
        launchBattleWithCustomQuiz(login, passcode);
      }
    } catch (e) {
      alert("Xatolik yuz berdi");
    }
  }
}
