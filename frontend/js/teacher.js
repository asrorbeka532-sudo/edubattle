// ========================================================
// EDUBATTLE - TEACHER PORTAL & CLASS MANAGEMENT
// O'QITUVCHI PORTALI: GURUHLAR, TESTLAR VA VIKTORINALAR
// ========================================================

let activeRosterGroupId = null;
let activeRosterInviteCode = null;
let cachedTeacherAllStudents = [];
let liveQuizSession = {
  quizId: null,
  pinCode: null,
  questions: [],
  currentIndex: 0,
  score: 0,
  correctCount: 0,
  timeLimitSec: 20,
  timerInterval: null,
  timeLeft: 20,
  startTime: null
};

async function loadTeacherPortalData() {
  if (!state.currentUser || state.currentUser.role !== 'teacher') {
    return;
  }

  const teacherId = state.currentUser.id;

  try {
    // 1. Fetch Teacher Groups
    const res = await fetch(`/api/teacher/${teacherId}/groups`);
    const groups = await res.json();
    renderTeacherGroups(groups);

    const groupCountEl = document.getElementById('teacherTotalGroups');
    if (groupCountEl) groupCountEl.textContent = groups.length;

    const totalStudents = groups.reduce((acc, g) => acc + (g.student_count || 0), 0);
    const studentCountEl = document.getElementById('teacherTotalStudents');
    if (studentCountEl) studentCountEl.textContent = totalStudents;

    const profileGroupCount = document.getElementById('profileTeacherGroupCount');
    if (profileGroupCount) profileGroupCount.textContent = groups.length;

    const profileStudentCount = document.getElementById('profileTeacherStudentCount');
    if (profileStudentCount) profileStudentCount.textContent = totalStudents;

    const quizGroupSelect = document.getElementById('newQuizGroupSelect');
    if (quizGroupSelect) {
      if (groups.length === 0) {
        quizGroupSelect.innerHTML = `<option value="">Avval sinf oching</option>`;
      } else {
        quizGroupSelect.innerHTML = groups.map(g => `<option value="${g.id}">${escapeHtml(g.group_name)} (${g.invite_code})</option>`).join('');
      }
    }

    const quizBotGroupSelect = document.getElementById('quizBotGroupSelect');
    if (quizBotGroupSelect) {
      if (groups.length === 0) {
        quizBotGroupSelect.innerHTML = `<option value="">Barcha o'quvchilar uchun</option>`;
      } else {
        quizBotGroupSelect.innerHTML = `<option value="">Barcha o'quvchilar uchun</option>` + groups.map(g => `<option value="${g.id}">${escapeHtml(g.group_name)} (${g.invite_code})</option>`).join('');
      }
    }

    const nameEl = document.getElementById('teacherName');
    if (nameEl) nameEl.textContent = state.currentUser.full_name;

    const teacherIdPill = document.getElementById('teacherIdPill');
    if (teacherIdPill) teacherIdPill.textContent = `ID: #${state.currentUser.id}`;

    const metaEl = document.getElementById('teacherMeta');
    if (metaEl) metaEl.textContent = `${state.currentUser.school_lyceum || 'Maktab/Litsey'} • ${state.currentUser.grade || 'Oliy toifa'} • ID: #${state.currentUser.id}`;

    // 2. Fetch Teacher Quizzes
    loadTeacherQuizzes(teacherId);

    // 3. Fetch Teacher-created questions
    loadTeacherQuestions(teacherId);

    // 4. Update overall stats
    loadTeacherAllStudents();
  } catch (e) {
    console.error("Teacher portal data load error:", e);
  }
}

function renderTeacherGroups(groups) {
  const container = document.getElementById('teacherGroupsContainer');
  if (!container) return;

  if (!groups || groups.length === 0) {
    container.innerHTML = `
      <div class="minimal-card" style="text-align:center; padding:22px 14px;">
        <div style="font-size:32px; margin-bottom:6px;">👥</div>
        <h4 style="font-size:13px; font-weight:700; color:#fff;">Hozircha hech qanday sinf ochilmagan</h4>
        <p style="color:var(--text-muted); font-size:11px; margin:4px 0 12px; line-height:1.4;">
          Sinfingizdagi o'quvchilarni to'plash uchun "Yangi Sinf Ochish" tugmasini bosing va taklif kodini o'quvchilarga bering.
        </p>
        <button class="btn btn-red btn-sm" onclick="openCreateGroupModal()">➕ Birinchi Sinfni Ochish</button>
      </div>
    `;
    return;
  }

  container.innerHTML = groups.map(g => `
    <div class="minimal-card" style="cursor:pointer; margin-bottom:10px;" onclick="openGroupRosterModal(${g.id}, '${escapeHtml(g.group_name)}', '${g.invite_code}')">
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
        <div style="font-size:14px; font-weight:800; color:#fff;">${escapeHtml(g.group_name)}</div>
        <div style="display:flex; gap:6px; align-items:center;">
          <span class="tag tag-red" title="Taklif kodi">${g.invite_code}</span>
          <button class="btn btn-outline btn-sm" onclick="event.stopPropagation(); copyGroupCodeDirect('${g.invite_code}')" style="padding:2px 6px; font-size:10px;" title="Kodni nusxalash">📋</button>
        </div>
      </div>
      <div style="font-size:11px; color:var(--text-muted); margin-bottom:10px;">
        ${escapeHtml(g.subject_name || 'Umumiy Fan')} • ${escapeHtml(g.description || 'Sinf guruhi')}
      </div>
      <div style="display:flex; justify-content:space-between; align-items:center; font-size:11px; border-top:1px solid rgba(255,255,255,0.06); padding-top:8px;">
        <span style="color:var(--accent-green); font-weight:700;">👥 ${g.student_count || 0} nafar o'quvchi</span>
        <span style="color:var(--accent-red); font-weight:700;">O'quvchilar ro'yxati ➔</span>
      </div>
    </div>
  `).join('');
}

