import sqlite3
import json

conn = sqlite3.connect('backend/edubattle.db')
c = conn.cursor()

# We will add 40 questions per subject across 8 subjects = 320 unique questions
# Clear existing questions to have a clean, non-duplicated 320+ bank
c.execute("DELETE FROM questions")

questions_data = []

# --- 1. MATEMATIKA (40 questions) ---
math_questions = [
    ("Algebra", "2x + 7 = 19 tenglamadagi x ning qiymatini toping.", ["4", "6", "5", "7"], 1, "2x = 19 - 7 => 2x = 12 => x = 6."),
    ("Funksiyalar", "y = 3x - 5 funksiyaning x = 4 dagi qiymatini hisoblang.", ["7", "12", "9", "17"], 0, "y = 3*(4) - 5 = 12 - 5 = 7."),
    ("Geometriya", "Gipotenuzasi 10 sm, bir kateti 6 sm bo'lgan to'g'ri burchakli uchburchakning ikkinchi katetini toping.", ["8 sm", "7 sm", "9 sm", "6.5 sm"], 0, "Pifagor teoremasi: b = sqrt(10^2 - 6^2) = sqrt(100 - 36) = 8 sm."),
    ("Ehtimollik", "Tanga bir marta tashlanganda gerb tushish ehtimolligi qancha?", ["1/4", "1/2", "1/3", "1"], 1, "Tanganing 2 tomoni bor, gerb tushishi 1/2."),
    ("Trigonometriya", "sin(30°) ning qiymati nimaga teng?", ["1/2", "sqrt(3)/2", "sqrt(2)/2", "1"], 0, "Standart trigonometrik jadval: sin(30°) = 0.5."),
    ("Logarifm", "log2(32) ning qiymatini hisoblang.", ["4", "5", "6", "3"], 1, "2^5 = 32, demak log2(32) = 5."),
    ("Progressiya", "Arifmetik progressiyada a1 = 3, d = 4 bo'lsa, a5 ni toping.", ["15", "19", "23", "17"], 1, "a5 = a1 + 4d = 3 + 4*4 = 19."),
    ("Geometriya", "Radiusi 7 sm bo'lgan doira yuzini toping (pi = 22/7 deb oling).", ["154 sm^2", "144 sm^2", "168 sm^2", "172 sm^2"], 0, "S = pi * r^2 = 22/7 * 49 = 154 sm^2."),
    ("Algebra", "x^2 - 9 = 0 tenglamaning musbat ildizini toping.", ["3", "-3", "9", "1"], 0, "x^2 = 9 => x = +-3, musbat ildiz: 3."),
    ("Funksiyalar", "f(x) = x^2 - 4x + 4 parabolaning uchi qaysi nuqtada joylashgan?", ["(2, 0)", "(0, 2)", "(-2, 0)", "(2, 4)"], 0, "x_uch = -b/(2a) = 4/2 = 2; y = 2^2 - 8 + 4 = 0."),
    ("Hosilalar", "f(x) = x^3 - 5x funksiyaning hosilasini toping.", ["3x^2 - 5", "3x^2", "x^2 - 5", "3x - 5"], 0, "(x^3)' = 3x^2, (-5x)' = -5."),
    ("Algebra", "|2x - 6| = 0 tenglamaning yechimini toping.", ["3", "6", "0", "-3"], 0, "2x - 6 = 0 => 2x = 6 => x = 3."),
    ("Geometriya", "Kvadratning perimetri 36 sm bo'lsa, uning yuzasi qancha?", ["81 sm^2", "64 sm^2", "100 sm^2", "72 sm^2"], 0, "Tomoni a = 36/4 = 9 sm. Yuza S = 9^2 = 81 sm^2."),
    ("Trigonometriya", "cos(60°) ning qiymatini toping.", ["1/2", "sqrt(3)/2", "0", "1"], 0, "cos(60°) = 1/2."),
    ("Kombinatorika", "5 nafar o'quvchini ketma-ket qatorga necha xil usulda joylashtirish mumkin?", ["120", "24", "60", "720"], 0, "P_5 = 5! = 5*4*3*2*1 = 120."),
    ("Algebra", "(a + b)^2 formulaning yoyilmasi qanday bo'ladi?", ["a^2 + 2ab + b^2", "a^2 + ab + b^2", "a^2 - 2ab + b^2", "a^2 + b^2"], 0, "Qisqa ko'paytirish formulasi: a^2 + 2ab + b^2."),
    ("Geometriya", "Teng tomonli uchburchakning ichki burchaklari necha gradusdan?", ["60°", "45°", "90°", "30°"], 0, "180° / 3 = 60°."),
    ("Algebra", "sqrt(144) ning qiymatini hisoblang.", ["12", "14", "16", "11"], 0, "12^2 = 144."),
    ("Tengsizliklar", "3x - 9 > 0 tengsizlikni yeching.", ["x > 3", "x < 3", "x > -3", "x > 9"], 0, "3x > 9 => x > 3."),
    ("Trigonometriya", "tg(45°) ning qiymati nimaga teng?", ["1", "0", "sqrt(3)", "1/sqrt(3)"], 0, "tg(45°) = sin(45°)/cos(45°) = 1."),
    ("Progressiya", "Geometrik progressiyada b1 = 2, q = 3 bo'lsa, b4 ni toping.", ["54", "18", "162", "27"], 0, "b4 = b1 * q^3 = 2 * 27 = 54."),
    ("Integral", "Integral(2x dx) nimaga teng?", ["x^2 + C", "2x^2 + C", "x + C", "x^3 + C"], 0, "Integral(2x dx) = 2*(x^2/2) + C = x^2 + C."),
    ("Vektorlar", "a(3; 4) vektorning uzunligini (modulini) toping.", ["5", "7", "12", "6"], 0, "|a| = sqrt(3^2 + 4^2) = sqrt(9 + 16) = 5."),
    ("Geometriya", "Rombning diagonallari 10 sm va 12 sm bo'lsa, yuzini toping.", ["60 sm^2", "120 sm^2", "48 sm^2", "72 sm^2"], 0, "S = (d1 * d2) / 2 = (10 * 12) / 2 = 60 sm^2."),
    ("Algebra", "2^x = 64 bo'lsa, x ni toping.", ["6", "5", "7", "8"], 0, "2^6 = 64, demak x = 6."),
    ("Matritsalar", "2x2 matritsada [[1, 2], [3, 4]] determinantini toping.", ["-2", "2", "10", "4"], 0, "det = 1*4 - 2*3 = 4 - 6 = -2."),
    ("Planimetriya", "Uchburchakning asosi 8 sm, balandligi 5 sm. Yuzini toping.", ["20 sm^2", "40 sm^2", "13 sm^2", "25 sm^2"], 0, "S = (a * h) / 2 = (8 * 5) / 2 = 20 sm^2."),
    ("Algebra", "x^2 - 5x + 6 = 0 tenglamaning ildizlari yig'indisini toping (Viyet).", ["5", "-5", "6", "-6"], 0, "Viyet teoremasi: x1 + x2 = -(-5) = 5."),
    ("Trigonometriya", "sin^2(x) + cos^2(x) ifodaning qiymati nimaga teng?", ["1", "0", "2", "-1"], 0, "Asosiy trigonometrik ayniyat: sin^2(x) + cos^2(x) = 1."),
    ("Foizlar", "200 sonining 25 foizi nechaga teng?", ["50", "40", "60", "25"], 0, "200 * 0.25 = 50."),
    ("Algebra", "Kasrni qisqartiring: (x^2 - 4) / (x - 2).", ["x + 2", "x - 2", "x", "2"], 0, "(x-2)(x+2)/(x-2) = x + 2."),
    ("Geometriya", "Doiraning diametri 20 sm bo'lsa, uning radiusi qancha?", ["10 sm", "5 sm", "40 sm", "15 sm"], 0, "r = d / 2 = 10 sm."),
    ("Statistika", "3, 5, 7, 9 sonlarining o'rta arifmetigini toping.", ["6", "7", "5.5", "8"], 0, "(3+5+7+9)/4 = 24/4 = 6."),
    ("Algebra", "x = 3 bo'lganda 2x^2 - 4 ifodaning qiymatini toping.", ["14", "12", "18", "10"], 0, "2*(3^2) - 4 = 2*9 - 4 = 18 - 4 = 14."),
    ("Trigonometriya", "cos(0°) ning qiymati nimaga teng?", ["1", "0", "-1", "1/2"], 0, "cos(0°) = 1."),
    ("Geometriya", "Trapetsiyaning asoslari 6 sm va 10 sm, balandligi 4 sm. Yuzi qancha?", ["32 sm^2", "64 sm^2", "24 sm^2", "40 sm^2"], 0, "S = ((a+b)/2)*h = ((6+10)/2)*4 = 8*4 = 32 sm^2."),
    ("Algebra", "sqrt(81) + sqrt(49) ifodani hisoblang.", ["16", "15", "14", "17"], 0, "9 + 7 = 16."),
    ("Ehtimollik", "O'yin kubigi tashlanganda 6 raqami tushish ehtimolligi qancha?", ["1/6", "1/2", "1/3", "1/4"], 0, "Jami 6 xil holat bor, 6 tushishi 1/6."),
    ("Funksiyalar", "y = 2x to'g'ri chiziq koordinata boshidan o'tadimi?", ["Ha, (0,0) nuqtadan o'tadi", "Yo'q", "Faqat manfiy sohada", "Aniqlab bo'lmaydi"], 0, "x=0 bo'lganda y=0, demak (0,0) orqali o'tadi."),
    ("Algebra", "3^4 ning qiymati nechaga teng?", ["81", "27", "64", "243"], 0, "3*3*3*3 = 81.")
]

for item in math_questions:
    questions_data.append((1, item[0], item[1], json.dumps(item[2], ensure_ascii=False), item[3], item[4], "o'rta", "10-sinf"))

