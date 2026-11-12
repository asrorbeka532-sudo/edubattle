# -*- coding: utf-8 -*-
"""
EduBattle - 2020-2023 Yangi darsliklar asosidagi savollar banki:
Fan 3: Kimyo (7-11-sinf yangi nashrlar) - 50 ta savol
Fan 4: Biologiya (6-11-sinf yangi nashrlar) - 50 ta savol
"""

# ==========================================
# 3. KIMYO (Subject ID: 3) - 50 TA SAVOL
# ==========================================
KIMYO_QUESTIONS = [
    # 7-sinf
    {
        "subject_id": 3,
        "grade": "7-sinf",
        "chapter_title": "Boshlang'ich kimyoviy tushunchalar",
        "question_text": "Quyidagi moddalardan qaysi biri oddiy modda hisoblanadi?",
        "options": ["Kislorod (O₂)", "Suv (H₂O)", "Osh tuzi (NaCl)", "Karbonat angidrid (CO₂)"],
        "correct_index": 0,
        "explanation": "Bitta turdagi kimyoviy element atomlaridan tuzilgan moddalar oddiy modda deyiladi (masalan, O₂).",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "7-sinf",
        "chapter_title": "Boshlang'ich kimyoviy tushunchalar",
        "question_text": "Fizik hodisani aniqlang.",
        "options": ["Muzning erishi", "Temirning zanglashishi", "Qog'ozning yonishi", "Sutning achishi"],
        "correct_index": 0,
        "explanation": "Muz eriganda moddaning tarkibi o'zgarmaydi, faqat agregat holati o'zgaradi, shuning uchun bu fizik hodisa.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "7-sinf",
        "chapter_title": "Valentlik",
        "question_text": "Al₂O₃ birikmasida alyuminiyning valentligi nechaga teng?",
        "options": ["III", "II", "I", "IV"],
        "correct_index": 0,
        "explanation": "Kislorod birikmalarda II valentli, 3*2 = 6, 6 / 2 = 3. Alyuminiy valentligi III.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "7-sinf",
        "chapter_title": "Nisbiy molekulyar massa",
        "question_text": "Sulfat kislotaning (H₂SO₄) nisbiy molekulyar massasini toping (Ar(H)=1, Ar(S)=32, Ar(O)=16).",
        "options": ["98", "96", "100", "82"],
        "correct_index": 0,
        "explanation": "Mr(H₂SO₄) = 1*2 + 32 + 16*4 = 2 + 32 + 64 = 98.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "7-sinf",
        "chapter_title": "Modda miqdori",
        "question_text": "0.5 mol suvda (H₂O) nechta molekula bor? (N_A = 6.02*10²³)",
        "options": ["3.01*10²³", "6.02*10²³", "1.204*10²⁴", "1.5*10²³"],
        "correct_index": 0,
        "explanation": "N = ν * N_A = 0.5 * 6.02*10²³ = 3.01*10²³.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "7-sinf",
        "chapter_title": "Gazlarning molyar hajmi",
        "question_text": "Normal sharoitda 44.8 litr kislorod gazi necha mol bo'ladi?",
        "options": ["2 mol", "1 mol", "0.5 mol", "4 mol"],
        "correct_index": 0,
        "explanation": "Normal sharoitda 1 mol har qanday gaz 22.4 l hajmni egallaydi. 44.8 / 22.4 = 2 mol.",
        "difficulty": "oson"
    },
    # 8-sinf
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Atom tuzilishi",
        "question_text": "Fosfor atomi yadrosida nechta proton va neytron bor? (³¹₁₅P)",
        "options": ["15 ta proton, 16 ta neytron", "15 ta proton, 15 ta neytron", "16 ta proton, 15 ta neytron", "31 ta proton, 15 ta neytron"],
        "correct_index": 0,
        "explanation": "Tartib raqami Z = 15 (protonlar). Neytronlar soni N = A - Z = 31 - 15 = 16.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Davriy qonun",
        "question_text": "Davriy sistemada bitta guruhda yuqoridan pastga tushgan sari elementlarning metallik xossasi qanday o'zgaradi?",
        "options": ["Kuchayadi", "Kamayadi", "O'zgarmaydi", "Dastlab kamayadi, so'ng kuchayadi"],
        "correct_index": 0,
        "explanation": "Guruhda yuqoridan pastga atom radiusi ortadi, elektron berish osonlashadi va metallik xossasi kuchayadi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Kimyoviy bog'lanish",
        "question_text": "Osh tuzi (NaCl) molekulasidagi kimyoviy bog'lanish turini aniqlang.",
        "options": ["Ionli bog'lanish", "Kovalent qutbsiz bog'lanish", "Kovalent qutbli bog'lanish", "Vodorod bog'lanish"],
        "correct_index": 0,
        "explanation": "Tipik metall (Na) va tipik metallmas (Cl) orasida elektrmanfiyliklar farqi katta bo'lgani sababli ionli bog'lanish hosil bo'ladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Kimyoviy bog'lanish",
        "question_text": "Quyidagi molekulalardan qaysi birida kovalent qutbsiz bog'lanish mavjud?",
        "options": ["N₂ (azot)", "HCl (xlorid kislota)", "H₂O (suv)", "NH₃ (ammiak)"],
        "correct_index": 0,
        "explanation": "Bir xil elektrmanfiylikka ega bo'lgan bir xil metallmas atomlari orasida kovalent qutbsiz bog' hosil bo'ladi (N₂).",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Oksidlar",
        "question_text": "Asosli oksidni ko'rsating.",
        "options": ["CaO", "SO₃", "CO₂", "P₂O₅"],
        "correct_index": 0,
        "explanation": "CaO (kalsiy oksid) asosli oksid bo'lib, suv bilan reaksiyaga kirishib ishqor (Ca(OH)₂) hosil qiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Eritmalar",
        "question_text": "180 g suvda 20 g shakar eritildi. Hosil bo'lgan eritmadagi shakarning massa ulushini (%) toping.",
        "options": ["10%", "20%", "11.1%", "15%"],
        "correct_index": 0,
        "explanation": "Eritma massasi = 180 + 20 = 200 g. Massa ulushi ω = (20 / 200) * 100% = 10%.",
        "difficulty": "orta"
    },
    # 9-sinf
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Elektrolitik dissotsiatsiya",
        "question_text": "Suvli eritmada dissotsiyalanganda kation sifatida faqat H⁺ ionlarini ajratadigan moddalar nima deyiladi?",
        "options": ["Kislotalar", "Asoslar", "Tuzlar", "Oksidlar"],
        "correct_index": 0,
        "explanation": "Elektrolitik dissotsiatsiya nazariyasiga ko'ra kislotalar dissotsiyalanganda kation sifatida faqat vodorod ionlari (H⁺) hosil bo'ladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Elektrolitik dissotsiatsiya",
        "question_text": "Ishqoriy muhitda lakmus qog'ozining rangi qanday tusga kiradi?",
        "options": ["Ko'k", "Qizil", "Sariq", "Rangsiz"],
        "correct_index": 0,
        "explanation": "Lakmus indikatori neytral muhitda binafsha, kislotali muhitda qizil, ishqoriy muhitda ko'k rangga kiradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Oksidlanish-qaytarilish reaksiyalari",
        "question_text": "Zn + 2HCl → ZnCl₂ + H₂ reaksiyasida qaysi element qaytaruvchi hisoblanadi?",
        "options": ["Rux (Zn)", "Vodorod (H⁺)", "Xlor (Cl⁻)", "ZnCl₂"],
        "correct_index": 0,
        "explanation": "Rux o'zining oksidlanish darajasini 0 dan +2 ga oshirib elektron beradi, demak u qaytaruvchi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Kimyoviy muvozanat",
        "question_text": "N₂(g) + 3H₂(g) ⇌ 2NH₃(g) + Q ekzotermik reaksiyasida ammiak unumini oshirish uchun qanday sharoit kerak?",
        "options": ["Bosimni oshirish va temperaturani pasaytirish", "Bosimni pasaytirish va temperaturani oshirish", "Faqat temperaturani oshirish", "Katalizator qo'shish"],
        "correct_index": 0,
        "explanation": "Le Shatelye prinsipiga binoan, gazlar hajmi kamayayotgani uchun bosimni oshirish va ekzotermik reaksiya bo'lgani uchun temperaturani pasaytirish ammiak chiqishini oshiradi.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Galogenlar",
        "question_text": "Galogenlardan qaysi biri oddiy sharoitda qizg'ish-qo'ng'ir rangli suyuqlik hisoblanadi?",
        "options": ["Brom (Br₂)", "Xlor (Cl₂)", "Yod (I₂)", "Ftor (F₂)"],
        "correct_index": 0,
        "explanation": "Oddiy sharoitda ftor va xlor gaz, brom suyuqlik, yod esa qattiq kristall moddadir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Metallmaslar",
        "question_text": "Oltingugurt (IV) oksidining (SO₂) o'tkir hidli gazi suvda eriganda qaysi kislotani hosil qiladi?",
        "options": ["Sulfit kislota (H₂SO₃)", "Sulfat kislota (H₂SO₄)", "Vodorod sulfid (H₂S)", "Tiosulfat kislota"],
        "correct_index": 0,
        "explanation": "SO₂ + H₂O ⇌ H₂SO₃ (sulfit kislota).",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Azot va uning birikmalari",
        "question_text": "Laboratoriyada ammiak gazini (NH₃) qanday usulda aniqlash mumkin?",
        "options": ["Nam qizil lakmus qog'ozini ko'kartirishi bilan", "Ohakli suvni loyqalantirishi bilan", "Yonayotgan cho'pni o'chirishi bilan", "Qo'ng'ir rangli tusi bilan"],
        "correct_index": 0,
        "explanation": "Ammiak o'ziga xos o'tkir hidli, suvda ishqoriy muhit hosil qiluvchi gaz bo'lib, nam qizil lakmusni ko'kartiradi.",
        "difficulty": "orta"
    },
    # 10-sinf
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Organik kimyoga kirish",
        "question_text": "Organik birikmalarning kimyoviy tuzilish nazariyasi asoschisi kim?",
        "options": ["A.M.Butlerov", "D.I.Mendeleyev", "M.V.Lomonosov", "A.Lavuazye"],
        "correct_index": 0,
        "explanation": "1861-yilda rus olimi Aleksandr Mixaylovich Butlerov organik moddalarning kimyoviy tuzilish nazariyasini yaratdi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Alkanlar",
        "question_text": "To'yingan uglevodorodlarning (alkanlarning) umumiy formulasini ko'rsating.",
        "options": ["C_n H_(2n+2)", "C_n H_(2n)", "C_n H_(2n-2)", "C_n H_(2n-6)"],
        "correct_index": 0,
        "explanation": "Alkanlarning umumiy formulasi C_n H_(2n+2).",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Alkanlar",
        "question_text": "Metanning xlorlanish reaksiyasi (radikal o'rin olish) qanday sharoitda kechadi?",
        "options": ["Yorug'lik nuri (hν) ta'sirida", "Past temperaturada", "Faqat yuqori bosim ostida", "Katalizatorsiz qorong'ida"],
        "correct_index": 0,
        "explanation": "Metanning xlor bilan o'rin olish reaksiyasi ultrabinafsha yoki yorug'lik kvanti (hν) ta'sirida erkin radikal zanjir mexanizmida boradi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Alkenlar",
        "question_text": "Etilen (C₂H₄) molekulasidagi uglerod atomlarining gibridlanish turini aniqlang.",
        "options": ["sp²", "sp³", "sp", "Gibridlanmagan"],
        "correct_index": 0,
        "explanation": "Etilenda uglerodlar o'rtasida qo'shbog' mavjud bo'lib, har bir uglerod atomi sp² gibridlangan holatda bo'ladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Alkenlar",
        "question_text": "To'yinmagan uglevodorodlarni sifat jihatdan aniqlash uchun qaysi reaktivlar ishlatiladi?",
        "options": ["Bromli suv va kaliy permanganat eritmasi", "Faqat ohakli suv", "Litiy ishqori", "Kumush nitrat"],
        "correct_index": 0,
        "explanation": "Alken va alkinlar bromli suvni va KMnO₄ ning binafsha eritmasini rangsizlantiradi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Alkinlar",
        "question_text": "Asetilenning (C₂H₂) xalqaro IUPAC nomenklaturasi bo'yicha nomi nima?",
        "options": ["Etin", "Eten", "Propin", "Metan"],
        "correct_index": 0,
        "explanation": "Asetilen - bu etin (C₂H₂).",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Aromatik uglevodorodlar",
        "question_text": "Benzolning (C₆H₆) formulasini birinchi bo'lib halqa ko'rinishida taklif etgan olim kim?",
        "options": ["F.A.Kekule", "A.M.Butlerov", "V.V.Markovnikov", "N.N.Zinin"],
        "correct_index": 0,
        "explanation": "1865-yilda Fridrix Avgust Kekule benzolning olti burchakli halqa formulasini taklif qilgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Spirtlar",
        "question_text": "Tibbiyotda va antiseptik vosita sifatida keng qo'llaniladigan etanolning formulasi qaysi?",
        "options": ["C₂H₅OH", "CH₃OH", "C₃H₇OH", "C₆H₅OH"],
        "correct_index": 0,
        "explanation": "Etanol (etil spirt) formulasi: C₂H₅OH.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Ko'p atomli spirtlar",
        "question_text": "Uch atomli spirt - glitserinning formulasini toping.",
        "options": ["C₃H₅(OH)₃", "C₂H₄(OH)₂", "C₄H₉OH", "C₆H₄(OH)₂"],
        "correct_index": 0,
        "explanation": "Glitserin (propan-1,2,3-triol) formulasi C₃H₅(OH)₃.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Aldegidlar",
        "question_text": "Aldegidlar uchun sifat reaksiyasi bo'lgan 'kumush ko'zgu' reaksiyasida qaysi modda hosil bo'ladi?",
        "options": ["Sof kumush cho'kmasi (Ag)", "Oq rangli tuz", "Qizil rangli mis oksidi", "Gazsimon vodorod"],
        "correct_index": 0,
        "explanation": "Aldegidlar kumush oksidining ammiakli eritmasi [Ag(NH₃)₂]OH bilan qizdirilganda nay devorida yaltiroq kumush qatlami hosil qiladi.",
        "difficulty": "orta"
    },
    # 11-sinf
    {
        "subject_id": 3,
        "grade": "11-sinf",
        "chapter_title": "Karbon kislotalar",
        "question_text": "Sirka kislotaning (etan kislota) formulasini aniqlang.",
        "options": ["CH₃COOH", "HCOOH", "C₂H₅COOH", "C₆H₅COOH"],
        "correct_index": 0,
        "explanation": "Sirka kislota: CH₃COOH.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "11-sinf",
        "chapter_title": "Murakkab efirlar va yog'lar",
        "question_text": "Eterifikatsiya reaksiyasi nima?",
        "options": ["Spirt va karbon kislotadan murakkab efir hosil bo'lish reaksiyasi", "Yog'larning sovunlanishi", "Alkanlarning yonishi", "Spirtlarning degidratatsiyasi"],
        "correct_index": 0,
        "explanation": "Karbon kislotalarning spirtlar bilan kislotali katalizator ishtirokida murakkab efir hosil qilish jarayoni eterifikatsiya deyiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "11-sinf",
        "chapter_title": "Uglevodlar",
        "question_text": "Glyukozaning molekulyar formulasini ko'rsating.",
        "options": ["C₆H₁₂O₆", "C₁₂H₂₂O₁₁", "(C₆H₁₀O₅)_n", "C₅H₁₀O₅"],
        "correct_index": 0,
        "explanation": "Glyukoza va fruktozaning molekulyar formulasi C₆H₁₂O₆.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "11-sinf",
        "chapter_title": "Polisaxaridlar",
        "question_text": "Kraxmalga yod eritmasi ta'sir ettirilganda qanday rang hosil bo'ladi?",
        "options": ["To'q ko'k rang", "Qizil-qo'ng'ir rang", "Sariq rang", "Yashil rang"],
        "correct_index": 0,
        "explanation": "Kraxmalning yod bilan o'zaro ta'siri to'q ko'k rangli birikma hosil qiladi, bu kraxmalni sifat jihatdan aniqlash usulidir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "11-sinf",
        "chapter_title": "Aminlar va aminokislotalar",
        "question_text": "Aminokislotalar qanday funksional guruhlarni o'z ichiga oladi?",
        "options": ["Amin guruhi (-NH₂) va karboksil guruhi (-COOH)", "Faqat gidroksil guruhi (-OH)", "Aldegid (-CHO) va keton (-CO-) guruhi", "Faqat amin guruhi (-NH₂)"],
        "correct_index": 0,
        "explanation": "Aminokislotalar amfoter xossaga ega bo'lib, molekulasida asosli amin guruhi (-NH₂) va kislotali karboksil guruhi (-COOH) tutadi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "11-sinf",
        "chapter_title": "Oqsillar",
        "question_text": "Oqsillarning birlamchi tuzilishida aminokislotalar qanday bog'lar orqali birikadi?",
        "options": ["Peptid bog'lar", "Vodorod bog'lar", "Disulfid ko'prikchalar", "Ionli bog'lar"],
        "correct_index": 0,
        "explanation": "Aminokislotalar bir-biri bilan peptid (-CO-NH-) bog'lari orqali polipeptid zanjirini hosil qiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "11-sinf",
        "chapter_title": "Yuqori molekulyar birikmalar",
        "question_text": "Polietilen qaysi moddaning polimerlanishidan olinadi?",
        "options": ["Etilen (C₂H₄)", "Metan (CH₄)", "Asetilen (C₂H₂)", "Benzol (C₆H₆)"],
        "correct_index": 0,
        "explanation": "Etilenning (eten) qo'shbog'i uzilishi orqali yuqori molekulali polietilen (-CH₂-CH₂-)_n olinadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Tuzlarning gidrolizi",
        "question_text": "Kuchsiz asos va kuchli kislotadan hosil bo'lgan tuz (masalan, NH₄Cl) suvda eritilganda muhit qanday bo'ladi?",
        "options": ["Kislotali (pH < 7)", "Ishqoriy (pH > 7)", "Neytral (pH = 7)", "O'zgarmaydi"],
        "correct_index": 0,
        "explanation": "Kation bo'yicha gidroliz sodir bo'ladi, eritmada erkin H⁺ ionlari ko'payib, muhit kislotali bo'ladi.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Metallar",
        "question_text": "Quyidagi metallardan qaysi biri oddiy sharoitda suyuq holda bo'ladi?",
        "options": ["Simob (Hg)", "Qo'rg'oshin (Pb)", "Qalay (Sn)", "Galliy (Ga)"],
        "correct_index": 0,
        "explanation": "Simob (Hg) xona temperaturasida (oddiy sharoitda) suyuq bo'lgan yagona metalldir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Korroziya",
        "question_text": "Metallarning atrof-muhit ta'sirida yemirilishi nima deyiladi?",
        "options": ["Korroziya", "Gidroliz", "Elektroliz", "Diffuziya"],
        "correct_index": 0,
        "explanation": "Metallarning kimyoviy yoki elektrokimyoviy yo'l bilan yemirilish jarayoni korroziya deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Kislotalar",
        "question_text": "Konsentrlangan sulfat kislota (H₂SO₄) qaysi metallar bilan sovuqda passivlanadi va reaksiyaga kirishmaydi?",
        "options": ["Temir (Fe) va alyuminiy (Al)", "Mis (Cu) va rux (Zn)", "Kaliy (K) va natriy (Na)", "Kumush (Ag) va oltin (Au)"],
        "correct_index": 0,
        "explanation": "Konsentrlangan H₂SO₄ va HNO₃ temir, alyuminiy va xromni sovuqda passivlashtiradi (yuzasida zich oksid parda hosil qiladi).",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 3,
        "grade": "7-sinf",
        "chapter_title": "Kimyoviy reaksiyalar turlari",
        "question_text": "CaCO₃ → CaO + CO₂ reaksiyasi kimyoviy reaksiyalarning qaysi turiga kiradi?",
        "options": ["Parchalanish reaksiyasi", "Birikish reaksiyasi", "O'rin olish reaksiyasi", "Almashinish reaksiyasi"],
        "correct_index": 0,
        "explanation": "Bitta murakkab moddadan bir nechta yangi moddalar hosil bo'lishi parchalanish reaksiyasi deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Davriy sistema qonuniyatlari",
        "question_text": "Elementlarning elektrmanfiyligi eng yuqori bo'lgan element qaysi?",
        "options": ["Ftor (F)", "Kislorod (O)", "Xlor (Cl)", "Azot (N)"],
        "correct_index": 0,
        "explanation": "Poling shkalasi bo'yicha ftor (F) eng yuqori elektrmanfiylikka (≈ 4.0) ega.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Alkadienlar",
        "question_text": "Divinil (butadien-1,3) va izopren qaysi qimmatbaho mahsulotni ishlab chiqarishda xomashyo hisoblanadi?",
        "options": ["Sintetik kauchuk", "Dori vositalari", "Sintetik yoqilg'i", "Yuvish vositalari"],
        "correct_index": 0,
        "explanation": "Butadien-1,3 va izopren polimerlanib kauchuk hosil qiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "10-sinf",
        "chapter_title": "Fenollar",
        "question_text": "Karbol kislota deb qaysi moddaga aytiladi?",
        "options": ["Fenol (C₆H₅OH)", "Sirka kislota", "Benzoy kislota", "Pikrin kislota"],
        "correct_index": 0,
        "explanation": "Fenolning (oksibenzol) tarixiy nomi karbol kislota deb ataladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "11-sinf",
        "chapter_title": "Nuklein kislotalar",
        "question_text": "DNK tarkibiga kiruvchi azotli asoslarni aniqlang.",
        "options": ["Adenin, Guanin, Sitozin, Timin", "Adenin, Guanin, Sitozin, Uratsil", "Faqat Adenin va Timin", "Ribolaza va Dezoksiriboza"],
        "correct_index": 0,
        "explanation": "DNK tarkibida A, G, S, T bo'ladi. RNK da esa timin o'rniga uratsil (U) bo'ladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Silitsiy va uning birikmalari",
        "question_text": "Oddiy oyna (deraza oynasi) tayyorlashda qaysi xomashyolardan foydalaniladi?",
        "options": ["Soda (Na₂CO₃), ohaktosh (CaCO₃) va qum (SiO₂)", "Faqat toza qum", "Gips va gil", "Sement va marmar"],
        "correct_index": 0,
        "explanation": "Oddiy silikat oyna tarkibi: Na₂O · CaO · 6SiO₂ bo'lib, soda, ohaktosh va kvars qumidan eritib olinadi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "7-sinf",
        "chapter_title": "Havoning tarkibi",
        "question_text": "Atmosfera havosining hajm bo'yicha asosiy qismini (taxminan 78%) qaysi gaz tashkil etadi?",
        "options": ["Azot (N₂)", "Kislorod (O₂)", "Karbonat angidrid (CO₂)", "Argon (Ar)"],
        "correct_index": 0,
        "explanation": "Havoning taxminan 78% hajmini azot (N₂), 21% ini kislorod (O₂) tashkil qiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "8-sinf",
        "chapter_title": "Kislotalar klassifikatsiyasi",
        "question_text": "Bir negizli kislorodsiz kislotani aniqlang.",
        "options": ["HCl", "H₂SO₄", "HNO₃", "H₃PO₄"],
        "correct_index": 0,
        "explanation": "HCl (xlorid kislota) bitta vodorod atomiga ega (bir negizli) va tarkibida kislorod yo'q.",
        "difficulty": "oson"
    },
    {
        "subject_id": 3,
        "grade": "11-sinf",
        "chapter_title": "Disaxaridlar",
        "question_text": "Oddiy shakar (saxaroza) gidrolizlanganda qanday monosaxaridlar hosil bo'ladi?",
        "options": ["Glyukoza va fruktoza", "Faqat glyukoza", "Faqat galaktoza", "Glyukoza va riboza"],
        "correct_index": 0,
        "explanation": "C₁₂H₂₂O₁₁ + H₂O → C₆H₁₂O₆ (glyukoza) + C₆H₁₂O₆ (fruktoza).",
        "difficulty": "orta"
    },
    {
        "subject_id": 3,
        "grade": "9-sinf",
        "chapter_title": "Alyuminiy va uning xossalari",
        "question_text": "Alyuminiy gidroksidi (Al(OH)₃) kislotalar bilan ham, ishqorlar bilan ham reaksiyaga kirishadi. Bu uning qanday xossasini bildiradi?",
        "options": ["Amfoterlik xossasini", "Kislotalik xossasini", "Asoslik xossasini", "Neytrallik xossasini"],
        "correct_index": 0,
        "explanation": "Ham kislotalar, ham asoslar bilan ta'sirlasha oladigan birikmalar amfoter birikmalar deyiladi.",
        "difficulty": "oson"
    }
]

