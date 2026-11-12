# -*- coding: utf-8 -*-
"""
EduBattle - 2020-2023 Yangi darsliklar asosidagi savollar banki:
Fan 1: Matematika (Algebra va Geometriya 7-11-sinf) - 50 ta savol
Fan 2: Fizika (7-11-sinf yangi nashrlar) - 50 ta savol
"""

# ==========================================
# 1. MATEMATIKA (Subject ID: 1) - 50 TA SAVOL
# ==========================================
MATEMATIKA_QUESTIONS = [
    # 7-sinf
    {
        "subject_id": 1,
        "grade": "7-sinf",
        "chapter_title": "Chiziqli tenglamalar",
        "question_text": "3x - 14 = 2x + 7 tenglamaning ildizini toping.",
        "options": ["21", "-7", "14", "-21"],
        "correct_index": 0,
        "explanation": "3x - 2x = 7 + 14 => x = 21.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "7-sinf",
        "chapter_title": "Qisqa ko'paytirish formulalari",
        "question_text": "(a + 3b)² ifodani ko'phad shaklida yozing.",
        "options": ["a² + 6ab + 9b²", "a² + 3ab + 9b²", "a² + 9b²", "a² + 6ab + 3b²"],
        "correct_index": 0,
        "explanation": "(a + b)² = a² + 2ab + b² formulaga ko'ra: a² + 2*a*(3b) + (3b)² = a² + 6ab + 9b².",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "7-sinf",
        "chapter_title": "Qisqa ko'paytirish formulalari",
        "question_text": "49x² - 64 ifodani ko'paytuvchilarga ajrating.",
        "options": ["(7x - 8)(7x + 8)", "(7x - 8)²", "(49x - 8)(x + 8)", "(7x - 32)(7x + 2)"],
        "correct_index": 0,
        "explanation": "Kvadratlar ayirmasi: a² - b² = (a - b)(a + b). Shuning uchun (7x - 8)(7x + 8).",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "7-sinf",
        "chapter_title": "Birhadlar va ko'phadlar",
        "question_text": "(-3a²b³)³ birhadning standart shaklini toping.",
        "options": ["-27a⁶b⁹", "27a⁶b⁹", "-9a⁵b⁶", "-27a⁵b⁶"],
        "correct_index": 0,
        "explanation": "(-3)³ * (a²)³ * (b³)³ = -27 * a⁶ * b⁹.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "7-sinf",
        "chapter_title": "Burchaklar va ularning xossalari",
        "question_text": "Qo'shni burchaklardan biri ikkinchisidan 40° ga katta. Kichik burchakni toping.",
        "options": ["70°", "110°", "60°", "80°"],
        "correct_index": 0,
        "explanation": "x + (x + 40°) = 180° => 2x = 140° => x = 70°.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "7-sinf",
        "chapter_title": "Uchburchak burchaklari",
        "question_text": "To'g'ri burchakli uchburchakning o'tkir burchaklaridan biri 37° ga teng. Ikkinchi o'tkir burchakni toping.",
        "options": ["53°", "63°", "43°", "143°"],
        "correct_index": 0,
        "explanation": "To'g'ri burchakli uchburchakda o'tkir burchaklar yig'indisi 90° ga teng: 90° - 37° = 53°.",
        "difficulty": "oson"
    },
    # 8-sinf
    {
        "subject_id": 1,
        "grade": "8-sinf",
        "chapter_title": "Kvadrat tenglamalar",
        "question_text": "x² - 9x + 20 = 0 tenglamaning ildizlari yig'indisini Viyet teoremasiga ko'ra toping.",
        "options": ["9", "-9", "20", "-20"],
        "correct_index": 0,
        "explanation": "Viyet teoremasiga asosan keltirilgan kvadrat tenglamada x₁ + x₂ = -p = 9.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "8-sinf",
        "chapter_title": "Kvadrat tenglamalar",
        "question_text": "2x² - 5x + 2 = 0 tenglamaning diskriminantini hisoblang.",
        "options": ["9", "1", "17", "41"],
        "correct_index": 0,
        "explanation": "D = b² - 4ac = (-5)² - 4*2*2 = 25 - 16 = 9.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "8-sinf",
        "chapter_title": "Algebraik kasrlar",
        "question_text": "(x² - 4) / (x - 2) kasrni qisqartiring (x ≠ 2).",
        "options": ["x + 2", "x - 2", "x + 4", "1"],
        "correct_index": 0,
        "explanation": "(x - 2)(x + 2) / (x - 2) = x + 2.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "8-sinf",
        "chapter_title": "Kvadrat ildizlar",
        "question_text": "√(75) - √(12) ifodaning qiymatini soddalashtiring.",
        "options": ["3√3", "2√3", "5√3", "√63"],
        "correct_index": 0,
        "explanation": "√(25*3) - √(4*3) = 5√3 - 2√3 = 3√3.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "8-sinf",
        "chapter_title": "Pifagor teoremasi",
        "question_text": "To'g'ri burchakli uchburchakning katetlari 6 cm va 8 cm ga teng. Uning gipotenuzasini toping.",
        "options": ["10 cm", "12 cm", "14 cm", "100 cm"],
        "correct_index": 0,
        "explanation": "c² = a² + b² = 6² + 8² = 36 + 64 = 100 => c = 10 cm.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "8-sinf",
        "chapter_title": "Parallelogramm va to'rtburchaklar",
        "question_text": "Rombning diagonallari 12 cm va 16 cm ga teng. Rombning yuzini hisoblang.",
        "options": ["96 cm²", "192 cm²", "48 cm²", "100 cm²"],
        "correct_index": 0,
        "explanation": "Romb yuzi S = (d₁ * d₂) / 2 = (12 * 16) / 2 = 96 cm².",
        "difficulty": "orta"
    },
    # 9-sinf
    {
        "subject_id": 1,
        "grade": "9-sinf",
        "chapter_title": "Arifmetik progressiya",
        "question_text": "Arifmetik progressiyada a₁ = 3, d = 4 bo'lsa, a₁₀ ni toping.",
        "options": ["39", "43", "36", "40"],
        "correct_index": 0,
        "explanation": "a₁₀ = a₁ + 9d = 3 + 9*4 = 3 + 36 = 39.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "9-sinf",
        "chapter_title": "Arifmetik progressiya",
        "question_text": "Dastlabki 20 ta natural sonning yig'indisini toping.",
        "options": ["210", "200", "190", "420"],
        "correct_index": 0,
        "explanation": "S₂₀ = (1 + 20)*20 / 2 = 21 * 10 = 210.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "9-sinf",
        "chapter_title": "Geometrik progressiya",
        "question_text": "Geometrik progressiyada b₁ = 2, q = 3 bo'lsa, b₄ ni toping.",
        "options": ["54", "18", "162", "24"],
        "correct_index": 0,
        "explanation": "b₄ = b₁ * q³ = 2 * 3³ = 2 * 27 = 54.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "9-sinf",
        "chapter_title": "Kvadratik funksiya",
        "question_text": "y = x² - 6x + 5 parabolaning uchining koordinatalarini toping.",
        "options": ["(3; -4)", "(-3; -4)", "(3; 4)", "(-3; 4)"],
        "correct_index": 0,
        "explanation": "x₀ = -b / (2a) = 6 / 2 = 3. y₀ = 3² - 6*3 + 5 = 9 - 18 + 5 = -4. Demak (3; -4).",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "9-sinf",
        "chapter_title": "Kombinatorika",
        "question_text": "5 nafar o'quvchini bitta qatorga necha xil usulda o'tqazish mumkin (5!)?",
        "options": ["120", "24", "60", "720"],
        "correct_index": 0,
        "explanation": "P₅ = 5! = 5 * 4 * 3 * 2 * 1 = 120.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "9-sinf",
        "chapter_title": "Aylana va doira",
        "question_text": "Radiusi 5 cm bo'lgan aylananing uzunligini toping (π deb oling).",
        "options": ["10π cm", "25π cm", "5π cm", "20π cm"],
        "correct_index": 0,
        "explanation": "Aylana uzunligi C = 2πR = 2 * π * 5 = 10π cm.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "9-sinf",
        "chapter_title": "Trigonometriya boshlang'ich tushunchalari",
        "question_text": "sin²α + cos²α ifodaning qiymati nimaga teng?",
        "options": ["1", "0", "2", "-1"],
        "correct_index": 0,
        "explanation": "Asosiy trigonometrik ayniyatga ko'ra barcha α burchaklar uchun sin²α + cos²α = 1.",
        "difficulty": "oson"
    },
    # 10-sinf
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Trigonometriya",
        "question_text": "sin 150° ning aniq qiymatini toping.",
        "options": ["1/2", "√3/2", "-1/2", "-√3/2"],
        "correct_index": 0,
        "explanation": "sin 150° = sin(180° - 30°) = sin 30° = 1/2.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Trigonometriya",
        "question_text": "cos 2α ning asosiy formulalaridan birini ko'rsating.",
        "options": ["cos²α - sin²α", "cos²α + sin²α", "2cosα * sinα", "1 - sin²α"],
        "correct_index": 0,
        "explanation": "Ikkilangan burchak kosinusi: cos 2α = cos²α - sin²α = 2cos²α - 1 = 1 - 2sin²α.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Ko'rsatkichli tenglamalar",
        "question_text": "2^(x+3) = 32 tenglamaning ildizini toping.",
        "options": ["2", "3", "5", "1"],
        "correct_index": 0,
        "explanation": "32 = 2⁵ bo'lgani uchun: x + 3 = 5 => x = 2.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Logarifm",
        "question_text": "log₂ 64 ning qiymatini hisoblang.",
        "options": ["6", "8", "5", "32"],
        "correct_index": 0,
        "explanation": "2⁶ = 64 bo'lgani sababli log₂ 64 = 6.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Logarifm xossalari",
        "question_text": "log₃ 18 - log₃ 2 ifodani hisoblang.",
        "options": ["2", "3", "9", "1"],
        "correct_index": 0,
        "explanation": "log₃(18 / 2) = log₃ 9 = 2.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Stereometriya",
        "question_text": "Qirrasi 4 cm bo'lgan kubning hajmini toping.",
        "options": ["64 cm³", "96 cm³", "48 cm³", "16 cm³"],
        "correct_index": 0,
        "explanation": "Kub hajmi V = a³ = 4³ = 64 cm³.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Stereometriya",
        "question_text": "To'g'ri to'rtburchakli parallelepipedning o'lchamlari 3, 4 va 5 ga teng. Uning to'la sirtini toping.",
        "options": ["94", "60", "47", "120"],
        "correct_index": 0,
        "explanation": "S = 2(ab + bc + ac) = 2(3*4 + 4*5 + 3*5) = 2(12 + 20 + 15) = 2 * 47 = 94.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Ko'rsatkichli tengsizliklar",
        "question_text": "(1/3)^x > 9 tengsizlikni yeching.",
        "options": ["x < -2", "x > -2", "x > 2", "x < 2"],
        "correct_index": 0,
        "explanation": "(3⁻¹)^x > 3² => 3^(-x) > 3² => -x > 2 => x < -2.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Trigonometrik tenglamalar",
        "question_text": "sin x = 0 tenglamaning umumiy yechimini ko'rsating.",
        "options": ["x = πk, k ∈ Z", "x = π/2 + πk, k ∈ Z", "x = 2πk, k ∈ Z", "x = π/2 + 2πk, k ∈ Z"],
        "correct_index": 0,
        "explanation": "Sinus qiymati x = 0 da, π da, 2π da va hokazo 0 ga teng, ya'ni x = πk, k ∈ Z.",
        "difficulty": "orta"
    },
    # 11-sinf
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Hosila",
        "question_text": "f(x) = 4x³ - 5x² + 7x - 9 funksiyaning hosilasini toping.",
        "options": ["12x² - 10x + 7", "12x³ - 10x² + 7", "4x² - 5x + 7", "12x² - 5x + 7"],
        "correct_index": 0,
        "explanation": "f'(x) = 4*3x² - 5*2x + 7*1 - 0 = 12x² - 10x + 7.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Hosila va ekstremum",
        "question_text": "f(x) = x² - 8x + 12 funksiyaning minimum nuqtasini toping.",
        "options": ["x = 4", "x = -4", "x = 8", "x = 6"],
        "correct_index": 0,
        "explanation": "f'(x) = 2x - 8 = 0 => 2x = 8 => x = 4.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Hosilaning mexanik ma'nosi",
        "question_text": "Moddiy nuqta s(t) = 3t² + 2t + 5 qonun bo'yicha harakatlanmoqda. t = 2 sekunddagi tezlikni toping.",
        "options": ["14 m/s", "12 m/s", "10 m/s", "21 m/s"],
        "correct_index": 0,
        "explanation": "v(t) = s'(t) = 6t + 2. t = 2 bo'lganda v(2) = 6*2 + 2 = 14 m/s.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Urinma tenglamasi",
        "question_text": "y = x² funksiya grafigiga x₀ = 3 nuqtada o'tkazilgan urinmaning burchak koeffitsiyentini toping.",
        "options": ["6", "9", "3", "2"],
        "correct_index": 0,
        "explanation": "k = y'(x₀). y' = 2x, y'(3) = 2 * 3 = 6.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Boshlang'ich funksiya",
        "question_text": "f(x) = 6x² funksiyaning boshlang'ich funksiyalari umumiy ko'rinishini toping.",
        "options": ["2x³ + C", "3x³ + C", "12x + C", "6x³ + C"],
        "correct_index": 0,
        "explanation": "∫ 6x² dx = 6 * (x³ / 3) + C = 2x³ + C.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Aniq integral",
        "question_text": "∫₀² (3x²) dx aniq integralni hisoblang.",
        "options": ["8", "12", "6", "24"],
        "correct_index": 0,
        "explanation": "Boshlang'ich funksiya x³. Nyuton-Leybnits formulasi: 2³ - 0³ = 8.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Aylanish jismlari - Silindr",
        "question_text": "Asos radiusi 3 cm, balandligi 5 cm bo'lgan silindr hajmini toping (π deb oling).",
        "options": ["45π cm³", "15π cm³", "30π cm³", "90π cm³"],
        "correct_index": 0,
        "explanation": "V = πR²h = π * 3² * 5 = π * 9 * 5 = 45π cm³.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Aylanish jismlari - Konus",
        "question_text": "Asos radiusi 4 cm, balandligi 9 cm bo'lgan konus hajmini toping (π deb oling).",
        "options": ["48π cm³", "144π cm³", "36π cm³", "72π cm³"],
        "correct_index": 0,
        "explanation": "V = (1/3)πR²h = (1/3) * π * 16 * 9 = 48π cm³.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Aylanish jismlari - Shar",
        "question_text": "Radiusi 3 cm bo'lgan sharning sirt yuzini toping (π deb oling).",
        "options": ["36π cm²", "12π cm²", "27π cm²", "108π cm²"],
        "correct_index": 0,
        "explanation": "S = 4πR² = 4 * π * 3² = 36π cm².",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Ehtimollar nazariyasi",
        "question_text": "O'yin suyagi (zarik) bir marta tashlanganda juft son tushish ehtimolini toping.",
        "options": ["1/2", "1/3", "1/6", "2/3"],
        "correct_index": 0,
        "explanation": "Jami hollar 6 ta (1, 2, 3, 4, 5, 6). Qulay hollar 3 ta (2, 4, 6). P = 3/6 = 1/2.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Ehtimollar nazariyasi",
        "question_text": "Qutida 4 ta oq va 6 ta qora shar bor. Tavakkaliga olingan 1 ta sharning oq bo'lish ehtimoli qancha?",
        "options": ["0.4", "0.6", "0.25", "0.5"],
        "correct_index": 0,
        "explanation": "Jami sharlar 4 + 6 = 10 ta. Oq sharlar 4 ta. P = 4/10 = 0.4.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Vektorlar",
        "question_text": "a(3; -4) vektorning uzunligini (modulini) toping.",
        "options": ["5", "7", "1", "25"],
        "correct_index": 0,
        "explanation": "|a| = √(3² + (-4)²) = √(9 + 16) = √25 = 5.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Vektorlarning skalyar ko'paytmasi",
        "question_text": "a(2; 5) va b(4; -1) vektorlarning skalyar ko'paytmasini toping.",
        "options": ["3", "13", "8", "-5"],
        "correct_index": 0,
        "explanation": "a · b = x₁x₂ + y₁y₂ = 2*4 + 5*(-1) = 8 - 5 = 3.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "8-sinf",
        "chapter_title": "Tengsizliklar sistemasi",
        "question_text": "2x - 4 > 0 va 3x < 15 tengsizliklar sistemasining natural yechimlari nechta?",
        "options": ["2 ta", "3 ta", "4 ta", "1 ta"],
        "correct_index": 0,
        "explanation": "x > 2 va x < 5 => (2; 5) oralig'idagi natural sonlar: 3 va 4. Jami 2 ta.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "8-sinf",
        "chapter_title": "O'xshash uchburchaklar",
        "question_text": "Ikkita o'xshash uchburchakning o'xshashlik koeffitsiyenti k = 3 bo'lsa, ularning yuzlari nisbati nimaga teng?",
        "options": ["9", "3", "6", "27"],
        "correct_index": 0,
        "explanation": "O'xshash figuralar yuzlarining nisbati o'xshashlik koeffitsiyentining kvadratiga teng: k² = 3² = 9.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "7-sinf",
        "chapter_title": "Tenglamalar sistemasi",
        "question_text": "x + y = 10 va x - y = 4 tenglamalar sistemasidan x ni toping.",
        "options": ["7", "3", "8", "6"],
        "correct_index": 0,
        "explanation": "Tenglamalarni qo'shamiz: 2x = 14 => x = 7.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "9-sinf",
        "chapter_title": "Ratsional tengsizliklar",
        "question_text": "(x - 1)(x - 5) < 0 tengsizlikning butun yechimlari yig'indisini toping.",
        "options": ["9", "10", "12", "7"],
        "correct_index": 0,
        "explanation": "Intervallar usuli bo'yicha yechim (1; 5). Butun yechimlar: 2, 3, 4. Yig'indisi: 2 + 3 + 4 = 9.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Hosilaning tatbiqi",
        "question_text": "f(x) = x³ - 3x funksiyaning o'sish oraliqlarini toping.",
        "options": ["(-∞; -1) ∪ (1; +∞)", "(-1; 1)", "(0; +∞)", "(-∞; 0)"],
        "correct_index": 0,
        "explanation": "f'(x) = 3x² - 3 > 0 => x² - 1 > 0 => x < -1 yoki x > 1.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Murakkab funksiya hosilasi",
        "question_text": "y = sin(3x) funksiyaning hosilasini toping.",
        "options": ["3 cos(3x)", "cos(3x)", "-3 cos(3x)", "3 sin(3x)"],
        "correct_index": 0,
        "explanation": "y' = cos(3x) * (3x)' = 3 cos(3x).",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "9-sinf",
        "chapter_title": "Kombinatorika",
        "question_text": "C(6, 2) guruhlashlar (birikmalar) sonini hisoblang.",
        "options": ["15", "30", "12", "20"],
        "correct_index": 0,
        "explanation": "C(6, 2) = 6! / (2! * 4!) = (6 * 5) / 2 = 15.",
        "difficulty": "orta"
    },
    {
        "subject_id": 1,
        "grade": "10-sinf",
        "chapter_title": "Trigonometriya",
        "question_text": "tg α * ctg α ifodaning qiymati nimaga teng (burchak mavjud bo'lganda)?",
        "options": ["1", "0", "-1", "tg²α"],
        "correct_index": 0,
        "explanation": "tg α = sin α / cos α va ctg α = cos α / sin α, ularning ko'paytmasi har doim 1 ga teng.",
        "difficulty": "oson"
    },
    {
        "subject_id": 1,
        "grade": "11-sinf",
        "chapter_title": "Aniq integral va yuza",
        "question_text": "y = x² parabola va y = 0, x = 3 to'g'ri chiziqlar bilan chegaralangan soha yuzini hisoblang.",
        "options": ["9", "27", "3", "18"],
        "correct_index": 0,
        "explanation": "S = ∫₀³ x² dx = [x³ / 3]₀³ = 27 / 3 - 0 = 9.",
        "difficulty": "qiyin"
    }
]