# --- 2. FIZIKA (40 questions) ---
physics_questions = [
    ("Kinematika", "Tezlik birligi Xalqaro birliklar sistemasida (SI) qaysi?", ["m/s", "km/h", "sm/s", "m*s"], 0, "SI tizimida tezlik metriksasi m/s."),
    ("Dinamika", "Nyutonning ikkinchi qonuni formulasini toping.", ["F = m * a", "F = m / a", "F = a / m", "F = m * v"], 0, "Nyutonning II qonuni: Kuch = massa * tezlanish."),
    ("Optika", "Yorug'likning vakuumdagi tezligi qancha?", ["300 000 km/s", "150 000 km/s", "30 000 km/s", "3 000 km/s"], 0, "Vakuumda yorug'lik tezligi c ≈ 3 * 10^8 m/s = 300 000 km/s."),
    ("Elektrodinamika", "Ohm qonunining zanjir qismi uchun formulasi qaysi?", ["I = U / R", "I = U * R", "I = R / U", "U = I / R"], 0, "Tok kuchi kuchlanishga to'g'ri, qarshilikka teskari mutanosib: I = U / R."),
    ("Termodinamika", "Mutlaq nol harorat Selsiy shkalasida necha gradusga to'g'ri keladi?", ["-273.15 °C", "0 °C", "-100 °C", "-373.15 °C"], 0, "0 Kelvin = -273.15 Selsiy."),
    ("Mexanika", "Og'irlik kuchi formulasini toping.", ["F = m * g", "F = m / g", "F = k * x", "F = G * m"], 0, "Yer yuzida jismga ta'sir qiluvchi og'irlik kuchi F = mg."),
    ("Bosim", "Bosimning SI tizimidagi asosiy birligi qaysi?", ["Paskal (Pa)", "Nyuton (N)", "Joul (J)", "Vatt (W)"], 0, "Bosim birligi Paskal: 1 Pa = 1 N / m^2."),
    ("Ish va Energiya", "Kinetik energiya qaysi formula orqali hisoblanadi?", ["E = (m * v^2) / 2", "E = m * g * h", "E = m * v", "E = F * s"], 0, "Harakatdagi jismning kinetik energiyasi: Ek = mv^2 / 2."),
    ("Ish va Energiya", "Potensial energiya qaysi formula orqali hisoblanadi?", ["E = m * g * h", "E = m * v^2 / 2", "E = F * t", "E = m * a"], 0, "Balandlikdagi jism potensial energiyasi: Ep = mgh."),
    ("Elektrostatika", "Elektr zaryadining SI dagi birligi qaysi?", ["Kulon (C)", "Amper (A)", "Volt (V)", "Farad (F)"], 0, "Elektr zaryadi Kulon (C) bilan o'lchanadi."),
    ("Magnit maydoni", "Magnit induksiyasi birligi qaysi olim nomi bilan ataladi?", ["Tesla (T)", "Veber (Wb)", "Genri (H)", "Gauss"], 0, "Magnit induksiyasi birligi Tesla (T)."),
    ("Tebranishlar", "Matematik mayatnik tebranish davri formulasi qanday?", ["T = 2*pi*sqrt(l/g)", "T = 2*pi*sqrt(m/k)", "T = 2*pi*sqrt(g/l)", "T = l / g"], 0, "Gyuygens formulasi: T = 2*pi*sqrt(l/g)."),
    ("Optika", "Qavariq linza nurlarni nima qiladi?", ["Yig'adi", "Sochadi", "Yutadi", "Qaytarmaydi"], 0, "Qavariq linza yig'uvchi linza hisoblanadi."),
    ("Termodinamika", "Issiqlik miqdori birligi SI da nima?", ["Joul (J)", "Kaloriya", "Vatt (W)", "Kelvin"], 0, "SI tizimida energiya va issiqlik Joullarda (J) o'lchanadi."),
    ("Zichlik", "Massa 200 g, hajm 50 sm^3 bo'lgan jismning zichligini toping.", ["4 g/sm^3", "0.25 g/sm^3", "10 g/sm^3", "2.5 g/sm^3"], 0, "Zichlik ro = m / V = 200 / 50 = 4 g/sm^3."),
    ("Mexanika", "Kuch momenti formulasini toping.", ["M = F * d", "M = F / d", "M = F * v", "M = m * a"], 0, "Kuch momenti M = F * d (kuch ko'paytirilgan yelka)."),
    ("Elektrodinamika", "Elektr toki quvvati formulasi qaysi?", ["P = U * I", "P = U / I", "P = I / U", "P = U * R"], 0, "Elektr quvvati: P = UI = I^2*R = U^2/R."),
    ("Akustika", "Tovush to'lqinlari qaysi muhitda tarqala olmaydi?", ["Vakuumda", "Suvda", "Havoda", "Po'latda"], 0, "Tovush mexanik to'lqin bo'lib, moddiy muhit talab qiladi, vakuumda tarqalmaydi."),
    ("Kinematika", "Erkin tushish tezlanishi (g) ning Yer yuzidagi o'rtacha qiymati qancha?", ["9.8 m/s^2", "10.5 m/s^2", "8.9 m/s^2", "9.1 m/s^2"], 0, "g ≈ 9.8 m/s^2 (ko'p hisoblarda 10 olinadi)."),
    ("Gidrostatika", "Arximed kuchi qaysi formula bilan ifodalanadi?", ["F = ro * g * V", "F = m * g", "F = P * S", "F = ro * V"], 0, "Arximed kuchi: Fa = ro_suyuqlik * g * V_cho'kkan."),
    ("Termodinamika", "Suyuqlikning bug'ga aylanish jarayoni nima deyiladi?", ["Bug'lanish", "Kondensatsiya", "Kristallanish", "Sublimatsiya"], 0, "Suyuqlikdan gaz holatiga o'tish bug'lanish deyiladi."),
    ("Termodinamika", "Gazning suyuqlikka aylanish jarayoni nima deyiladi?", ["Kondensatsiya", "Bug'lanish", "Erish", "Diffuziya"], 0, "Gazdan suyuqlikka o'tish kondensatsiya deyiladi."),
    ("Yadro fizikasi", "Atom yadrosini qaysi zarrachalar tashkil qiladi?", ["Protonlar va neytronlar", "Elektronlar va protonlar", "Faqat elektronlar", "Faqat protonlar"], 0, "Yadro nuklonlardan (proton va neytronlar) iborat."),
    ("Elektrodinamika", "Qarshilik birligi qaysi?", ["Om (Ohm)", "Farad", "Genri", "Amper"], 0, "Elektr qarshiligi Om larda o'lchanadi."),
    ("Optika", "Ko'zgu sirtidan yorug'likning qaytish qonuniga ko'ra tushish burchagi qaytish burchagiga...", ["Tengdir", "Kattadir", "Kichikdir", "Bog'liq emas"], 0, "Tushish burchagi alpha = qaytish burchagi beta."),
    ("Mexanika", "Kuch birligi qaysi olim nomi bilan yuritiladi?", ["Isaak Nyuton", "Jeyms Joul", "Blez Paskal", "Albert Eynshteyn"], 0, "Kuch birligi Nyuton (N)."),
    ("Molekulyar fizika", "Modda molekulalarining o'z-o'zidan bir-biriga aralashib ketishi nima deyiladi?", ["Diffuziya", "Konveksiya", "Deformatsiya", "Iyonlashuv"], 0, "Molekulalar harakati natijasida aralashuv diffuziya deyiladi."),
    ("Elektrodinamika", "O'tkazgichlarni ketma-ket ulaganda umumiy qarshilik qanday topiladi?", ["R = R1 + R2", "1/R = 1/R1 + 1/R2", "R = R1 * R2", "R = R1 / R2"], 0, "Ketma-ket ulanganda qarshiliklar to'g'ridan-to'g'ri qo'shiladi: R = R1 + R2."),
    ("Elektrodinamika", "Paralel ulanganda barcha tarmoqlarda nima bir xil bo'ladi?", ["Kuchlanish (U)", "Tok kuchi (I)", "Qarshilik (R)", "Quvvat (P)"], 0, "Paralel zanjirda barcha shoxobchalardagi kuchlanish teng: U1 = U2 = U."),
    ("Astrofizika", "Quyosh sistemasidagi eng katta sayyora qaysi?", ["Yupiter", "Saturn", "Mars", "Neptun"], 0, "Yupiter Quyosh sistemasidagi eng massiv va eng katta sayyora."),
    ("Optika", "Oq yorug'lik prizmadan o'tganda kamalak ranglariga ajralishi nima deyiladi?", ["Dispersiya", "Interferensiya", "Difraksiya", "Polyarlanish"], 0, "Yorug'lik tezligining to'lqin uzunligiga bog'liqligi dispersiya deyiladi."),
    ("Mexanika", "Tezlanish nima?", ["Tezlikning vaqt birligi ichida o'zgarishi", "Bosib o'tilgan yo'l", "Jism massasi", "Kuch ta'siri"], 0, "Tezlanish a = delta_v / delta_t."),
    ("Elektrostatika", "Bir xil ishorali elektr zaryadlari o'zaro...", ["Bir-birini itaradi", "Bir-birini tortadi", "Ta'sirlashmaydi", "Neytrallanadi"], 0, "Bir xil zaryadlar itarishadi, qarama-qarshi zaryadlar tortishadi."),
    ("Termodinamika", "Selsiy shkalasi bo'yicha suvning qaynash harorati qancha?", ["100 °C", "0 °C", "212 °C", "80 °C"], 0, "Normal bosimda suv 100 °C da qaynaydi."),
    ("Kinematika", "Jism tinch holatdan 2 m/s^2 tezlanish bilan 4 soniya harakatlansa, oxirgi tezligi qancha?", ["8 m/s", "6 m/s", "16 m/s", "4 m/s"], 0, "v = a * t = 2 * 4 = 8 m/s."),
    ("Mexanika", "Inersiya hodisasi nima?", ["Jismning o'z tezligini saqlashga intilishi", "Jismning to'xtashi", "Jismning og'irligi", "Ishqalanish kuchi"], 0, "Tashqi kuch ta'sir qilmaganda jismning o'z holatini saqlashi inersiyadir."),
    ("Elektrodinamika", "Elektr tokining mavjudlik shartlaridan biri qaysi?", ["Erkin zaryadli zarrachalar va elektr maydoni", "Faqat vakuum", "Faqat yuqori harorat", "Magnitning yo'qligi"], 0, "Tok oqishi uchun erkin zaryadlar va ularni harakatlantiruvchi elektr maydoni kerak."),
    ("Magnit maydoni", "Yer sharining geografik shimoliy qutbida qanday magnit qutbi joylashgan?", ["Janubiy magnit qutbi", "Shimoliy magnit qutbi", "Magnit qutbi yo'q", "Ekvator qutbi"], 0, "Yerning geografik shimolida magnit jihatdan Janubiy magnit qutb joylashgan."),
    ("Rezonans", "Majburiy tebranishlar chastotasi xususiy chastotaga tenglashganda nima yuz beradi?", ["Rezonans (amplituda keskin ortadi)", "Tebranish to'xtaydi", "Tezlik nolga tenglashadi", "Chastota nol bo'ladi"], 0, "Bu hodisa rezonans deyiladi va amplituda keskin oshadi."),
    ("Mexanika", "Guk qonuni formulasini toping.", ["F = -k * x", "F = m * a", "F = G * m1*m2 / r^2", "F = I * B * L"], 0, "Elastiklik kuchi uchun Guk qonuni: F = -kx.")
]

for item in physics_questions:
    questions_data.append((2, item[0], item[1], json.dumps(item[2], ensure_ascii=False), item[3], item[4], "o'rta", "10-sinf"))