# ==========================================
# 4. BIOLOGIYA (Subject ID: 4) - 50 TA SAVOL
# ==========================================
BIOLOGIYA_QUESTIONS = [
    # 6-sinf (Botanika)
    {
        "subject_id": 4,
        "grade": "6-sinf",
        "chapter_title": "O'simlik hujayrasi",
        "question_text": "O'simlik hujayrasiga yashil rang beruvchi va fotosintez jarayonini amalga oshiruvchi plastidalar qaysi?",
        "options": ["Xloroplastlar", "Xromoplastlar", "Leykoplastlar", "Mitoxondriyalar"],
        "correct_index": 0,
        "explanation": "Xloroplastlar tarkibidagi xlorofill pigmenti hisobiga yashil rangda bo'lib, fotosintez jarayonini bajaradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "6-sinf",
        "chapter_title": "Ildiz sistemasi",
        "question_text": "Asosiy ildiz yaxshi rivojlangan ildiz sistemasi qanday ataladi?",
        "options": ["O'q ildiz sistemasi", "Popuk ildiz sistemasi", "Qo'shimcha ildiz", "Yon ildiz"],
        "correct_index": 0,
        "explanation": "Asosiy ildiz yaqqol ko'rinib turadigan ildiz sistemasi o'q ildiz sistemasi deyiladi (ikki urug'pallalilarda).",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "6-sinf",
        "chapter_title": "Fotosintez",
        "question_text": "Fotosintez jarayoni uchun zarur bo'lgan asosiy omillarni ko'rsating.",
        "options": ["Yorug'lik, xlorofill, karbonat angidrid va suv", "Faqat kislorod va issiqlik", "Azot, tuproq va qorong'ulik", "Kislorod, glyukoza va mineral tuzlar"],
        "correct_index": 0,
        "explanation": "6CO₂ + 6H₂O + yorug'lik → C₆H₁₂O₆ + 6O₂ (xlorofill ishtirokida).",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "6-sinf",
        "chapter_title": "Gulning tuzilishi",
        "question_text": "Gulning asosiy ko'payish a'zolari qaysilar?",
        "options": ["Changchi va urug'chi", "Gultojibarg va kosachabarg", "Gulband va gulo'rindi", "Tuguncha va ustuncha"],
        "correct_index": 0,
        "explanation": "Gulning asosiy jinsiy ko'payish a'zolari changchi (erkaklik) va urug'chi (urg'ochilik) hisoblanadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "6-sinf",
        "chapter_title": "Yopiq urug'lilar",
        "question_text": "Quyidagi o'simliklardan qaysi biri bir urug'pallalilar sinfiga kiradi?",
        "options": ["Bug'doy", "Loviya", "Olma", "Paxta"],
        "correct_index": 0,
        "explanation": "Bug'doy, makkajo'xori, sholi kabi boshoqlilar bir urug'pallali o'simliklardir.",
        "difficulty": "oson"
    },
    # 7-sinf (Zoologiya)
    {
        "subject_id": 4,
        "grade": "7-sinf",
        "chapter_title": "Bir hujayrali hayvonlar",
        "question_text": "Soxta oyoqlari (psevdopodiylar) yordamida harakatlanadigan bir hujayrali hayvon qaysi?",
        "options": ["Oddiy amyoba", "Yashil evglena", "Tufelka infuzoriyasi", "Volvoks"],
        "correct_index": 0,
        "explanation": "Oddiy amyoba sitoplazma o'simtalari - soxta oyoqlar chiqarib harakatlanadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "7-sinf",
        "chapter_title": "Bo'g'imoyoqlilar",
        "question_text": "Hasharotlarning tanasi qanday qismlardan iborat va ularda necha juft yurish oyoqlari bor?",
        "options": ["Bosh, ko'krak, qorin; 3 juft oyoq", "Boshko'krak va qorin; 4 juft oyoq", "Faqat tana; 5 juft oyoq", "Bosh va tana; 2 juft oyoq"],
        "correct_index": 0,
        "explanation": "Hasharotlar tanasi bosh, ko'krak va qorindan iborat bo'lib, ko'kragida 3 juft (jami 6 ta) yurish oyoqlari bo'ladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "7-sinf",
        "chapter_title": "Baliqlar",
        "question_text": "Suyakli baliqlarning qon aylanish sistemasi qanday tuzilgan?",
        "options": ["Bitta qon aylanish doirasi, 2 kamerali yurak (1 bo'lmacha, 1 qorincha)", "Ikkita qon aylanish doirasi, 3 kamerali yurak", "Ochiq qon aylanish sistemasi", "2 ta bo'lmacha va 2 ta qorincha"],
        "correct_index": 0,
        "explanation": "Baliqlarda bitta qon aylanish doirasi va yuragi 2 kamerali (yurakda faqat venoz qon oqadi).",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "7-sinf",
        "chapter_title": "Suvda va quruqlikda yashovchilar",
        "question_text": "Voyaga yetgan baqaning yuragi necha kamerali?",
        "options": ["3 kamerali (2 bo'lmacha, 1 qorincha)", "2 kamerali", "4 kamerali", "1 kamerali"],
        "correct_index": 0,
        "explanation": "Amfibiyalarda (baqalarda) yurak 3 kamerali bo'lib, 2 bo'lmacha va 1 qorinchadan iborat.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "7-sinf",
        "chapter_title": "Sutemizuvchilar",
        "question_text": "Qushlar va sutemizuvchilarning boshqa umurtqalilardan asosiy ustunligi nimada?",
        "options": ["Issiqqonli (tana temperaturasi doimiy) ekanligida", "Tuxum qo'yishida", "Suvda suzishida", "Terisi tangachalar bilan qoplanganligida"],
        "correct_index": 0,
        "explanation": "Qushlar va sutemizuvchilar 4 kamerali yurakka ega va issiqqonli (gomoyoterm) hayvonlardir.",
        "difficulty": "orta"
    },
    # 8-sinf (Odam va uning salomatligi)
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Qon va uning tarkibi",
        "question_text": "Qondagi kislorodni to'qimalarga tasiydigan va gemoglobin tutuvchi hujayralar qaysi?",
        "options": ["Eritrotsitlar", "Leykotsitlar", "Trombotsitlar", "Plazma oqsillari"],
        "correct_index": 0,
        "explanation": "Eritrotsitlar (qizil qon tanachalari) gemoglobin yordamida kislorod va qisman karbonat angidridni tashiydi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Immunitet",
        "question_text": "Organizmga kirgan yot jismlar va bakteriyalarni qamrab olib hazm qilish (fagotsitoz) hodisasini kashf etgan olim kim?",
        "options": ["I.I.Mechnikov", "L.Paster", "R.Kox", "I.P.Pavlov"],
        "correct_index": 0,
        "explanation": "Ilya Ilyich Mechnikov leykotsitlarning fagotsitoz xossasini ochib bergan va immunitetning fagotsitar nazariyasini yaratgan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Qon aylanish sistemasi",
        "question_text": "Odamda katta qon aylanish doirasi yurakning qaysi bo'limidan boshlanadi?",
        "options": ["Chap qorinchadan", "O'ng qorinchadan", "Chap bo'lmachadan", "O'ng bo'lmachadan"],
        "correct_index": 0,
        "explanation": "Katta qon aylanish doirasi chap qorinchadan (aorta orqali) boshlanib, o'ng bo'lmachaga quyiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Nafas olish sistemasi",
        "question_text": "O'pkada gazlar almashinuvi sodir bo'ladigan mayda pufakchalar nima deb ataladi?",
        "options": ["Alveolalar", "Bronxiolalar", "Plevra", "Traxeyalar"],
        "correct_index": 0,
        "explanation": "O'pka alveolalari kapillyarlar bilan zich o'ralgan bo'lib, ularda O₂ va CO₂ gaz almashinuvi kechadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Ovqat hazm qilish",
        "question_text": "Inson organizmidagi eng yirik ichki bez bo'lib, o't suyuqligi (safro) ishlab chiqaruvchi a'zo qaysi?",
        "options": ["Jigar", "Oshqozon osti bezi", "Qalqonsimon bez", "Buyrak"],
        "correct_index": 0,
        "explanation": "Jigar insonning eng yirik bezi bo'lib, yog'larni emulsiyalaydigan safro ishlab chiqaradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Endokrin sistema",
        "question_text": "Qondagi qand miqdorini (glyukozani) kamaytiruvchi insulin gormoni qaysi bezdan ajraladi?",
        "options": ["Oshqozon osti bezi", "Buyrak usti bezi", "Gipofiz bezi", "Qalqonsimon bez"],
        "correct_index": 0,
        "explanation": "Oshqozon osti bezining Langergans orolchalari beta-hujayralari insulin gormonini ishlab chiqaradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Ayirish sistemasi",
        "question_text": "Buyrakning strukturaviy va funksional birligi nima deb ataladi?",
        "options": ["Nefron", "Neyron", "Osteon", "Miofibrilla"],
        "correct_index": 0,
        "explanation": "Har bir buyrak taxminan 1 millionta nefrondan iborat bo'lib, siydik hosil bo'lishi nefronlarda kechadi.",
        "difficulty": "oson"
    },
    # 9-sinf (Sitologiya va Umumiy biologiya)
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "Sitologiya",
        "question_text": "Hujayraning 'energiya stansiyasi' deb ataluvchi va ATF sintezlaydigan organoid qaysi?",
        "options": ["Mitoxondriya", "Ribosoma", "Golji majmuasi", "Lizosoma"],
        "correct_index": 0,
        "explanation": "Mitoxondriyalarda hujayraviy nafas olish va biologik oksidlanish kechadi, ATF energiyasi ishlab chiqariladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "Sitologiya",
        "question_text": "Hujayrada oqsil sintezini amalga oshiruvchi membranasiz organoid qaysi?",
        "options": ["Ribosoma", "Sentriola", "Lizosoma", "Peroksisoma"],
        "correct_index": 0,
        "explanation": "Ribosomalar rRNK va oqsillardan tuzilgan bo'lib, oqsil biosintezini amalga oshiradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "Nuklein kislotalar",
        "question_text": "DNK qo'sh spirali tuzilish modelini 1953-yilda kimlar kashf etgan?",
        "options": ["J.Uotson va F.Krik", "G.Mendel va T.Morgan", "Ch.Darvin va A.Uolles", "R.Guk va A.Levenguk"],
        "correct_index": 0,
        "explanation": "Jeyms Uotson va Frensis Krik 1953-yilda DNKning qo'sh spiral modelini yaratdilar.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "Hujayra bo'linishi",
        "question_text": "Tana (somatik) hujayralarining xromosoma to'plamini saqlab bo'linish usuli nima deyiladi?",
        "options": ["Mitoz", "Meyoz", "Amitoz", "Schizogoniya"],
        "correct_index": 0,
        "explanation": "Mitoz natijasida bitta ona hujayradan xromosoma to'plami teng saqlangan (2n) ikkita qiz hujayra hosil bo'ladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "Hujayra bo'linishi",
        "question_text": "Meyoz bo'linishi natijasida nechta va qanday xromosoma to'plamiga ega hujayralar hosil bo'ladi?",
        "options": ["4 ta gaploid (n) hujayra", "2 ta diploid (2n) hujayra", "2 ta gaploid (n) hujayra", "4 ta diploid (2n) hujayra"],
        "correct_index": 0,
        "explanation": "Meyoz bo'linish jinsiy hujayralarni (gametalarni) hosil qiladi: 1 ta diploid hujayradan 4 ta gaploid (n) hujayra hosil bo'ladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "Genetika asoslari",
        "question_text": "Gregor Mendelning birinchi qonuni qanday nomlanadi?",
        "options": ["Birinchi bo'g'in duragaylarining bir xillik qonuni", "Belgilarning ajralish qonuni", "Belgilarning erkin birikish qonuni", "Birikkan holda irsiylanish qonuni"],
        "correct_index": 0,
        "explanation": "Mendelning 1-qonuni: toza navlar chatishtirilganda F1 bo'g'inda barcha duragaylar fenotipik va genotipik jihatdan bir xil bo'ladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "Genetika asoslari",
        "question_text": "Geterozigota no'xat o'simliklari (Aa x Aa) o'zaro chatishtirilganda F2 bo'g'inda fenotip bo'yicha ajralish nisbati qanday bo'ladi?",
        "options": ["3 : 1", "1 : 2 : 1", "9 : 3 : 3 : 1", "1 : 1"],
        "correct_index": 0,
        "explanation": "To'liq dominantlikda fenotip bo'yicha 3 ta sariq va 1 ta yashil (3:1) nisbatda ajraladi.",
        "difficulty": "orta"
    },
    # 10-sinf
    {
        "subject_id": 4,
        "grade": "10-sinf",
        "chapter_title": "Irsiyatning xromosoma nazariyasi",
        "question_text": "Irsiyatning xromosoma nazariyasini kim va qaysi obyektda ishlab chiqqan?",
        "options": ["Tomas Morgan, drozofila pashshasida", "Gregor Mendel, no'xatda", "Gugo de Friz, oenoterada", "N.I.Vavilov, bug'doyda"],
        "correct_index": 0,
        "explanation": "Tomas Xant Morgan va uning maktabi meva pashshasi (drozofila) ustida irsiyatning xromosoma nazariyasini yaratgan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "10-sinf",
        "chapter_title": "O'zgaruvchanlik",
        "question_text": "Genotip o'zgarmasdan tashqi muhit omillari ta'sirida fenotipning o'zgarishi nima deb ataladi?",
        "options": ["Modifikatsion o'zgaruvchanlik", "Mutatsion o'zgaruvchanlik", "Kombinativ o'zgaruvchanlik", "Sitoplazmatik o'zgaruvchanlik"],
        "correct_index": 0,
        "explanation": "Modifikatsion (fenotipik) o'zgaruvchanlik irsiylanmaydi va muhit sharoitlariga moslashish xarakteriga ega.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "10-sinf",
        "chapter_title": "Seleksiya asoslari",
        "question_text": "Madaniy o'simliklarning kelib chiqish markazlarini aniqlagan mashhur olim kim?",
        "options": ["N.I.Vavilov", "I.V.Michurin", "G.D.Karpechenko", "M.F.Ivanov"],
        "correct_index": 0,
        "explanation": "Nikolay Ivanovich Vavilov madaniy o'simliklarning kelib chiqishi va xilma-xilligining asosiy 7 ta birlamchi markazini aniqlagan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "10-sinf",
        "chapter_title": "Biotexnologiya",
        "question_text": "Boshqa tur organizm genini qabul qilgan organizmlar nima deb ataladi?",
        "options": ["Transgen organizmlar", "Klonlar", "Gibridlar", "Mutantlar"],
        "correct_index": 0,
        "explanation": "Gen muhandisligi orqali begona gen kiritilgan organizmlar transgen organizmlar (GMO) deyiladi.",
        "difficulty": "oson"
    },
    # 11-sinf
    {
        "subject_id": 4,
        "grade": "11-sinf",
        "chapter_title": "Evolyutsiya ta'limoti",
        "question_text": "Evolyutsiyaning harakatlantiruvchi kuchlarini ko'rsating (Charlz Darvin ta'limotiga binoan).",
        "options": ["Irsiyat, o'zgaruvchanlik va tabiiy tanlanish", "Faqat sun'iy tanlanish", "Faqat mutatsiyalar", "Tashqi muhitga intilish"],
        "correct_index": 0,
        "explanation": "Darvin evolyutsiyaning 3 ta asosiy omilini ko'rsatgan: irsiyat, o'zgaruvchanlik va yashash uchun kurash asosidagi tabiiy tanlanish.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "11-sinf",
        "chapter_title": "Evolyutsiya dalillari",
        "question_text": "Kelib chiqishi bir xil bo'lib, bajaradigan funksiyasi har xil bo'lgan a'zolar nima deyiladi?",
        "options": ["Gomologik a'zolar", "Analogik a'zolar", "Rudimentlar", "Atavizmlar"],
        "correct_index": 0,
        "explanation": "Gomologik a'zolar (masalan, qush qanoti, kit suzgichi va odam qo'li) kelib chiqishi bitta murtak varag'idan rivojlanadi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "11-sinf",
        "chapter_title": "Evolyutsiya dalillari",
        "question_text": "Evolyutsiya jarayonida o'zining dastlabki ahamiyatini yo'qotgan va qoldiq holida saqlanib qolgan a'zolar nima deyiladi?",
        "options": ["Rudimentlar", "Atavizmlar", "Gomologlar", "Analoglar"],
        "correct_index": 0,
        "explanation": "Rudimentlar - avlodlarda qoldiq sifatida uchraydigan a'zolar (masalan, odamda ko'richak o'simtasi - appendiks).",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "11-sinf",
        "chapter_title": "Makroevolyutsiya yo'nalishlari",
        "question_text": "Organizm tuzilishining umumiy yuksalishiga va hayotiy faoliyat darajasining oshishiga olib keluvchi evolyutsion o'zgarish nima deyiladi?",
        "options": ["Aromorfoz", "Idioadaptatsiya", "Umumiy degeneratsiya", "Konvergensiya"],
        "correct_index": 0,
        "explanation": "A.N.Severtsov ta'limotiga ko'ra aromorfoz - morfofiziologik progress (masalan, 4 kamerali yurakning paydo bo'lishi).",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "11-sinf",
        "chapter_title": "Ekologiya asoslari",
        "question_text": "Ekotizimda organik moddalarni noorganik moddalardan sintezlovchi avtotrof organizmlar qanday ataladi?",
        "options": ["Produsentlar", "Konsumentlar", "Redusentlar", "Parazitlar"],
        "correct_index": 0,
        "explanation": "Produsentlar (yashil o'simliklar) quyosh energiyasidan foydalanib birlamchi organik moddalarni yaratuvchilardir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "11-sinf",
        "chapter_title": "Ekologiya asoslari",
        "question_text": "O'lik organik qoldiqlarni parchalab yana mineral moddalarga aylantiruvchi organizmlar (bakteriya va zamburug'lar) nima deyiladi?",
        "options": ["Redusentlar", "Produsentlar", "Konsumentlar", "Yirtqichlar"],
        "correct_index": 0,
        "explanation": "Redusentlar organik qoldiqlarni noorganik minerallarga qadar parchalaydi va moddalar aylanishini yopadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "11-sinf",
        "chapter_title": "Biosfera haqida ta'limot",
        "question_text": "Biosfera va uning chegaralari haqidagi mukammal ta'limotni kim yaratgan?",
        "options": ["V.I.Vernadskiy", "E.Zyuss", "E.Gekkel", "K.Linney"],
        "correct_index": 0,
        "explanation": "Vladimir Ivanovich Vernadskiy biosferaning yaxlit ta'limotini va tirik moddaning sayyoraviy rolini yaratdi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "6-sinf",
        "chapter_title": "Bargning anatomik tuzilishi",
        "question_text": "Barg epidermasida gaz almashinuvi va suv bug'latishni (transpiratsiya) boshqaruvchi tuzilma nima?",
        "options": ["Og'izchalar", "Xlorenxima", "Tolalar", "Naylar"],
        "correct_index": 0,
        "explanation": "Og'izcha (ustitsa) hujayralari ochilib-yopilib transpiratsiya va gaz almashinuvini ta'minlaydi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "7-sinf",
        "chapter_title": "Molyuskalar",
        "question_text": "Chig'anoqli molyuskalarning tanasini qoplab turuvchi maxsus teri burmasi nima deb ataladi?",
        "options": ["Mantiya", "Kutikula", "Xitin", "Epidermis"],
        "correct_index": 0,
        "explanation": "Mantiya molyuskalarning ichki a'zolarini o'rab turadi va uning tashqi qavati chig'anoq hosil qiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Nerv sistemasi",
        "question_text": "Nerv to'qimasining asosiy hujayrasi nima deb ataladi?",
        "options": ["Neyron", "Neyrogliya", "Mioblast", "Sinaps"],
        "correct_index": 0,
        "explanation": "Nerv sistemasi neyronlardan (tana, dendrit va aksondan iborat) tuzilgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Nerv sistemasi",
        "question_text": "Odam miyasining harakatlarni muvofiqlashtirish va muvozanatni saqlashga javobgar qismi qaysi?",
        "options": ["Miyacha", "Uzunchoq miya", "O'rta miya", "Gipotalamus"],
        "correct_index": 0,
        "explanation": "Miyacha (cerebellum) tana muvozanatini va nozik harakatlar aniqligini boshqaradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "Biopolimerlar",
        "question_text": "Oqsillarning monomeri nima?",
        "options": ["Aminokislotalar", "Monosaxaridlar", "Nukleotidlar", "Yog' kislotalari"],
        "correct_index": 0,
        "explanation": "Oqsillar 20 xil aminokislotalarning peptid bog'i orqali birikishidan hosil bo'lgan biopolimerlardir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "Biopolimerlar",
        "question_text": "Nuklein kislotalarning (DNK va RNK) monomeri nima?",
        "options": ["Nukleotidlar", "Aminokislotalar", "Glyukoza", "Glitserin"],
        "correct_index": 0,
        "explanation": "DNK va RNK nukleotidlardan tashkil topgan bo'lib, har bir nukleotid azot asosi, uglevod va fosfat kislota qoldig'idan iborat.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "10-sinf",
        "chapter_title": "Genetik kod",
        "question_text": "Bitta aminokislotani kodlash uchun mRNK dagi nechta nukleotid (triplet) javobgar?",
        "options": ["3 ta nukleotid", "1 ta nukleotid", "2 ta nukleotid", "4 ta nukleotid"],
        "correct_index": 0,
        "explanation": "Genetik kod tripletli bo'lib, 3 ta ketma-ket kelgan nukleotid (kodon) bitta aminokislotani kodlaydi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "10-sinf",
        "chapter_title": "Xromosoma mutatsiyalari",
        "question_text": "Xromosoma qismining 180 gradusga burilib qolishi qanday nomlanadi?",
        "options": ["Inversiya", "Delesiya", "Duplikatsiya", "Translokatsiya"],
        "correct_index": 0,
        "explanation": "Xromosoma segmentining uzilib, 180° ga teskari ulanib qolishi inversiya deb ataladi.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 4,
        "grade": "11-sinf",
        "chapter_title": "Antropogenez",
        "question_text": "Odamning paydo bo'lishida (antropogenezda) yetakchi ijtimoiy omil nima bo'lgan?",
        "options": ["Mehnat va nutq", "Faqat tabiiy tanlanish", "Iqlim o'zgarishi", "Oziq-ovqat yetishmovchiligi"],
        "correct_index": 0,
        "explanation": "F.Engels ta'limotiga ko'ra, maymundan odam shakllanishida mehnat, jamoa bo'lib yashash va nutq hal qiluvchi rol o'ynagan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "6-sinf",
        "chapter_title": "Zamburug'lar dunyosi",
        "question_text": "Qaysi xususiyat zamburug'larni hayvonlarga yaqinlashtiradi?",
        "options": ["Geterotrof oziqlanishi, xitin qobig'i va glikogen to'plashi", "Fotosintez qilishi", "Harakatchanligi", "Hujayra qobig'ining sellyulozadan iboratligi"],
        "correct_index": 0,
        "explanation": "Zamburug'lar tayyor organik modda bilan oziqlanadi (geterotrof), zaxira moddasi glikogen va xitin moddasiga ega.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "7-sinf",
        "chapter_title": "Sudralib yuruvchilar",
        "question_text": "Sudralib yuruvchilarning terisi qanday xususiyatga ega?",
        "options": ["Quruq, bezsiz va muguz tangachalar bilan qoplangan", "Nam va shilimshiq", "Patlar bilan qoplangan", "Tukli va ter bezlari ko'p"],
        "correct_index": 0,
        "explanation": "Sudralib yuruvchilar quruqlikda yashashga moslashgan bo'lib, tanasi quruq muguz tangachalar bilan qoplangan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "8-sinf",
        "chapter_title": "Vitaminlar",
        "question_text": "Organizmda D vitamini yetishmaganda bolalarda qanday kasallik rivojlanadi?",
        "options": ["Raxit", "Singa (tsinga)", "Beri-beri", "Tovuqko'rlik"],
        "correct_index": 0,
        "explanation": "D vitamini (kalsiferol) yetishmaganda kalsiy va fosfor almashinuvi buzilib, suyaklar yumshab qoladi (raxit).",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "9-sinf",
        "chapter_title": "O'simlik to'qimalari",
        "question_text": "O'simliklarda suv va unda erigan mineral moddalarni ildizdan barglarga qarab o'tkazuvchi to'qima nima?",
        "options": ["Ksilema (naylar)", "Floema (elaksimon naylar)", "Kambiy", "Periderma"],
        "correct_index": 0,
        "explanation": "Ksilema orqali yuqoriga o'suvchi oqim (suv va tuzlar), floema orqali pastga tushuvchi organik moddalar oqimi harakatlanadi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 4,
        "grade": "11-sinf",
        "chapter_title": "Ekologik omillar",
        "question_text": "Tirik organizmlarning bir-biriga ko'rsatadigan ta'siri qanday ekologik omil deb ataladi?",
        "options": ["Biotik omillar", "Abiotik omillar", "Antropogen omillar", "Iqlimiy omillar"],
        "correct_index": 0,
        "explanation": "Biotik omillar - tirik organizmlarning o'zaro ta'sir munosabatlari (simbioz, yirtqichlik, raqobat va h.k.).",
        "difficulty": "oson"
    },
    {
        "subject_id": 4,
        "grade": "10-sinf",
        "chapter_title": "Jinsiy ko'payish",
        "question_text": "Gulli o'simliklarda qo'sh urug'lanish hodisasini 1898-yilda kashf etgan olim kim?",
        "options": ["S.G.Navashin", "I.V.Michurin", "K.A.Timiryazev", "N.I.Vavilov"],
        "correct_index": 0,
        "explanation": "Sergey Gavrilovich Navashin yopiq urug'li o'simliklarda qo'sh urug'lanish jarayonini kashf etgan.",
        "difficulty": "orta"
    }
]