# ==========================================
# 2. FIZIKA (Subject ID: 2) - 50 TA SAVOL
# ==========================================
FIZIKA_QUESTIONS = [
    # 7-sinf
    {
        "subject_id": 2,
        "grade": "7-sinf",
        "chapter_title": "Mexanik harakat",
        "question_text": "Avtomobil 72 km/h tezlik bilan harakatlanmoqda. Uning tezligini m/s da ifodalang.",
        "options": ["20 m/s", "15 m/s", "25 m/s", "36 m/s"],
        "correct_index": 0,
        "explanation": "72 km/h = 72 * (1000 m / 3600 s) = 72 / 3.6 = 20 m/s.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "7-sinf",
        "chapter_title": "Zichlik",
        "question_text": "Hajmi 2 m³ bo'lgan jismning massasi 5400 kg. Jism moddasining zichligini toping.",
        "options": ["2700 kg/m³", "10800 kg/m³", "1350 kg/m³", "270 kg/m³"],
        "correct_index": 0,
        "explanation": "ρ = m / V = 5400 kg / 2 m³ = 2700 kg/m³ (alyuminiy zichligi).",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "7-sinf",
        "chapter_title": "Kuch va og'irlik kuchi",
        "question_text": "Massasi 60 kg bo'lgan odamga ta'sir qiluvchi og'irlik kuchini toping (g = 9.8 N/kg).",
        "options": ["588 N", "600 N", "60 N", "98 N"],
        "correct_index": 0,
        "explanation": "F = m * g = 60 kg * 9.8 N/kg = 588 N.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "7-sinf",
        "chapter_title": "Gidrostatik bosim",
        "question_text": "Suv tubidagi chuqurlik 5 metr bo'lsa, u yerdagi gidrostatik bosimni hisoblang (ρ = 1000 kg/m³, g = 10 m/s²).",
        "options": ["50 kPa", "5 kPa", "500 kPa", "100 kPa"],
        "correct_index": 0,
        "explanation": "p = ρgh = 1000 * 10 * 5 = 50 000 Pa = 50 kPa.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "7-sinf",
        "chapter_title": "Arximed kuchi",
        "question_text": "Hajmi 0.02 m³ bo'lgan jism suvga to'liq botirilganda unga ta'sir qiluvchi Arximed kuchini toping (ρ_suv = 1000 kg/m³, g = 10 N/kg).",
        "options": ["200 N", "20 N", "100 N", "2000 N"],
        "correct_index": 0,
        "explanation": "F_a = ρ * g * V = 1000 * 10 * 0.02 = 200 N.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "7-sinf",
        "chapter_title": "Mexanik ish va quvvat",
        "question_text": "Jism 50 N kuch ta'sirida kuch yo'nalishida 4 m masofaga ko'chdi. Bajarilgan ishni toping.",
        "options": ["200 J", "12.5 J", "54 J", "20 J"],
        "correct_index": 0,
        "explanation": "A = F * s = 50 N * 4 m = 200 J.",
        "difficulty": "oson"
    },
    # 8-sinf
    {
        "subject_id": 2,
        "grade": "8-sinf",
        "chapter_title": "Issiqlik miqdori",
        "question_text": "Massasi 2 kg bo'lgan suvni 20°C dan 50°C gacha qizdirish uchun qancha issiqlik miqdori kerak? (c = 4200 J/(kg·°C))",
        "options": ["252 kJ", "126 kJ", "420 kJ", "84 kJ"],
        "correct_index": 0,
        "explanation": "Q = cmΔT = 4200 * 2 * (50 - 20) = 4200 * 2 * 30 = 252 000 J = 252 kJ.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "8-sinf",
        "chapter_title": "Elektr zaryadi va Kulon qonuni",
        "question_text": "Kulon qonuniga ko'ra ikkita nuqtaviy zaryad orasidagi masofa 2 marta oshirilsa, o'zaro ta'sir kuchi qanday o'zgaradi?",
        "options": ["4 marta kamayadi", "2 marta kamayadi", "4 marta oshadi", "O'zgarmaydi"],
        "correct_index": 0,
        "explanation": "F = k * |q₁q₂| / r². Masofa r ikki marta oshsa, r² to'rt marta oshadi, kuch 4 marta kamayadi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "8-sinf",
        "chapter_title": "Zanjir qismi uchun Om qonuni",
        "question_text": "Qarshiligi 20 Ω bo'lgan o'tkazgich uchlaridagi kuchlanish 60 V ga teng. Undan o'tayotgan tok kuchini toping.",
        "options": ["3 A", "1200 A", "0.33 A", "40 A"],
        "correct_index": 0,
        "explanation": "I = U / R = 60 V / 20 Ω = 3 A.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "8-sinf",
        "chapter_title": "O'tkazgichlarni ulash",
        "question_text": "Har birining qarshiligi 10 Ω bo'lgan ikkita o'tkazgich parallel ulanganda umumiy qarshilik qanchaga teng bo'ladi?",
        "options": ["5 Ω", "20 Ω", "10 Ω", "2.5 Ω"],
        "correct_index": 0,
        "explanation": "Parallel ulanganda: R_umumiy = R / n = 10 / 2 = 5 Ω.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "8-sinf",
        "chapter_title": "Elektr toki quvvati",
        "question_text": "220 V kuchlanish tarmog'iga ulangan lampochkadan 0.5 A tok o'tmoqda. Lampochkaning quvvatini toping.",
        "options": ["110 W", "440 W", "220 W", "55 W"],
        "correct_index": 0,
        "explanation": "P = U * I = 220 V * 0.5 A = 110 W.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "8-sinf",
        "chapter_title": "Joul-Lens qonuni",
        "question_text": "Joul-Lens qonuni formulasini aniqlang.",
        "options": ["Q = I²Rt", "Q = IRt²", "Q = UIt²", "Q = I² / Rt"],
        "correct_index": 0,
        "explanation": "Joul-Lens qonuniga ko'ra o'tkazgichdan ajraladigan issiqlik miqdori: Q = I²Rt.",
        "difficulty": "oson"
    },
    # 9-sinf
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "Tekis tezlanuvchan harakat",
        "question_text": "Boshlang'ich tezligi nol bo'lgan jism 3 m/s² tezlanish bilan 4 sekund harakatlandi. Jism bosib o'tgan yo'lni toping.",
        "options": ["24 m", "12 m", "48 m", "36 m"],
        "correct_index": 0,
        "explanation": "s = (a * t²) / 2 = (3 * 4²) / 2 = (3 * 16) / 2 = 24 m.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "Nyutonning ikkinchi qonuni",
        "question_text": "Massasi 5 kg bo'lgan jismga 25 N kuch ta'sir qilganda u qanday tezlanish oladi?",
        "options": ["5 m/s²", "125 m/s²", "0.2 m/s²", "20 m/s²"],
        "correct_index": 0,
        "explanation": "a = F / m = 25 N / 5 kg = 5 m/s².",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "Impuls va saqlanish qonuni",
        "question_text": "Massasi 2 kg bo'lgan jism 6 m/s tezlik bilan harakatlanmoqda. Uning impulsini toping.",
        "options": ["12 kg·m/s", "3 kg·m/s", "36 kg·m/s", "72 kg·m/s"],
        "correct_index": 0,
        "explanation": "p = m * v = 2 kg * 6 m/s = 12 kg·m/s.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "Kinetik energiya",
        "question_text": "Massasi 4 kg bo'lgan tosh 5 m/s tezlik bilan uchmoqda. Toshning kinetik energiyasini hisoblang.",
        "options": ["50 J", "100 J", "20 J", "25 J"],
        "correct_index": 0,
        "explanation": "E_k = (m * v²) / 2 = (4 * 5²) / 2 = (4 * 25) / 2 = 50 J.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "Potensial energiya",
        "question_text": "Massasi 3 kg bo'lgan yuk 4 m balandlikka ko'tarildi. Uning potensial energiyasi qanchaga teng? (g = 10 m/s²)",
        "options": ["120 J", "12 J", "60 J", "240 J"],
        "correct_index": 0,
        "explanation": "E_p = mgh = 3 * 10 * 4 = 120 J.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "Mexanik tebranishlar",
        "question_text": "Matematik mayatnikning tebranish davri formulasi qaysi?",
        "options": ["T = 2π√(l / g)", "T = 2π√(m / k)", "T = 2π√(g / l)", "T = 1 / ν"],
        "correct_index": 0,
        "explanation": "Matematik mayatnik uchun Tomson/Gyuygens formulasi: T = 2π√(l / g).",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "To'lqinlar",
        "question_text": "Chastotasi 500 Hz bo'lgan tovush to'lqinining havoda tarqalish tezligi 340 m/s bo'lsa, to'lqin uzunligini toping.",
        "options": ["0.68 m", "1.47 m", "170 m", "0.34 m"],
        "correct_index": 0,
        "explanation": "λ = v / ν = 340 / 500 = 0.68 m.",
        "difficulty": "orta"
    },
    # 10-sinf
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Molekulyar-kinetik nazariya",
        "question_text": "Ideal gaz holat tenglamasi (Mendeleyev-Klapeyron) qaysi javobda to'g'ri ifodalangan?",
        "options": ["pV = (m / M) * RT", "p / V = RT", "pM = mVR", "pV = NkT²"],
        "correct_index": 0,
        "explanation": "pV = (m / M) * RT yoki pV = νRT.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Izojarayonlar",
        "question_text": "O'zgarmas temperaturada (T = const) kechadigan jarayon qanday ataladi?",
        "options": ["Izotermik jarayon", "Izobarik jarayon", "Izoxorik jarayon", "Adiabatik jarayon"],
        "correct_index": 0,
        "explanation": "Temperatura doimiy bo'lgan jarayon izotermik jarayon deyiladi (Boyl-Mariott qonuni).",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Izojarayonlar",
        "question_text": "Bosim o'zgarmas bo'lgan (p = const) holatdagi jarayon qanday nomlanadi?",
        "options": ["Izobarik jarayon", "Izotermik jarayon", "Izoxorik jarayon", "Politropik jarayon"],
        "correct_index": 0,
        "explanation": "Doimiy bosimdagi jarayon izobarik deb ataladi (Gey-Lyussak qonuni: V/T = const).",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Termodinamikaning birinchi qonuni",
        "question_text": "Tizimga 800 J issiqlik miqdori berildi va tizim tashqi kuchlar ustidan 500 J ish bajardi. Ichki energiya o'zgarishini toping.",
        "options": ["300 J", "1300 J", "-300 J", "400 J"],
        "correct_index": 0,
        "explanation": "Q = ΔU + A => ΔU = Q - A = 800 J - 500 J = 300 J.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Issiqlik dvigatellari",
        "question_text": "Karno sikli bo'yicha ishlaydigan dvigatel isitgichining temperaturasi 600 K, sovitkichiniki 300 K. Dvigatelning maksimal FIK ini toping.",
        "options": ["50%", "25%", "75%", "33%"],
        "correct_index": 0,
        "explanation": "η = (T₁ - T₂) / T₁ = (600 - 300) / 600 = 300 / 600 = 0.5 ya'ni 50%.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Elektr sig'imi",
        "question_text": "Kondensator zaryadi 4*10⁻⁶ C va uning plastinkalari orasidagi kuchlanish 200 V bo'lsa, uning elektr sig'imini toping.",
        "options": ["0.02 μF", "0.2 μF", "2 μF", "800 μF"],
        "correct_index": 0,
        "explanation": "C = q / U = (4*10⁻⁶ C) / 200 V = 2*10⁻⁸ F = 0.02 μF.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "To'liq zanjir uchun Om qonuni",
        "question_text": "EYuKi 12 V va ichki qarshiligi 1 Ω bo'lgan manbaga 5 Ω li tashqi qarshilik ulangan. Zanjirdagi tok kuchini toping.",
        "options": ["2 A", "2.4 A", "12 A", "1.5 A"],
        "correct_index": 0,
        "explanation": "I = ε / (R + r) = 12 / (5 + 1) = 12 / 6 = 2 A.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Magnit maydoni va Amper kuchi",
        "question_text": "Induksiyasi 0.5 T bo'lgan bir jinsli magnit maydoniga perpendikulyar joylashgan uzunligi 0.4 m o'tkazgichdan 6 A tok o'tmoqda. Unga ta'sir etuvchi Amper kuchini toping.",
        "options": ["1.2 N", "2.4 N", "0.6 N", "4.8 N"],
        "correct_index": 0,
        "explanation": "F = I * B * l * sin 90° = 6 * 0.5 * 0.4 * 1 = 1.2 N.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Lorents kuchi",
        "question_text": "Magnit maydonida harakatlanayotgan zaryadlangan zarrachaga ta'sir qiluvchi kuch nima deb ataladi?",
        "options": ["Lorents kuchi", "Amper kuchi", "Kulon kuchi", "Arximed kuchi"],
        "correct_index": 0,
        "explanation": "Magnit maydonida harakatlanayotgan zaryadli zarrachaga ta'sir qiluvchi kuch Lorents kuchi deyiladi.",
        "difficulty": "oson"
    },
    # 11-sinf
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "Elektromagnit induksiya",
        "question_text": "G'altakdagi magnit oqimi 0.05 sekundda 0.2 Wb ga kamayganda hosil bo'ladigan induksiya EYuKini toping.",
        "options": ["4 V", "0.01 V", "10 V", "2.5 V"],
        "correct_index": 0,
        "explanation": "ε = |ΔФ / Δt| = 0.2 / 0.05 = 4 V.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "O'zinduksiya hodisasi",
        "question_text": "Induktivligi 0.2 H bo'lgan g'altakdan 5 A tok o'tmoqda. G'altak magnit maydonining energiyasini toping.",
        "options": ["2.5 J", "5 J", "1 J", "0.5 J"],
        "correct_index": 0,
        "explanation": "W = (L * I²) / 2 = (0.2 * 5²) / 2 = (0.2 * 25) / 2 = 2.5 J.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "Geometrik optika",
        "question_text": "Yorug'lik nuri havoda shisha sirtiga 60° burchak ostida tushadi va 30° burchak ostida sinadi. Shishaning sindirish ko'rsatkichini toping.",
        "options": ["√3", "1 / √3", "2", "1.5"],
        "correct_index": 0,
        "explanation": "n = sin α / sin β = sin 60° / sin 30° = (√3 / 2) / (1 / 2) = √3 ≈ 1.73.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "Yupqa linzalar",
        "question_text": "Fokus masofasi 0.25 m bo'lgan yig'uvchi linzaning optik kuchini toping.",
        "options": ["4 dptr", "2.5 dptr", "0.25 dptr", "0.4 dptr"],
        "correct_index": 0,
        "explanation": "D = 1 / F = 1 / 0.25 = 4 dioptriya (dptr).",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "Fotoeffekt hodisasi",
        "question_text": "Eynshteynning fotoeffekt tenglamasi qaysi?",
        "options": ["hν = A_chiq + E_k", "E = mc²", "hν = A_chiq - E_k", "λ = h / p"],
        "correct_index": 0,
        "explanation": "Yutilgan foton energiyasi chiqish ishi va fotoelektronlarning kinetik energiyasiga sarflanadi: hν = A + E_k.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "Atom va yadro fizikasi",
        "question_text": "Eynshteynning massa va energiya bog'liqligi formulasini toping.",
        "options": ["E = mc²", "E = mgh", "E = mv² / 2", "E = hν / c"],
        "correct_index": 0,
        "explanation": "Tinchlikdagi energiyaning massaga bog'liqligi: E = mc².",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "Radioaktiv yemirilish",
        "question_text": "Radioaktiv elementning yarim yemirilish davri 10 kun. 30 kundan so'ng dastlabki atomlarning qancha qismi qoladi?",
        "options": ["1/8 qismi", "1/4 qismi", "1/6 qismi", "1/16 qismi"],
        "correct_index": 0,
        "explanation": "30 kun ichida 3 ta yarim yemirilish davri o'tadi: (1/2)³ = 1/8 qismi qoladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "Yadro fizikasi",
        "question_text": "Geliy atomi yadrosi (alfa-zarracha) qanday tarkibga ega?",
        "options": ["2 ta proton va 2 ta neytron", "2 ta proton va 1 ta neytron", "4 ta proton", "1 ta proton va 3 ta neytron"],
        "correct_index": 0,
        "explanation": "Alfa-zarracha (⁴₂He) 2 ta proton va 2 ta neytrondan iborat.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "7-sinf",
        "chapter_title": "Oddiy mexanizmlar",
        "question_text": "Richagning uzun yelkasi 80 cm, qisqa yelkasi 20 cm. Bu richag kuchdan necha marta yutuq beradi?",
        "options": ["4 marta", "2 marta", "8 marta", "16 marta"],
        "correct_index": 0,
        "explanation": "Yutuq yelkalar nisbatiga teng: L₁ / L₂ = 80 / 20 = 4 marta.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "8-sinf",
        "chapter_title": "Agregat holat o'zgarishlari",
        "question_text": "Moddaning suyuq holatdan gaz holatiga o'tish jarayoni nima deyiladi?",
        "options": ["Bug'lanish", "Kondensatsiya", "Erish", "Sublimatsiya"],
        "correct_index": 0,
        "explanation": "Suyuqlikning gazga aylanishi bug'lanish deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "8-sinf",
        "chapter_title": "Agregat holat o'zgarishlari",
        "question_text": "Moddaning qattiq holatdan to'g'ridan-to'g'ri gaz holatiga o'tishi nima deyiladi?",
        "options": ["Sublimatsiya", "Kondensatsiya", "Kristallanish", "Bug'lanish"],
        "correct_index": 0,
        "explanation": "Qattiq moddaning suyuqlikka aylanmasdan to'g'ridan-to'g'ri gazga aylanishi sublimatsiya (haydalish) deyiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "Aylanma harakat",
        "question_text": "Radiusi 2 m bo'lgan aylana bo'ylab 4 m/s tezlik bilan harakatlanayotgan jismning markazga intilma tezlanishini toping.",
        "options": ["8 m/s²", "4 m/s²", "2 m/s²", "16 m/s²"],
        "correct_index": 0,
        "explanation": "a = v² / R = 4² / 2 = 16 / 2 = 8 m/s².",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "Gravitatsiya",
        "question_text": "Yer sirtida erkin tushish tezlanishi g bo'lsa, Yer radiusiga teng balandlikda (h = R) erkin tushish tezlanishi qanday bo'ladi?",
        "options": ["g / 4", "g / 2", "2g", "g / 8"],
        "correct_index": 0,
        "explanation": "g(h) = GM / (R + h)² = GM / (2R)² = g / 4.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Ichki energiya",
        "question_text": "Bir atomli ideal gazning ichki energiyasi formulasi qaysi?",
        "options": ["U = (3/2) * (m/M) * RT", "U = (5/2) * νRT", "U = (1/2) * mv²", "U = pV²"],
        "correct_index": 0,
        "explanation": "Bir atomli ideal gazning ichki energiyasi U = 3/2 * νRT = 3/2 * (m/M) * RT.",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "10-sinf",
        "chapter_title": "Elektrostatika",
        "question_text": "Nuqtaviy zaryad hosil qilgan elektr maydon kuchlanganligi E qaysi formula bilan ifodalanadi?",
        "options": ["E = k * |q| / r²", "E = k * q / r", "E = F * q", "E = U * d"],
        "correct_index": 0,
        "explanation": "E = F / q = k * |q| / r².",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "Tebranish konturi",
        "question_text": "Tomson formulasi bo'yicha elektromagnit tebranishlar davri qanday hisoblanadi?",
        "options": ["T = 2π√(LC)", "T = 2π√(L / C)", "T = 1 / (2π√(LC))", "T = 2πLC"],
        "correct_index": 0,
        "explanation": "Ideal tebranish konturida erkin elektromagnit tebranishlar davri Tomson formulasi: T = 2π√(LC).",
        "difficulty": "orta"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "To'lqin optikasi",
        "question_text": "Yorug'lik to'lqinlarining to'siqlarni aylanib o'tish hodisasi nima deyiladi?",
        "options": ["Diffraksiya", "Interferensiya", "Dispersiya", "Polyarizatsiya"],
        "correct_index": 0,
        "explanation": "To'lqinlarning to'siqlar chetini aylanib o'tishi va geometrik soya sohasiga kirishi diffraksiya deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "To'lqin optikasi",
        "question_text": "Oq yorug'likning prizmadan o'tganda spektrga ajralishi qaysi hodisaga asoslangan?",
        "options": ["Dispersiya", "Diffraksiya", "Interferensiya", "Fotoeffekt"],
        "correct_index": 0,
        "explanation": "Yorug'likning moddada sinish ko'rsatkichining to'lqin uzunligiga (chastotasiga) bog'liqligi dispersiya deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "8-sinf",
        "chapter_title": "Solishtirma qarshilik",
        "question_text": "Uzunligi l, ko'ndalang kesim yuzi S bo'lgan o'tkazgichning qarshiligi formulasi qaysi?",
        "options": ["R = ρ * (l / S)", "R = ρ * (S / l)", "R = l / (ρ * S)", "R = ρ * l * S"],
        "correct_index": 0,
        "explanation": "O'tkazgich qarshiligi: R = ρ * l / S, bu yerda ρ - solishtirma qarshilik.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "9-sinf",
        "chapter_title": "Nyutonning uchinchi qonuni",
        "question_text": "Nyutonning uchinchi qonunining fizik ma'nosi qaysi javobda to'g'ri berilgan?",
        "options": ["Jismlarning bir-biriga ta'sir kuchlari miqdor jihatdan teng va yo'nalishi qarama-qarshi", "Kuch massaga teskari proporsional", "Jismga kuch ta'sir qilmasa u doim to'xtab qoladi", "Inersiya kuchi tezlikka teng"],
        "correct_index": 0,
        "explanation": "Ta'sir aks ta'sirga teng: F₁ = -F₂.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "11-sinf",
        "chapter_title": "Kvant fizikasi",
        "question_text": "Fotonning energiyasi qaysi formula bilan aniqlanadi?",
        "options": ["E = hν", "E = hc / ν", "E = h / ν", "E = p / c"],
        "correct_index": 0,
        "explanation": "Plank gipotezasiga binoan kvant (foton) energiyasi E = hν = hc / λ.",
        "difficulty": "oson"
    },
    {
        "subject_id": 2,
        "grade": "7-sinf",
        "chapter_title": "Diffuziya hodisasi",
        "question_text": "Bir modda molekulalarining ikkinchi modda molekulalari oralig'iga o'z-o'zidan kirib borish hodisasi nima deb ataladi?",
        "options": ["Diffuziya", "Konveksiya", "Radiatsiya", "Adgeziya"],
        "correct_index": 0,
        "explanation": "Molekulalarning tartibsiz harakati oqibatida moddalarning o'zaro aralashishi diffuziya deb ataladi.",
        "difficulty": "oson"
    }
]