# --- 3. KIMYO (40 questions) ---
chem_questions = [
    ("Davriy qonun", "Mendeleyev davriy jadvalidagi birinchi element qaysi?", ["Vodorod (H)", "Geliy (He)", "Litiy (Li)", "Kislorod (O)"], 0, "Davriy jadval 1-raqamli elementi Vodorod (H)."),
    ("Modda tuzilishi", "Suv molekulasining kimyoviy formulasi qaysi?", ["H2O", "H2O2", "HO", "OH"], 0, "Suv formulasi H2O."),
    ("Reaksiyalar", "Metan gazining yonish mahsulotlari nimalardan iborat?", ["CO2 va H2O", "CO va H2", "C va H2O", "CH3OH va O2"], 0, "CH4 + 2O2 -> CO2 + 2H2O."),
    ("Eritmalar", "Neytral muhitda pH ko'rsatkichi nechaga teng bo'ladi?", ["7", "0", "14", "1"], 0, "Neytral suvli eritmalarda pH = 7."),
    ("Metall va Nometallar", "Osh tuzi (oshxona tuzi)ning kimyoviy nomi nima?", ["Natriy xlorid (NaCl)", "Kalsiy xlorid (CaCl2)", "Kaliy xlorid (KCl)", "Magniy sulfat (MgSO4)"], 0, "Osh tuzi natriy xlorid (NaCl)."),
    ("Kislotalar", "Sulfat kislotaning formulasi qaysi?", ["H2SO4", "HCl", "HNO3", "H3PO4"], 0, "Sulfat kislota formulasi H2SO4."),
    ("Organik kimyo", "Alkanlar gomologik qatorining umumiy formulasi qanday?", ["CnH2n+2", "CnH2n", "CnH2n-2", "CnH2n-6"], 0, "To'yingan uglevodorodlar (alkanlar): CnH2n+2."),
    ("Elementlar", "Oltinning kimyoviy belgisi qaysi?", ["Au", "Ag", "Fe", "Cu"], 0, "Oltin - Aurum (Au)."),
    ("Elementlar", "Kumushning kimyoviy belgisi qaysi?", ["Ag", "Au", "Pt", "Al"], 0, "Kumush - Argentum (Ag)."),
    ("Elementlar", "Temirning kimyoviy belgisi qaysi?", ["Fe", "F", "Fr", "Ir"], 0, "Temir - Ferrum (Fe)."),
    ("Oksidlar", "Uglerod (IV) oksidining xalq orasidagi nomi nima?", ["Karbonat angidrid (gaz)", "Is gazi", "Chala yonish gazi", "Quruq muz emas"], 0, "CO2 - karbonat angidrid."),
    ("Zaharli gazlar", "Is gazining kimyoviy formulasi qaysi?", ["CO", "CO2", "CH4", "SO2"], 0, "Uglerod (II) oksidi CO - is gazi, juda zaharli."),
    ("Kimyoviy bog'lanish", "NaCl molekulasida qanday kimyoviy bog'lanish mavjud?", ["Ion bog'lanish", "Kovalent qutbsiz", "Metall bog'lanish", "Vodorod bog'lanish"], 0, "Metall (Na) va nometall (Cl) o'rtasida ion bog'lanish hosil bo'ladi."),
    ("Organik kimyo", "Eng oddiy bir atomli to'yingan spirt qaysi?", ["Metanol (CH3OH)", "Etanol (C2H5OH)", "Propanol", "Glitserin"], 0, "Metil spirti (metanol) CH3OH."),
    ("Davriy qonun", "Eng kuchli nometallik (elektromanfiylik) xususiyatiga ega element qaysi?", ["Ftor (F)", "Kislorod (O)", "Xlor (Cl)", "Azot (N)"], 0, "Ftor eng yuqori elektromanfiylikka ega (Poling bo'yicha 4.0)."),
    ("Kislotalar", "Xlorid kislotaning formulasi qaysi?", ["HCl", "H2SO4", "HNO3", "HF"], 0, "Xlorid (tuz kislotasi) HCl."),
    ("Asoslar", "O'yuvchi natriy (kaustik soda) ning formulasi nima?", ["NaOH", "KOH", "Ca(OH)2", "Na2CO3"], 0, "Natriy gidroksid NaOH."),
    ("Eritmalar", "Kislotali muhitda lakmus qog'ozi qanday rangga kiradi?", ["Qizil", "Ko'k", "Sariq", "Yashil"], 0, "Kislotalar lakmusni qizil rangga bo'yaydi."),
    ("Eritmalar", "Ishqoriy muhitda fenolftalein qanday rangga kiradi?", ["Malina (to'q pushti)", "Rangsiz qoladi", "Sariq", "Moviy"], 0, "Fenolftalein ishqorda malina rang beradi."),
    ("Gazlar", "Havoning eng katta qismini (taxminan 78%) qaysi gaz tashkil qiladi?", ["Azot (N2)", "Kislorod (O2)", "Argon (Ar)", "Karbonat angidrid (CO2)"], 0, "Havo tarkibining 78% ini azot tashkil qiladi."),
    ("Molekula massasi", "Kislorod (O2) gazining molyar massasi qancha?", ["32 g/mol", "16 g/mol", "8 g/mol", "64 g/mol"], 0, "M(O) = 16 => M(O2) = 16*2 = 32 g/mol."),
    ("Avogadro qonuni", "1 mol har qanday gaz normal sharoitda qancha hajm egallaydi?", ["22.4 litr", "11.2 litr", "44.8 litr", "1 litr"], 0, "Molyar hajm Vm = 22.4 l/mol."),
    ("Organik kimyo", "Glyukozaning kimyoviy formulasi qaysi?", ["C6H12O6", "C12H22O11", "C6H6", "CH3COOH"], 0, "Glyukoza formulasi C6H12O6."),
    ("Kislotalar", "Sirka kislotasining formulasi qaysi?", ["CH3COOH", "HCOOH", "C2H5COOH", "C6H5COOH"], 0, "Sirka kislotasi CH3COOH."),
    ("Allotropiya", "Olmos va grafit qaysi kimyoviy elementning allotropik shakl o'zgarishlaridir?", ["Uglerod (C)", "Kremniy (Si)", "Fosfor (P)", "Oltingugurt (S)"], 0, "Olmos, grafit va fulleren uglerod atomlaridan iborat."),
    ("Metallmaslar", "Ozon gazining molekulyar formulasi qanday?", ["O3", "O2", "O", "O4"], 0, "Ozon kislorodning uch atomli allotropik shakli: O3."),
    ("Metallmaslar", "Tirik organizmlar suyak to'qimasida eng ko'p uchraydigan metall qaysi?", ["Kalsiy (Ca)", "Kaliy (K)", "Temir (Fe)", "Rux (Zn)"], 0, "Suyak to'qimasi kalsiy fosfat va birikmalaridan iborat."),
    ("Redoks", "Oksidlanish jarayonida atom elektronlarni nima qiladi?", ["Beradi (yo'qotadi)", "Biriktirib oladi", "O'zgartirmaydi", "Bo'linadi"], 0, "Elektron berish oksidlanish, biriktirib olish qaytarilishdir."),
    ("Metalllar", "Oddiy sharoitda suyuq holatda bo'ladigan yagona metall qaysi?", ["Simob (Hg)", "Qo'rg'oshin (Pb)", "Qalay (Sn)", "Galliy (Ga)"], 0, "Simob (Hg) xona haroratida suyuq metaldur."),
    ("Organik kimyo", "Benzolning kimyoviy formulasi qaysi?", ["C6H6", "C6H12", "C6H14", "C2H2"], 0, "Benzol aromatik halqasi C6H6."),
    ("Anorganik kimyo", "Ohaktoshning asosiy kimyoviy tarkibi nima?", ["Kalsiy karbonat (CaCO3)", "Kalsiy sulfat (CaSO4)", "Kalsiy xlorid (CaCl2)", "Kalsiy oksidi (CaO)"], 0, "Ohaktosh va bo'r kalsiy karbonat CaCO3."),
    ("Elementlar", "Qon gemoglobini tarkibiga kiruvchi muhim mikroelement qaysi?", ["Temir (Fe)", "Mis (Cu)", "Magniy (Mg)", "Kobalt (Co)"], 0, "Gemoglobin tarkibida Fe2+ ioni kislorodni tashiydi."),
    ("Organik kimyo", "Atsetilen gazining formulasi qaysi?", ["C2H2", "C2H4", "C2H6", "CH4"], 0, "Alkinlarning birinchisi atsetilen C2H2."),
    ("Elementlar", "O'simliklar xlorofill pigmenti markazida qaysi metall ioni turadi?", ["Magniy (Mg)", "Temir (Fe)", "Marganes (Mn)", "Kalsiy (Ca)"], 0, "Xlorofill porfirin halqasi markazida Magniy (Mg) joylashgan."),
    ("Termokimyo", "Issiqlik ajralib chiqishi bilan boradigan reaksiyalar nima deyiladi?", ["Ekzotermik reaksiyalar", "Endotermik reaksiyalar", "Katalitik reaksiyalar", "Neytrallanish"], 0, "Issiqlik chiqishi +Q ekzotermik jarayondir."),
    ("Termokimyo", "Issiqlik yutilishi bilan boradigan reaksiyalar nima deyiladi?", ["Endotermik reaksiyalar", "Ekzotermik reaksiyalar", "Yonish reaksiyalari", "Redoks"], 0, "Issiqlik yutilishi -Q endotermik deyiladi."),
    ("Elementlar", "Inert (aslzoda) gazlarga qaysi guruh elementlari kiradi?", ["VIII (18) guruh", "I guruh", "VII guruh", "II guruh"], 0, "Geliy, Neon, Argon, Kripton, Ksenon VIII guruh inert gazlaridir."),
    ("Suv qattiqligi", "Suvning qattiqligi undagi qaysi ionlar miqdoriga bog'liq?", ["Ca2+ va Mg2+", "Na+ va K+", "Fe2+ va Cu2+", "H+ va OH-"], 0, "Suv qattiqligi kalsiy va magniy tuzlari tufayli vujudga keladi."),
    ("Polimerlar", "Polietilen qaysi monomerning polimerlanishidan olinadi?", ["Etilen (C2H4)", "Propilen (C3H6)", "Vinilxlorid", "Stirol"], 0, "Etilen polimerlanib polietilen hosil qiladi."),
    ("Gazlar", "Tuxum hidini eslatuvchi qo'lansa hidli gaz qaysi?", ["Vodorod sulfid (H2S)", "Amiak (NH3)", "Metan (CH4)", "Xlor (Cl2)"], 0, "H2S sassiq tuxum hidi beruvchi gaz.")
]

for item in chem_questions:
    questions_data.append((3, item[0], item[1], json.dumps(item[2], ensure_ascii=False), item[3], item[4], "o'rta", "10-sinf"))

