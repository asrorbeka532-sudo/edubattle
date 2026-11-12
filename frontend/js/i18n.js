// EduBattle Platform Multi-Language Localization (i18n)
// Supports: Uzbek (uz), Russian (ru), English (en)

const I18N_DICTIONARY = {
  uz: {
    // Brand & Header
    brand_title: "EDUBATTLE",
    role_student: "O'quvchi",
    role_teacher: "O'qituvchi",
    role_admin: "Administrator",
    btn_app: "📲 Ilova",
    btn_pro: "💎 PRO: 29 000 so'm",
    btn_back: "‹ Ortga",
    my_profile: "Mening profilim",

    // Navigation Tabs
    nav_home: "Asosiy",
    nav_library: "Darsliklar",
    nav_battle: "Batl",
    nav_friends: "Do'stlar",
    nav_profile: "Profil",
    nav_dashboard: "Kabinet",
    nav_quiz: "Viktorina",
    nav_students: "O'quvchilar",
    nav_new_subject: "Yangi Fan",

    // Home View
    greeting_default: "Salom",
    greeting_sub: "Maktab / Litsey",
    stat_grade: "O'rtacha Baho",
    stat_streak: "Faollik",
    banner_title: "Darsliklar & Testlar",
    banner_desc: "Fan bo'yicha darslik o'qing yoki testlar bilan bilimlaringizni oshiring",
    section_subjects: "Fanlar bo'yicha ta'lim",
    section_teacher_tests: "Ustozingiz bergan testlar",
    enter_test_pin: "Test Kodini kiriting...",
    enter_test_pass: "Test Paroli...",
    btn_start_test: "Testga Kirish ➔",
    join_group_title: "Sinf guruhiga a'zo bo'lish",
    enter_group_code: "Guruh taklif kodi...",
    btn_join_group: "Guruhga Qo'shilish",

    // Modals - Download
    modal_dl_title: "EduBattle Ilovasini O'rnatish",
    modal_dl_sub: "Android, iOS (iPhone) va Telegram bot",
    dl_android_name: "Android (.APK)",
    dl_android_badge: "Rasmiy ilova • 1.9 MB",
    btn_download: "Yuklab olish",
    dl_android_desc: "Faylni yuklab oling va telefonda oching, so'ng 'O'rnatish' (Install) tugmasini bosing.",
    dl_ios_title: "iPhone / iPad (iOS)",
    dl_ios_sub: "Safari orqali 10 soniyada Bosh ekranga o'rnatish",
    dl_ios_step1: "Saytni Safari brauzerida oching.",
    dl_ios_step2: "Pastdagi 'Ulashish' (Share ⬆️) belgisini bosing.",
    dl_ios_step3: "'Bosh ekranga qo'shish' (Add to Home Screen ➕) ni tanlang.",
    dl_ios_step4: "'Qo'shish' (Add) tugmasini bosing — tayyor!",
    dl_tg_title: "Telegram Bot",
    btn_open_bot: "Botni ochish",

    // Modals - Auth
    modal_auth_title: "EduBattle Ta'lim Platformasi",
    modal_auth_sub: "Kiber-himoyalangan xavfsiz tizim",
    tab_login: "Kirish",
    tab_register: "Ro'yxatdan O'tish",
    tab_forgot: "Parolni Tiklash",
    label_login_user: "Foydalanuvchi nomi / Tizim ID (Login):",
    ph_login_user: "Masalan: EB-74921 yoki login",
    label_password: "Parol:",
    ph_password: "Parolingizni kiriting...",
    forgot_link: "Parolni unutdingizmi?",
    btn_submit_login: "Kirish ➔",
    no_account: "Akkauntingiz yo'qmi?",
    label_fullname: "F.I.Sh (Ism va Familiya):",
    ph_fullname: "Masalan: Sardor Aliyev",
    label_auto_id: "Tizim IDsi (Loginingiz - Avtomatik):",
    btn_refresh: "🎲 Yangilash",
    auto_id_hint: "* Tizim siz uchun avtomatik takrorlanmas ID yaratdi. Buni eslab qoling!",
    label_tg_verify: "✈️ Telegram orqali tasdiqlash:",
    ph_tg_user: "@username yoki telefon raqamingiz",
    btn_get_code: "Kod olish 📨",
    tg_verify_hint: "Telegram botimiz orqali 6-xonali tasdiqlash kodi beriladi.",
    label_otp_code: "Telegram orqali kelgan 6-xonali kod:",
    label_your_role: "Sizning rolingiz:",
    label_grade: "Sinfingiz:",
    label_school: "Maktab yoki Litsey:",
    ph_school: "Masalan: 172-maktab",
    btn_submit_register: "Ro'yxatdan O'tish ➔",
    forgot_box_title: "🔐 Parolni Telegram orqali tiklash",
    forgot_box_desc: "Loginingiz (Tizim IDsi) yoki Telegram akkauntingizni kiriting. @edubattleuz_bot orqali 6-xonali tiklash kodi beriladi.",
    label_forgot_user: "Tizim ID (Login) yoki @username:",
    label_reset_code: "6-xonali Tiklash Kodi:",
    label_new_pass: "Yangi Parol:",
    ph_new_pass: "Kamida 4 ta belgi",
    btn_save_new_pass: "✅ Parolni Yangilash va Saqlash",
    btn_back_to_login: "‹ Kirish oynasiga qaytish",

    // Action Hub & Reader
    action_read_book: "Darslikni O'qish",
    action_read_book_desc: "Kitob qismlari, qoidalar va formulalar",
    action_take_quiz: "Test Ishlash",
    action_take_quiz_desc: "Mavzular bo'yicha bilimlarni sinash",
    btn_start_battle: "⚔️ Ushbu fan bo'yicha Batl boshlash",
    battle_emotions_title: "His-tuyg'ular & Stikerlar",
    btn_see_all_books: "Barcha darsliklarni ko'rish ➔",
    grade_selector_sub: "Sinfingiz yoki bosqichni tanlang:",

    // Teacher View
    teacher_portal_title: "O'qituvchi Boshqaruv Markazi",
    teacher_groups_title: "Mening Sinf Guruhlarim",
    btn_create_group: "+ Yangi Guruh",
    teacher_quizzes_title: "Yaratilgan Testlar",
    btn_create_quiz: "+ Test Tuzish",
    btn_upload_book: "+ Darslik Yuklash",
    group_students_title: "O'quvchilar Ro'yxati",
    theme_title: "Tizim Ko'rinishi (Mavzu)",
    theme_dark: "Qorong'u rejim (Dark Mode)",
    theme_light: "Yoruq rejim (Light Mode)"
  },

  ru: {
    // Brand & Header
    brand_title: "EDUBATTLE",
    role_student: "Ученик",
    role_teacher: "Учитель",
    role_admin: "Администратор",
    btn_app: "📲 Приложение",
    btn_pro: "💎 PRO: 29 000 сум",
    btn_back: "‹ Назад",
    my_profile: "Мой профиль",

    // Navigation Tabs
    nav_home: "Главная",
    nav_library: "Учебники",
    nav_battle: "Битва",
    nav_friends: "Друзья",
    nav_profile: "Профиль",
    nav_dashboard: "Кабинет",
    nav_quiz: "Викторина",
    nav_students: "Ученики",
    nav_new_subject: "Новый предмет",

    // Home View
    greeting_default: "Привет",
    greeting_sub: "Школа / Лицей",
    stat_grade: "Средний балл",
    stat_streak: "Ударный режим",
    banner_title: "Учебники и Тесты",
    banner_desc: "Читайте учебники и проверяйте знания интерактивными тестами",
    section_subjects: "Обучение по предметам",
    section_teacher_tests: "Тесты от вашего учителя",
    enter_test_pin: "Введите код теста...",
    enter_test_pass: "Пароль теста...",
    btn_start_test: "Начать тест ➔",
    join_group_title: "Вступить в группу класса",
    enter_group_code: "Код группы...",
    btn_join_group: "Вступить в группу",

    // Modals - Download
    modal_dl_title: "Установка приложения EduBattle",
    modal_dl_sub: "Android, iOS (iPhone) и Telegram бот",
    dl_android_name: "Android (.APK)",
    dl_android_badge: "Официальное приложение • 1.9 МБ",
    btn_download: "Скачать",
    dl_android_desc: "Скачайте APK файл и откройте на телефоне, затем нажмите 'Установить'.",
    dl_ios_title: "iPhone / iPad (iOS)",
    dl_ios_sub: "Установка на главный экран через Safari за 10 секунд",
    dl_ios_step1: "Откройте сайт в браузере Safari.",
    dl_ios_step2: "Нажмите кнопку 'Поделиться' (Share ⬆️) внизу.",
    dl_ios_step3: "Выберите 'На экран «Домой»' (Add to Home Screen ➕).",
    dl_ios_step4: "Нажмите 'Добавить' (Add) — готово!",
    dl_tg_title: "Telegram Бот",
    btn_open_bot: "Открыть бота",

    // Modals - Auth
    modal_auth_title: "Образовательная платформа EduBattle",
    modal_auth_sub: "Кибер-защищенная безопасная система",
    tab_login: "Вход",
    tab_register: "Регистрация",
    tab_forgot: "Сброс пароля",
    label_login_user: "Имя пользователя / ID системы (Логин):",
    ph_login_user: "Например: EB-74921 или логин",
    label_password: "Пароль:",
    ph_password: "Ваш пароль...",
    forgot_link: "Забыли пароль?",
    btn_submit_login: "Войти ➔",
    no_account: "Нет аккаунта?",
    label_fullname: "Ф.И.О (Имя и Фамилия):",
    ph_fullname: "Например: Сардор Алиев",
    label_auto_id: "ID системы (Логин - Автоматически):",
    btn_refresh: "🎲 Обновить",
    auto_id_hint: "* Система создала для вас уникальный ID. Запомните его!",
    label_tg_verify: "✈️ Подтверждение через Telegram:",
    ph_tg_user: "@username или номер телефона",
    btn_get_code: "Получить код 📨",
    tg_verify_hint: "Через нашего бота будет отправлен 6-значный код подтверждения.",
    label_otp_code: "6-значный код из Telegram:",
    label_your_role: "Ваша роль:",
    label_grade: "Класс / Курс:",
    label_school: "Школа или Лицей:",
    ph_school: "Например: Школа №172",
    btn_submit_register: "Зарегистрироваться ➔",
    forgot_box_title: "🔐 Восстановление пароля через Telegram",
    forgot_box_desc: "Введите ваш логин (ID системы) или Telegram username. Через @edubattleuz_bot вы получите 6-значный код сброса.",
    label_forgot_user: "ID системы (Логин) или @username:",
    label_reset_code: "6-значный код сброса:",
    label_new_pass: "Новый пароль:",
    ph_new_pass: "Минимум 4 символа",
    btn_save_new_pass: "✅ Обновить и сохранить пароль",
    btn_back_to_login: "‹ Вернуться ко входу",

    // Action Hub & Reader
    action_read_book: "Читать учебник",
    action_read_book_desc: "Главы книги, правила и формулы",
    action_take_quiz: "Пройти тест",
    action_take_quiz_desc: "Проверка знаний по темам",
    btn_start_battle: "⚔️ Начать битву по этому предмету",
    battle_emotions_title: "Эмоции & Стикеры",
    btn_see_all_books: "Все учебники предмета ➔",
    grade_selector_sub: "Выберите ваш класс или уровень:",

    // Teacher View
    teacher_portal_title: "Панель управления учителя",
    teacher_groups_title: "Мои группы классов",
    btn_create_group: "+ Новая группа",
    teacher_quizzes_title: "Созданные тесты",
    btn_create_quiz: "+ Создать тест",
    btn_upload_book: "+ Загрузить учебник",
    group_students_title: "Ученики и Журнал оценок",
    theme_title: "Оформление системы (Тема)",
    theme_dark: "Темная тема (Dark Mode)",
    theme_light: "Светлая тема (Light Mode)"
  },

  en: {
    // Brand & Header
    brand_title: "EDUBATTLE",
    role_student: "Student",
    role_teacher: "Teacher",
    role_admin: "Administrator",
    btn_app: "📲 App",
    btn_pro: "💎 PRO: 29,000 UZS",
    btn_back: "‹ Back",
    my_profile: "My Profile",

    // Navigation Tabs
    nav_home: "Home",
    nav_library: "Textbooks",
    nav_battle: "Battle",
    nav_friends: "Friends",
    nav_profile: "Profile",
    nav_dashboard: "Dashboard",
    nav_quiz: "Quiz",
    nav_students: "Students",
    nav_new_subject: "New Subject",

    // Home View
    greeting_default: "Hello",
    greeting_sub: "School / Lyceum",
    stat_grade: "Average Grade",
    stat_streak: "Daily Streak",
    banner_title: "Textbooks & Quizzes",
    banner_desc: "Read textbooks and master concepts through interactive quizzes",
    section_subjects: "Subjects & Learning",
    section_teacher_tests: "Assigned Quizzes from Teacher",
    enter_test_pin: "Enter quiz PIN...",
    enter_test_pass: "Quiz passcode...",
    btn_start_test: "Start Quiz ➔",
    join_group_title: "Join Class Group",
    enter_group_code: "Group invite code...",
    btn_join_group: "Join Group",

    // Modals - Download
    modal_dl_title: "Install EduBattle App",
    modal_dl_sub: "Android, iOS (iPhone) and Telegram Bot",
    dl_android_name: "Android (.APK)",
    dl_android_badge: "Official App • 1.9 MB",
    btn_download: "Download",
    dl_android_desc: "Download the APK file and open on your device, then tap 'Install'.",
    dl_ios_title: "iPhone / iPad (iOS)",
    dl_ios_sub: "Install to Home Screen via Safari in 10 seconds",
    dl_ios_step1: "Open this site in Safari browser.",
    dl_ios_step2: "Tap the 'Share' (⬆️) button at the bottom.",
    dl_ios_step3: "Select 'Add to Home Screen' (➕).",
    dl_ios_step4: "Tap 'Add' in the top right — all set!",
    dl_tg_title: "Telegram Bot",
    btn_open_bot: "Open Bot",

    // Modals - Auth
    modal_auth_title: "EduBattle Learning Platform",
    modal_auth_sub: "Cyber-protected secure education ecosystem",
    tab_login: "Sign In",
    tab_register: "Sign Up",
    tab_forgot: "Reset Password",
    label_login_user: "Username / System ID (Login):",
    ph_login_user: "e.g., EB-74921 or username",
    label_password: "Password:",
    ph_password: "Your password...",
    forgot_link: "Forgot password?",
    btn_submit_login: "Sign In ➔",
    no_account: "Don't have an account?",
    label_fullname: "Full Name:",
    ph_fullname: "e.g., Sardor Aliyev",
    label_auto_id: "System ID (Login - Auto Generated):",
    btn_refresh: "🎲 Refresh",
    auto_id_hint: "* The system generated a unique ID for you. Keep it handy!",
    label_tg_verify: "✈️ Telegram Verification:",
    ph_tg_user: "@username or phone number",
    btn_get_code: "Get Code 📨",
    tg_verify_hint: "A 6-digit confirmation code will be sent via our Telegram bot.",
    label_otp_code: "6-digit code from Telegram:",
    label_your_role: "Your Role:",
    label_grade: "Grade / Year:",
    label_school: "School or Lyceum:",
    ph_school: "e.g., School No. 172",
    btn_submit_register: "Create Account ➔",
    forgot_box_title: "🔐 Password Reset via Telegram",
    forgot_box_desc: "Enter your System ID (Login) or Telegram username. You will receive a 6-digit reset code via @edubattleuz_bot.",
    label_forgot_user: "System ID (Login) or @username:",
    label_reset_code: "6-digit Reset Code:",
    label_new_pass: "New Password:",
    ph_new_pass: "At least 4 characters",
    btn_save_new_pass: "✅ Save New Password",
    btn_back_to_login: "‹ Back to Sign In",

    // Action Hub & Reader
    action_read_book: "Read Textbook",
    action_read_book_desc: "Chapters, rules and formulas",
    action_take_quiz: "Take Quiz",
    action_take_quiz_desc: "Test knowledge across topics",
    btn_start_battle: "⚔️ Start Battle for Subject",
    battle_emotions_title: "Emotions & Stickers",
    btn_see_all_books: "View All Textbooks ➔",
    grade_selector_sub: "Select your grade or course level:",

    // Teacher View
    teacher_portal_title: "Teacher Dashboard",
    teacher_groups_title: "My Class Groups",
    btn_create_group: "+ New Group",
    teacher_quizzes_title: "Created Quizzes",
    btn_create_quiz: "+ Create Quiz",
    btn_upload_book: "+ Upload Textbook",
    group_students_title: "Students & Grading Journal",
    theme_title: "Theme Appearance",
    theme_dark: "Dark Mode",
    theme_light: "Light Mode"
  }
};

