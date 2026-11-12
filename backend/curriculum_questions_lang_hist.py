# -*- coding: utf-8 -*-
"""
EduBattle - 2020-2023 Yangi darsliklar asosidagi savollar banki:
Fan 5: Ona tili va Adabiyot (6-11-sinf yangi nashrlar) - 50 ta savol
Fan 6: Tarix (O'zbekiston tarixi va Jahon tarixi 7-11-sinf yangi nashrlar) - 50 ta savol
"""

# ==========================================
# 5. ONA TILI VA ADABIYOT (Subject ID: 5) - 50 TA SAVOL
# ==========================================
ONA_TILI_ADABIYOT_QUESTIONS = [
    # 6-sinf
    {
        "subject_id": 5,
        "grade": "6-sinf",
        "chapter_title": "Fonetika va imlo",
        "question_text": "O'zbek tilida nechta unli tovush va nechta unli harf mavjud?",
        "options": ["6 ta unli tovush, 6 ta harf", "9 ta tovush, 6 ta harf", "10 ta tovush, 8 ta harf", "6 ta tovush, 8 ta harf"],
        "correct_index": 0,
        "explanation": "Hozirgi o'zbek adabiy tilida 6 ta unli fonema mavjud: a, o, i, u, o', e. Ular 6 ta harf bilan ifodalanadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "6-sinf",
        "chapter_title": "Leksikologiya",
        "question_text": "Talaffuzi va yozilishi bir xil, ammo ma'nolari mutlaqo har xil bo'lgan so'zlar nima deyiladi?",
        "options": ["Omonimlar", "Sinonimlar", "Antonimlar", "Paronimlar"],
        "correct_index": 0,
        "explanation": "Shakli bir xil, ma'nosi har xil so'zlar omonimlar deyiladi (masalan, olma - meva va olma - buyruq fe'li).",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "6-sinf",
        "chapter_title": "Frazeologiya",
        "question_text": "'Yulduzni benarvon uradigan' iborasining ma'nosi nima?",
        "options": ["Juda uddaburon, chaqqon", "Baland bo'yli", "Kamsuqum, yuvosh", "Kekkaygan, manman"],
        "correct_index": 0,
        "explanation": "Bu frazeologizm o'ta epchil, har qanday vaziyatdan yo'l topa oladigan shaxsga nisbatan ishlatiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "6-sinf",
        "chapter_title": "Adabiyot - Xalq og'zaki ijodi",
        "question_text": "O'zbek xalq qahramonlik eposining gultoji bo'lgan doston qaysi?",
        "options": ["'Alpomish'", "'Go'ro'g'li'", "'Ravshan'", "'Kuntug'mish'"],
        "correct_index": 0,
        "explanation": "'Alpomish' dostoni xalqimizning jasorati, or-nomusi va birligini madh etuvchi ulkan qahramonlik dostonidir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "6-sinf",
        "chapter_title": "Morfologiya - Ot",
        "question_text": "Qaratqich kelishigining qo'shimchasi qaysi?",
        "options": ["-ning", "-ni", "-ga", "-da"],
        "correct_index": 0,
        "explanation": "Qaratqich kelishigi -ning qo'shimchasi orqali shakllanadi va kimning? nimaning? savollariga javob beradi.",
        "difficulty": "oson"
    },
    # 7-sinf
    {
        "subject_id": 5,
        "grade": "7-sinf",
        "chapter_title": "Morfologiya - Sifat",
        "question_text": "Sifatning qiyosiy daraja qo'shimchasini aniqlang.",
        "options": ["-roq", "-dek", "-day", "-cha"],
        "correct_index": 0,
        "explanation": "Qiyosiy daraja -roq qo'shimchasi yordamida yasaladi (masalan: kattaroq, yaxshiroq).",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "7-sinf",
        "chapter_title": "Morfologiya - Fe'l nisbatlari",
        "question_text": "'Xat yozildi' jumlasidagi fe'l qaysi nisbatda qo'llangan?",
        "options": ["Majhul nisbat", "Aniq nisbat", "O'zlik nisbati", "Birgalik nisbati"],
        "correct_index": 0,
        "explanation": "Harakatning bajaruvchisi noma'lum bo'lib, -il qo'shimchasi qo'shilgan, bu majhul nisbatdir.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "7-sinf",
        "chapter_title": "Mumtoz adabiyot",
        "question_text": "Alisher Navoiyning 'Xamsa'siga kiruvchi birinchi doston nomi nima?",
        "options": ["'Hayrat ul-abror'", "'Farhod va Shirin'", "'Layli va Majnun'", "'Saddi Iskandariy'"],
        "correct_index": 0,
        "explanation": "Navoiy 'Xamsa'sining birinchi dostoni falsafiy-ta'limiy 'Hayrat ul-abror' (Yaxshi kishilarning hayratlanishi) dostonidir (1483).",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "7-sinf",
        "chapter_title": "Morfologiya - Ravish",
        "question_text": "Quyidagi so'zlardan qaysi biri payt ravishi hisoblanadi?",
        "options": ["Kecha", "Tez", "Ko'p", "Ichkariga"],
        "correct_index": 0,
        "explanation": "'Kecha' so'zi ish-harakatning bajarilish vaqtini bildiradi va qachon? so'rog'iga javob bo'ladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "7-sinf",
        "chapter_title": "Mumtoz adabiyot",
        "question_text": "Boburning dunyo adabiyotida mashhur bo'lgan memorial-tarixiy asari qaysi?",
        "options": ["'Boburnoma'", "'Vaqoyi'", "'Mubayyin'", "'Aruz risolasi'"],
        "correct_index": 0,
        "explanation": "Zahiriddin Muhammad Boburning shoh asari 'Vaqoyi' bo'lib, xalq orasida 'Boburnoma' nomi bilan mashhur.",
        "difficulty": "oson"
    },
    # 8-sinf
    {
        "subject_id": 5,
        "grade": "8-sinf",
        "chapter_title": "Sintaksis - So'z birikmasi",
        "question_text": "Boshqaruv aloqasiga asoslangan so'z birikmasini aniqlang.",
        "options": ["Kitobni o'qimoq", "Chiroyli gul", "Tez yugurmoq", "Besh nafar o'quvchi"],
        "correct_index": 0,
        "explanation": "Tobe so'z bosh so'z talabi bilan kelishik yoki ko'makchi olganda boshqaruv aloqasi deyiladi ('kitobni o'qimoq').",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "8-sinf",
        "chapter_title": "Gap bo'laklari",
        "question_text": "Gapning qaysi ikkinchi darajali bo'lagi qanday? qanaqa? qaysi? so'roqlariga javob bo'ladi?",
        "options": ["Aniqlovchi", "To'ldiruvchi", "Hol", "Kesim"],
        "correct_index": 0,
        "explanation": "Narsa-buyumning belgisini bildirib, qanday? qanaqa? qaysi? so'rog'iga javob bo'luvchi bo'lak aniqlovchi deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "8-sinf",
        "chapter_title": "Uyushiq bo'laklar",
        "question_text": "Gapda bir xil so'roqqa javob bo'lib, bitta so'zga bog'lanadigan bo'laklar nima deyiladi?",
        "options": ["Uyushiq bo'laklar", "Ajratilgan bo'laklar", "Kiritma bo'laklar", "Undalmalar"],
        "correct_index": 0,
        "explanation": "Bir xil sintaktik vazifani bajaruvchi teng huquqli bo'laklar uyushiq bo'laklar deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "8-sinf",
        "chapter_title": "Jadid adabiyoti",
        "question_text": "Birinchi o'zbek dramasi bo'lgan 'Padarkush' muallifi kim?",
        "options": ["Mahmudxo'ja Behbudiy", "Abdulla Avloniy", "Fitrat", "Hamza"],
        "correct_index": 0,
        "explanation": "1911-yilda Mahmudxo'ja Behbudiy birinchi o'zbek pesasi - 'Padarkush yoxud o'qimagan bolaning holi'ni yaratgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "8-sinf",
        "chapter_title": "O'zbek romanchiligi",
        "question_text": "O'zbek adabiyotidagi ilk realistik roman qaysi va uning muallifi kim?",
        "options": ["'O'tkan kunlar', Abdulla Qodiriy", "'Kecha va kunduz', Cho'lpon", "'Qutlug' qon', Oybek", "'Sarob', Abdulla Qahhor"],
        "correct_index": 0,
        "explanation": "Ilk o'zbek romani Abdulla Qodiriy qalamiga mansub 'O'tkan kunlar' (1922-1926) romanidir.",
        "difficulty": "oson"
    },
    # 9-sinf
    {
        "subject_id": 5,
        "grade": "9-sinf",
        "chapter_title": "Qo'shma gap sintaksisi",
        "question_text": "Qismlari teng huquqli bo'lib, teng bog'lovchilar yordamida birikkan qo'shma gap qanday ataladi?",
        "options": ["Bog'langan qo'shma gap", "Ergashgan qo'shma gap", "Bog'lovchisiz qo'shma gap", "Murakkab qo'shma gap"],
        "correct_index": 0,
        "explanation": "Teng bog'lovchilar (va, ammo, lekin, biroq, yoki) vositasida bog'langan gaplar bog'langan qo'shma gap deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "9-sinf",
        "chapter_title": "Ergashgan qo'shma gap",
        "question_text": "'Kim ko'p o'qisa, u ko'p biladi' gapida qanday ergash gap qo'llangan?",
        "options": ["Ega ergash gap", "Kesim ergash gap", "Hol ergash gap", "To'ldiruvchi ergash gap"],
        "correct_index": 0,
        "explanation": "Ergash gap bosh gapdagi 'u' olmosh-egasini izohlab kelmoqda (Kim ko'p biladi? - Kim ko'p o'qisa), bu ega ergash gapdir.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "9-sinf",
        "chapter_title": "Ko'chirma va o'zlashtirma gap",
        "question_text": "O'zgalar nutqining shakli va mazmuni o'zgartirilmasdan aynan berilishi nima deyiladi?",
        "options": ["Ko'chirma gap", "O'zlashtirma gap", "Kirish so'z", "Undalma"],
        "correct_index": 0,
        "explanation": "Muallif tomonidan aynan o'zgarishsiz keltirilgan o'zga gap ko'chirma gap deyiladi va qo'shtirnoqqa olinadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "9-sinf",
        "chapter_title": "20-asr o'zbek adabiyoti",
        "question_text": "Cho'lponning mashhur romani qaysi?",
        "options": ["'Kecha va kunduz'", "'Mehrobdan chayon'", "'Abulfayzxon'", "'Navoiy'"],
        "correct_index": 0,
        "explanation": "Abdulhamid Sulaymon o'g'li Cho'lponning nodir romani 'Kecha va kunduz'dir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "9-sinf",
        "chapter_title": "O'zbek hikoyachiligi",
        "question_text": "'O'zbek adabiyotining Chexovi' deb atalgan, 'Anor', 'Bemor', 'Dahshat' hikoyalari muallifi kim?",
        "options": ["Abdulla Qahhor", "G'afur G'ulom", "Oybek", "Said Ahmad"],
        "correct_index": 0,
        "explanation": "Abdulla Qahhor ixcham va o'tkir syujetli psixologik hikoyalari bilan o'zbek nasri ustasi hisoblanadi.",
        "difficulty": "oson"
    },
    # 10-sinf
    {
        "subject_id": 5,
        "grade": "10-sinf",
        "chapter_title": "Nutq uslublari",
        "question_text": "Qonunlar, farmonlar, nizomlar va arizalar qaysi nutq uslubida yoziladi?",
        "options": ["Rasmiy-idoraviy uslub", "Ilmiy uslub", "Publitsistik uslub", "Badiiy uslub"],
        "correct_index": 0,
        "explanation": "Davlat hujjatlari, arizalar va shartnomalar rasmiy-idoraviy uslubda aniq qoliplar asosida tuziladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "10-sinf",
        "chapter_title": "She'r tuzilishi va aruz vazni",
        "question_text": "Mumtoz sharq she'riyatida (Navoiy, Bobur, Fuzuliy) qaysi vazn asosiy o'rin tutgan?",
        "options": ["Aruz vazni", "Barmoq vazni", "Erkin vazn", "Sillabik vazn"],
        "correct_index": 0,
        "explanation": "Mumtoz adabiyotimizda cho'ziq va qisqa bo'g'inlarning navbatlashuviga asoslangan aruz vazni qo'llangan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "10-sinf",
        "chapter_title": "Zamonaviy o'zbek adabiyoti",
        "question_text": "O'zbekiston Qahramoni, O'zbekiston Respublikasi Davlat madhiyasi matni muallifi kim?",
        "options": ["Abdulla Oripov", "Erkin Vohidov", "Muhammad Yusuf", "Rauf Parfi"],
        "correct_index": 0,
        "explanation": "O'zbekiston Respublikasining Davlat madhiyasi she'ri ulug' shoir Abdulla Oripov tomonidan yozilgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "10-sinf",
        "chapter_title": "Zamonaviy o'zbek adabiyoti",
        "question_text": "'O'zbegim' qasidasi va 'Ruhlar isyoni' dostoni muallifi bo'lgan shoir kim?",
        "options": ["Erkin Vohidov", "Abdulla Oripov", "Usmon Azim", "Shavkat Rahmon"],
        "correct_index": 0,
        "explanation": "O'zbekiston Qahramoni Erkin Vohidov 'O'zbegim' qasidasi hamda Nazrul Islomga bag'ishlangan 'Ruhlar isyoni' dostonining muallifidir.",
        "difficulty": "oson"
    },
    # 11-sinf
    {
        "subject_id": 5,
        "grade": "11-sinf",
        "chapter_title": "Matn tilshunosligi",
        "question_text": "Matnning asosiy belgilari qaysilar?",
        "options": ["Mazmuniy birlik, bog'liqlik va tugallanganlik", "Faqat bir xil so'zlardan iboratlik", "Kamida 50 ta gapdan tuzilganlik", "Faqat she'riy shaklda bo'lishlik"],
        "correct_index": 0,
        "explanation": "Matn fikriy butunlik, mavzuviy birlik va qismlararo izchil mantiqiy bog'liqlikka ega bo'lgan nutqiy tuzilmadir.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "11-sinf",
        "chapter_title": "Tinish belgilari sintaksisi",
        "question_text": "Quyidagi holatlarning qaysi birida tire (-) belgisi qo'yiladi?",
        "options": ["Ega va kesim ot yoki son bilan ifodalanib, bog'lamasiz kelganda", "Barcha qo'shma gaplarda", "Undalma gap boshida kelganda", "Kirish so'z o'rtada kelganda"],
        "correct_index": 0,
        "explanation": "Ega va kesim bosh kelishikdagi ot, olmosh yoki son bilan ifodalanganda ular orasiga tire qo'yiladi (masalan: O'zbekiston - buyuk davlat).",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "11-sinf",
        "chapter_title": "Nasriy dostonlar",
        "question_text": "'Yulduzlar mangu yonadi', 'Ot kishnagan oqshom', 'Odam ato va Momo havo' asarlari muallifi kim?",
        "options": ["Tog'ay Murod", "O'tkir Hoshimov", "Shukur Xolmirzayev", "Murod Muhammad Do'st"],
        "correct_index": 0,
        "explanation": "O'zbek xalqining milliy ruhiyati va fe'l-atvorini betakror tasvirlagan adib Tog'ay Muroddir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "11-sinf",
        "chapter_title": "Zamonaviy roman",
        "question_text": "'Dunyoning ishlari' qissasi va 'Ikki eshik orasi' romani muallifi bo'lgan xalq yozuvchisi kim?",
        "options": ["O'tkir Hoshimov", "Said Ahmad", "Tohir Malik", "Xudoyberdi To'xtaboyev"],
        "correct_index": 0,
        "explanation": "O'tkir Hoshimov onalar madhi bo'lgan 'Dunyoning ishlari' va urush yillari fojiasini aks ettirgan 'Ikki eshik orasi' asarlarining muallifidir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "6-sinf",
        "chapter_title": "Imlo qoidalari",
        "question_text": "Tutuq belgisi (') so'zlarda qanday vazifalarni bajaradi?",
        "options": ["Unlini cho'ziqroq talaffuz ettirish va unli bilan undoshni ajratib aytish", "Faqat urg'u bildirish", "Gapni tugallash", "Faqat so'z yasash"],
        "correct_index": 0,
        "explanation": "Tutuq belgisi unlidan keyin kelganda unlini cho'zadi (ma'no), undoshdan keyin kelsa tovushlarni ajratadi (in'om).",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "7-sinf",
        "chapter_title": "Olmosh",
        "question_text": "'Hech kim', 'hech qachon', 'hech qanday' so'zlari olmoshning qaysi ma'no turiga kiradi?",
        "options": ["Bo'lishsizlik olmoshlari", "Ko'rsatish olmoshlari", "Belgilash olmoshlari", "Gumon olmoshlari"],
        "correct_index": 0,
        "explanation": "'Hech' so'zi yordamida yasalgan olmoshlar bo'lishsizlik olmoshlari deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "8-sinf",
        "chapter_title": "Kirish so'zlar",
        "question_text": "'Shubhasiz', 'albatta', 'ehtimol' so'zlari gapda qanday bo'lak bo'ladi?",
        "options": ["Kiritma bo'lak (kirish so'z)", "Hol", "Ega", "To'ldiruvchi"],
        "correct_index": 0,
        "explanation": "So'zlovchining bayon etilayotgan fikrga munosabatini bildiruvchi so'zlar kirish so'zlar bo'lib, vergul bilan ajratiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "9-sinf",
        "chapter_title": "Dramaturgiya",
        "question_text": "O'zbek adabiyotida 'Sohibqiron', 'Jaloliddin Manguberdi' tarixiy dramalarining muallifi kim?",
        "options": ["Abdulla Oripov va Maqsud Shayxzoda", "Cho'lpon", "Hamza", "Abdulla Qodiriy"],
        "correct_index": 0,
        "explanation": "Maqsud Shayxzoda 'Jaloliddin Manguberdi', Abdulla Oripov esa 'Sohibqiron' dramasini yaratgan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "10-sinf",
        "chapter_title": "Paronimlar",
        "question_text": "'Aql' va 'asl' so'zlari kabi talaffuzi yaqin, ammo ma'nosi butunlay boshqa so'zlar nima deyiladi?",
        "options": ["Paronimlar", "Omonimlar", "Sinonimlar", "Antonimlar"],
        "correct_index": 0,
        "explanation": "Talaffuzi yoki yozilishi yaqin, biroq ma'nosi farqli so'zlar paronimlar deyiladi (masalan: asr - fasl, yadro - yalla).",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "11-sinf",
        "chapter_title": "Badiiy san'atlar",
        "question_text": "Mumtoz she'riyatda qarama-qarshi tushunchalarni yonma-yon qo'llash san'ati nima deyiladi?",
        "options": ["Tazod san'ati", "Tashbeh san'ati", "Talmeh san'ati", "Iyhom san'ati"],
        "correct_index": 0,
        "explanation": "Qarama-qarshi ma'noli so'zlarni (oq va qora, kecha va kunduz) qo'llash tazod (antiteza) san'ati deyiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "6-sinf",
        "chapter_title": "Son so'z turkumi",
        "question_text": "'Beshovlon', 'oltovlon' so'zlari sonning qaysi ma'no turiga kiradi?",
        "options": ["Jamlovchi son", "Dona son", "Chama son", "Taqsim son"],
        "correct_index": 0,
        "explanation": "-ov, -ovlon, -ala qo'shimchalari jamlovchi sonlarni yasaydi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "7-sinf",
        "chapter_title": "Ko'makchi so'zlar",
        "question_text": "Quyidagi so'zlardan qaysi biri sof ko'makchi hisoblanadi?",
        "options": ["Uchun", "Tez", "Ham", "Goh"],
        "correct_index": 0,
        "explanation": "'Uchun', 'kabi', 'singari', 'sayin' kabi so'zlar sof ko'makchilar guruhiga kiradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "8-sinf",
        "chapter_title": "Undalma",
        "question_text": "'Vatan, seni jonimdek sevarman!' gapida undalma qaysi so'z?",
        "options": ["Vatan", "Seni", "Jonimdek", "Sevarman"],
        "correct_index": 0,
        "explanation": "Nutq qaratilgan shaxs yoki narsani bildiruvchi so'z undalma deyiladi ('Vatan').",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "10-sinf",
        "chapter_title": "Adabiyot nazariyasi",
        "question_text": "Lirika, epos va drama nimaning turlari hisoblanadi?",
        "options": ["Adabiy turlar", "She'r vaznlari", "Uslublar", "Badiiy tasvir vositalari"],
        "correct_index": 0,
        "explanation": "Badiiy adabiyot uch asosiy adabiy turga bo'linadi: epik tur (epos), lirik tur (lirika) va dramatik tur (drama).",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "9-sinf",
        "chapter_title": "Yuklamalar",
        "question_text": "So'z yoki gapga so'roq, ta'kid, ayiruv-chegaralov kabi qo'shimcha ma'no yuklaydigan yordamchi so'zlar nima deyiladi?",
        "options": ["Yuklama", "Bog'lovchi", "Ko'makchi", "Modal so'z"],
        "correct_index": 0,
        "explanation": "Yuklamalar (-mi, -chi, -gina, hatto, axir va b.) ma'no nozikliklarini kiritadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "11-sinf",
        "chapter_title": "Mumtoz adabiyot",
        "question_text": "Nodirabegim (Komila) va Uvaysiy qaysi adabiy muhitning yetakchi shoiralari bo'lgan?",
        "options": ["Qo'qon adabiy muhiti", "Xiva adabiy muhiti", "Buxoro adabiy muhiti", "Samarqand adabiy muhiti"],
        "correct_index": 0,
        "explanation": "Nodira, Uvaysiy va Zebuniso kabi shoiralar XIX asr Qo'qon adabiy muhitida faoliyat yuritgan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "8-sinf",
        "chapter_title": "Sifatdosh",
        "question_text": "'Kelgan mehmon', 'o'qiyotgan bola' birikmalaridagi sifatdosh qo'shimchalarini aniqlang.",
        "options": ["-gan, -yotgan", "-ar, -mas", "-moqda", "-gach"],
        "correct_index": 0,
        "explanation": "-gan, -digan, -yotgan qo'shimchalari fe'ldan sifatdosh shaklini yasaydi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "7-sinf",
        "chapter_title": "O'zbek ertaklari",
        "question_text": "'Uch og'a-ini botirlar' ertagi xalq ertaklarining qaysi turiga kiradi?",
        "options": ["Sehrli-fantastik ertaklar", "Hayvonlar haqidagi ertaklar", "Maishiy ertaklar", "Tarixiy ertaklar"],
        "correct_index": 0,
        "explanation": "G'ayritabiiy kuchlar, devlar va sehrli voqealar tasvirlangan ertaklar sehrli-fantastik ertaklar deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "10-sinf",
        "chapter_title": "Fe'l mayllari",
        "question_text": "'Kitobni o'qisang, bilib olasan' gapidagi 'o'qisang' fe'li qaysi maylda kelgan?",
        "options": ["Shart mayli", "Buyruq-istak mayli", "Xabar mayli", "Maqsad mayli"],
        "correct_index": 0,
        "explanation": "-sa qo'shimchasi harakatning bajarilish shartini bildirib, shart maylini ifodalaydi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "9-sinf",
        "chapter_title": "Mustaqillik davri adabiyoti",
        "question_text": "Mashhur 'Lolazor', 'Otamdan qolgan dalalar' romanlari muallifi kim?",
        "options": ["Murod Muhammad Do'st va Tog'ay Murod", "O'tkir Hoshimov", "Odil Yoqubov", "Pirimqul Qodirov"],
        "correct_index": 0,
        "explanation": "Murod Muhammad Do'st 'Lolazor' romanini, Tog'ay Murod esa 'Otamdan qolgan dalalar' romanini yozgan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "6-sinf",
        "chapter_title": "Antonimlar",
        "question_text": "'Saxiy' so'zining antonimini (zid ma'noli so'zini) toping.",
        "options": ["Baxil (xasis)", "Saxovatli", "Ochiqqo'l", "Jasur"],
        "correct_index": 0,
        "explanation": "Saxiy kishiga qarama-qarshi xarakterdagi shaxs baxil yoki xasis deb ataladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "11-sinf",
        "chapter_title": "Sintaktik tahlil",
        "question_text": "Bog'lovchisiz qo'shma gaplarda tinish belgilari nimalarga asosan qo'yiladi?",
        "options": ["Qismlar orasidagi mazmuniy munosabatga (sabab, zidlash, ketma-ketlik, natija)", "Faqat gap uzunligiga", "Fe'llar soniga", "Muallif xohishiga"],
        "correct_index": 0,
        "explanation": "Bog'lovchisiz qo'shma gaplarda intonatsiya va mazmun munosabatiga ko'ra vergul, nuqtali vergul, ikki nuqta yoki tire qo'yiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "8-sinf",
        "chapter_title": "Adabiy turlar - Komediya",
        "question_text": "Abdulla Qahhorning jamiyatdagi illatlarni hajv qiluvchi mashhur komediyasi qaysi?",
        "options": ["'Tobutdan tovush'", "'O'tkan kunlar'", "'Sinchalak'", "'Sarob'"],
        "correct_index": 0,
        "explanation": "'Tobutdan tovush' va 'Ayajonlarim' Abdulla Qahhorning o'tkir satirik komediyalaridir.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "10-sinf",
        "chapter_title": "Ravishdosh",
        "question_text": "'U kulib gapirdi' gapidagi 'kulib' so'zi qanday grammatik shakl?",
        "options": ["Ravishdosh", "Sifatdosh", "Harakat nomi", "Sof ravish"],
        "correct_index": 0,
        "explanation": "-b, -ib, -gach, -guncha qo'shimchalari fe'lning ravishdosh shaklini yasaydi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 5,
        "grade": "7-sinf",
        "chapter_title": "Mumtoz adabiyot",
        "question_text": "Lutfiyning Navoiy tomonidan nihoyatda yuksak baholangan mashhur g'azali matlasini ko'rsating.",
        "options": ["'Arazlab ketdi ul oy, bilmadim ne bo'ldi yana...'", "'Meni men istagan o'z suhbatiga arjumand etmas...'", "'Kecha kelgumdir debon ul sarvi gulro' kelmadi...'", "'Sensan sevarim xoh inon, xoh inonma...'"],
        "correct_index": 3,
        "explanation": "Mavlono Lutfiyning 'Sensan sevarim xoh inon, xoh inonma...' g'azalini Navoiy g'oyat yuksak e'zozlagan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 5,
        "grade": "11-sinf",
        "chapter_title": "Zamonaviy o'zbek she'riyati",
        "question_text": "Milliy ruh va Vatanga bo'lgan samimiy muhabbatni oddiy va dardli misralarda kuylagan Xalq shoiri kim?",
        "options": ["Muhammad Yusuf", "Oybek", "Hamid Olimjon", "G'afur G'ulom"],
        "correct_index": 0,
        "explanation": "Muhammad Yusuf ('Ulug'imsan, Vatanim', 'Erka kiyik') xalq qalbidan chuqur joy olgan sevimli shoirdir.",
        "difficulty": "oson"
    }
]