# --- 4. BIOLOGIYA (40 questions) ---
bio_questions = [
    ("Sitologiya", "Hujayraning energetik stansiyasi deb qaysi organoid ataladi?", ["Mitoxondriya", "Ribosoma", "Lizosoma", "Golji majmuasi"], 0, "Mitoxondriyada ATF sintezlanadi, hujayra energiya manbai."),
    ("Genetika", "DNK molekulasida Adeninga komplementar asos qaysi?", ["Timin (T)", "Guanin (G)", "Sitozin (S)", "Uratsil (U)"], 0, "DNKda A har doim T bilan, G har doim S bilan bog'lanadi."),
    ("Fiziologiya", "Inson tanasidagi eng katta ichki a'zo qaysi?", ["Jigar", "Yurak", "O'pka", "Oshqozon osti bezi"], 0, "Jigar inson tanasidagi eng yirik ichki a'zo (vazni ~1.5 kg)."),
    ("Botanika", "O'simliklarda fotosintez jarayoni asosan qaysi organoidda boradi?", ["Xloroplast", "Xromoplast", "Leykoplast", "Vakuola"], 0, "Xloroplastlardagi xlorofill quyosh nurini yutib fotosintezni amalga oshiradi."),
    ("Sitologiya", "Oqsillar sintezi qaysi organoidda amalga oshiriladi?", ["Ribosoma", "Lizosoma", "Sentriola", "Yadrocha"], 0, "Ribosomalar oqsil sintezlovchi molekulyar apparatlardir."),
    ("Anatomiya", "Inson skeletida taxminan nechta suyak bor?", ["206 ta", "150 ta", "300 ta", "100 ta"], 0, "Katta yoshli odam skeletida 206 ta suyak mavjud."),
    ("Qon aylanish", "Yurakdan a'zolarga qon olib boruvchi qon tomirlari nima deyiladi?", ["Arteriyalar", "Venalar", "Kapillarlar", "Limfa tomirlari"], 0, "Arteriyalar qonni yurakdan a'zolarga tashiydi."),
    ("Qon aylanish", "A'zolardan yurakka qon olib keluvchi tomirlar nima deyiladi?", ["Venalar", "Arteriyalar", "Aorta", "Kapillarlar"], 0, "Venalar qonni yurakka qaytaradi."),
    ("Sitologiya", "Hujayra ichidagi eskirgan moddalarni parchalovchi organoid qaysi?", ["Lizosoma", "Ribosoma", "Plastida", "Peroksisoma"], 0, "Lizosomalar gidrolitik fermentlarga ega bo'lib, hazm qilish vazifasini bajaradi."),
    ("Genetika", "Insonning somatik (tana) hujayralarida nechta xromosoma bor?", ["46 ta (23 juft)", "23 ta", "48 ta", "44 ta"], 0, "Inson diploid to'plami 46 ta (23 juft) xromosomadir."),
    ("Genetika", "Inson jinsiy hujayralarida (gametalarda) nechta xromosoma bo'ladi?", ["23 ta", "46 ta", "44 ta", "2 ta"], 0, "Gametalarda gaploid to'plam (23 ta) bo'ladi."),
    ("Zoologiya", "Sutemizuvchilarning yuragi necha kamerali?", ["4 kamerali", "3 kamerali", "2 kamerali", "1 kamerali"], 0, "Sutemizuvchilar va qushlarda yurak 4 kamerali (2 bo'lmacha, 2 qorincha)."),
    ("Zoologiya", "Baliqlarning yuragi necha kamerali bo'ladi?", ["2 kamerali", "3 kamerali", "4 kamerali", "Kameralarga bo'linmagan"], 0, "Baliqlarda yurak 2 kamerali (1 bo'lmacha va 1 qorincha)."),
    ("Anatomiya", "Inson qonida kislorod tashuvchi qon hujayralari nima deyiladi?", ["Eritrotsitlar", "Leykotsitlar", "Trombotsitlar", "Fagotsitlar"], 0, "Eritrotsitlar (qizil qon tanachalari) gemoglobin orqali O2 tashiydi."),
    ("Immunologiya", "Organizmda immunitetni ta'minlovchi oq qon tanachalari qaysilar?", ["Leykotsitlar", "Eritrotsitlar", "Trombotsitlar", "Plazma"], 0, "Leykotsitlar yot bakteriya va viruslarga qarshi kurashadi."),
    ("Qon ivishi", "Qon ivish jarayonida qaysi qon plastinkalari qatnashadi?", ["Trombotsitlar", "Eritrotsitlar", "Monotsitlar", "Limfotsitlar"], 0, "Trombotsitlar qon to'xtatish va ivishni ta'minlaydi."),
    ("Nerv sistemasi", "Nerv sistemasining asosiy strukturaviy va funksional birligi nima?", ["Neyron", "Nefron", "Miofibrilla", "Osteotsit"], 0, "Nerv hujayrasi neyron deb ataladi."),
    ("Ayirish sistemasi", "Buyrakning strukturaviy birligi nima?", ["Nefron", "Neyron", "Alveola", "Gepatotsit"], 0, "Buyrakning mikroskopik filtrlash birligi nefrondir."),
    ("Botanika", "O'simlik ildizining asosiy vazifalaridan biri qaysi?", ["Suv va mineral moddalarni so'rish", "Fotosintez qilish", "Changlanish", "Meva hosil qilish"], 0, "Ildiz o'simlikni tuproqqa mustahkamlaydi va suv-tuzlarni so'radi."),
    ("Endokrinologiya", "Qonda qand miqdorini kamaytiruvchi gormon qaysi?", ["Insulin", "Adrenalin", "Tiroksin", "Glukagon"], 0, "Insulin oshqozon osti bezida ishlab chiqarilib, qand miqdorini pasaytiradi."),
    ("Endokrinologiya", "Qo'rquv va hayajonda buyrak usti bezidan ajraluvchi gormon nima?", ["Adrenalin", "Insulin", "Gipofiz gormoni", "Oksitotsin"], 0, "Adrenalin xavf paytida yurak urishini va bosimni oshiradi."),
    ("Genetika", "Genetika fanining asoschisi kim?", ["Gregor Mendel", "Charlz Darvin", "Lui Paster", "Robert Guk"], 0, "Gregor Mendel no'xat ustida tajribalar o'tkazib irsiyat qonunlarini ochgan."),
    ("Evolyutsiya", "Turlarning kelib chiqishi va tabiiy tanlanish nazariyasi muallifi kim?", ["Charlz Darvin", "Jan Batist Lamark", "Karl Linney", "Tomas Morgan"], 0, "Charlz Darvin tabiiy tanlanish nazariyasini yaratgan."),
    ("Sitologiya", "Hujayra atamasini fanga birinchi bo'lib kiritgan olim kim?", ["Robert Guk (1665)", "Antoni van Levenguk", "Robert Broun", "Teodor Shvann"], 0, "Robert Guk po'kak kesmasini mikroskopda ko'rib 'hujayra' deb atagan."),
    ("Sitologiya", "O'simlik hujayrasida bo'lib, hayvon hujayrasida bo'lmaydigan qobiq nima?", ["Sellyulozali hujayra devori", "Membrana", "Sitoplazma", "Yadro"], 0, "O'simlik hujayralari qattiq sellyuloza devoriga ega."),
    ("Anatomiya", "O'pkada gazlar almashinuvi kechadigan pufakchalar nima deyiladi?", ["Alveolalar", "Bronxlar", "Traxeyalar", "Plevra"], 0, "Alveolalar kapillyarlar bilan o'ralgan gaz almashinuvchi mikropufakchalardir."),
    ("Virusologiya", "Viruslar hujayraviy tuzilishga egami?", ["Yo'q, hujayrasiz hayot shakli", "Ha, bir hujayrali", "Ha, ko'p hujayrali", "Yadroga ega"], 0, "Viruslar hujayrasiz tuzilishga ega bo'lib, faqat xo'jayin hujayrasida ko'payadi."),
    ("Mikrobiologiya", "Bakteriyalarning yadrosi shakllanganmi?", ["Yo'q, ular prokariotlar", "Ha, eukariotlar", "Ikki yadroli", "Faqat ko'payganda hosil bo'ladi"], 0, "Bakteriyalar yadro qobig'iga ega bo'lmagan prokariotlardir."),
    ("Sitologiya", "DNK molekulasi qayerda joylashgan (eukariotlarda)?", ["Yadro ichida", "Faqat sitoplazmada", "Vakuolada", "Hujayra devorida"], 0, "Eukariotlarda asosiy genetik ma'lumot yadro xromosomalarida joylashgan."),
    ("Moddalar almashinuvi", "Inson tanasidagi asosiy energiya akkumulyatori (valyutasi) qaysi modda?", ["ATF (Adenozintrifosfat)", "Glyukoza", "DNK", "Xolesterin"], 0, "ATF barcha hayotiy jarayonlar uchun kimyoviy energiya manbaidir."),
    ("Zoologiya", "Hasharotlarning nafas olish organi nima?", ["Traxeyalar", "Jabralar", "O'pka", "Teri orqali"], 0, "Hasharotlar butun tanasiga tarqalgan traxeya naychalari bilan nafas oladi."),
    ("Ekologiya", "Oziq zanjirida organik modda ishlab chiqaruvchi o'simliklar nima deyiladi?", ["Produtsentlar", "Konsumentlar", "Redutsentlar", "Parazitlar"], 0, "Produtsentlar avtotrof yo'l bilan organik modda sintezlaydi."),
    ("Ekologiya", "Organik qoldiqlarni parchalab noorganik holga keltiruvchi bakteriya va zamburug'lar nima deyiladi?", ["Redutsentlar", "Produtsentlar", "Yirtqichlar", "Avtotroflar"], 0, "Redutsentlar chirindi va o'lik qoldiqlarni parchalaydi."),
    ("Botanika", "Urug'li o'simliklarda changlanishdan so'ng nima hosil bo'ladi?", ["Urug' va meva", "Ildiz", "Poya", "Barg"], 0, "Urug'lanishdan so'ng tugunchadan meva, urug'kurtakdan urug' rivojlanadi."),
    ("Genetika", "RNK tarkibida Timin o'rniga qaysi azot asosi bo'ladi?", ["Uratsil (U)", "Adenin (A)", "Guanin (G)", "Sitozin (S)"], 0, "RNKda Timin o'rnini Uratsil (U) egallaydi."),
    ("Anatomiya", "Katta qon aylanish doirasi yurakning qaysi qismidan boshlanadi?", ["Chap qorinchadan", "O'ng qorinchadan", "Chap bo'lmachadan", "O'ng bo'lmachadan"], 0, "Katta doira kislorodli qonni chap qorinchadan aortaga haydash bilan boshlanadi."),
    ("Anatomiya", "Kichik (o'pka) qon aylanish doirasi qayerdan boshlanadi?", ["O'ng qorinchadan", "Chap qorinchadan", "Aortadan", "Venadan"], 0, "Kichik doira o'ng qorinchadan o'pka arteriyasiga qon haydash bilan boshlanadi."),
    ("Gematologiya", "I (0) qon guruhiga ega inson qaysi guruh egalariga qon bera oladi?", ["Barcha guruhlarga (universal donor)", "Faqat I guruhga", "Faqat IV guruhga", "Hech kimga"], 0, "I guruh eritrotsitlarida agglyutinogenlar yo'qligi uchun universal donordir."),
    ("Fiziologiya", "Ko'z to'r pardasidagi ranglarni ajratuvchi retseptorlar nima deyiladi?", ["Kolbachasimon hujayralar", "Tayoqchasimon hujayralar", "Nerv tugunlari", "Gavhar"], 0, "Kolbachalar yorug'lik va rangni, tayoqchalar esa qorong'uda oq-qorani sezadi."),
    ("Botanika", "Suv va erigan mineral moddalar o'simlik bo'ylab qaysi to'qima naylari orqali ko'tariladi?", ["Ksilema (yog'ochlik)", "Floema (lub)", "Po'kak", "Kambiy"], 0, "Ksilema orqali suv pastdan yuqoriga harakatlanadi.")
]

for item in bio_questions:
    questions_data.append((4, item[0], item[1], json.dumps(item[2], ensure_ascii=False), item[3], item[4], "o'rta", "10-sinf"))