let currentLang = localStorage.getItem('edubattle_lang') || 'uz';

function t(key, fallback = '') {
  const dict = I18N_DICTIONARY[currentLang] || I18N_DICTIONARY.uz;
  return dict[key] !== undefined ? dict[key] : (I18N_DICTIONARY.uz[key] || fallback || key);
}

function setAppLanguage(lang) {
  if (!['uz', 'ru', 'en'].includes(lang)) lang = 'uz';
  currentLang = lang;
  localStorage.setItem('edubattle_lang', lang);
  document.documentElement.lang = lang;

  // Update header dropdown label
  const labelEl = document.getElementById('currentLangLabel');
  if (labelEl) labelEl.innerText = lang.toUpperCase();

  // Update active state in dropdown
  document.querySelectorAll('.lang-option').forEach(el => {
    if (el.getAttribute('data-lang') === lang) el.classList.add('active');
    else el.classList.remove('active');
  });

  // Close dropdown menu
  const menu = document.getElementById('langDropdownMenu');
  if (menu) menu.classList.remove('active');

  // Translate all DOM elements with data-i18n
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    const val = t(key);
    if (val) el.innerText = val;
  });

  // Translate all placeholders with data-i18n-ph
  document.querySelectorAll('[data-i18n-ph]').forEach(el => {
    const key = el.getAttribute('data-i18n-ph');
    const val = t(key);
    if (val) el.placeholder = val;
  });

  // Re-render role bottom nav and header if available
  if (typeof updateBottomNavForRole === 'function' && window.state && window.state.currentUser) {
    updateBottomNavForRole(window.state.currentUser.role);
  }
  if (typeof updateHeaderAndProfileUI === 'function') {
    updateHeaderAndProfileUI();
  }
  if (typeof applyTheme === 'function') {
    applyTheme(document.documentElement.getAttribute('data-theme') || 'dark');
  }

  // Dispatch global language change event
  window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));

  // Sync to user profile on server if logged in
  if (window.state && window.state.token) {
    fetch('/api/user/language?token=' + encodeURIComponent(window.state.token), {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ lang: lang })
    }).catch(function(e) { /* background sync */ });
  }
}

function toggleLangDropdown() {
  const menu = document.getElementById('langDropdownMenu');
  if (menu) menu.classList.toggle('active');
}

// Close dropdown on outside click
document.addEventListener('click', function(e) {
  const dropdown = document.querySelector('.lang-selector-dropdown');
  if (dropdown && !dropdown.contains(e.target)) {
    const menu = document.getElementById('langDropdownMenu');
    if (menu) menu.classList.remove('active');
  }
});

// Auto-initialize language on page load
document.addEventListener('DOMContentLoaded', () => {
  setAppLanguage(currentLang);
});
