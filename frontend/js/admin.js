// ========================================================
// ZUKKO EDUBATTLE - SUPER ADMIN PANEL CONTROLLER
// Complete system control: Users, PRO toggles, Questions, Textbooks
// ========================================================

async function loadAdminDashboard() {
  try {
    const res = await fetch('/api/admin/stats');
    const stats = await res.json();

    document.getElementById('adminStatStudents').textContent = stats.students;
    document.getElementById('adminStatTeachers').textContent = stats.teachers;
    document.getElementById('adminStatPro').textContent = stats.pro_users;
    document.getElementById('adminStatQuestions').textContent = stats.questions;

    await loadAdminUsersList();
  } catch (e) {
    console.error('Load admin dashboard error:', e);
  }
}

function switchAdminTab(tabName, btnElement) {
  playSound('click');
  document.querySelectorAll('#view-admin .btn-sm').forEach(b => b.classList.remove('active'));
  if (btnElement) btnElement.classList.add('active');

  const tabs = ['UploadResource', 'Users', 'AddQ'];
  tabs.forEach(t => {
    const el = document.getElementById(`adminTab${t}`);
    if (el) el.style.display = 'none';
  });

  const map = {
    'upload-resource': 'adminTabUploadResource',
    'users': 'adminTabUsers',
    'add-q': 'adminTabAddQ'
  };

  const target = document.getElementById(map[tabName]);
  if (target) target.style.display = 'block';
}

// ----------------- USERS MANAGEMENT & PRO TOGGLES -----------------
async function loadAdminUsersList() {
  const container = document.getElementById('adminUsersList');
  if (!container) return;

  try {
    const res = await fetch('/api/users');
    const users = await res.json();

    container.innerHTML = users.map(u => `
      <div style="display:flex; align-items:center; justify-content:space-between; padding:10px 8px; border-bottom:1px solid var(--border-subtle);">
        <div style="display:flex; align-items:center; gap:10px;">
          <span style="font-size:18px;">${u.role === 'teacher' ? '👨‍🏫' : (u.role === 'admin' ? '🛡️' : '👤')}</span>
          <div>
            <div style="font-size:13px; font-weight:700;">
              ${u.full_name} 
              <span class="badge badge-subtle" style="font-size:9px;">${u.role.toUpperCase()}</span>
            </div>
            <div style="font-size:10px; color:var(--text-muted);">${u.school_lyceum || 'Maktab'} • ${u.grade || ''} • ${(u.coins || 0).toLocaleString()} 🪙</div>
          </div>
        </div>
        <div style="display:flex; align-items:center; gap:6px;">
          <button class="btn btn-sm ${u.is_pro ? 'btn-purple' : 'btn-outline'}" onclick="adminToggleUserPro(${u.id}, this)">
            ${u.is_pro ? '💎 PRO (29 000)' : '➕ PRO Berish'}
          </button>
          <button class="btn btn-sm btn-outline" onclick="adminDeleteUser(${u.id}, '${escapeHtml(u.full_name)}')" style="border-color:#ef4444; color:#ef4444; font-weight:700;">
            🗑️ O'chirish
          </button>
        </div>
      </div>
    `).join('');
  } catch (e) {
    console.error(e);
  }
}

async function adminToggleUserPro(userId, btn) {
  playSound('click');
  try {
    const res = await fetch('/api/admin/toggle-pro', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId })
    });
    const data = await res.json();
    if (data.success) {
      playSound('correct');
      loadAdminDashboard();
    }
  } catch (e) {
    console.error(e);
  }
}

async function adminDeleteUser(userId, userName) {
  if (!confirm(`⚠️ DIQQAT!\n\n"${userName}" (ID: ${userId}) ni platformadan butunlay o'chirmoqchimisiz?`)) {
    return;
  }
  playSound('click');
  try {
    const res = await fetch(`/api/admin/users/${userId}?secret=asoee321`, {
      method: 'DELETE'
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('victory');
      alert(`✅ ${data.message || 'Muvaffaqiyatli o\'chirildi!'}`);
      loadAdminDashboard();
    } else {
      alert(data.detail || data.message || "O'chirishda xatolik yuz berdi!");
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik!");
  }
}

// ----------------- UPLOAD RESOURCE (READY FOR USER'S BOOK FILES) -----------------
async function submitAdminUploadedResource() {
  const subjectId = parseInt(document.getElementById('uploadResourceSubject').value) || 1;
  const grade = document.getElementById('uploadResourceGrade').value;
  const title = (document.getElementById('uploadResourceTitle').value || '').trim();
  const author = (document.getElementById('uploadResourceAuthor').value || '').trim() || "Mualliflar guruhi";
  const content = (document.getElementById('uploadResourceContent').value || '').trim();

  if (!title) {
    alert("Iltimos, darslik yoki manba nomini kiriting!");
    return;
  }

  const defaultChapters = [
    {
      title: `${title} - Asosiy konspekt`,
      summary: content || "Mavzular bo'yicha tayanch nazariy ma'lumotlar va qoidalar.",
      key_rules: ["Muhim qoidalar", "Formulalar"]
    }
  ];

  try {
    const res = await fetch('/api/admin/add-book', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        subject_id: subjectId,
        title: title,
        author: author,
        grade: grade,
        summary: content ? content.slice(0, 180) + '...' : 'Darslik tavsifi',
        chapters: defaultChapters
      })
    });
    if (res.ok) {
      playSound('correct');
      alert(`✅ "${title}" darsligi ${grade} uchun bazaga muvaffaqiyatli kiritildi! Siz yuboradigan keyingi resurslar va testlar ham shu tartibda sinflar bo'yicha joylashtiriladi.`);
      document.getElementById('uploadResourceTitle').value = '';
      document.getElementById('uploadResourceContent').value = '';
      loadAdminDashboard();
      loadTextbooks();
    }
  } catch (e) {
    console.error(e);
  }
}

// ----------------- ADD QUESTION -----------------
async function submitAdminNewQuestion() {
  const subjectId = parseInt(document.getElementById('adminQSubject').value) || 1;
  const chapter = (document.getElementById('adminQChapter').value || '').trim() || 'Umumiy mavzu';
  const text = (document.getElementById('adminQText').value || '').trim();
  const opt0 = (document.getElementById('adminQOpt0').value || '').trim();
  const opt1 = (document.getElementById('adminQOpt1').value || '').trim();
  const opt2 = (document.getElementById('adminQOpt2').value || '').trim();
  const opt3 = (document.getElementById('adminQOpt3').value || '').trim();
  const correctIdx = parseInt(document.getElementById('adminQCorrect').value) || 0;

  if (!text || !opt0 || !opt1) {
    alert("Iltimos, savol matni va kamida 2 ta variantni kiriting!");
    return;
  }

  const options = [opt0, opt1, opt2 || 'Variant C', opt3 || 'Variant D'];

  try {
    const res = await fetch('/api/admin/add-question', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        subject_id: subjectId,
        chapter_title: chapter,
        question_text: text,
        options: options,
        correct_index: correctIdx,
        explanation: "To'g'ri javob asoslandi.",
        difficulty: 'orta'
      })
    });
    if (res.ok) {
      playSound('correct');
      alert("✅ Yangi test savoli muvaffaqiyatli qo'shildi!");
      document.getElementById('adminQText').value = '';
      document.getElementById('adminQOpt0').value = '';
      document.getElementById('adminQOpt1').value = '';
      document.getElementById('adminQOpt2').value = '';
      document.getElementById('adminQOpt3').value = '';
      loadAdminDashboard();
    }
  } catch (e) {
    console.error(e);
  }
}