# --- 5. ONA TILI VA ADABIYOT (40 questions) ---
lang_questions = [
    ("Morfologiya", "O'zbek tilida nechta so'z turkumi mavjud?", ["12 ta", "9 ta", "6 ta", "10 ta"], 0, "Mustaqil (6), yordamchi (3) va alohida (3) jami 12 ta so'z turkumi bor."),
    ("Sintaksis", "Gapning qaysi bo'lagi egaga bog'lanib, uning harakati yoki holatini bildiradi?", ["Kesim", "To'ldiruvchi", "Hol", "Aniqlash"], 0, "Kesim gapning bosh bo'lagi bo'lib, eganing harakatini bildiradi."),
    ("Adabiyot", "'Xamsa' asari nechta dostondan iborat bo'ladi?", ["5 ta doston", "4 ta doston", "7 ta doston", "3 ta doston"], 0, "Xamsa arabcha 'beshlik' demakdir, 5 dostondan iborat."),
    ("Adabiyot", "O'zbek tilida birinchi 'Xamsa'ni yaratgan buyuk shoir kim?", ["Alisher Navoiy", "Nizomiy Ganjaviy", "Zahiriddin Muhammad Bobur", "Lutfiy"], 0, "Turkiy tilda birinchi Xamsani Alisher Navoiy yaratgan (1483-1485)."),
    ("Adabiyot", "'O'tkan kunlar' asarining muallifi kim?", ["Abdulla Qodiriy", "Cho'lpon", "Oybek", "G'afur G'ulom"], 0, "O'zbek adabiyotidagi birinchi roman muallifi Abdulla Qodiriy."),
    ("Fonetika", "O'zbek adabiy tilida nechta unli tovush bor?", ["6 ta", "10 ta", "8 ta", "5 ta"], 0, "A, O, I, U, E, O' - 6 ta unli fonema mavjud."),
    ("Fonetika", "Jarangli undosh tovushni toping.", ["B", "P", "T", "K"], 0, "B jarangli, uning jufti P esa jarangsizdir."),
    ("Morfologiya", "Otning qaratqich kelishigi qo'shimchasi qaysi?", ["-ning", "-ni", "-ga", "-da"], 0, "Qaratqich kelishigi -ning qo'shimchasi bilan yasaladi."),
    ("Morfologiya", "Tushum kelishigi qo'shimchasi qaysi?", ["-ni", "-ning", "-ga", "-dan"], 0, "Tushum kelishigi -ni qo'shimchasi."),
    ("Morfologiya", "Sifat darajalaridan qiyosiy daraja qo'shimchasi qaysi?", ["-roq", "-dek", "-cha", "-ona"], 0, "Qiyosiy daraja -roq orqali yasaladi (katta - kattaroq)."),
    ("Adabiyot", "'Boburnoma' asari qaysi janrga oid?", ["Tarixiy-memuar (esdalik)", "Doston", "Roman", "Qasida"], 0, "Boburnoma - Zahiriddin Muhammad Boburning memuar va tarixiy asari."),
    ("Adabiyot", "'Kecha va kunduz' romani muallifi kim?", ["Abdulhamid Cho'lpon", "Abdulla Qahhor", "Fitrat", "Oybek"], 0, "Cho'lponning mashhur romani 'Kecha va kunduz'."),
    ("Adabiyot", "O'zbek nasrida ixcham, o'tkir hikoyalari bilan mashhur adib kim?", ["Abdulla Qahhor", "Erkin Vohidov", "Asqad Muxtor", "Tohir Malik"], 0, "Abdulla Qahhor o'zbek adabiyotining hikoya ustasidir."),
    ("Morfologiya", "Fe'lning o'tgan zamon shaxs-son qo'shimchasi qaysi?", ["-di", "-yapti", "-moqchi", "-adi"], 0, "Aniq o'tgan zamon qo'shimchasi -di (yozdi, keldi)."),
    ("Morfologiya", "Sonning turlaridan dona son qo'shimchasi qaysi?", ["-ta", "-tadan", "-inchi", "-ovlon"], 0, "Dona son -ta qo'shimchasi bilan yasaladi (beshta, o'nta)."),
    ("Leksikologiya", "Shakli bir xil, ammo ma'nosi butunlay boshqa bo'lgan so'zlar nima deyiladi?", ["Omonimlar", "Sinonimlar", "Antonimlar", "Paronimlar"], 0, "Omonimlar yozilishi bir xil, ma'nosi har xil so'zlar (masalan: olma - meva / olma - fe'l)."),
    ("Leksikologiya", "Ma'nolari bir-biriga qarama-qarshi bo'lgan so'zlar nima deyiladi?", ["Antonimlar", "Sinonimlar", "Omonimlar", "Neologizmlar"], 0, "Antonimlar qarama-qarshi ma'noni bildiradi (katta - kichik)."),
    ("Leksikologiya", "Ma'nodosh so'zlar nima deb ataladi?", ["Sinonimlar", "Antonimlar", "Paronimlar", "Arxaizmlar"], 0, "Sinonimlar ma'nosi yaqin so'zlar (chiroyli, go'zal)."),
    ("Adabiyot", "O'zbekiston Qahramoni, shoir Erkin Vohidovning mashhur qasidasi qaysi?", ["O'zbegim", "Dildoshlik", "Ona tilim", "Dunyo"], 0, "Erkin Vohidov 'O'zbegim' qasidasi bilan katta shuhrat qozongan."),
    ("Adabiyot", "O'zbekiston Qahramoni Abdulla Oripov qaysi mashhur asar muallifi?", ["O'zbekiston Respublikasi Davlat Madhiyasi", "Alpomish dostoni", "Yulduzli tunlar", "Sariq devni minib"], 0, "Abdulla Oripov Davlat Madhiyamiz matni muallifidir."),
    ("Adabiyot", "Sehrli shlyapa va Xoshimjon sarguzashtlari haqidagi 'Sariq devni minib' asari muallifi kim?", ["Xudoyberdi To'xtaboyev", "Anvar Obidjon", "Po'lat Mo'min", "Qudrat Hikmat"], 0, "Bolalar yozuvchisi Xudoyberdi To'xtaboyev."),
    ("Imlo qoidalari", "Qaysi so'z imlo jihatdan to'g'ri yozilgan?", ["Muallim", "Mualim", "Muallimn", "Muvallim"], 0, "To'g'ri shakli: 'Muallim'."),
    ("Morfologiya", "Olmoshning turlaridan kishilik olmoshlarini toping.", ["Men, sen, u, biz, siz, ular", "Bu, shu, o'sha", "Kim, nima", "Hamma, barcha"], 0, "Kishilik olmoshlari shaxsni bildiradi: men, sen, u..."),
    ("Sintaksis", "Faqat bosh bo'laklardan (ega va kesimdan) iborat gap nima deyiladi?", ["Yig'iq gap", "Yoyiq gap", "So'z-gap", "To'liqsiz gap"], 0, "Ikkinchi darajali bo'laklar qatnashmagan gap yig'iq gap deyiladi."),
    ("Sintaksis", "Tarkibida ikkinchi darajali bo'laklar ham qatnashgan gap nima deyiladi?", ["Yoyiq gap", "Yig'iq gap", "Bir bosh bo'lakli gap", "Undalmali gap"], 0, "Ikkinchi darajali bo'laklar bo'lsa, bu yoyiq gap."),
    ("Adabiyot", "Qadimgi xalq qahramonlik eposi qaysi?", ["Alpomish", "Farhod va Shirin", "Layli va Majnun", "Ravshan"], 0, "Alpomish - o'zbek xalq qahramonlik dostoni."),
    ("Adabiyot", "'Dunyoning ishlari' qissasi muallifi kim?", ["O'tkir Hoshimov", "Said Ahmad", "Tohir Malik", "Shukur Xolmirzayev"], 0, "O'tkir Hoshimov onalar madhiga bag'ishlangan ushbu asarni yozgan."),
    ("Adabiyot", "'Ufq' trilogiyasi muallifi qaysi adib?", ["Said Ahmad", "Oybek", "Asqad Muxtor", "Pirimqul Qodirov"], 0, "Said Ahmad mashhur 'Ufq' trilogiyasi muallifidir."),
    ("Adabiyot", "Boburiylar sulolasi haqidagi 'Yulduzli tunlar' romani muallifi kim?", ["Pirimqul Qodirov", "Mirkarim Osim", "Odil Yoqubov", "Oybek"], 0, "Pirimqul Qodirov Bobur hayotiga bag'ishlangan 'Yulduzli tunlar' romanini yozgan."),
    ("Morfologiya", "Ravish qaysi so'roqlarga javob bo'ladi?", ["Qanday? Qay tarzda? Qachon? Qayerda?", "Kim? Nima?", "Nechta? Nechanchi?", "Qanday qildi?"], 0, "Ravish harakatning belgisi, payti, o'rnini bildiradi."),
    ("Morfologiya", "Ko'makchilar qaysi so'z turkumiga kiradi?", ["Yordamchi so'z turkumi", "Mustaqil so'z turkumi", "Alohida so'z turkumi", "Modal so'zlar"], 0, "Ko'makchi, bog'lovchi va yuklama yordamchi so'zlardir."),
    ("Fonetika", "Alifbodagi harflarning qat'iy belgilangan tartibi nima deyiladi?", ["Alifbo (Alfavit)", "Lug'at", "Imlo", "Morfologiya"], 0, "Harflarning tartiblangan qatori alifbodir."),
    ("Adabiyot", "'Diyonat' va 'Ko'hna dunyo' romanlari muallifi kim?", ["Odil Yoqubov", "Abdulla Qahhor", "Asqad Muxtor", "Ibrohim Rahim"], 0, "Odil Yoqubov mashhur tarixiy va ijtimoiy romanlar muallifi."),
    ("Leksikologiya", "Iste'moldan chiqqan, tarixiy davr bilan ketgan so'zlar nima deyiladi?", ["Tarixiy so'zlar (istorizmlar)", "Neologizmlar", "Varvarizmlar", "Dialektizmlar"], 0, "Masalan: xon, bek, mingboshi tarixiy so'zlardir."),
    ("Leksikologiya", "Yangi paydo bo'lgan tushunchalarni ifodalovchi yangi so'zlar nima deyiladi?", ["Neologizmlar", "Arxaizmlar", "Omonimlar", "Slenglar"], 0, "Yangi so'zlar neologizmlar deyiladi."),
    ("Frazeologiya", "'Qo'li ochiq' iborasining ma'nosi nima?", ["Saxiy, saxovatpesha", "Qo'li katta", "O'g'ri", "Kambag'al"], 0, "Qo'li ochiq - himmatli, saxiy odamga nisbatan aytiladi."),
    ("Frazeologiya", "'Yulduzni benarvon uradigan' iborasi qanday odamga aytiladi?", ["Juda ayyor, uddaburon, chaqqon", "Baland bo'yli", "Astronom", "Kamsuqum"], 0, "Epchil va uddaburon odamga nisbatan aytiladi."),
    ("Sintaksis", "Teng bog'langan qo'shma gaplarda qismlar nima orqali bog'lanadi?", ["Teng bog'lovchilar yoki ohang orqali", "Egasiz", "Faqat vergul bilan", "Bosh gap orqali"], 0, "Va, ammo, lekin, biroq kabi teng bog'lovchilar orqali bog'lanadi."),
    ("Morfologiya", "Undov so'zlarga misol toping.", ["Oh! Voy! E voh!", "Chunki, agar", "Bilanoq, sari", "Balki, ehtimol"], 0, "His-tuyg'u bildiruvchi so'zlar undovlardir."),
    ("Adabiyot", "Alisher Navoiy qaysi asarida turkiy tilning forsiy tildan kam emasligini isbotlagan?", ["Muhokamat ul-lug'atayn", "Lison ut-tayr", "Majolis un-nafois", "Mahbub ul-qulub"], 0, "'Ikki til muhokamasi' asarida turkiy tilning boyligini isbotlagan.")
]