async function loadTeacherQuizzes(teacherId) {
  const container = document.getElementById('teacherQuizzesContainer');
  if (!container) return;

  try {
    const res = await fetch(`/api/teacher/${teacherId}/quizzes`);
    const quizzes = await res.json();

    const totalQuizzesEl = document.getElementById('teacherTotalQuizzes');
    if (totalQuizzesEl) totalQuizzesEl.textContent = quizzes ? quizzes.length : 0;

    if (!quizzes || quizzes.length === 0) {
      container.innerHTML = `
        <div class="minimal-card" style="text-align:center; padding:14px; color:var(--text-muted); font-size:11px;">
          Hozircha viktorinalar o'tkazilmagan. Yuqoridagi "➕ Yangi Viktorina" tugmasi orqali test tashkil qiling.
        </div>
      `;
      return;
    }

    container.innerHTML = quizzes.map(q => {
      const qCount = q.questions ? (Array.isArray(q.questions) ? q.questions.length : 0) : 0;
      const safeTitle = (q.title || 'Test').replace(/'/g, "\\'");
      return `
      <div class="minimal-card highlight-green" style="margin-bottom:8px; padding:12px;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
          <div>
            <div style="font-size:13px; font-weight:800; color:#fff;">${escapeHtml(q.title)}</div>
            <div style="font-size:10px; color:var(--text-muted); margin-top:2px;">
              ${escapeHtml(q.group_name || 'Barcha sinflar')} • ${escapeHtml(q.subject_name || 'Fan')} • ⏱ ${q.time_limit_sec || 30}s
            </div>
          </div>
          <div style="text-align:right;">
            <span class="tag tag-green" style="font-family:monospace; font-weight:800; font-size:11px;">KOD: ${q.pin_code}</span>
            ${q.passcode ? `<div style="font-size:10px; color:#38bdf8; font-weight:700; margin-top:2px; font-family:monospace;">Parol: ${q.passcode}</div>` : ''}
          </div>
        </div>
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px; font-size:10px; color:var(--text-muted); border-top:1px solid rgba(255,255,255,0.06); padding-top:6px;">
          <span>Savollar: <b style="color:#fff;">${qCount} ta</b></span>
          <div style="display:flex; gap:6px;">
            <button class="btn btn-outline btn-sm" onclick="copyQuizCredentialsDirect('${q.pin_code}', '${q.passcode || ''}', '${safeTitle}', ${q.time_limit_sec || 30}, ${qCount})" style="padding:2px 8px; font-size:10px;">📋 Kod & Parol</button>
            <button class="btn btn-green btn-sm" onclick="openLiveQuizArena('${q.pin_code}')" style="padding:2px 8px; font-size:10px;">⚡ Boshlash</button>
            <button class="btn btn-outline btn-sm" onclick="showQuizLeaderboard(${q.id})" style="padding:2px 8px; font-size:10px;">🏆 Reyting</button>
          </div>
        </div>
      </div>
    `;
    }).join('');
  } catch (e) {
    console.error("Error loading quizzes:", e);
  }
}

async function loadTeacherQuestions(teacherId) {
  const container = document.getElementById('teacherMyQuestionsContainer');
  if (!container) return;

  try {
    const res = await fetch(`/api/teacher/${teacherId}/questions`);
    const questions = await res.json();

    if (!questions || questions.length === 0) {
      container.innerHTML = `
        <div class="minimal-card" style="text-align:center; padding:14px; color:var(--text-muted); font-size:11px;">
          Hozircha o'zingiz test kiritmadingiz. "➕ Yangi Test" tugmasi orqali o'quvchilaringiz uchun maxsus testlar qo'shing.
        </div>
      `;
      return;
    }

    container.innerHTML = questions.map(q => `
      <div class="minimal-card" style="margin-bottom:8px; padding:10px;">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:4px;">
          <div style="font-size:12px; font-weight:800; color:#fff;">${escapeHtml(q.question_text)}</div>
          <span class="tag tag-subtle">${escapeHtml(q.grade || '9-sinf')}</span>
        </div>
        <div style="font-size:10px; color:var(--text-muted); margin-bottom:6px;">
          Mavzu: ${escapeHtml(q.chapter_title || 'Umumiy')} • Fan: ${escapeHtml(q.subject_name || '')}
        </div>
        <div style="font-size:11px; color:var(--accent-green); font-weight:600;">
          To'g'ri javob: ${escapeHtml(q.options ? q.options[q.correct_index] : 'Aniqlanmagan')}
        </div>
      </div>
    `).join('');
  } catch (e) {
    console.error("Error loading teacher questions:", e);
  }
}

// ----------------- ALL STUDENTS MONITORING -----------------
async function loadTeacherAllStudents() {
  if (!state.currentUser || state.currentUser.role !== 'teacher') return;

  const container = document.getElementById('teacherAllStudentsContainer');
  const countBadge = document.getElementById('teacherStudentsCountBadge');

  try {
    const res = await fetch(`/api/teacher/${state.currentUser.id}/all-students`);
    const students = await res.json();
    cachedTeacherAllStudents = students || [];

    if (countBadge) countBadge.textContent = `${cachedTeacherAllStudents.length} nafar`;

    renderTeacherStudentsList(cachedTeacherAllStudents);
  } catch (e) {
    if (container) {
      container.innerHTML = `<div class="minimal-card" style="text-align:center; padding:16px; color:var(--accent-red);">O'quvchilarni yuklashda xatolik yuz berdi.</div>`;
    }
  }
}

let teacherSearchStudentTimeout = null;

async function filterTeacherAllStudents(query) {
  const q = (query || '').trim();
  if (!q) {
    renderTeacherStudentsList(cachedTeacherAllStudents);
    return;
  }
  const qLower = q.toLowerCase();
  const filtered = cachedTeacherAllStudents.filter(s => 
    (s.full_name && s.full_name.toLowerCase().includes(qLower)) ||
    (s.username && s.username.toLowerCase().includes(qLower)) ||
    (s.group_name && s.group_name.toLowerCase().includes(qLower))
  );

  if (filtered.length > 0) {
    renderTeacherStudentsList(filtered);
    return;
  }

  // If not found in current groups, search system-wide by EB- ID or name
  if (teacherSearchStudentTimeout) clearTimeout(teacherSearchStudentTimeout);
  teacherSearchStudentTimeout = setTimeout(async () => {
    try {
      const res = await fetch(`/api/teacher/search-students?q=${encodeURIComponent(q)}&teacher_id=${state.currentUser?.id || 0}`);
      if (res.ok) {
        const globalStudents = await res.json();
        if (globalStudents && globalStudents.length > 0) {
          renderTeacherGlobalFoundStudents(globalStudents, q);
          return;
        }
      }
    } catch (e) {}
    renderTeacherStudentsList([]);
  }, 300);
}

function renderTeacherGlobalFoundStudents(students, query) {
  const container = document.getElementById('teacherAllStudentsContainer');
  if (!container) return;

  container.innerHTML = `
    <div style="font-size:11px; font-weight:700; color:var(--text-muted); margin-bottom:8px;">
      🔍 Tizimdan topilgan o'quvchilar ("${escapeHtml(query)}"):
    </div>
    <div style="display:flex; flex-direction:column; gap:8px;">
      ${students.map(s => `
        <div class="minimal-card" style="padding:10px; margin-bottom:0; display:flex; justify-content:space-between; align-items:center;">
          <div style="display:flex; align-items:center; gap:10px;">
            <div style="width:36px; height:36px; border-radius:50%; background:var(--bg-elevated); border:1px solid var(--border-card); display:flex; align-items:center; justify-content:center; font-size:18px;">
              👨‍🎓
            </div>
            <div>
              <div style="font-size:13px; font-weight:800; color:#fff;">${escapeHtml(s.full_name)}</div>
              <div style="font-size:11px; color:var(--text-muted);">
                <b style="color:var(--accent-red); font-family:monospace;">ID: ${escapeHtml(s.username)}</b> • ${escapeHtml(s.school_lyceum || 'Maktab')} (${escapeHtml(s.grade || '9-sinf')})
              </div>
            </div>
          </div>
          <button class="btn btn-red btn-sm" onclick="promptAddStudentToTeacherGroup(${s.id}, '${escapeHtml(s.username)}', '${escapeHtml(s.full_name)}')" style="font-size:11px; padding:6px 12px; font-weight:700;">
            ➕ Guruhga qo'shish
          </button>
        </div>
      `).join('')}
    </div>
  `;
}

async function promptAddStudentToTeacherGroup(studentId, studentEB, studentName) {
  if (typeof playSound === 'function') playSound('click');
  if (!cachedTeacherGroups || cachedTeacherGroups.length === 0) {
    alert("Avval '👥 Sinflarim' bo'limida kamida 1 ta sinf guruhi ochishingiz kerak!");
    return;
  }

  const groupOptions = cachedTeacherGroups.map((g, idx) => `${idx + 1}. ${g.group_name}`).join('\n');
  const chosenIndex = prompt(`"${studentName}" (${studentEB}) ni qaysi guruhga qo'shmoqchisiz?\nGuruh raqamini kiriting:\n\n${groupOptions}`);
  if (!chosenIndex) return;

  const idx = parseInt(chosenIndex.trim(), 10) - 1;
  if (isNaN(idx) || idx < 0 || idx >= cachedTeacherGroups.length) {
    alert("Noto'g'ri raqam kiritildi!");
    return;
  }

  const selectedGroup = cachedTeacherGroups[idx];
  try {
    const res = await fetch(`/api/teacher/groups/${selectedGroup.id}/add-student`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        teacher_id: state.currentUser.id,
        student_id: studentId,
        student_eb: studentEB
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      if (typeof playSound === 'function') playSound('victory');
      alert(data.message || `O'quvchi "${selectedGroup.group_name}" guruhiga qo'shildi!`);
      loadTeacherAllStudents();
    } else {
      alert(data.detail || data.message || "Xatolik yuz berdi!");
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik!");
  }
}

function renderTeacherStudentsList(students) {
  const container = document.getElementById('teacherAllStudentsContainer');
  if (!container) return;

  if (!students || students.length === 0) {
    container.innerHTML = `
      <div class="minimal-card" style="text-align:center; padding:24px 14px;">
        <div style="font-size:32px; margin-bottom:6px;">👨‍🎓</div>
        <h4 style="font-size:13px; font-weight:700; color:#fff;">O'quvchilar topilmadi</h4>
        <p style="color:var(--text-muted); font-size:11px; margin-top:4px;">
          Sinf taklif kodini o'quvchilarga ulashsangiz, ular bu yerda paydo bo'ladi.
        </p>
      </div>
    `;
    return;
  }

  container.innerHTML = `
    <div style="display:flex; flex-direction:column; gap:8px;">
      ${students.map((s, idx) => `
        <div class="minimal-card" style="padding:10px; margin-bottom:0; display:flex; justify-content:space-between; align-items:center;">
          <div style="display:flex; align-items:center; gap:10px;">
            <div style="font-size:12px; font-weight:800; color:var(--text-muted); width:16px;">#${idx+1}</div>
            <div style="width:36px; height:36px; border-radius:50%; background:var(--bg-elevated); border:1px solid var(--border-card); display:flex; align-items:center; justify-content:center; font-size:18px;">
              👨‍🎓
            </div>
            <div>
              <div style="font-size:13px; font-weight:800; color:#fff;">${escapeHtml(s.full_name)}</div>
              <div style="font-size:11px; color:var(--text-muted);">
                <b style="color:var(--accent-red); font-family:monospace;">ID: ${escapeHtml(s.username)}</b> • <span style="color:var(--accent-red); font-weight:700;">${escapeHtml(s.group_name || 'Guruh')}</span>
              </div>
            </div>
          </div>

          <div style="display:flex; align-items:center; gap:8px;">
            <div style="text-align:right;">
              <div class="score-badge-100 ${getScoreBadgeClass(s.grade_score)}">${(s.grade_score !== undefined && s.grade_score !== null) ? s.grade_score : 0} ball</div>
              <div style="font-size:9px; color:var(--text-muted); margin-top:2px;">
                ${s.tests_completed || 0} ta test
              </div>
            </div>
            <button class="btn btn-outline btn-sm" onclick="openStudentGradesHistoryModal(${s.id}, '${escapeHtml(s.full_name)}')" style="padding:4px 10px; font-size:11px;" title="Test natijalari asosidagi baholar jurnali">
              📊 Test Baholari
            </button>
          </div>
        </div>
      `).join('')}
    </div>
  `;
}

// ----------------- DARSLIK YUKLASH (UPLOAD BOOK) -----------------
function openTeacherUploadBookModal() {
  playSound('click');
  if (!state.currentUser || (state.currentUser.role !== 'teacher' && state.currentUser.role !== 'admin')) {
    alert("Darslik yuklash faqat o'qituvchi va adminlar uchun!");
    return;
  }
  const authorInput = document.getElementById('uploadBookAuthor');
  if (authorInput) authorInput.value = state.currentUser.full_name;
  document.getElementById('uploadBookModal').classList.add('active');
}

async function submitTeacherUploadBook() {
  playSound('click');
  const title = (document.getElementById('uploadBookTitle').value || '').trim();
  const subjectId = parseInt(document.getElementById('uploadBookSubjectSelect').value) || 1;
  const grade = document.getElementById('uploadBookGradeSelect').value || '9-sinf';
  const author = (document.getElementById('uploadBookAuthor').value || state.currentUser.full_name).trim();
  const summary = (document.getElementById('uploadBookSummary').value || '').trim();
  const content = (document.getElementById('uploadBookContent').value || '').trim();

  if (!title) {
    alert("Iltimos, darslik nomini kiriting!");
    return;
  }

  const chapters = content ? [{ title: "1-Bob / Asosiy Mavzu", summary: content.substring(0, 80) + '...', content: content }] : [];

  try {
    const res = await fetch('/api/teacher/textbooks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        teacher_id: state.currentUser.id,
        subject_id: subjectId,
        title: title,
        grade: grade,
        author: author,
        summary: summary || `${grade} uchun maxsus darslik va qo'llanma`,
        file_url: "",
        chapters: chapters
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('victory');
      alert("🎉 Darslik muvaffaqiyatli kutubxonaga yuklandi!");
      closeModal('uploadBookModal');
      document.getElementById('uploadBookTitle').value = '';
      document.getElementById('uploadBookSummary').value = '';
      document.getElementById('uploadBookContent').value = '';
      if (typeof loadLibraryBooks === 'function') loadLibraryBooks();
    } else {
      playSound('wrong');
      alert(data.detail || "Darslikni yuklashda xatolik!");
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik!");
  }
}

// ----------------- TEST SAVOLI TUZISH (CREATE QUESTION) -----------------
function openTeacherCreateQuestionModal() {
  playSound('click');
  if (!state.currentUser || state.currentUser.role !== 'teacher') {
    alert("Faqat o'qituvchilar test tuza oladi!");
    return;
  }
  document.getElementById('createQuestionModal').classList.add('active');
}

async function submitTeacherCreateQuestion() {
  playSound('click');
  const subjectId = parseInt(document.getElementById('newQuestionSubjectSelect').value) || 1;
  const grade = document.getElementById('newQuestionGradeSelect').value || '9-sinf';
  const chapter = (document.getElementById('newQuestionChapter').value || 'Umumiy').trim();
  const text = (document.getElementById('newQuestionText').value || '').trim();
  const a = (document.getElementById('optA').value || '').trim();
  const b = (document.getElementById('optB').value || '').trim();
  const c = (document.getElementById('optC').value || '').trim();
  const d = (document.getElementById('optD').value || '').trim();
  const correctIdx = parseInt(document.getElementById('newQuestionCorrectOpt').value) || 0;
  const explanation = (document.getElementById('newQuestionExplanation').value || '').trim();

  if (!text || !a || !b) {
    alert("Iltimos, savol matni va kamida A va B variantlarini to'ldiring!");
    return;
  }

  const options = [a, b];
  if (c) options.push(c);
  if (d) options.push(d);

  try {
    const res = await fetch('/api/teacher/questions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        teacher_id: state.currentUser.id,
        subject_id: subjectId,
        grade: grade,
        chapter_title: chapter,
        question_text: text,
        options: options,
        correct_index: correctIdx,
        explanation: explanation
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('victory');
      alert("🎉 Test savoli muvaffaqiyatli saqlandi!");
      closeModal('createQuestionModal');
      document.getElementById('newQuestionText').value = '';
      document.getElementById('optA').value = '';
      document.getElementById('optB').value = '';
      document.getElementById('optC').value = '';
      document.getElementById('optD').value = '';
      document.getElementById('newQuestionExplanation').value = '';
      loadTeacherQuestions(state.currentUser.id);
    } else {
      playSound('wrong');
      alert(data.detail || "Savol saqlashda xatolik!");
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik!");
  }
}

// ----------------- TEST BUILDER -----------------
let quizBotDraft = {
  title: '',
  subject_id: 1,
  grade: '9-sinf',
  group_id: null,
  time_limit_sec: 30,
  passcode: '1234',
  questions: []
};
let activeCreatedQuiz = null;

function openQuizBotModal() {
  playSound('click');
  if (!state.currentUser) {
    openAuthModal();
    return;
  }
  if (state.currentUser.role !== 'teacher' && state.currentUser.role !== 'admin') {
    alert("Faqat o'qituvchilar test tuza oladi!");
    return;
  }

  // Random 4-digit passcode
  const randomPass = Math.floor(1000 + Math.random() * 9000).toString();
  quizBotDraft = {
    title: '',
    subject_id: state.subjects && state.subjects[0] ? state.subjects[0].id : 1,
    grade: '9-sinf',
    group_id: null,
    time_limit_sec: 30,
    passcode: randomPass,
    questions: []
  };

  // Reset inputs
  const topicInput = document.getElementById('quizBotTopicInput');
  if (topicInput) topicInput.value = '';

  const passInput = document.getElementById('quizBotPasscodeInput');
  if (passInput) passInput.value = randomPass;

  const timerSelect = document.getElementById('quizBotTimerSelect');
  if (timerSelect) timerSelect.value = '30';

  // Show Stage 1, hide Stage 2 and 3
  document.getElementById('quizBotStageSetup').style.display = 'block';
  document.getElementById('quizBotStageQuestions').style.display = 'none';
  document.getElementById('quizBotStageSuccess').style.display = 'none';

  document.getElementById('quizBotModal').classList.add('active');
  if (topicInput) topicInput.focus();
}

// Aliases so all buttons open Test Modal
function openCreateQuizModal() {
  openQuizBotModal();
}
function openTeacherCreateQuestionModal() {
  openQuizBotModal();
}

function quizBotGenerateNewPasscode() {
  playSound('click');
  const pass = Math.floor(1000 + Math.random() * 9000).toString();
  const passInput = document.getElementById('quizBotPasscodeInput');
  if (passInput) passInput.value = pass;
}

function quizBotProceedToQuestions() {
  playSound('click');
  const topic = (document.getElementById('quizBotTopicInput').value || '').trim();
  if (!topic) {
    alert("Iltimos, test mavzusi yoki nomini kiriting!\nMasalan: Kvadrat tenglamalar mavzusidagi test");
    document.getElementById('quizBotTopicInput').focus();
    return;
  }

  const subId = parseInt(document.getElementById('quizBotSubjectSelect').value) || 1;
  const grade = document.getElementById('quizBotGradeSelect').value || '9-sinf';
  const groupId = parseInt(document.getElementById('quizBotGroupSelect').value) || null;
  const timer = parseInt(document.getElementById('quizBotTimerSelect').value) || 30;
  const pass = (document.getElementById('quizBotPasscodeInput').value || '').trim() || Math.floor(1000 + Math.random() * 9000).toString();

  quizBotDraft.title = topic;
  quizBotDraft.subject_id = subId;
  quizBotDraft.grade = grade;
  quizBotDraft.group_id = groupId;
  quizBotDraft.time_limit_sec = timer;
  quizBotDraft.passcode = pass;

  // Transition to Stage 2
  document.getElementById('quizBotStageSetup').style.display = 'none';
  document.getElementById('quizBotStageQuestions').style.display = 'flex';
  document.getElementById('quizBotTopicBadge').textContent = topic;

  updateQuizBotQuestionsUI();
  resetQuizBotQuestionInputs();
  document.getElementById('quizBotQuestionText').focus();
}

function onQuizBotRadioChange(idx) {
  playSound('click');
  for (let i = 0; i < 4; i++) {
    const row = document.getElementById(`quizBotOptRow${i}`);
    if (row) {
      if (i === idx) {
        row.classList.add('checked');
      } else {
        row.classList.remove('checked');
      }
    }
  }
}

function onQuizBotOptInput(idx) {
  const radio = document.getElementById(`quizBotRadio${idx}`);
  if (radio && !radio.checked && idx === 0) {
    radio.checked = true;
    onQuizBotRadioChange(idx);
  }
}

function resetQuizBotQuestionInputs() {
  document.getElementById('quizBotQuestionText').value = '';
  document.getElementById('quizBotOpt0').value = '';
  document.getElementById('quizBotOpt1').value = '';
  document.getElementById('quizBotOpt2').value = '';
  document.getElementById('quizBotOpt3').value = '';
  document.getElementById('quizBotExplanation').value = '';

  const r0 = document.getElementById('quizBotRadio0');
  if (r0) r0.checked = true;
  onQuizBotRadioChange(0);
}

function updateQuizBotQuestionsUI() {
  const count = quizBotDraft.questions.length;
  document.getElementById('quizBotQuestionIndexBadge').textContent = `Savol #${count + 1}`;
  document.getElementById('quizBotSavedCountBadge').textContent = count;
  document.getElementById('quizBotQuestionsSummaryLabel').textContent = `${count} ta savol tayyor`;

  const listContainer = document.getElementById('quizBotSavedQuestionsList');
  if (!listContainer) return;

  if (count === 0) {
    listContainer.innerHTML = '';
    return;
  }

  const letters = ['A', 'B', 'C', 'D'];
  listContainer.innerHTML = quizBotDraft.questions.map((q, idx) => {
    const correctLetter = letters[q.correct_index] || 'A';
    return `
      <div style="background:rgba(255,255,255,0.03); border:1px solid rgba(255,255,255,0.08); border-radius:6px; padding:6px 10px; display:flex; justify-content:space-between; align-items:center;">
        <div style="font-size:11px; color:#fff; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; max-width:240px;">
          <b>${idx + 1}.</b> ${escapeHtml(q.question_text)} <span style="color:var(--accent-green); font-weight:700;">(${correctLetter})</span>
        </div>
        <button class="btn btn-subtle btn-sm" onclick="quizBotRemoveQuestion(${idx})" style="padding:2px 6px; font-size:10px; color:#ef4444;" title="O'chirish">🗑</button>
      </div>
    `;
  }).join('');
}

function quizBotRemoveQuestion(idx) {
  playSound('click');
  quizBotDraft.questions.splice(idx, 1);
  updateQuizBotQuestionsUI();
}

function quizBotSaveAndNextQuestion() {
  const text = (document.getElementById('quizBotQuestionText').value || '').trim();
  const opt0 = (document.getElementById('quizBotOpt0').value || '').trim();
  const opt1 = (document.getElementById('quizBotOpt1').value || '').trim();
  const opt2 = (document.getElementById('quizBotOpt2').value || '').trim();
  const opt3 = (document.getElementById('quizBotOpt3').value || '').trim();
  const checkedRadio = document.querySelector('input[name="quizBotCorrectChoice"]:checked');
  const radioChoice = checkedRadio ? parseInt(checkedRadio.value) : 0;
  const explanation = (document.getElementById('quizBotExplanation').value || '').trim();

  if (!text) {
    alert("Iltimos, savol matnini yozing!");
    document.getElementById('quizBotQuestionText').focus();
    return;
  }

  const rawOpts = [opt0, opt1, opt2, opt3];
  const selectedText = rawOpts[radioChoice];
  if (!selectedText || !selectedText.trim()) {
    alert("Siz to'g'ri deb tanlagan variant bo'sh! Iltimos, unga javob yozing yoki boshqa variantni tanlang.");
    return;
  }

  const validOpts = rawOpts.filter(o => o.trim().length > 0);
  if (validOpts.length < 2) {
    alert("Iltimos, kamida 2 ta variant (A va B) kiriting!");
    return;
  }

  const actualCorrectIdx = validOpts.indexOf(selectedText.trim());

  // Push question into draft array
  quizBotDraft.questions.push({
    question_text: text,
    options: validOpts,
    correct_index: actualCorrectIdx >= 0 ? actualCorrectIdx : 0,
    explanation: explanation
  });

  // Sound and UI feedback
  playSound('correct');
  const pill = document.getElementById('quizBotNotificationPill');
  if (pill) {
    pill.textContent = `✓ ${quizBotDraft.questions.length}-savol saqlandi! Keyingi savolni yozing.`;
    pill.style.display = 'block';
    setTimeout(() => { pill.style.display = 'none'; }, 2500);
  }

  // Clear inputs and keep builder open!
  resetQuizBotQuestionInputs();
  updateQuizBotQuestionsUI();
  document.getElementById('quizBotQuestionText').focus();
}

async function quizBotFinishAndPublish() {
  playSound('click');
  // Check if teacher has an unsaved question currently typed
  const text = (document.getElementById('quizBotQuestionText').value || '').trim();
  const opt0 = (document.getElementById('quizBotOpt0').value || '').trim();
  const opt1 = (document.getElementById('quizBotOpt1').value || '').trim();
  const opt2 = (document.getElementById('quizBotOpt2').value || '').trim();
  const opt3 = (document.getElementById('quizBotOpt3').value || '').trim();

  if (text && opt0 && opt1) {
    const checkedRadio = document.querySelector('input[name="quizBotCorrectChoice"]:checked');
    const radioChoice = checkedRadio ? parseInt(checkedRadio.value) : 0;
    const explanation = (document.getElementById('quizBotExplanation').value || '').trim();
    const rawOpts = [opt0, opt1, opt2, opt3];
    const selectedText = rawOpts[radioChoice] || opt0;
    const validOpts = rawOpts.filter(o => o.trim().length > 0);
    const actualCorrectIdx = validOpts.indexOf(selectedText.trim());

    quizBotDraft.questions.push({
      question_text: text,
      options: validOpts,
      correct_index: actualCorrectIdx >= 0 ? actualCorrectIdx : 0,
      explanation: explanation
    });
  }

  if (quizBotDraft.questions.length === 0) {
    alert("Iltimos, kamida bitta savol tuzing va '➕ Keyingi Savol' tugmasi orqali saqlang!");
    return;
  }

  const finishBtn = document.getElementById('quizBotFinishBtn');
  if (finishBtn) {
    finishBtn.disabled = true;
    finishBtn.textContent = '🚀 Saqlanmoqda...';
  }

  try {
    const res = await fetch('/api/teacher/create-quiz', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        teacher_id: state.currentUser.id,
        group_id: quizBotDraft.group_id,
        title: quizBotDraft.title,
        subject_id: quizBotDraft.subject_id,
        grade: quizBotDraft.grade,
        time_limit_sec: quizBotDraft.time_limit_sec,
        passcode: quizBotDraft.passcode,
        description: `Ustoz tomonidan tuzilgan maxsus test (${quizBotDraft.questions.length} ta savol)`,
        questions: quizBotDraft.questions
      })
    });

    const data = await res.json();
    if (finishBtn) {
      finishBtn.disabled = false;
      finishBtn.textContent = '✅ Tayyor (Saqlash)';
    }

    if (res.ok && data.success) {
      playSound('victory');
      activeCreatedQuiz = data;

      document.getElementById('successQuizTitle').textContent = data.title;
      document.getElementById('successQuizPin').textContent = data.pin_code;
      document.getElementById('successQuizPasscode').textContent = data.passcode;
      document.getElementById('successQuizTimer').textContent = `${data.time_limit_sec} soniya`;
      document.getElementById('successQuizCount').textContent = `${data.total_questions} ta`;

      document.getElementById('quizBotStageQuestions').style.display = 'none';
      document.getElementById('quizBotStageSuccess').style.display = 'block';

      loadTeacherQuizzes(state.currentUser.id);
      loadTeacherQuestions(state.currentUser.id);
    } else {
      playSound('wrong');
      alert(data.detail || "Viktorina yaratishda xatolik yuz berdi!");
    }
  } catch (e) {
    if (finishBtn) {
      finishBtn.disabled = false;
      finishBtn.textContent = '✅ Tayyor (Saqlash)';
    }
    alert("Viktorinani saqlashda server xatosi!");
  }
}

function quizBotBackToSetup() {
  playSound('click');
  document.getElementById('quizBotStageQuestions').style.display = 'none';
  document.getElementById('quizBotStageSetup').style.display = 'block';
}

function quizBotCloseOrCancel() {
  if (quizBotDraft.questions.length > 0) {
    if (!confirm("Test yaratishdan chiqmoqchimisiz? Kiritilgan savollar saqlanmasligi mumkin.")) {
      return;
    }
  }
  closeModal('quizBotModal');
}

function copyQuizCredentials() {
  playSound('click');
  if (!activeCreatedQuiz) return;
  const msg = `📝 YANGI TEST TAYYOR!\n` +
              `━━━━━━━━━━━━━━━━━━━━━━\n` +
              `📚 Mavzu: ${activeCreatedQuiz.title}\n` +
              `🔑 Test KODI (Login/PIN): ${activeCreatedQuiz.pin_code}\n` +
              `🔒 Test PAROLI: ${activeCreatedQuiz.passcode}\n` +
              `⏱ Vaqt: Har bir savolga ${activeCreatedQuiz.time_limit_sec} soniya\n` +
              `📝 Savollar soni: ${activeCreatedQuiz.total_questions} ta\n` +
              `━━━━━━━━━━━━━━━━━━━━━━\n` +
              `📲 O'quvchilar ushbu Kod va Parol orqali ilovada yoki Telegram botimizda (@edubattleuz_bot) testni yechishlari mumkin!`;

  navigator.clipboard.writeText(msg).then(() => {
    alert("📋 Nusxalandi! Ushbu ma'lumotni o'quvchilarga taqdim eting.");
  }).catch(() => {
    prompt("Matnni nusxalab oling:", msg);
  });
}


function copyQuizCredentialsDirect(pin, passcode, title, timer, count) {
  playSound('click');
  const msg = `📝 YANGI TEST TAYYOR!\n` +
              `━━━━━━━━━━━━━━━━━━━━━━\n` +
              `📚 Mavzu: ${title}\n` +
              `🔑 Test KODI (Login/PIN): ${pin}\n` +
              `🔒 Test PAROLI: ${passcode}\n` +
              `⏱ Vaqt: Har bir savolga ${timer} soniya\n` +
              `📝 Savollar soni: ${count} ta\n` +
              `━━━━━━━━━━━━━━━━━━━━━━\n` +
              `📲 Ilovada yoki Telegram botimizda (@edubattleuz_bot) ushbu Kod va Parolni kiritib testni yeching!`;

  navigator.clipboard.writeText(msg).then(() => {
    alert(`📋 Nusxalandi!\nTest KODI: ${pin}\nTest PAROLI: ${passcode}\nO'quvchilarga yuborishingiz mumkin.`);
  }).catch(() => {
    prompt("Matnni nusxalab oling:", msg);
  });
}

function tryPublishedQuizNow() {
  playSound('click');
  closeModal('quizBotModal');
  if (activeCreatedQuiz && activeCreatedQuiz.pin_code) {
    openLiveQuizArena(activeCreatedQuiz.pin_code);
  }
}

// Seamless runner connection:
async function openLiveQuizArena(pinCode) {
  playSound('click');
  try {
    const res = await fetch(`/api/quiz/info/${pinCode}`);
    const quiz = await res.json();
    if (!quiz || !quiz.questions || quiz.questions.length === 0) {
      alert("Ushbu testda hali savollar mavjud emas!");
      return;
    }
    if (typeof openQuizBotRunner === 'function') {
      openQuizBotRunner(quiz);
    }
  } catch (e) {
    alert("Viktorinani yuklashda xatolik!");
  }
}


async function showQuizLeaderboard(quizId) {
  const listEl = document.getElementById('liveQuizLeaderboardList');
  if (!listEl) return;

  listEl.innerHTML = '<div style="text-align:center; padding:12px; color:var(--text-muted);">Natijalar yuklanmoqda...</div>';
  document.getElementById('liveQuizModal').classList.add('active');
  document.getElementById('liveQuizPlayingContainer').style.display = 'none';
  document.getElementById('liveQuizResultsContainer').style.display = 'block';

  try {
    const res = await fetch(`/api/quiz/${quizId}/leaderboard`);
    const leaderboard = await res.json();

    if (!leaderboard || leaderboard.length === 0) {
      listEl.innerHTML = `
        <div class="minimal-card" style="text-align:center; padding:14px; color:var(--text-muted); font-size:11px;">
          Hozircha natijalar kiritilmagan.
        </div>
      `;
      return;
    }

    const rankIcons = ['🥇', '🥈', '🥉'];
    listEl.innerHTML = leaderboard.map((row, idx) => `
      <div class="minimal-card" style="padding:10px; margin-bottom:6px; display:flex; justify-content:space-between; align-items:center;">
        <div style="display:flex; align-items:center; gap:8px;">
          <span style="font-size:16px;">${rankIcons[idx] || `#${idx+1}`}</span>
          <div>
            <div style="font-size:12px; font-weight:800; color:#fff;">${escapeHtml(row.full_name)}</div>
            <div style="font-size:10px; color:var(--text-muted);">@${escapeHtml(row.username)} • ⏱ ${row.time_taken_sec}s</div>
          </div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:13px; font-weight:900; color:var(--accent-green);">${row.correct_answers} / ${row.total_questions}</div>
          <div style="font-size:9px; color:var(--text-muted);">${row.score} ball</div>
        </div>
      </div>
    `).join('');
  } catch (e) {
    listEl.innerHTML = '<div style="color:var(--accent-red); padding:10px;">Reytingni yuklashda xatolik!</div>';
  }
}

// ----------------- GROUPS ROSTER MODAL -----------------
async function openGroupRosterModal(groupId, groupName, inviteCode) {
  playSound('click');
  activeRosterGroupId = groupId;
  activeRosterInviteCode = inviteCode;

  document.getElementById('groupRosterTitle').textContent = `👥 ${groupName}`;
  document.getElementById('groupRosterInvite').textContent = `Taklif kodi: ${inviteCode}`;

  const listContainer = document.getElementById('groupRosterList');
  listContainer.innerHTML = '<div style="text-align:center; padding:16px; color:var(--text-muted); font-size:11px;">O\'quvchilar ro\'yxati yuklanmoqda...</div>';
  document.getElementById('groupRosterModal').classList.add('active');

  loadGroupStudentsList(groupId, inviteCode);
}

async function loadGroupStudentsList(groupId, inviteCode) {
  const listContainer = document.getElementById('groupRosterList');
  if (!listContainer) return;

  try {
    const res = await fetch(`/api/teacher/groups/${groupId}/students`);
    const students = await res.json();

    if (!students || students.length === 0) {
      listContainer.innerHTML = `
        <div style="text-align:center; padding:20px 10px; color:var(--text-muted); font-size:11px;">
          Ushbu guruhga hali o'quvchilar a'zo bo'lmagan.<br>
          O'quvchilarga taklif kodini bering: <b style="color:var(--accent-red); font-size:13px; font-family:monospace;">${inviteCode}</b>
        </div>
      `;
      return;
    }

    listContainer.innerHTML = `
      <div style="font-size:11px; font-weight:700; color:var(--text-muted); margin-bottom:8px;">Guruh a'zolari (${students.length} nafar):</div>
      <div style="display:flex; flex-direction:column; gap:6px;">
        ${students.map((s, idx) => `
          <div style="display:flex; align-items:center; justify-content:space-between; padding:8px; background:var(--bg-elevated); border:1px solid var(--border-card); border-radius:6px;">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:10px; font-weight:800; color:var(--text-muted); width:14px;">#${idx+1}</span>
              <div>
                <div style="font-size:12px; font-weight:800; color:#fff;">${escapeHtml(s.full_name)}</div>
                <div style="font-size:10px; color:var(--text-muted);">@${escapeHtml(s.username)} • ${s.tests_completed || 0} ta test yechgan</div>
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:6px;">
              <div style="text-align:right;">
                <div class="score-badge-100 ${getScoreBadgeClass(s.grade_score)}">${(s.grade_score !== undefined && s.grade_score !== null) ? s.grade_score + ' ball' : '0 ball'}</div>
                <div style="font-size:9px; color:var(--text-muted);">${s.xp} XP</div>
              </div>
              <button class="btn btn-outline btn-sm" onclick="openStudentGradesHistoryModal(${s.id}, '${escapeHtml(s.full_name)}')" style="padding:3px 8px; font-size:10px;" title="Test baholari kundaligi">
                📊 Test Baholari
              </button>
              <button class="btn btn-outline btn-sm" onclick="removeStudentFromGroup(${groupId}, ${s.id}, '${escapeHtml(s.full_name)}')" style="color:var(--accent-red); border-color:rgba(225,29,72,0.3); padding:3px 6px; font-size:10px;" title="Guruhdan chiqarish">
                ✕
              </button>
            </div>
          </div>
        `).join('')}
      </div>
    `;
  } catch (e) {
    listContainer.innerHTML = '<div style="color:var(--accent-red); font-size:11px; padding:10px;">O\'quvchilarni yuklashda xatolik!</div>';
  }
}

function copyActiveGroupInviteCode() {
  if (activeRosterInviteCode) {
    copyGroupCodeDirect(activeRosterInviteCode);
  }
}

function copyGroupCodeDirect(code) {
  playSound('click');
  navigator.clipboard.writeText(code).then(() => {
    alert(`📋 Nusxalandi: ${code}\nO'quvchilarga ushbu kodni yuboring!`);
  }).catch(() => {
    prompt("Kodni nusxalab oling:", code);
  });
}

async function deleteActiveGroupPrompt() {
  if (!activeRosterGroupId || !state.currentUser) return;
  playSound('click');

  if (confirm("⚠️ Diqqat: Ushbu sinfni va uning tarkibidagi barcha a'zolik ma'lumotlarini o'chirishni xohlaysizmi?")) {
    try {
      const res = await fetch(`/api/teacher/groups/${activeRosterGroupId}?teacher_id=${state.currentUser.id}`, {
        method: 'DELETE'
      });
      const data = await res.json();
      if (res.ok && data.success) {
        playSound('correct');
        alert("🗑 Sinf muvaffaqiyatli o'chirildi.");
        closeModal('groupRosterModal');
        loadTeacherPortalData();
      } else {
        alert(data.detail || "Sinfni o'chirishda xatolik!");
      }
    } catch (e) {
      alert("Serverga ulanishda xatolik!");
    }
  }
}

async function removeStudentFromGroup(groupId, studentId, studentName) {
  if (!state.currentUser) return;
  playSound('click');

  if (confirm(`Haqiqatan ham "${studentName}" o'quvchisini ushbu sinfdan chiqarmoqchimisiz?`)) {
    try {
      const res = await fetch(`/api/teacher/groups/${groupId}/students/${studentId}?teacher_id=${state.currentUser.id}`, {
        method: 'DELETE'
      });
      const data = await res.json();
      if (res.ok && data.success) {
        playSound('correct');
        loadGroupStudentsList(groupId, activeRosterInviteCode);
        loadTeacherPortalData();
      } else {
        alert(data.detail || "O'quvchini chiqarishda xatolik!");
      }
    } catch (e) {
      alert("Serverga ulanishda xatolik!");
    }
  }
}

function openCreateGroupModal() {
  playSound('click');
  document.getElementById('createGroupModal').classList.add('active');
}

async function submitCreateGroup() {
  playSound('click');
  const name = (document.getElementById('newGroupName').value || '').trim();
  const subjectId = parseInt(document.getElementById('newGroupSubject').value) || 1;
  const customCode = (document.getElementById('newGroupInviteCode').value || '').trim();

  if (!name) {
    alert("Iltimos, sinf yoki guruh nomini kiriting!");
    return;
  }

  try {
    const res = await fetch('/api/teacher/groups', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        teacher_id: state.currentUser.id,
        group_name: name,
        subject_id: subjectId,
        invite_code: customCode || null,
        description: "Rasmiy sinf guruhi"
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('correct');
      alert(`🎉 Guruh yaratildi! O'quvchilarga taklif kodini bering: ${data.invite_code}`);
      closeModal('createGroupModal');
      document.getElementById('newGroupName').value = '';
      document.getElementById('newGroupInviteCode').value = '';
      loadTeacherPortalData();
    } else {
      playSound('wrong');
      alert(data.detail || "Guruh yaratishda xatolik!");
    }
  } catch (e) {
    alert("Guruh yaratishda server xatosi!");
  }
}

// ----------------- O'QUVCHILARNI BAHOLASH (STUDENT GRADING SYSTEM) -----------------
let activeGradingStudentId = null;

function getScoreBadgeClass(score) {
  const val = (score !== undefined && score !== null) ? Number(score) : 0;
  if (val >= 86) return 'score-badge-alo';
  if (val >= 71) return 'score-badge-yaxshi';
  if (val >= 56) return 'score-badge-qoniqarli';
  if (val > 0) return 'score-badge-qoniqarsiz';
  return 'score-badge-yangi';
}

function computeVisualGrade(score) {
  const val = Math.max(0, Math.min(100, Number(score) || 0));
  if (val >= 86) {
    return { text: "🟢 5 (A'lo) ⭐⭐⭐⭐⭐", color: "var(--accent-green)", label: "A'lo" };
  } else if (val >= 71) {
    return { text: "🔵 4 (Yaxshi) ⭐⭐⭐⭐", color: "#3b82f6", label: "Yaxshi" };
  } else if (val >= 56) {
    return { text: "🟡 3 (Qoniqarli) ⭐⭐⭐", color: "#f59e0b", label: "Qoniqarli" };
  } else if (val > 0) {
    return { text: "🔴 2 (Qoniqarsiz) ⭐⭐", color: "var(--accent-red)", label: "Qoniqarsiz" };
  } else {
    return { text: "⚪ 0 (Boshlang'ich)", color: "var(--text-muted)", label: "Boshlang'ich" };
  }
}

function updateVisualGradeDisplay(score) {
  const val = Math.max(0, Math.min(100, Number(score) || 0));
  const ballEl = document.getElementById('gradeVisualBallText');
  const letterEl = document.getElementById('gradeVisualLetterText');
  const info = computeVisualGrade(val);

  if (ballEl) ballEl.textContent = `${val} ball`;
  if (letterEl) {
    letterEl.textContent = info.text;
    letterEl.style.color = info.color;
  }
}

function openGradeStudentModal(studentId, studentName) {
  openStudentGradesHistoryModal(studentId, studentName);
}

async function openStudentGradesHistoryModal(studentId, studentName) {
  playSound('click');
  const modal = document.getElementById('studentGradesModal');
  const listContainer = document.getElementById('diaryGradesListContainer');

  document.getElementById('diaryStudentName').textContent = `📊 ${studentName} — Baholar Jurnali`;
  listContainer.innerHTML = '<div style="text-align:center; padding:18px; color:var(--text-muted); font-size:11px;">Baholar yuklanmoqda...</div>';
  modal.classList.add('active');

  try {
    const res = await fetch(`/api/student/${studentId}/grades`);
    const data = await res.json();

    if (!res.ok) {
      listContainer.innerHTML = `<div style="color:var(--accent-red); padding:10px;">${data.detail || 'Yuklashda xatolik'}</div>`;
      return;
    }

    // Set overall stats
    document.getElementById('diaryOverallScore').textContent = `${data.overall_average} / 100`;
    document.getElementById('diaryOverallLetter').textContent = `${data.overall_letter.grade} (${data.overall_letter.label}) ${data.overall_letter.stars}`;
    document.getElementById('diaryTotalGradesLabel').textContent = `${data.total_grades} ta baho kiritilgan`;

    document.getElementById('diaryCountAlo').textContent = data.breakdown.alo;
    document.getElementById('diaryCountYaxshi').textContent = data.breakdown.yaxshi;
    document.getElementById('diaryCountQoniqarli').textContent = data.breakdown.qoniqarli;
    document.getElementById('diaryCountQoniqarsiz').textContent = data.breakdown.qoniqarsiz;

    if (!data.grades || data.grades.length === 0) {
      listContainer.innerHTML = `
        <div class="minimal-card" style="text-align:center; padding:20px; font-size:11px; color:var(--text-muted);">
          Ushbu o'quvchiga hozircha baholar kiritilmagan.
        </div>
      `;
      return;
    }

    listContainer.innerHTML = data.grades.map(g => `
      <div class="grade-history-card">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:4px;">
          <div>
            <span style="font-size:11px; font-weight:800; color:#fff;">${escapeHtml(g.grade_type)}</span>
            <span style="font-size:10px; color:var(--text-muted); margin-left:4px;">• ${escapeHtml(g.subject_name || 'Fan')}</span>
          </div>
          <span class="score-badge-100 ${getScoreBadgeClass(g.score)}">${g.score} ball (${g.letter.grade})</span>
        </div>
        ${g.comment ? `<div style="font-size:11px; color:var(--text-secondary); margin:4px 0;">"${escapeHtml(g.comment)}"</div>` : ''}
        <div style="display:flex; justify-content:space-between; align-items:center; font-size:9px; color:var(--text-muted); margin-top:4px;">
          <span>Ustoz: <b style="color:var(--text-secondary);">${escapeHtml(g.teacher_name || 'Tizim testi')}</b></span>
          <span>${g.created_at ? g.created_at.split('T')[0] || g.created_at.substring(0, 10) : ''}</span>
        </div>
      </div>
    `).join('');
  } catch (e) {
    listContainer.innerHTML = '<div style="color:var(--accent-red); padding:10px;">Baholar tarixini yuklashda xatolik!</div>';
  }
}