# ==========================================
# 6. TARIX (Subject ID: 6) - 50 TA SAVOL
# ==========================================
TARIX_QUESTIONS = [
    # 7-sinf
    {
        "subject_id": 6,
        "grade": "7-sinf",
        "chapter_title": "Qadimgi davlatlar",
        "question_text": "O'zbekiston hududida vujudga kelgan eng qadimgi davlat birlashmalaridan biri qaysi?",
        "options": ["Qadimgi Baqtriya davlati", "Turk xoqonligi", "Somoniylar davlati", "Xorazmshohlar davlati"],
        "correct_index": 0,
        "explanation": "Miloddan avvalgi VIII-VII asrlarda Baqtriya va Katta Xorazm eng qadimgi davlat uyushmalari bo'lgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "7-sinf",
        "chapter_title": "Zardushtiylik",
        "question_text": "Qadimgi ajdodlarimiz e'tiqod qilgan zardushtiylik dinining muqaddas kitobi nima deb ataladi?",
        "options": ["Avesto", "Veda", "Injil", "Qur'on"],
        "correct_index": 0,
        "explanation": "Zardushtiylik dinining muqaddas yozma yodgorligi 'Avesto' hisoblanadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "7-sinf",
        "chapter_title": "Makedoniyalik Iskandar istilosi",
        "question_text": "Miloddan avvalgi 329-327-yillarda Aleksandr Makedonskiyga (Iskandarga) qarshi So'g'diyona xalqi qo'zg'oloniga kim boshchilik qilgan?",
        "options": ["Spitamen", "To'maris", "Shiroq", "Frada"],
        "correct_index": 0,
        "explanation": "Spitamen So'g'd va Baqtriyada Iskandar qo'shiniga qarshi 3 yil davomida qahramonona partizanlik urushini olib borgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "7-sinf",
        "chapter_title": "Kushon podsholigi",
        "question_text": "Kushon podsholigining eng qudratli hukmdori kim bo'lgan va u qaysi dinning keng tarqalishiga homiylik qilgan?",
        "options": ["Kanishka, Buddizm", "Kudzul Kadfiz, Islom", "Vima Kadfiz, Zardushtiylik", "Kanishka, Xristianlik"],
        "correct_index": 0,
        "explanation": "Podsho Kanishka I davrida Kushon davlati gullab-yashnagan va buddizm davlat homiyligidagi dinga aylangan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "7-sinf",
        "chapter_title": "Buyuk Ipak yo'li",
        "question_text": "Buyuk Ipak yo'lining asosiy qismi qaysi qadimgi o'lkalar orqali o'tib, Sharq bilan G'arbni bog'lagan?",
        "options": ["O'rta Osiyo (Xorazm, So'g'd, Farg'ona)", "Faqat Shimoliy Sibir", "Faqat Arabiston yarim oroli", "Janubiy Afrika"],
        "correct_index": 0,
        "explanation": "O'rta Osiyo Buyuk Ipak yo'lining chorrahasi bo'lib, Xitoyni O'rta yer dengizi havzasi bilan bog'lagan.",
        "difficulty": "oson"
    },
    # 8-sinf
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "Turk xoqonligi",
        "question_text": "VI asr o'rtalarida (552-yil) Buyuk Turk xoqonligiga asos solgan shaxs kim?",
        "options": ["Bumin xoqon", "Muqan xoqon", "Bilga xoqon", "Kultegin"],
        "correct_index": 0,
        "explanation": "552-yilda Bumin xoqon Oltoyda Turk xoqonligiga asos soldi va 'Elxon' unvonini oldi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "Arablar istilosi va ozodlik kurashi",
        "question_text": "VIII asrning 70-80-yillarida Movarounnahrda arab xalifaligiga qarshi 'Oq kiyimlilar' harakatiga kim rahbarlik qilgan?",
        "options": ["Muqanna (Hoshim ibn Hakim)", "Abu Muslim", "Rofe ibn Lays", "Spitamen"],
        "correct_index": 0,
        "explanation": "Muqanna boshchiligidagi 'Oq kiyimlilar' qo'zg'oloni 770-780-yillarda arablarga qarshi 10 yildan ortiq davom etgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "Sharq Renessansi",
        "question_text": "Algebra faniga asos solgan va nol raqami hamda o'nlik sanoq sistemasini kiritgan alloma kim?",
        "options": ["Muhammad al-Xorazmiy", "Ahmad al-Farg'oniy", "Abu Rayhon Beruniy", "Ibn Sino"],
        "correct_index": 0,
        "explanation": "Al-Xorazmiy 'Al-kitob al-muxtasar fi hisob al-jabr va al-muqobala' asari orqali algebra faniga asos soldi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "Sharq Renessansi",
        "question_text": "'Tib qonunlari' (Al-Qonun fit-tibb) asari muallifi, 'Tibbiyot amiri' deb atalgan olim kim?",
        "options": ["Abu Ali ibn Sino", "Abu Bakr ar-Roziy", "Abu Rayhon Beruniy", "Mirzo Ulug'bek"],
        "correct_index": 0,
        "explanation": "Ibn Sino (Avitsenna) yaratgan 5 jildlik 'Tib qonunlari' asari asrlar davomida Yevropa universitetlarida asosiy tibbiy darslik bo'lgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "Somoniylar davlati",
        "question_text": "Movarounnahrda mustaqil Somoniylar davlatining asoschisi va Buxoroni poytaxt qilgan amir kim?",
        "options": ["Ismoil Somoniy", "Nasr I", "Ahmad Somoniy", "Nuh II"],
        "correct_index": 0,
        "explanation": "Ismoil Somoniy (892-907) Movarounnahr va Xurosonni markazlashgan kuchli davlatga aylantirdi.",
        "difficulty": "oson"
    },
    # 9-sinf
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Mo'g'ullar istilosi",
        "question_text": "Mo'g'ul bosqinchilariga qarshi so'nggi nafasigacha mardonavor kurashgan Xorazmshohlar sarkardasi kim?",
        "options": ["Jaloliddin Manguberdi", "Aloviddin Muhammad", "Najmiddin Kubro", "Temur Malik"],
        "correct_index": 0,
        "explanation": "Jaloliddin Manguberdi Chingizxonga qarshi Parvon jangida yirik g'alabaga erishgan va 11 yil jasorat bilan kurashgan milliy qahramondir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Amir Temur davlati",
        "question_text": "Amir Temur qachon va qaysi shaharda markazlashgan davlat tuzganini e'lon qildi va taxtga o'tirdi?",
        "options": ["1370-yil, Balx qurultoyida", "1365-yil, Samarqandda", "1380-yil, Shahrisabzda", "1405-yil, O'trorda"],
        "correct_index": 0,
        "explanation": "1370-yil aprelda Balx qurultoyida Amir Temur Movarounnahrning oliy hukmdori deb e'lon qilindi va poytaxt Samarqand etib belgilandi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Amir Temur davlati",
        "question_text": "Amir Temurning davlat boshqaruvi va adolat qoidalarini o'zida mujassam etgan mashhur shiori qanday edi?",
        "options": ["'Kuch - adolatdadir'", "'Adolat - hayot garovi'", "'Ilm - najot yo'li'", "'Birlikda - qudrat'"],
        "correct_index": 0,
        "explanation": "Sohibqiron Amir Temurning davlat siyosatidagi bosh shiori 'Rosti-rusti' ya'ni 'Kuch - adolatdadir' bo'lgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Temuriylar Renessansi",
        "question_text": "Samarqandda ulug'vor rasadxona qurdirgan va 1018 ta yulduzning jadvalini ('Ziji jadidi Ko'ragoniy') tuzgan temuriy hukmdor olim kim?",
        "options": ["Mirzo Ulug'bek", "Shohruh Mirzo", "Sulton Husayn Boyqaro", "Mirzo Bobur"],
        "correct_index": 0,
        "explanation": "Mirzo Ulug'bek (1394-1449) jahon ilm-fani tarixida tengsiz astronom, matematik va adolatli davlat arbobidir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Temuriylar davri",
        "question_text": "Temuriylar davrida Hirotda madaniyat, san'at va adabiyotning yuksak cho'qqiga chiqishiga kimlar rahnamolik qilgan?",
        "options": ["Sulton Husayn Boyqaro va Alisher Navoiy", "Mirzo Shohruh va Gavkharshodbegim", "Amir Temur va Bibixonim", "Abu Said va Jomiy"],
        "correct_index": 0,
        "explanation": "Sulton Husayn Boyqaro va uning bosh vaziri Alisher Navoiy davrida Hirot Sharq madaniyatining yirik poytaxtiga aylandi.",
        "difficulty": "oson"
    },
    # 10-sinf
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Uch xonlik davri",
        "question_text": "XVI-XIX asrlarda O'zbekiston hududida mavjud bo'lgan 3 ta davlatni ko'rsating.",
        "options": ["Buxoro amirligi, Xiva xonligi va Qo'qon xonligi", "Qoraxoniylar, G'aznaviylar va Saljuqiylar", "Shayboniylar, Ashtarxoniylar va Temuriylar", "Xorazm, So'g'd va Baqtriya"],
        "correct_index": 0,
        "explanation": "O'rta Osiyoda XVI-XIX asrlarda uch xonlik: Buxoro amirligi (xonligi), Xiva xonligi va Qo'qon xonligi vujudga keldi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Chor Rossiyasi bosqini",
        "question_text": "Toshkent shahri general Chernyayev boshchiligidagi chor qo'shinlari tomonidan qaysi yili bosib olindi?",
        "options": ["1865-yil", "1868-yil", "1873-yil", "1876-yil"],
        "correct_index": 0,
        "explanation": "1865-yil iyun oyida chor Rossiyasi qo'shinlari qattiq janglardan so'ng Toshkent shahrini egalladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Chor Rossiyasi bosqini",
        "question_text": "Qo'qon xonligi rasman tugatilib, Farg'ona viloyati tashkil etilgan yilni aniqlang.",
        "options": ["1876-yil", "1868-yil", "1873-yil", "1885-yil"],
        "correct_index": 0,
        "explanation": "1876-yil fevral oyida Qo'qon xonligi tugatilib, Rossiya imperiyasi tarkibiga Farg'ona viloyati sifatida qo'shib olindi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Milliy ozodlik harakatlari",
        "question_text": "1898-yilda Andijonda chor mustamlakachilariga qarshi ko'tarilgan xalq qo'zg'oloniga kim yetakchilik qilgan?",
        "options": ["Dukchi eshon (Muhammadali xalfa)", "Po'latxon", "Madaminbek", "Ibrohimbek"],
        "correct_index": 0,
        "explanation": "1898-yil may oyida Andijonda Dukchi eshon boshchiligida xalq milliy-ozodlik qo'zg'oloni bo'lib o'tdi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Jadidchilik harakati",
        "question_text": "Turkistonda 'usuli savtiya' (yangi usul) maktablari ochgan va 'Taraqqiy', 'Oyina' jurnallarini chop etgan ma'rifatparvarlar harakati nima deb ataldi?",
        "options": ["Jadidchilik harakati", "Populizm", "Slavyanparvarlar", "Xalqparvarlar"],
        "correct_index": 0,
        "explanation": "XIX asr oxiri - XX asr boshida vujudga kelgan ma'rifatparvarlik va ozodlik harakati 'Jadidlar' deb nomlandi.",
        "difficulty": "oson"
    },
    # 11-sinf
    {
        "subject_id": 6,
        "grade": "11-sinf",
        "chapter_title": "Turkiston Muxtoriyati",
        "question_text": "1917-yil noyabr oyida Qo'qonda e'lon qilingan ilk demokratik milliy hukumat qanday atalgan?",
        "options": ["Turkiston Muxtoriyati", "Buxoro Xalq Respublikasi", "Xorazm Respublikasi", "Turkiston ASSR"],
        "correct_index": 0,
        "explanation": "1917-yil 27-noyabrda IV Favqulodda umumturkiston o'lka musulmonlar syezdida Turkiston Muxtoriyati e'lon qilindi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "11-sinf",
        "chapter_title": "Qatag'on fojiasi",
        "question_text": "1937-1938-yillardagi sovet qatag'onlarida 'xalq dushmani' tamg'asi bilan qatl etilgan buyuk millat fidoiylari qaysilar?",
        "options": ["Abdulla Qodiriy, Cho'lpon, Fitrat", "Hamza, Sobir Rahimov, Oybek", "Navoiy, Bobur, Mashrab", "Avloniy, Muqimiy, Furqat"],
        "correct_index": 0,
        "explanation": "1938-yil 4-5-oktabr kunlari Cho'lpon, Abdulla Qodiriy, Fitrat kabi o'nlab jadid allomalari otib tashlangan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "11-sinf",
        "chapter_title": "Ikkinchi jahon urushi davri",
        "question_text": "Ikkinchi jahon urushida jasorat ko'rsatib birinchi o'zbek generali unvoniga sazovor bo'lgan qo'mondon kim?",
        "options": ["Sobir Rahimov", "To'ychi Ortiqov", "Mamajon Shokirov", "Qo'chqor Turdiyev"],
        "correct_index": 0,
        "explanation": "Gvardiya general-mayori Sobir Rahimov jasorati uchun 'Temir general' nomini olgan va qahramonlik ko'rsatgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "11-sinf",
        "chapter_title": "O'zbekiston Mustaqilligi",
        "question_text": "O'zbekiston Respublikasining davlat mustaqilligi qachon e'lon qilingan?",
        "options": ["1991-yil 31-avgust", "1991-yil 1-sentabr", "1990-yil 20-iyun", "1992-yil 8-dekabr"],
        "correct_index": 0,
        "explanation": "1991-yil 31-avgustda Oliy Kengashning navbatdan tashqari sessiyasida O'zbekiston Respublikasining Davlat mustaqilligi e'lon qilindi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "11-sinf",
        "chapter_title": "Davlat ramzlari",
        "question_text": "O'zbekiston Respublikasining Davlat bayrog'i qachon qabul qilingan?",
        "options": ["1991-yil 18-noyabr", "1992-yil 2-iyul", "1992-yil 10-dekabr", "1991-yil 30-sentabr"],
        "correct_index": 0,
        "explanation": "O'zbekiston Respublikasi Davlat bayrog'i to'g'risidagi qonun 1991-yil 18-noyabrda qabul qilingan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "11-sinf",
        "chapter_title": "BMT ga a'zolik",
        "question_text": "O'zbekiston Respublikasi qachon Birlashgan Millatlar Tashkilotiga (BMT) to'laqonli a'zo bo'ldi?",
        "options": ["1992-yil 2-mart", "1991-yil 31-avgust", "1993-yil 1-yanvar", "1994-yil 5-may"],
        "correct_index": 0,
        "explanation": "1992-yil 2-martda BMT Bosh Assambleyasida O'zbekiston Respublikasi BMT ga teng huquqli a'zo sifatida qabul qilindi.",
        "difficulty": "orta"
    },
    # Jahon tarixi
    {
        "subject_id": 6,
        "grade": "7-sinf",
        "chapter_title": "Qadimgi dunyo tarixi",
        "question_text": "Qadimgi Misr davlatida eng baland ehrom (piramida) qaysi fir'avn sharafiga qurilgan?",
        "options": ["Xeops (Xufu)", "Xafra", "Mikerin", "Tutanxamon"],
        "correct_index": 0,
        "explanation": "Gizada miloddan avvalgi XXVI asrda bunyod etilgan eng ulug'vor piramida fir'avn Xeops piramidasidir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "7-sinf",
        "chapter_title": "Qadimgi Yunoniston",
        "question_text": "Qadimgi Yunonistonda Olimpiya o'yinlari dastlab qaysi yili o'tkazilgan?",
        "options": ["Miloddan avvalgi 776-yil", "Miloddan avvalgi 500-yil", "Miloddan avvalgi 336-yil", "Milodiy 394-yil"],
        "correct_index": 0,
        "explanation": "Birinchi umumyunon Olimpiya o'yinlari miloddan avvalgi 776-yilda Zevs sharafiga o'tkazilgan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "O'rta asrlar jahon tarixi",
        "question_text": "476-yilda Qadimgi dunyo tarixining tugashiga va o'rta asrlarning boshlanishiga qaysi voqea sabab bo'lgan?",
        "options": ["G'arbiy Rim imperiyasining qulashi", "Vizantiya imperiyasining tugashi", "Arab xalifaligining tashkil topishi", "Salib yurishlarining boshlanishi"],
        "correct_index": 0,
        "explanation": "476-yilda Odoakr tomonidan so'nggi Rim imperatori Romul Avgustulning taxtdan ag'darilishi G'arbiy Rimning yemirilishi bo'ldi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "Buyuk geografik kashfiyotlar",
        "question_text": "1492-yilda Yevropadan g'arbga suzib, yangi qit'ani (Amerikani) kashf etgan dengizchi kim?",
        "options": ["Xristofor Kolumb", "Vasko da Gama", "Fernan Magellan", "Amerigo Vespuchchi"],
        "correct_index": 0,
        "explanation": "1492-yil 12-oktabrda Xristofor Kolumb ekspeditsiyasi Yangi Dunyo qirg'oqlariga (Bagama orollariga) yetib bordi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "Buyuk geografik kashfiyotlar",
        "question_text": "Tarixda birinchi bo'lib dunyo bo'ylab dengiz sayohatini (1519-1522) amalga oshirgan ekspeditsiya rahbari kim?",
        "options": ["Fernan Magellan", "Jeyms Kuk", "Vasko da Gama", "Fransis Dreyk"],
        "correct_index": 0,
        "explanation": "Fernan Magellan ekspeditsiyasi Yer shari dumaloq ekanligini amalda to'liq isbotladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Yangi davr jahon tarixi",
        "question_text": "XVIII asr oxirida (1789-yil 14-iyul) Bastiliya qal'asining egallanishi bilan boshlangan ulkan tarixiy voqea nima?",
        "options": ["Buyuk Fransuz inqilobi", "Angliya burjua inqilobi", "AQSh mustaqillik urushi", "Vena kongressi"],
        "correct_index": 0,
        "explanation": "1789-yil 14-iyulda Bastiliyaning olinishi Buyuk Fransuz inqilobining boshlanish nuqtasi bo'ldi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Sanoat to'ntarishi",
        "question_text": "XVIII asrning ikkinchi yarmida universal bug' mashinasini ixtiro qilib sanoat to'ntarishiga yo'l ochgan olim kim?",
        "options": ["Jeyms Uatt", "Jorj Stefenson", "Tomas Edison", "Maykl Faradey"],
        "correct_index": 0,
        "explanation": "Shotland muhandisi Jeyms Uatt 1769-1784-yillarda universal bug' dvigatelini yaratdi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Birinchi jahon urushi",
        "question_text": "Birinchi jahon urushi qaysi yillar oralig'ida bo'lib o'tdi?",
        "options": ["1914-1918-yillar", "1912-1916-yillar", "1939-1945-yillar", "1905-1907-yillar"],
        "correct_index": 0,
        "explanation": "Birinchi jahon urushi 1914-yil 28-iyuldan 1918-yil 11-noyabrgacha davom etgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Ikkinchi jahon urushi",
        "question_text": "Fashistlar Germaniyasining so'zsiz taslim bo'lish (kapitulyatsiya) to'g'risidagi akti qachon imzolandi?",
        "options": ["1945-yil 8-may", "1945-yil 2-sentabr", "1944-yil 6-iyun", "1945-yil 9-avgust"],
        "correct_index": 0,
        "explanation": "1945-yil 8-mayda Berlinda fashistlar Germaniyasining so'zsiz taslim bo'lish akti imzolandi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Ikkinchi jahon urushi",
        "question_text": "Ikkinchi jahon urushi rasman qachon va qayerda yakunlangan?",
        "options": ["1945-yil 2-sentabr, 'Missuri' linkorida Yaponiya taslim bo'lishi bilan", "1945-yil 9-may, Berlinda", "1945-yil 6-avgust, Xirosimada", "1946-yil 1-yanvarda"],
        "correct_index": 0,
        "explanation": "1945-yil 2-sentabrda AQShning 'Missuri' harbiy kemasida Yaponiya so'zsiz taslim bo'ldi va Ikkinchi jahon urushi tugadi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "11-sinf",
        "chapter_title": "Xalqaro tashkilotlar",
        "question_text": "Dunyo xavfsizligini ta'minlash maqsadida 1945-yil 24-oktabrda tuzilgan asosiy xalqaro tashkilot qaysi?",
        "options": ["Birlashgan Millatlar Tashkiloti (BMT)", "Millatlar Ligasi", "Yevropa Ittifoqi", "NATO"],
        "correct_index": 0,
        "explanation": "1945-yil 24-oktabrda San-Fransisko konferensiyasi natijasida BMT nizomi kuchga kirdi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "7-sinf",
        "chapter_title": "Qadimgi Bobil",
        "question_text": "Tarixda birinchi mukammal yozma qonunlar to'plamini tosh ustunga yozdirgan Bobil hukmdori kim?",
        "options": ["Xammurapi", "Navuxodonosor", "Kir II", "Doro I"],
        "correct_index": 0,
        "explanation": "Miloddan avvalgi XVIII asrda Bobil podshosi Xammurapi 282 moddadan iborat mashhur qonunlar to'plamini tuzdirgan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "Xorazmshohlar davlati",
        "question_text": "Xorazmshohlar davlatini yuksaltirib, poytaxtni Gurganjdan Samarqandga ko'chirgan hukmdor kim?",
        "options": ["Aloviddin Muhammad", "Takash", "Qutbiddin Muhammad", "Atsiz"],
        "correct_index": 0,
        "explanation": "Aloviddin Muhammad (1200-1220) davrida Xorazmshohlar ulkan saltanatga aylandi va poytaxt Samarqandga ko'chirildi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Temuriylar diplomatiyasi",
        "question_text": "Amir Temur saroyiga Kastiliya (Ispaniya) qiroli Genrix III nomidan elchi bo'lib kelgan va kundalik yozib qoldirgan shaxs kim?",
        "options": ["Rui Gonsales de Klavixo", "Marko Polo", "Ibn Battuta", "Plano Karpini"],
        "correct_index": 0,
        "explanation": "Ispan elchisi Rui Gonsales de Klavixo 1404-yilda Samarqandda Amir Temur qabulida bo'lib, 'Samarqandga Amir Temur saroyiga sayohat kundaligi' asarini yozgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Xiva xonligi",
        "question_text": "Xiva xonligining mashhur 'Shajarayi turk' va 'Shajarayi tarokima' asarlarini yozgan hukmdor va tarixchi kim?",
        "options": ["Abulg'ozi Bahodirxon", "Arab Muhammadxon", "Elbarsxon", "Muhammad Rahimxon I"],
        "correct_index": 0,
        "explanation": "Abulg'ozi Bahodirxon (1643-1663) yirik davlat arbobi, shifokor va mohir tarixchi olim bo'lgan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "11-sinf",
        "chapter_title": "Mustaqillik yillari",
        "question_text": "O'zbekiston Respublikasining milliy valyutasi - 'So'm' qachon muomalaga kiritilgan?",
        "options": ["1994-yil 1-iyul", "1991-yil 1-sentabr", "1992-yil 1-yanvar", "1995-yil 1-sentabr"],
        "correct_index": 0,
        "explanation": "1994-yil 1-iyuldan boshlab O'zbekiston Respublikasining yagona qonuniy to'lov vositasi - milliy so'm muomalaga kiritildi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "7-sinf",
        "chapter_title": "Qadimgi Rim",
        "question_text": "Miloddan avvalgi 73-71-yillarda Qadimgi Rimda gladiatorlar qo'zg'oloniga kim yetakchilik qilgan?",
        "options": ["Spartak", "Yuliy Sezar", "Gannibal", "Krass"],
        "correct_index": 0,
        "explanation": "Spartak boshchiligidagi qullar va gladiatorlar qo'zg'oloni Rim respublikasini qattiq larzaga solgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "G'aznaviylar davlati",
        "question_text": "Mahmud G'aznaviy saroyida yashab ijod qilgan, 'Hindiston' asarini yozgan alloma kim?",
        "options": ["Abu Rayhon Beruniy", "Firdavsiy", "Ibn Sino", "Farobiy"],
        "correct_index": 0,
        "explanation": "Abu Rayhon Beruniy Mahmud G'aznaviy bilan Hindistonga borib, o'zining nodir 'Hindiston' (Tahqiq ma li-l-Hind) asarini yozdi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Anqara jangi",
        "question_text": "1402-yilda Amir Temur va Usmonli turk sultoni Boyazid Yildirim o'rtasidagi tarixiy jang qayerda yuz berdi?",
        "options": ["Anqara yonida", "Damashqda", "Izmirda", "Bag'dodda"],
        "correct_index": 0,
        "explanation": "1402-yil 20-iyulda Anqara jangi bo'lib o'tdi va Amir Temur Yevropani xaloskor sifatida qutqardi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Buxoro amirligi",
        "question_text": "Buxoro amirligida mang'itlar sulolasiga asos solgan hukmdor kim?",
        "options": ["Muhammad Rahimiy (Muhammad Rahim)", "Doniyolbiy", "Amir Shohmurod", "Amir Nasrulloh"],
        "correct_index": 0,
        "explanation": "1756-yilda Muhammad Rahim otaliq o'zini Buxoro taxtining xoni deb e'lon qilib, mang'itlar sulolasiga asos soldi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "11-sinf",
        "chapter_title": "Mustaqil O'zbekiston",
        "question_text": "YUNESKO qarori bilan Samarqand shahrining 2750 yillik yubileyi qaysi yili keng nishonlandi?",
        "options": ["2007-yil", "1997-yil", "2002-yil", "2010-yil"],
        "correct_index": 0,
        "explanation": "2007-yilda qadimiy va navqiron Samarqand shahrining 2750 yilligi xalqaro miqyosda nishonlandi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 6,
        "grade": "8-sinf",
        "chapter_title": "O'rta asrlar madaniyati",
        "question_text": "XV asr o'rtalarida (1450-yillar) Yevropada kitob bosish dastgohini (tipografiya) ixtiro qilgan kashfiyotchi kim?",
        "options": ["Iogann Gutenberg", "Leonardo da Vinchi", "Nikolay Kopernik", "Galileo Galiley"],
        "correct_index": 0,
        "explanation": "Nemis kashfiyotchisi Iogann Gutenberg metalldan quyilgan harflar yordamida kitob bosishni kashf etdi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "9-sinf",
        "chapter_title": "Temuriylar shajarasi",
        "question_text": "Hindistonda 300 yildan ortiq hukm surgan Buyuk Boburiylar imperiyasiga kim asos solgan?",
        "options": ["Zahiriddin Muhammad Bobur", "Humoyun Mirzo", "Jaloliddin Akbar", "Shoh Jahon"],
        "correct_index": 0,
        "explanation": "1526-yilda Panipat jangidagi g'alabadan so'ng Bobur Hindistonda qudratli Boburiylar davlatiga asos soldi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 6,
        "grade": "10-sinf",
        "chapter_title": "Qo'qon xonligi",
        "question_text": "Qo'qon xonligida o'zbeklarning qaysi urug'i hukmronlik qilgan?",
        "options": ["Ming urug'i", "Mang'it urug'i", "Qo'ng'irot urug'i", "Nayman urug'i"],
        "correct_index": 0,
        "explanation": "Qo'qon xonligida ming sulolasi, Xivada qo'ng'irotlar, Buxoroda esa mang'itlar sulolasi hukm surgan.",
        "difficulty": "orta"
    }
]