for item in lang_questions:
    questions_data.append((5, item[0], item[1], json.dumps(item[2], ensure_ascii=False), item[3], item[4], "o'rta", "10-sinf"))

# --- 6. TARIX (40 questions) ---
hist_questions = [
    ("Amir Temur davri", "Sohibqiron Amir Temur qaysi yili tavallud topgan?", ["1336-yil 9-aprel", "1340-yil 1-may", "1320-yil 15-mart", "1350-yil 9-aprel"], 0, "Amir Temur 1336-yil 9-aprelda Xo'ja Ilg'or qishlog'ida tug'ilgan."),
    ("Amir Temur davri", "Amir Temur davlatining poytaxti qaysi shahar bo'lgan?", ["Samarqand", "Buxoro", "Shahrisabz", "Hirot"], 0, "Amir Temur Samarqandni poytaxt qilib, dunyoning eng go'zal shahriga aylantirdi."),
    ("Temuriylar", "Samarqandda mashhur rasadxona qurdirgan olim va hukmdor kim?", ["Mirzo Ulug'bek", "Bobur Mirzo", "Shohrux Mirzo", "Husayn Boyqaro"], 0, "Mirzo Ulug'bek 1424-1428 yillarda Samarqandda rasadxona qurdirgan."),
    ("Qadimgi davr", "Zardushtiylik dinining muqaddas kitobi qaysi?", ["Avesto", "Injil", "Tavrot", "Qur'on"], 0, "Zardushtiylikning muqaddas kitobi - Avesto."),
    ("O'rta asrlar", "Tibbiyot qonunlari ('Al-Qonun fit-tibb') asarining muallifi kim?", ["Abu Ali ibn Sino", "Abu Rayhon Beruniy", "Al-Xorazmiy", "Al-Farg'oniy"], 0, "Buyuk tabib Abu Ali ibn Sino (Avitsenna)."),
    ("O'rta asrlar", "Algebra faniga asos solgan buyuk alloma kim?", ["Muhammad al-Xorazmiy", "Ibn Sino", "Farobiy", "Mirzo Ulug'bek"], 0, "Al-Xorazmiy 'Al-Jabr' asari bilan algebraga asos solgan."),
    ("O'rta asrlar", "'Ikkinchi muallim' (Arastudan keyingi) unvoniga sazovor bo'lgan olim kim?", ["Abu Nasr Forobiy", "Beruniy", "Ibn Sino", "Zamaxshariy"], 0, "Abu Nasr Forobiy qomusiy bilimlari uchun 'Muallimi soniy' atalgan."),
    ("Jadidchilik", "Turkistonda birinchi yangi usul (jadid) maktabini ochgan ma'rifatparvar kim?", ["Mahmudxo'ja Behbudiy", "Munavvarqori Abdurashidxonov", "Abdulla Avloniy", "Fitrat"], 0, "Mahmudxo'ja Behbudiy jadidchilik harakatining yetakchisi edi."),
    ("Jadidchilik", "'Turkiy Guliston yoxud axloq' asarining muallifi kim?", ["Abdulla Avloniy", "Hamza", "Behbudiy", "Cho'lpon"], 0, "Abdulla Avloniy mashhur ma'rifiy asar muallifi."),
    ("Xonliklar davri", "XIX asr o'rtalarida O'zbekiston hududida nechta davlat (xonlik) mavjud edi?", ["3 ta (Buxoro, Xiva, Qo'qon)", "2 ta", "4 ta", "Yagona davlat"], 0, "Buxoro amirligi, Xiva xonligi va Qo'qon xonligi mavjud edi."),
    ("Jahon tarixi", "Qadimgi Misr hukmdorlari nima deb atalgan?", ["Fir'avn", "Shoh", "Imperator", "Xon"], 0, "Misr hukmdorlari fir'avn (faraon) deb atalgan."),
    ("Jahon tarixi", "Dunyodagi eng qadimgi yetti mo''jizadan hozirgacha saqlanib qolgani qaysi?", ["Misr ehromlari (Xufu piramidasi)", "Semiramida osma bog'lari", "Rodos haykali", "Aleksandriya mayog'i"], 0, "Giza ehromlari bugungi kungacha saqlangan yagona mo''jiza."),
    ("Qadimgi davr", "Buyuk Ipak yo'li qaysi mamlakatlarni bog'lagan?", ["Xitoydan O'rta Osiyo orqali Yevropaga", "Faqat Hindiston va Eronni", "Faqat Rossiya va Xitoyni", "Afrika va Amerikani"], 0, "Xitoydan boshlanib O'rta Osiyo orqali O'rtayer dengizigacha borgan."),
    ("Jahon tarixi", "Birinchi jahon urushi qaysi yillarda bo'lib o'tgan?", ["1914 - 1918-yillar", "1939 - 1945-yillar", "1905 - 1911-yillar", "1917 - 1922-yillar"], 0, "I Jahon urushi 1914-1918 yillarda bo'lgan."),
    ("Jahon tarixi", "Ikkinchi jahon urushi qaysi yillarda bo'lib o'tgan?", ["1939 - 1945-yillar", "1914 - 1918-yillar", "1941 - 1945-yillar", "1935 - 1940-yillar"], 0, "II Jahon urushi 1939-yil 1-sentyabrdan 1945-yil 2-sentyabrgacha davom etgan."),
    ("Temuriylar", "Boburiylar davlatiga (Buyuk Mo'g'ullar imperiyasiga) Hindistonda kim asos solgan?", ["Zahiriddin Muhammad Bobur", "Akbarshoh", "Humoyun", "Shoh Jahon"], 0, "Bobur Mirzo 1526-yilda Panipat jangidagi g'alabadan so'ng asos solgan."),
    ("Temuriylar", "Dunyoga mashhur 'Tojmahal' me'moriy yodgorligini kim qurdirgan?", ["Shoh Jahon", "Bobur", "Akbarshoh", "Jahongirshoh"], 0, "Boburning nabirasi Shoh Jahon suyukli rafiqasi Mumtoz Mahal sharafiga qurdirgan."),
    ("O'zbekiston tarixi", "O'zbekiston Respublikasi Mustaqilligi qachon e'lon qilingan?", ["1991-yil 31-avgust", "1991-yil 1-sentyabr", "1990-yil 20-iyun", "1992-yil 8-dekabr"], 0, "1991-yil 31-avgustda O'zbekiston davlat mustaqilligi e'lon qilingan."),
    ("O'zbekiston tarixi", "O'zbekiston Respublikasi Konstitutsiyasi qachon qabul qilingan?", ["1992-yil 8-dekabr", "1991-yil 1-sentyabr", "1993-yil 18-noyabr", "1992-yil 2-iyul"], 0, "Bosh qomusimiz 1992-yil 8-dekabrda qabul qilingan."),
    ("O'zbekiston tarixi", "O'zbekiston Respublikasi Davlat bayrog'i qachon qabul qilingan?", ["1991-yil 18-noyabr", "1992-yil 2-iyul", "1992-yil 8-dekabr", "1991-yil 1-sentyabr"], 0, "Davlat bayrog'i 1991-yil 18-noyabrda qabul qilingan."),
    ("O'zbekiston tarixi", "O'zbekiston Respublikasi Davlat gerbi qachon qabul qilingan?", ["1992-yil 2-iyul", "1991-yil 18-noyabr", "1993-yil 8-dekabr", "1992-yil 1-sentyabr"], 0, "Davlat gerbi 1992-yil 2-iyulda qabul qilingan."),
    ("O'zbekiston tarixi", "O'zbekiston Respublikasining milliy valyutasi 'So'm' qachon muomalaga kiritilgan?", ["1994-yil 1-iyul", "1991-yil 1-sentyabr", "1993-yil 15-noyabr", "1995-yil 1-yanvar"], 0, "Milliy valyutamiz 1994-yil 1-iyulda joriy qilingan."),
    ("O'zbekiston tarixi", "O'zbekiston BMT (Birlashgan Millatlar Tashkiloti)ga qachon a'zo bo'lgan?", ["1992-yil 2-mart", "1991-yil 1-sentyabr", "1993-yil 1-iyun", "1992-yil 8-dekabr"], 0, "1992-yil 2-martda BMT Bosh Assambleyasida qabul qilingan."),
    ("Qadimgi davr", "Aleksandr Makedonskiy (Iskandar Zulqarnayn) O'rta Osiyoga qachon bostirib kirgan?", ["Mil. avv. 329-yilda", "Mil. avv. 500-yilda", "Milodiy 100-yilda", "Mil. avv. 200-yilda"], 0, "Makedonskiy miloddan avvalgi 329-yilda So'g'diyona va Baqtriyaga yurish qilgan."),
    ("Qadimgi davr", "Iskandar Zulqarnaynga qarshi mardonavor kurashgan So'g'diyona xalq qahramoni kim?", ["Spitamen", "To'maris", "Shiroq", "Muqanna"], 0, "Spitamen Iskandar qo'shiniga qarshi 3 yil partizanlik urushini olib borgan."),
    ("Qadimgi davr", "Fors shohi Kir II ga qarshi kurashgan massagetlar malikasi kim?", ["To'maris", "Zarina", "Barchinoy", "Gavharshod"], 0, "To'maris Kir II qo'shinini tor-mor etgan."),
    ("Qadimgi davr", "Eron shohi Doro I qo'shinini dashtga adashtirib halok qilgan cho'pon qahramon kim?", ["Shiroq", "Spitamen", "Rustam", "Alpomish"], 0, "Cho'pon Shiroq o'z jonini fido qilib dushmanni adashtirgan."),
    ("O'rta asrlar", "Mo'g'ullarga (Chingizxonga) qarshi afsonaviy jasorat ko'rsatgan Xorazmshoh kim?", ["Jaloliddin Manguberdi", "Muhammad Xorazmshoh", "Tekesh", "Qutbiddin"], 0, "Jaloliddin Manguberdi vatan ozodligi yo'lida 11 yil mardonavor jang qilgan."),
    ("O'rta asrlar", "Mo'g'ullar istilosi paytida Xo'jand mudofaasiga rahbarlik qilgan qahramon kim?", ["Temur Malik", "Jaloliddin", "Najmiddin Kubro", "Mahmud Torobiy"], 0, "Temur Malik Sirdaryo orqali suzib ketib qahramonlik ko'rsatgan."),
    ("O'rta asrlar", "Samarqand mudofaasida mo'g'ullarga qarshi xalq harakatiga boshchilik qilgan shayx kim?", ["Najmiddin Kubro", "Bahouddin Naqshband", "Ahmad Yassaviy", "Xoja Ahror"], 0, "Xorazmda Najmiddin Kubro vatan himoyasida shahid bo'lgan."),
    ("Is lom madaniyati", "Eng ishonchli hadislar to'plami 'Al-Jome' as-Sahih' muallifi kim?", ["Imom al-Buxoriy", "Imom at-Termiziy", "Imom Moturidiy", "Burhoniddin Marg'inoniy"], 0, "Hadis ilmining sultoni Imom al-Buxoriy."),
    ("Is lom madaniyati", "Islom huquqshunosligi (fiqh) bo'yicha 'Al-Hidoya' asari muallifi kim?", ["Burhoniddin Marg'inoniy", "Imom Buxoriy", "Zamaxshariy", "Qaffol Shoshiy"], 0, "Burhoniddin Marg'inoniy butun islom olamiga mashhur fiqh olimi."),
    ("Is lom madaniyati", "Kalom ilmi va aqida maktabi asoschisi bo'lgan buyuk samarqandlik alloma kim?", ["Imom Abu Mansur Moturidiy", "G'azzoliy", "Ibn Rushd", "Termiziy"], 0, "Imom Moturidiy moturidiylik aqidaviy yo'nalishining asoschisidir."),
    ("O'rta asrlar", "'Hindiston' va 'Qadimgi xalqlardan qolgan yodgorliklar' asarlari muallifi kim?", ["Abu Rayhon Beruniy", "Ibn Sino", "Al-Farg'oniy", "Ibn Battuta"], 0, "Buyuk astronom va geograf Abu Rayhon Beruniy."),
    ("O'rta asrlar", "Nil daryosi sathini o'lchovchi 'Nilometr' qurilmasini ixtiro qilgan alloma kim?", ["Ahmad al-Farg'oniy", "Al-Xorazmiy", "Beruniy", "Ulug'bek"], 0, "Al-Farg'oniy Qohirada Nilometrni barpo etgan."),
    ("Xonliklar davri", "Buxoro amirligida hukmronlik qilgan oxirgi sulola qaysi?", ["Mang'itlar sulolasi", "Ashtarxoniylar", "Shayboniylar", "Temuriylar"], 0, "1756-1920 yillarda Mang'itlar hukmronlik qilgan."),
    ("Xonliklar davri", "Qo'qon xonligida hukmronlik qilgan sulola qaysi?", ["Minglar sulolasi", "Qo'ng'irotlar", "Mang'itlar", "Saljuqiylar"], 0, "Qo'qon xonligini Ming sulolasi boshqargan."),
    ("Xonliklar davri", "Xiva xonligida hukmronlik qilgan sulola qaysi?", ["Qo'ng'irotlar sulolasi", "Mang'itlar", "Minglar", "Somoniylar"], 0, "Xiva xonligida Qo'ng'irot sulolasi hukmron bo'lgan."),
    ("Jahon tarixi", "Fransuz buyuk inqilobi qaysi yili boshlangan?", ["1789-yil", "1812-yil", "1776-yil", "1848-yil"], 0, "1789-yil 14-iyulda Bastiliya qal'asi ishg'ol qilingan."),
    ("O'zbekiston tarixi", "O'zbek tili Davlat tili maqomini qachon olgan?", ["1989-yil 21-oktyabr", "1991-yil 1-sentyabr", "1992-yil 8-dekabr", "1990-yil 20-iyun"], 0, "1989-yil 21-oktyabrda 'Davlat tili haqida'gi Qonun qabul qilingan.")
]

for item in hist_questions:
    questions_data.append((6, item[0], item[1], json.dumps(item[2], ensure_ascii=False), item[3], item[4], "o'rta", "10-sinf"))

# --- 7. INGLIZ TILI (40 questions) ---
eng_questions = [
    ("Grammar", "Choose the correct form: She _____ to school every day.", ["goes", "go", "going", "is go"], 0, "Present Simple he/she/it takes -s/es: 'goes'."),
    ("Grammar", "Choose the correct past form of the irregular verb 'buy':", ["bought", "buyed", "boughted", "buys"], 0, "Buy -> Bought -> Bought."),
    ("Grammar", "If I _____ rich, I would travel around the world.", ["were", "am", "will be", "have been"], 0, "Second Conditional: If + past simple (were), would + verb."),
    ("Vocabulary", "What is the opposite (antonym) of the word 'generous'?", ["mean (stingy)", "kind", "polite", "friendly"], 0, "'Generous' means saxiy, opposite is 'mean' (xasis)."),
    ("Prepositions", "I am interested _____ learning computer programming.", ["in", "on", "at", "with"], 0, "Collocation: 'interested in something'."),
    ("Grammar", "They haven't finished their homework _____.", ["yet", "already", "still", "just"], 0, "Present Perfect negative sentences use 'yet' at the end."),
    ("Grammar", "This car is _____ than that one.", ["more expensive", "expensiver", "most expensive", "as expensive"], 0, "Comparative for multi-syllable adjectives: 'more expensive'."),
    ("Grammar", "The book was written _____ Mark Twain.", ["by", "with", "from", "of"], 0, "Passive voice agent marker is 'by'."),
    ("Vocabulary", "A person who looks after people's teeth is called a _____.", ["dentist", "surgeon", "pilot", "lawyer"], 0, "Teeth specialist is a dentist."),
    ("Grammar", "Look at those dark clouds! It _____ rain.", ["is going to", "will", "shall", "does"], 0, "Be going to is used for predictions based on present evidence."),
    ("Modals", "You _____ wear a seatbelt while driving. It is the law.", ["must", "might", "could", "may"], 0, "'Must' expresses strong obligation and legal rule."),
    ("Articles", "He is _____ honest person.", ["an", "a", "the", "-"], 0, "'Honest' starts with a vowel sound /ɒ/, so we use 'an'."),
    ("Prepositions", "She arrived _____ the airport at 6 PM.", ["at", "in", "to", "on"], 0, "Arrive at a specific building/place (airport, station)."),
    ("Vocabulary", "What is the synonym of 'rapid'?", ["fast", "slow", "quiet", "heavy"], 0, "'Rapid' means tez, synonym is 'fast'."),
    ("Grammar", "Neither Tom _____ Jerry was at the party.", ["nor", "or", "and", "but"], 0, "Correlative conjunction pair is 'neither ... nor'."),
    ("Grammar", "Either you apologize, _____ leave the room.", ["or", "nor", "and", "both"], 0, "Correlative conjunction pair is 'either ... or'."),
    ("Grammar", "I have known him _____ five years.", ["for", "since", "during", "from"], 0, "'For' is used with a duration of time (for 5 years)."),
    ("Grammar", "She has lived in Tashkent _____ 2015.", ["since", "for", "in", "from"], 0, "'Since' is used with a specific starting point in the past."),
    ("Grammar", "Listen! The baby _____.", ["is crying", "cries", "cried", "cry"], 0, "Action happening right now at the moment of speech: Present Continuous."),
    ("Conditionals", "If you heat ice, it _____.", ["melts", "will melt", "melted", "would melt"], 0, "Zero Conditional (scientific fact): If + present, present."),
    ("Vocabulary", "What does the idiom 'piece of cake' mean?", ["Very easy", "Very delicious", "Difficult", "Expensive"], 0, "'Piece of cake' means juda oson ish."),
    ("Vocabulary", "What does 'break a leg' mean in English?", ["Good luck!", "Be careful!", "Go home!", "Stop talking!"], 0, "The idiom 'break a leg' wishes good luck to performers."),
    ("Grammar", "How _____ money do you have in your pocket?", ["much", "many", "few", "any"], 0, "Money is uncountable, so we ask 'How much'."),
    ("Grammar", "How _____ apples are there in the basket?", ["many", "much", "little", "any"], 0, "Apples are countable plural, so we ask 'How many'."),
    ("Reported Speech", "'I am tired,' said John. -> John said that he _____ tired.", ["was", "is", "were", "had been"], 0, "Tense shifts back: Present Simple 'am' becomes Past Simple 'was'."),
    ("Grammar", "By 2030, scientists _____ a cure for the disease.", ["will have found", "will find", "find", "found"], 0, "Future Perfect for actions completed before a future deadline: 'will have found'."),
    ("Vocabulary", "A place where books are kept for people to read or borrow is a _____.", ["library", "bookshop", "laboratory", "bakery"], 0, "Library - kutubxona."),
    ("Prepositions", "The cat is sleeping _____ the table.", ["under", "between", "into", "through"], 0, "'Under the table' - stolning tagida."),
    ("Phrasal Verbs", "He decided to _____ smoking to improve his health.", ["give up", "look for", "take off", "turn on"], 0, "'Give up' means to quit (tashlamoq)."),
    ("Phrasal Verbs", "Please _____ your shoes before entering the house.", ["take off", "put on", "turn off", "get up"], 0, "'Take off' means yechmoq (kiyim yoki poyabzal)."),
    ("Grammar", "This task is _____ difficult for me to solve alone.", ["too", "enough", "such", "so that"], 0, "'Too + adjective + to-infinitive' means ortiqcha darajada qiyin."),
    ("Grammar", "She is old _____ to drive a car.", ["enough", "too", "so", "such"], 0, "'Adjective + enough' means yetarlicha (old enough)."),
    ("Vocabulary", "Which word is a synonym for 'gigantic'?", ["huge", "tiny", "fragile", "narrow"], 0, "'Gigantic' means ulkan, synonym is 'huge'."),
    ("Grammar", "I look forward to _____ you soon.", ["hearing from", "hear from", "heard from", "be heard"], 0, "'Look forward to' is followed by a gerund (-ing): hearing from."),
    ("Vocabulary", "Someone who writes computer software is a _____.", ["programmer", "accountant", "carpenter", "plumber"], 0, "Software developer is a programmer."),
    ("Grammar", "Unless you study hard, you _____ pass the exam.", ["will not", "will", "would", "shall"], 0, "'Unless' means 'if not' (agar o'qimasang, o'ta olmaysan)."),
    ("Grammar", "Who _____ that beautiful picture?", ["painted", "did paint", "paints", "painting"], 0, "Subject question: Who + past verb (Who painted)."),
    ("Pronouns", "Everybody should do _____ best.", ["their", "his", "her", "its"], 0, "Modern standard English uses singular 'their' for indefinite pronouns."),
    ("Grammar", "I would rather _____ at home tonight.", ["stay", "to stay", "staying", "stayed"], 0, "'Would rather' takes bare infinitive: 'stay'."),
    ("Prepositions", "Congratulations _____ your graduation!", ["on", "for", "with", "at"], 0, "Collocation: 'congratulations on something'.")
]

for item in eng_questions:
    questions_data.append((7, item[0], item[1], json.dumps(item[2], ensure_ascii=False), item[3], item[4], "o'rta", "10-sinf"))

# --- 8. INFORMATIKA / IT (40 questions) ---
it_questions = [
    ("Python", "Python dasturlash tilida ekranga ma'lumot chiqarish funksiyasi qaysi?", ["print()", "echo()", "cout", "System.out.println()"], 0, "Python'da konsolga chiqarish print() funksiyasi orqali bajariladi."),
    ("Sanoq sistemalari", "Ikkilik (binar) sanoq sistemasida qaysi raqamlar ishlatiladi?", ["Faqat 0 va 1", "0 dan 9 gacha", "0 dan 7 gacha", "0 dan F gacha"], 0, "Binar sanoq sistemasida faqat 0 va 1 raqamlari mavjud."),
    ("Python", "Python'da butun sonlar (integer) qaysi toifaga kiradi?", ["int", "float", "str", "bool"], 0, "Butun sonlar int ma'lumot turi bilan belgilanadi."),
    ("Python", "Python'da haqiqiy (o'nli kasr) sonlar qaysi toifaga kiradi?", ["float", "int", "decimal", "double"], 0, "Suzuvchi nuqtali o'nli kasr sonlar float deyiladi."),
    ("Python", "Qaysi belgi Python'da bir qatorli izoh (kommentariya) uchun ishlatiladi?", ["#", "//", "/*", "--"], 0, "Python'da # belgisi izoh bildiradi."),
    ("Ma'lumotlar tuzilmasi", "Python'da o'zgarmas (immutable) ketma-ketlik qaysi?", ["tuple (kortej)", "list (ro'yxat)", "dict (lug'at)", "set (to'plam)"], 0, "Tuple elementlarini yaratilgach o'zgartirib bo'lmaydi."),
    ("Algoritmlar", "To'g'ri chiziqli ketma-ket bajariladigan algoritm nima deyiladi?", ["Chiziqli algoritm", "Tarmoqlanuvchi algoritm", "Takrorlanuvchi algoritm", "Rekursiv algoritm"], 0, "Hech qanday shartsiz ketma-ket bajariladigan jarayon chiziqli deyiladi."),
    ("Tarmoqlar", "IP manzil nechta baytdan (IPv4 da) iborat bo'ladi?", ["4 bayt (32 bit)", "16 bayt", "8 bayt", "2 bayt"], 0, "IPv4 manzili 32 bit (4 ta 8-bitli oktet)dan iborat."),
    ("Web", "Veb-sahifaning asosiy skeletini (tuzilishini) yaratuvchi til qaysi?", ["HTML", "CSS", "JavaScript", "Python"], 0, "HTML - HyperText Markup Language gipermatn belgilash tili."),
    ("Web", "Veb-sahifalarga vizual dizayn va bezak beruvchi til qaysi?", ["CSS", "HTML", "SQL", "PHP"], 0, "CSS - Cascading Style Sheets dizayn tilidir."),
    ("Web", "Veb-sahifalarga interaktivlik va dinamik harakat qo'shuvchi dasturlash tili qaysi?", ["JavaScript", "HTML", "CSS", "SQL"], 0, "Brauzerda ishlovchi dinamik dasturlash tili JavaScript."),
    ("Ma'lumotlar bazasi", "SQL tilida jadvaldan ma'lumotlarni tanlab olish uchun qaysi buyruq ishlatiladi?", ["SELECT", "INSERT", "UPDATE", "DELETE"], 0, "Ma'lumotlarni so'rash va tanlash SELECT operatori bilan bajariladi."),
    ("Ma'lumotlar bazasi", "SQL tilida jadvalga yangi qator qo'shish buyrug'i qaysi?", ["INSERT INTO", "ADD ROW", "CREATE", "PUSH"], 0, "INSERT INTO table_name VALUES (...) yangi ma'lumot qo'shadi."),
    ("Xotira", "1 Kilobayt (KB) necha baytga teng?", ["1024 bayt", "1000 bayt", "512 bayt", "2048 bayt"], 0, "1 KB = 2^10 = 1024 bayt."),
    ("Xotira", "1 Bayt necha bitga teng?", ["8 bit", "4 bit", "16 bit", "2 bit"], 0, "1 bayt = 8 bit."),
    ("Apparat ta'minoti", "Kompyuterning asosiy 'miyasi' hisoblangan qurilma qaysi?", ["Protsessor (CPU)", "Qattiq disk (HDD)", "Tezkor xotira (RAM)", "Videokarta (GPU)"], 0, "CPU (Central Processing Unit) barcha hisoblashlarni amalga oshiradi."),
    ("Xotira", "Kompyuter o'chirilganda qaysi xotiradagi ma'lumotlar o'chib ketadi?", ["RAM (Tezkor xotira)", "ROM (Doimiy xotira)", "SSD", "Flash xotira"], 0, "RAM uchuvchan xotira bo'lib, tok uzilsa ma'lumot yo'qoladi."),
    ("Python", "Python'da ro'yxatga oxiridan element qo'shish metodi qaysi?", ["append()", "push()", "add()", "insert_last()"], 0, "list.append(item) elementni ro'yxat oxiriga qo'shadi."),
    ("Python", "Python'da ro'yxat uzunligini aniqlovchi funksiya qaysi?", ["len()", "length()", "size()", "count()"], 0, "len(my_list) ro'yxat elementlari sonini qaytaradi."),
    ("Dasturlash", "O'z-o'zini chaqiruvchi funksiya nima deyiladi?", ["Rekursiv funksiya", "Siklik funksiya", "Statik funksiya", "Anonim funksiya"], 0, "Funksiya o'z tanasida o'zini chaqirsa rekursiya deyiladi."),
    ("Kiberxavfsizlik", "Kompyuterni zararli dasturlardan himoyalovchi dastur nima deyiladi?", ["Antivirus", "Fayrvoll emas", "Brauzer", "Drayver"], 0, "Antivirus dasturlari virus va troyanlarni aniqlaydi va zararsizlantiradi."),
    ("Algoritmlar", "Ikkilik qidiruv (Binary Search) algoritmining o'rtacha murakkabligi qanday?", ["O(log n)", "O(n)", "O(n^2)", "O(1)"], 0, "Saralangan massivda binar qidiruv O(log n) vaqt oladi."),
    ("Tarmoqlar", "Veb-saytlarga xavfsiz shifrlangan ulanish protokoli qaysi?", ["HTTPS", "HTTP", "FTP", "Telnet"], 0, "HTTPS (SSL/TLS orqali) xavfsiz ma'lumot almashinuvini ta'minlaydi."),
    ("Python", "Python'da qaysi kalit so'z siklni (loop) muddatidan oldin to'xtatadi?", ["break", "continue", "pass", "return"], 0, "'break' sikldan darhol chiqib ketadi."),
    ("Python", "Python'da siklning navbatdagi qadamiga o'tib ketish uchun nima ishlatiladi?", ["continue", "break", "skip", "next"], 0, "'continue' joriy iteratsiyani tugatib keyingisiga o'tadi."),
    ("Operatsion tizim", "Ochiq kodli va tekin tarqatiladigan mashhur operatsion tizim qaysi?", ["Linux", "Windows", "macOS", "MS-DOS"], 0, "Linux ochiq manbali va erkin operatsion tizim yadrosidir."),
    ("Tarmoqlar", "Domen nomini (masalan: google.com) IP manzilga aylantirib beruvchi tizim qaysi?", ["DNS", "DHCP", "FTP", "SMTP"], 0, "DNS (Domain Name System) nomlarni IP ga bog'laydi."),
    ("Python", "Python'da mantiqiy toifa qanday ataladi?", ["bool", "boolean", "logical", "binary"], 0, "True va False qiymatlarini saqlovchi toifa bool."),
    ("Python", "3 ** 3 ifodaning natijasi nima bo'ladi?", ["27", "9", "6", "81"], 0, "Python'da ** darajaga ko'tarish: 3^3 = 27."),
    ("Dasturlash", "OOP (Obyektga yo'naltirilgan dasturlash) ning asosiy tamoyillaridan biri qaysi?", ["Inkapsulyatsiya", "Kompilyatsiya", "Translyatsiya", "Formatlash"], 0, "Inkapsulyatsiya, merosxo'rlik va polimorfizm OOP asosidir."),
    ("Dasturlash", "Faqat bitta xususiyat yoki harakatni o'zida ifodalovchi qolip nima deyiladi?", ["Klass (Class)", "Modul", "Paket", "Fayl"], 0, "Klass obyektlar yaratish uchun andoza (qolip) hisoblanadi."),
    ("Python", "Python'da lug'at (dictionary) qanday qavslar bilan yoziladi?", ["Figurali qavs { }", "Kvadrat qavs [ ]", "Dumaloq qavs ( )", "Burchakli qavs < >"], 0, "Lug'atlar {key: value} shaklida figurali qavsda yoziladi."),
    ("Python", "Ro'yxat (list) qaysi qavslar bilan belgilanadi?", ["Kvadrat qavs [ ]", "Figurali qavs { }", "Dumaloq qavs ( )", "Qo'shtirnoq"], 0, "Ro'yxatlar [1, 2, 3] shaklida kvadrat qavsda bo'ladi."),
    ("Sun'iy intellekt", "Kompyuterning insoniy aql talab qiladigan vazifalarni bajarish sohasi nima?", ["AI (Sun'iy intellekt)", "Kriptografiya", "Grafika", "Web-dizayn"], 0, "Artificial Intelligence (AI) - sun'iy intellekt."),
    ("Tarmoqlar", "Lokal kompyuter tarmog'ining qisqartma nomi qanday?", ["LAN", "WAN", "MAN", "PAN"], 0, "LAN - Local Area Network (mahalliy tarmoq)."),
    ("Kiberxavfsizlik", "Foydalanuvchilarni aldatib parollarini o'g'irlash kiberhujumi nima deyiladi?", ["Fishing (Phishing)", "Spam", "DDoS", "Brute Force"], 0, "Fishing - soxta saytlar orqali maxfiy ma'lumotlarni o'g'irlash."),
    ("Web", "Saytning foydalanuvchiga ko'rinadigan tomoni qanday ataladi?", ["Frontend", "Backend", "Database", "DevOps"], 0, "Mijoz (foydalanuvchi) ko'radigan qismi Frontend deyiladi."),
    ("Web", "Saytning server tomoni va ma'lumotlar bilan ishlovchi qismi nima deyiladi?", ["Backend", "Frontend", "UI Design", "Layout"], 0, "Server mantig'i va API qismi Backend deyiladi."),
    ("Versiyalarni boshqarish", "Kod versiyalarini boshqarish va jamoaviy ishlash uchun eng mashhur tizim qaysi?", ["Git", "Docker", "Apache", "Nginx"], 0, "Git - taqsimlangan versiyalarni boshqarish tizimi."),
    ("Python", "Python dasturlash tilining yaratuvchisi kim?", ["Gvido van Rossum", "Jeyms Gosling", "Dennis Ritchi", "Bjarne Straustrup"], 0, "Python 1991-yilda Gvido van Rossum tomonidan yaratilgan.")
]

for item in it_questions:
    questions_data.append((8, item[0], item[1], json.dumps(item[2], ensure_ascii=False), item[3], item[4], "o'rta", "10-sinf"))

# Insert all 320 questions
for q in questions_data:
    c.execute("""
        INSERT INTO questions (subject_id, chapter_title, question_text, options, correct_index, explanation, difficulty, grade)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, q)

conn.commit()

c.execute("SELECT subject_id, COUNT(*) FROM questions GROUP BY subject_id")
print("New counts per subject:", c.fetchall())
c.execute("SELECT COUNT(*) FROM questions")
total = c.fetchone()[0]
print(f"Total seeded questions: {total}")

conn.close()
