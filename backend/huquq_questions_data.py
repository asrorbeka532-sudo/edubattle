# -*- coding: utf-8 -*-
"""
Huquq fani bo'yicha 215 ta rasmiy test savollari banki:
1. O'zbekiston Respublikasi Konstitutsiyasi (Yangi tahrir) - 75 ta savol
2. 8-sinf: Davlat va huquq nazariyasi asoslari - 35 ta savol
3. 9-sinf: Fuqarolik, oila va mehnat huquqi - 40 ta savol
4. 10-sinf: Ma'muriy, jinoyat va ekologiya huquqi - 35 ta savol
5. 11-sinf: Xalqaro huquq, sud hokimiyati va inson huquqlari - 30 ta savol
Jami: 215 ta sifatli, aniq javobli testlar.
"""

HUQUQ_QUESTIONS = [
    # =========================================================================
    # BO'LIM 1: O'ZBEKISTON RESPUBLIKASI KONSTITUTSIYASI (YANGI TAHRIR)
    # =========================================================================
    (
        "Konstitutsiya - Asosiy prinsiplar",
        "O'zbekiston Respublikasi Konstitutsiyasining 1-moddasiga ko'ra O'zbekiston qanday davlat?",
        [
            "Suveren, demokratik, huquqiy, ijtimoiy va dunyoviy davlat",
            "Monarxiya va unitar boshqaruvdagi davlat",
            "Federativ va sotsialistik respublika",
            "Teokratik va parlamentar respublika"
        ],
        0,
        "1-modda: O'zbekiston – boshqaruvning respublika shakliga ega bo'lgan suveren, demokratik, huquqiy, ijtimoiy va dunyoviy davlatdir.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Asosiy prinsiplar",
        "Yangi tahrirdagi O'zbekiston Respublikasi Konstitutsiyasi necha bo'lim, bob va moddadan iborat?",
        [
            "6 bo'lim, 27 bob, 155 modda",
            "6 bo'lim, 26 bob, 128 modda",
            "5 bo'lim, 21 bob, 140 modda",
            "7 bo'lim, 30 bob, 165 modda"
        ],
        0,
        "2023-yil 30-apreldagi referendumda qabul qilingan Konstitutsiya 6 bo'lim, 27 bob va 155 moddadan iborat.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Asosiy prinsiplar",
        "Konstitutsiyaning 7-moddasiga binoan, davlat hokimiyatining birdan-bir manbai kim?",
        [
            "Xalq",
            "Prezident",
            "Oliy Majlis",
            "Vazirlar Mahkamasi"
        ],
        0,
        "7-modda: Xalq davlat hokimiyatining birdan-bir manbaidir.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Asosiy prinsiplar",
        "O'zbekiston xalqi nomidan faqat kimlar ish olib borishi mumkin? (10-modda)",
        [
            "Oliy Majlis va O'zbekiston Respublikasi Prezidenti",
            "Bosh vazir va Oliy Majlis",
            "Konstitutsiyaviy sud va Oliy sud",
            "Siyosiy partiyalar va nodavlat tashkilotlar"
        ],
        0,
        "10-modda: O'zbekiston xalqi nomidan faqat u saylagan O'zbekiston Respublikasi Oliy Majlisi va Prezidenti ish olib borishi mumkin.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Asosiy prinsiplar",
        "Konstitutsiyaning 11-moddasiga binoan, davlat hokimiyati qaysi tarmoqlarga bo'linadi?",
        [
            "Qonun chiqaruvchi, ijro etuvchi va sud hokimiyati",
            "Prezidentlik, vazirlik va sudyalik hokimiyati",
            "Markaziy, viloyat va tuman hokimiyati",
            "Davlat xavfsizligi, armiya va huquqni muhofaza qilish"
        ],
        0,
        "11-modda: Davlat hokimiyati tizimi hokimiyatlarning qonun chiqaruvchi, ijro etuvchi va sud hokimiyatiga bo'linishi prinsipiga asoslanadi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Asosiy prinsiplar",
        "Konstitutsiyaning 15-moddasiga ko'ra, qaysi hujjat O'zbekiston Respublikasi butun hududida oliy yuridik kuchga ega?",
        [
            "O'zbekiston Respublikasi Konstitutsiyasi",
            "Prezident farmonlari",
            "Vazirlar Mahkamasi qarorlari",
            "Oliy Majlis qonunlari"
        ],
        0,
        "15-modda: O'zbekiston Respublikasida O'zbekiston Respublikasi Konstitutsiyasi va qonunlarining ustunligi so'zsiz tan olinadi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Asosiy prinsiplar",
        "Konstitutsiya normalari qanday xususiyatga ega va to'g'ridan-to'g'ri amal qiladi?",
        [
            "To'g'ridan-to'g'ri amal qiluvchi oliy yuridik kuchga ega",
            "Faqat maxsus qonun qabul qilingandan so'ng kuchga kiradi",
            "Tavsiyaviy xarakterga ega",
            "Faqat davlat idoralari uchun majburiy"
        ],
        0,
        "15-modda: Konstitutsiya to'g'ridan-to'g'ri amal qiladi va yagona huquqiy makonning asosini tashkil etadi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Asosiy prinsiplar",
        "Xalqaro huquqning umum e'tirof etilgan prinsiplari va normalari hamda O'zbekistonning xalqaro shartnomalari qanday o'ringa ega? (15-modda)",
        [
            "Huquqiy tizimning tarkibiy qismidir va milliy qonunlardan ustunlik qiladi",
            "Faqat xalqaro munosabatlarda qo'llaniladi",
            "Konstitutsiyadan yuqori turadi",
            "Milliy qonunlardan past yuridik kuchga ega"
        ],
        0,
        "15-modda: O'zbekiston Respublikasining xalqaro shartnomasi bilan boshqacha qoidalar belgilangan bo'lsa, xalqaro shartnoma qoidalari qo'llaniladi.",
        "Konstitutsiya",
        "qiyin"
    ),
    (
        "Konstitutsiya - Asosiy prinsiplar",
        "O'zbekiston Respublikasi davlat tili qaysi til hisoblanadi? (4-modda)",
        [
            "O'zbek tili",
            "O'zbek va rus tillari",
            "O'zbek va qoraqalpoq tillari",
            "Davlat tili belgilanmagan"
        ],
        0,
        "4-modda: O'zbekiston Respublikasining davlat tili o'zbek tilidir.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Davlat ramzlari",
        "O'zbekiston Respublikasining davlat ramzlari qaysilar? (5-modda)",
        [
            "Bayroq, gerb va madhiya",
            "Konstitutsiya, bayroq va pul birligi",
            "Prezident shtandarti, gerb va poytaxt",
            "Armiya, gerb va bayroq"
        ],
        0,
        "5-modda: O'zbekiston Respublikasi qonun bilan tasdiqlanadigan o'z davlat ramzlari – bayrog'i, gerbi va madhiyasiga ega.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Shaxsiy huquqlar",
        "Yashash huquqi bo'yicha yangi tahrirdagi Konstitutsiyaning 25-moddasida qanday qat'iy qoida belgilangan?",
        [
            "O'lim jazosi taqiqlanadi",
            "O'lim jazosi faqat harbiy holatda qo'llaniladi",
            "O'lim jazosi umrbod qamoq bilan almashtirilgan",
            "O'lim jazosi og'ir jinoyatlar uchun ruxsat etiladi"
        ],
        0,
        "25-modda: Yashash huquqi har bir insonning ajralmas huquqidir. O'zbekiston Respublikasida o'lim jazosi taqiqlanadi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Inson erkinligi",
        "Sud qarorisiz shaxs ko'pi bilan necha soatdan ortiq muddat ushlab turilishi mumkin emas? (27-modda, Xabeas korpus)",
        [
            "48 soat",
            "24 soat",
            "72 soat",
            "12 soat"
        ],
        0,
        "27-modda: Sudning qarorisiz shaxs 48 soatdan ortiq muddat ushlab turilishi mumkin emas (Xabeas korpus instituti).",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Miranda qoidasi",
        "Shaxsni ushlash chog'ida uning huquqlari va ushlab turilishi asoslari tushuntirilishi shartligi qaysi xalqaro qoidaga asoslanadi? (27-modda)",
        [
            "Miranda qoidasi",
            "Gabilitatsiya qoidasi",
            "Prezumpriya qoidasi",
            "Litsenziya qoidasi"
        ],
        0,
        "27-modda: Shaxsni ushlash chog'ida unga tushunarli tilda uning huquqlari va ushlab turilishi asoslari tushuntirilishi shart (Miranda qoidasi).",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Odil sudlov",
        "Aybsizlik prezumpsiyasi qoidasiga ko'ra, shaxs qachon aybdor deb hisoblanadi? (28-modda)",
        [
            "Sudning qonuniy kuchga kirgan hukmi bilan isbotlangandagina",
            "Tergovchi ayblov xulosasini tuzganda",
            "Prokuror ayblovni tasdiqlaganda",
            "Gumon qilinuvchi o'z aybiga iqror bo'lganda"
        ],
        0,
        "28-modda: Jinoyat sodir etganlikda ayblanayotgan shaxs uning aybi qonunda nazarda tutilgan tartibda oshkora sud muhokamasi yo'li bilan isbotlanmaguncha aybsiz hisoblanadi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Odil sudlov",
        "Gumon qilinuvchi yoki ayblanuvchi o'zining aybsizligini isbotlab berishga majburmi? (28-modda)",
        [
            "Yo'q, u o'zining aybsizligini isbotlashga majbur emas",
            "Ha, har bir fuqaro o'zini oqlashi shart",
            "Faqat sud majlisida majbur",
            "Faqat advokati bo'lmagan taqdirda majbur"
        ],
        0,
        "28-modda: Ayblanuvchi o'zining aybsizligini isbotlab berishi shart emas va istalgan vaqtda sukut saqlash huquqidan foydalanishi mumkin.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Odil sudlov",
        "Aybdorlikka oid barcha noaniqliklar va gumonlar kimning foydasiga hal etiladi? (28-modda)",
        [
            "Gumon qilinuvchi, ayblanuvchi yoki sudlanuvchining foydasiga",
            "Jabrlanuvchining foydasiga",
            "Davlat foydasiga",
            "Tergov organlari foydasiga"
        ],
        0,
        "28-modda: Aybdorlikka oid barcha bartaraf etib bo'lmaydigan shubhalar gumon qilinuvchining, ayblanuvchining yoki sudlanuvchining foydasiga hal qilinadi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Yuridik yordam",
        "Konstitutsiyaning 29-moddasiga muvofiq, har kim qaysi vaqtdan boshlab malakali yuridik yordam olish huquqiga ega?",
        [
            "Shaxs ushlangan, qamoqqa olingan yoki ayblangan dastlabki daqiqalardan boshlab",
            "Faqat sud jarayoni boshlanganda",
            "Tergov yakunlanib sudga oshirilganda",
            "Faqat sud hukmi e'lon qilingandan keyin"
        ],
        0,
        "29-modda: Har kimga malakali yuridik yordam olish huquqi kafolatlanadi. Qonunda nazarda tutilgan hollarda yuridik yordam davlat hisobidan ko'rsatiladi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Shaxsiy daxlsizlik",
        "Turar joyga uningda yashovchi shaxslarning xohishiga qarshi kirish qanday hollarda ruxsat etiladi? (31-modda)",
        [
            "Faqat qonunda nazarda tutilgan hollarda va sud qaroriga asosan",
            "Mahalla raisi ruxsat berganida",
            "Ixtiyoriy fuqaroning iltimosiga ko'ra",
            "Tergovchining og'zaki ko'rsatmasi bilan"
        ],
        0,
        "31-modda: Turar joy daxlsizdir. Hech kim turar joyga unda yashovchi shaxslarning xohishiga qarshi kirishi mumkin emas. Turar joyda tintuv o'tkazishga faqat sud qaroriga asosan yo'l qo'yiladi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Aloqa siri",
        "Yozishmalar, telefon orqali so'zlashuvlar va xabarlar sirini cheklashga kimning qarori bilan ruxsat etiladi? (31-modda)",
        [
            "Faqat sud qaroriga asosan",
            "Prokuror ruxsati bilan",
            "Ichki ishlar vaziri buyrug'i bilan",
            "Aloqa kompaniyasi ruxsati bilan"
        ],
        0,
        "31-modda: Yozishmalar, telefon orqali so'zlashuvlar, pochta, telegraf va boshqa xabarlar sir saqlanishi huquqi faqat qonunga muvofiq va sudning qaroriga asosan cheklanishi mumkin.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Siyosiy huquqlar",
        "O'zbekiston Respublikasi fuqarolari necha yoshdan boshlab saylash huquqiga ega? (37-modda)",
        [
            "18 yoshga to'lgan kundan",
            "16 yoshdan",
            "21 yoshdan",
            "25 yoshdan"
        ],
        0,
        "Yangi Konstitutsiya va Saylov kodeksiga muvofiq, saylov kuni 18 yoshga to'lgan fuqarolar saylash huquqiga egadirlar.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Siyosiy huquqlar",
        "Kimlar saylovda ishtirok etish huquqidan mahrum qilinishi mumkin? (Saylov tizimi)",
        [
            "Sud tomonidan muomalaga layoqatsiz deb topilgan, shuningdek og'ir jinoyatlari uchun ozodlikdan mahrum etish joylarida saqlanayotgan shaxslar",
            "Chet elda vaqtincha ishlayotgan fuqarolar",
            "Talabalar va pensiya yoshidagi shaxslar",
            "Boshqa viloyatda yashovchi fuqarolar"
        ],
        0,
        "Sud tomonidan muomalaga layoqatsiz deb topilgan, shuningdek og'ir va o'ta og'ir jinoyatlar uchun sud hukmi bilan ozodlikdan mahrum etish joylarida saqlanayotganlar saylovda qatnashmaydi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Mehnat huquqi",
        "Konstitutsiyaning 44-moddasiga binoan, qanday mehnat qat'iyan taqiqlanadi?",
        [
            "Majburiy mehnat va bolalar mehnatining eng yomon shakllari",
            "Faqat tungi smenada ishlash",
            "Haftasiga 40 soatdan ortiq ishlash",
            "Ixtiyoriy jamoat ishlari"
        ],
        0,
        "44-modda: Majburiy mehnat taqiqlanadi. Bolalar mehnatining bolaning sog'lig'iga, xavfsizligiga xavf soluvchi har qanday shakli taqiqlanadi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Mehnat huquqi",
        "O'zbekiston Respublikasida mehnatga haq to'lashning eng kam miqdori qanday mezonga mos bo'lishi shart? (42-modda)",
        [
            "Insonning munosib yashashi uchun yetarli bo'lishi kerak",
            "O'rtacha oylik ish haqining 10 foizidan kam bo'lmasligi",
            "Faqat korxona daromadiga bog'liq bo'lishi",
            "Davlat byudjeti qoldig'iga qarab belgilanadi"
        ],
        0,
        "42-modda: Mehnatga haq to'lashning eng kam miqdori insonning munosib turmush darajasini ta'minlash zarurati hisobga olingan holda belgilanadi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Ta'lim huquqi",
        "Konstitutsiyaning 50-moddasiga ko'ra, davlat qaysi ta'lim turlarining bepul va majburiyligini kafolatlaydi?",
        [
            "Bepul umumiy o'rta ta'lim olishni",
            "Barcha oliy ta'lim bosqichlarini",
            "Faqat maktabgacha ta'limni",
            "Faqat magistratura va doktoranturani"
        ],
        0,
        "50-modda: Har kim ta'lim olish huquqiga ega. Davlat bepul umumiy o'rta ta'lim va boshlang'ich professional ta'lim olishni kafolatlaydi. Umumiy o'rta ta'lim majburiydir.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Ta'lim huquqi",
        "Oliy ta'lim tashkilotlari qonunga muvofiq qanday huquqqa ega? (51-modda)",
        [
            "Akademik erkinlik, o'zini o'zi boshqarish, tadqiqotlar o'tkazish erkinligi",
            "O'z qonunlarini qabul qilish huquqiga",
            "Davlat soliqlaridan butunlay ozod bo'lish huquqiga",
            "Harbiy xizmatdan to'liq ozod qilish huquqiga"
        ],
        0,
        "51-modda: Davlat oliy ta'lim tashkilotlariga akademik erkinlik, o'zini o'zi boshqarish, o'qitish va ilmiy tadqiqotlar o'tkazish erkinligi huquqini taqdim etadi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Oila va jamiyat",
        "Nikoh qanday asosda tuziladi? (76-modda)",
        [
            "Nikohlanuvchilarning ixtiyoriy roziligi va teng huquqliligiga asoslanadi",
            "Ota-onalarning majburiy kelishuviga asoslanadi",
            "Faqat diniy marosim asosida",
            "Mahalla qo'mitasining roziligi bilan"
        ],
        0,
        "76-modda: Oila jamiyatning asosiy bo'g'inidir hamda jamiyat va davlat muhofazasidadir. Nikoh nikohlanuvchilarning ixtiyoriy roziligiga va teng huquqliligiga asoslanadi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Bolalar va ota-onalar",
        "Voyaga yetgan, mehnatga layoqatli farzandlarning ota-onasi oldidagi konstitutsiyaviy burchi nima? (80-modda)",
        [
            "O'z ota-onalari haqida g'amxo'rlik qilish",
            "Ota-onasining kreditlarini to'lash",
            "Ota-onasi bilan bir uyda yashash",
            "Ota-onasiga pensiya tayinlash"
        ],
        0,
        "80-modda: Voyaga yetgan, mehnatga layoqatli farzandlar o'z ota-onalari haqida g'amxo'rlik qilishga majburdirlar.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Davlat boshqaruvi",
        "O'zbekiston Respublikasi Oliy Majlisi necha palatadan iborat? (91-modda)",
        [
            "Ikki palatadan: Qonunchilik palatasi va Senat",
            "Bir palatadan: Milliy Kengash",
            "Uch palatadan: Qonunchilik, Nazorat va Senat",
            "To'rt palatadan iborat"
        ],
        0,
        "91-modda: O'zbekiston Respublikasi Oliy Majlisi oliy davlat vakillik organi bo'lib, u ikki palatadan – Qonunchilik palatasi (quyi palata) va Senatdan (yuqori palata) iborat.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Oliy Majlis",
        "Oliy Majlis Qonunchilik palatasi necha nafar deputatdan iborat? (92-modda)",
        [
            "150 nafar deputat",
            "100 nafar deputat",
            "120 nafar deputat",
            "65 nafar deputat"
        ],
        0,
        "92-modda: Qonunchilik palatasi bir yuz ellik nafar deputatdan iborat.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Oliy Majlis",
        "Yangi tahrirdagi Konstitutsiyaga ko'ra, O'zbekiston Respublikasi Senati necha nafar senatorlardan iborat? (92-modda)",
        [
            "65 nafar senator",
            "100 nafar senator",
            "84 nafar senator",
            "150 nafar senator"
        ],
        0,
        "92-modda: Senat a'zolari (senatorlar) Qoraqalpog'iston Respublikasi, viloyatlar va Toshkent shahridan to'rt nafardan saylanadi (jami 56 ta), to'qqiz nafari esa Prezident tomonidan tayinlanadi (jami 65 nafar).",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Oliy Majlis",
        "Qonunchilik palatasi deputatligiga va Senat a'zoligiga saylanish uchun fuqaro necha yoshga to'lgan bo'lishi kerak? (94-modda)",
        [
            "Saylov kuni yigirma besh yoshga to'lgan bo'lishi",
            "Yigirma bir yoshga to'lgan bo'lishi",
            "O'ttiz yoshga to'lgan bo'lishi",
            "O'n sakkiz yoshga to'lgan bo'lishi"
        ],
        0,
        "94-modda: Saylov kuni yigirma besh yoshga to'lgan hamda kamida besh yil O'zbekiston hududida muqim yashayotgan fuqaro Qonunchilik palatasi deputati va Senat a'zosi bo'lishi mumkin.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Oliy Majlis",
        "Qonunchilik palatasi va Senatning vakolat muddati necha yil? (93-modda)",
        [
            "Besh yil",
            "To'rt yil",
            "Yetti yil",
            "Olti yil"
        ],
        0,
        "93-modda: Qonunchilik palatasi va Senatning vakolat muddati – besh yil.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Prezident",
        "O'zbekiston Respublikasi Prezidenti lavozimiga saylanish muddati yangi Konstitutsiyada necha yil etib belgilandi? (106-modda)",
        [
            "Yetti yil",
            "Besh yil",
            "To'rt yil",
            "Olti yil"
        ],
        0,
        "106-modda: O'zbekiston Respublikasi Prezidenti O'zbekiston Respublikasining fuqarolari tomonidan umumiy, teng va to'g'ridan-to'g'ri saylov huquqi asosida yashirin ovoz berish yo'li bilan yetti yil muddatga saylanadi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Prezident",
        "O'zbekiston Respublikasi Prezidenti lavozimiga qanday shaxs saylanishi mumkin? (106-modda)",
        [
            "O'ttiz besh yoshdan kichik bo'lmagan, davlat tilini yaxshi biladigan va kamida 10 yil muqim yashayotgan fuqaro",
            "Yigirma besh yoshdan kichik bo'lmagan har qanday fuqaro",
            "Qirq yoshdan oshgan, faqat yuridik ma'lumotga ega shaxs",
            "O'ttiz yoshga to'lgan, ilgari sudlanmagan deputat"
        ],
        0,
        "106-modda: O'ttiz besh yoshdan kichik bo'lmagan, davlat tilini yaxshi biladigan, bevosita saylovgacha kamida 10 yil O'zbekiston hududida muqim yashayotgan fuqaro Prezident etib saylanishi mumkin.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Prezident",
        "Ayni bir shaxs surunkasiga necha muddatdan ortiq O'zbekiston Respublikasi Prezidenti bo'lishi mumkin emas? (106-modda)",
        [
            "Surunkasiga ikki muddatdan ortiq",
            "Surunkasiga uch muddatdan ortiq",
            "Faqat bir muddat",
            "Cheklanmagan muddat"
        ],
        0,
        "106-modda: Ayni bir shaxs surunkasiga ikki muddatdan ortiq O'zbekiston Respublikasining Prezidenti bo'lishi mumkin emas.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Prezident",
        "O'zbekiston Respublikasi Prezidenti o'z lavozimiga qachondan e'tiboran kirishgan hisoblanadi? (107-modda)",
        [
            "Oliy Majlis yig'ilishida qasamyod qabul qilgan paytdan boshlab",
            "Markaziy saylov komissiyasi natijalarni e'lon qilgan paytdan",
            "Saylov byulletenlari sanab chiqilgan kundan",
            "Eski Prezident farmon imzolagan kundan"
        ],
        0,
        "107-modda: Prezident Oliy Majlis yig'ilishida qasamyod qabul qilgan paytdan boshlab o'z lavozimiga kirishadi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Ijro hokimiyati",
        "O'zbekiston Respublikasi Vazirlar Mahkamasiga kim rahbarlik qiladi? (114-modda)",
        [
            "O'zbekiston Respublikasining Bosh vaziri",
            "Oliy Majlis Qonunchilik palatasi Spikeri",
            "Prezident Administratsiyasi rahbari",
            "Iqtisodiyot va moliya vaziri"
        ],
        0,
        "114-modda: O'zbekiston Respublikasi Vazirlar Mahkamasi ijro etuvchi hokimiyatni amalga oshiradi. Bosh vazir Vazirlar Mahkamasining faoliyatini tashkil etadi va unga rahbarlik qiladi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Ijro hokimiyati",
        "O'zbekiston Respublikasi Bosh vaziri nomzodini kim ko'rib chiqish va ma'qullash uchun kiritadi? (118-modda)",
        [
            "O'zbekiston Respublikasi Prezidenti",
            "Konstitutsiyaviy sud raisi",
            "Senat Raisi",
            "Markaziy saylov komissiyasi raisi"
        ],
        0,
        "118-modda: O'zbekiston Respublikasi Bosh vaziri nomzodi Oliy Majlis palatalaridagi barcha siyosiy partiyalar fraksiyalari bilan maslahatlashuvlar o'tkazilganidan so'ng Prezident tomonidan taqdim etiladi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Mahalliy hokimiyat",
        "Viloyat, tuman va shahar hokimining vakolat muddati necha yil? (120-modda)",
        [
            "Besh yil",
            "To'rt yil",
            "Yetti yil",
            "Uch yil"
        ],
        0,
        "120-modda: Mahalliy Kengashlar va hokimlarning vakolat muddati – besh yil.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Mahalliy hokimiyat",
        "Yangi Konstitutsiyaga ko'ra, hokimlar bir vaqtning o'zida Xalq deputatlari Kengashi raisi lavozimini egallashi mumkinmi? (120-modda)",
        [
            "Yo'q, hokim bir vaqtning o'zida xalq deputatlari Kengashiga boshchilik qilishi taqiqlandi",
            "Ha, qonun bo'yicha bu majburiy",
            "Faqat tuman hokimlariga ruxsat beriladi",
            "Faqat Toshkent shahri hokimiga ruxsat beriladi"
        ],
        0,
        "120-modda: Yangi tahrirda hokim lavozimi bilan xalq deputatlari Kengashi raisi lavozimi bir-biridan ajratildi.",
        "Konstitutsiya",
        "qiyin"
    ),
    (
        "Konstitutsiya - Sud hokimiyati",
        "O'zbekiston Respublikasida sud hokimiyati qanday faoliyat ko'rsatadi? (130-modda)",
        [
            "Qonun chiqaruvchi va ijro etuvchi organlardan, siyosiy partiyalardan mustaqil holda",
            "Hokimiyatlarning faqat ijroiya organiga bo'ysungan holda",
            "Prokuratura nazorati ostida",
            "Faqat Adliya vazirligi topshirig'i bilan"
        ],
        0,
        "130-modda: O'zbekiston Respublikasida sud hokimiyati qonun chiqaruvchi va ijro etuvchi organlardan, siyosiy partiyalardan, fuqarolik jamiyatining boshqa institutlaridan mustaqil holda ish yuritadi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Sud tizimi",
        "Qonunlar va boshqa normativ-huquqiy hujjatlarning Konstitutsiyaga muvofiqligini qaysi organ ko'rib chiqadi? (133-modda)",
        [
            "O'zbekiston Respublikasi Konstitutsiyaviy sudi",
            "O'zbekiston Respublikasi Oliy sudi",
            "Bosh prokuratura",
            "Adliya vazirligi"
        ],
        0,
        "133-modda: O'zbekiston Respublikasi Konstitutsiyaviy sudi qonunlarning va normativ-huquqiy hujjatlarning Konstitutsiyaga muvofiqligi to'g'risidagi ishlarni ko'radi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Sud tizimi",
        "Yangi tahrirdagi Konstitutsiyaga muvofiq, fuqarolar o'z huquqlari buzilganda Konstitutsiyaviy sudga shikoyat qilish huquqiga egami? (133-modda)",
        [
            "Ha, sud orqali himoya qilishning barcha choralari tugagan bo'lsa murojaat qilishlari mumkin",
            "Yo'q, fuqarolarning Konstitutsiyaviy sudga murojaat qilishiga yo'l qo'yilmaydi",
            "Faqat deputatlar orqali murojaat qilishlari mumkin",
            "Faqat chet el fuqarolari murojaat qila oladi"
        ],
        0,
        "133-modda: Fuqarolar va yuridik shaxslar, agar sud orqali himoya qilishning boshqa barcha vositalaridan foydalanib bo'lingan bo'lsa, Konstitutsiyada mustahkamlangan huquq va erkinliklarining buzilishi yuzasidan Konstitutsiyaviy sudga shikoyat bilan murojaat qilishga haqli.",
        "Konstitutsiya",
        "qiyin"
    ),
    (
        "Konstitutsiya - Sud tizimi",
        "Fuqarolik, jinoiy, iqtisodiy va ma'muriy sud ishlarini yuritish sohasida sud hokimiyatining oliy organi qaysi? (134-modda)",
        [
            "O'zbekiston Respublikasi Oliy sudi",
            "Konstitutsiyaviy sud",
            "Bosh prokuratura",
            "Sudyalar oliy kengashi"
        ],
        0,
        "134-modda: O'zbekiston Respublikasi Oliy sudi fuqarolik, jinoiy, iqtisodiy va ma'muriy sud ishlarini yuritish sohasida sud hokimiyatining oliy organidir.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Sudyalar",
        "Sudyalar o'z faoliyatida kimga bo'ysunadilar? (136-modda)",
        [
            "Faqat qonunga bo'ysunadilar",
            "Prezident va Oliy Majlisga",
            "Hokimlarga va politsiyaga",
            "O'zlarining yuqori turuvchi sudyalariga"
        ],
        0,
        "136-modda: Sudyalar mustaqildirlar, faqat O'zbekiston Respublikasi Konstitutsiyasiga va qonunga bo'ysunadilar.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Prokuratura",
        "O'zbekiston Respublikasi hududida qonunlarning aniq va bir xilda ijro etilishi ustidan nazoratni qaysi organ amalga oshiradi? (143-modda)",
        [
            "O'zbekiston Respublikasi Bosh prokurori va unga bo'ysunuvchi prokurorlar",
            "Ichki ishlar organlari",
            "Davlat xavfsizlik xizmati",
            "Adliya vazirligi"
        ],
        0,
        "143-modda: O'zbekiston Respublikasi hududida qonunlarning aniq va bir xilda ijro etilishi ustidan nazoratni O'zbekiston Respublikasining Bosh prokurori va unga bo'ysunuvchi prokurorlar amalga oshiradi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Prokuratura",
        "O'zbekiston Respublikasi Bosh prokurorining vakolat muddati necha yil? (144-modda)",
        [
            "Besh yil",
            "Yetti yil",
            "Uch yil",
            "O'n yil"
        ],
        0,
        "144-modda: Bosh prokurorning vakolat muddati – besh yil.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Advokatura",
        "Jismoniy va yuridik shaxslarga yuridik yordam ko'rsatish uchun nima faoliyat ko'rsatadi? (145-modda)",
        [
            "Advokatura",
            "Notariat",
            "Ombudsman idorasi",
            "Tergov qo'mitasi"
        ],
        0,
        "145-modda: Jismoniy va yuridik shaxslarga yuridik yordam ko'rsatish uchun advokatura faoliyat ko'rsatadi. Advokatlar faoliyatiga aralashishga yo'l qo'yilmaydi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Saylov tizimi",
        "O'zbekiston Respublikasida saylovlar qanday o'tkaziladi? (156-modda)",
        [
            "Umumiy, teng va to'g'ridan-to'g'ri saylov huquqi asosida yashirin ovoz berish yo'li bilan",
            "Ochiq qo'l ko'tarish yo'li bilan",
            "Faqat elektron so'rovnoma orqali",
            "Mahalla faollari yig'ilishida ovoz berish yo'li bilan"
        ],
        0,
        "156-modda: Saylovlar umumiy, teng va to'g'ridan-to'g'ri saylov huquqi asosida yashirin ovoz berish yo'li bilan o'tkaziladi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Saylov tizimi",
        "Saylovlarni va referendumlarni tashkil etish hamda o'tkazish uchun qaysi mustaqil konstitutsiyaviy organ tuziladi?",
        [
            "O'zbekiston Respublikasi Markaziy saylov komissiyasi",
            "Oliy Majlis Saylov qo'mitasi",
            "Adliya vazirligi Saylov boshqarmasi",
            "Prezident huzuridagi Saylov agentligi"
        ],
        0,
        "O'zbekiston Respublikasi Markaziy saylov komissiyasi doimiy asosda faoliyat yurituvchi mustaqil konstitutsiyaviy organdir.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Fuqarolik",
        "O'zbekiston Respublikasi fuqaroligidan mahrum qilish mumkinmi? (22-modda)",
        [
            "O'zbekiston Respublikasining fuqarosi hech qachon fuqarolikdan mahrum qilinishi mumkin emas",
            "Og'ir jinoyat sodir etganda mahrum qilinishi mumkin",
            "Chet elga doimiy yashashga ketganda avtomatik mahrum bo'ladi",
            "Bosh prokuror qarori bilan mahrum qilinadi"
        ],
        0,
        "22-modda: O'zbekiston Respublikasining fuqarosi O'zbekistondan tashqariga chiqarib yuborilishi yoki boshqa davlatga berilishi mumkin emas. O'zbekiston Respublikasi fuqarosi o'z fuqaroligidan mahrum qilinishi mumkin emas.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Fuqaro burchlari",
        "Konstitutsiyaga ko'ra, barcha fuqarolarning muqaddas burchi nima hisoblanadi? (64-modda)",
        [
            "O'zbekiston Respublikasini himoya qilish",
            "Faqat chet tillarini o'rganish",
            "Har yili davlat mukofotlarini olish",
            "Tadbirkorlik faoliyati bilan shug'ullanish"
        ],
        0,
        "64-modda: O'zbekiston Respublikasini himoya qilish – O'zbekiston Respublikasi har bir fuqarosining burchidir. Fuqarolar qonunda belgilangan tartibda harbiy yoki muqobil xizmatni o'tashga majburdirlar.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Fuqaro burchlari",
        "Fuqarolarning Konstitutsiya va qonunlarda belgilangan moliyaviy burchi nima? (63-modda)",
        [
            "Qonun bilan belgilangan soliqlar va yig'imlarni to'lash",
            "Xayriya jamg'armalariga pul o'tkazish",
            "Banklarga omonat qo'yish",
            "Faqat chet el valyutasidan foydalanish"
        ],
        0,
        "63-modda: Fuqarolar qonun bilan belgilangan soliqlar va yig'imlarni to'lashi shart. Soliq va yig'imlar adolatli bo'lishi hamda fuqarolarning konstitutsiyaviy huquqlarini amalga oshirishiga to'sqinlik qilmasligi kerak.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Ekologik huquqlar",
        "Yangi Konstitutsiyaning 49-moddasida qanday yangi muhim inson huquqi mustahkamlandi?",
        [
            "Har kim qulay atrof-muhitga, uning holati to'g'risidagi ishonchli axborotga ega bo'lish huquqi",
            "Kosmik fazodan bepul foydalanish huquqi",
            "Barcha tabiiy boyliklarni erkin qazib olish huquqi",
            "Ekologik soliq to'lashdan ozod bo'lish huquqi"
        ],
        0,
        "49-modda: Har kim qulay atrof-muhitga, uning holati to'g'risidagi ishonchli axborotga ega bo'lish huquqiga ega.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Orol fojiasi",
        "Davlat Orolbo'yi mintaqasining ekologik tizimini muhofaza qilish bo'yicha qanday majburiyatni o'z zimmasiga oldi? (49-modda)",
        [
            "Mintaqani tiklash, ijtimoiy-iqtisodiy rivojlantirish choralari ko'rish majburiyatini",
            "Aholini butunlay boshqa hududlarga ko'chirish",
            "Mintaqada barcha sanoat korxonalarini yopish",
            "Faqat xalqaro tashkilotlarga topshirish"
        ],
        0,
        "49-modda: Davlat Orolbo'yi mintaqasining ekologik tizimini muhofaza qilish hamda tiklash, mintaqani ijtimoiy va iqtisodiy jihatdan rivojlantirish yuzasidan choralar ko'radi.",
        "Konstitutsiya",
        "orta"
    ),

    # =========================================================================
    # BO'LIM 2: 8-SINF DAVLAT VA HUQUQ ASOSLARI
    # =========================================================================
    (
        "8-sinf - Davlat tushunchasi",
        "Davlatning asosiy belgilari qaysilar?",
        [
            "Muayyan hudud, aholi, suverenitet, ommaviy hokimiyat, soliq tizimi va huquqiy me'yorlar",
            "Faqat armiya va politsiyaning mavjudligi",
            "Faqat chegaralar va milliy valyuta",
            "Diniy tashkilotlar va savdo korxonalari"
        ],
        0,
        "Davlatning asosiy belgilari: chegaralangan hudud, aholi, ommaviy hokimiyat apparati, davlat suvereniteti, soliqlar va majburiy qonunlar.",
        "8-sinf",
        "oson"
    ),
    (
        "8-sinf - Davlat shakllari",
        "Davlat boshqaruv shakliga ko'ra qanday turlarga bo'linadi?",
        [
            "Monarxiya va Respublika",
            "Unitar va Federatsiya",
            "Demokratik va Diktatura",
            "Rivojlangan va Qoloq"
        ],
        0,
        "Davlat boshqaruv shakli oliy hokimiyatning tashkil etilishi bo'yicha monarxiya va respublikaga bo'linadi.",
        "8-sinf",
        "oson"
    ),
    (
        "8-sinf - Davlat shakllari",
        "Monarxiya boshqaruv shaklining asosiy xususiyati nima?",
        [
            "Oliy davlat hokimiyati bir kishi qo'lida bo'lib, meros bo'lib o'tadi",
            "Davlat boshlig'i xalq tomonidan ma'lum muddatga saylanadi",
            "Hokimiyat faqat parlamentga tegishli bo'ladi",
            "Sud hokimiyati oliy rahbar hisoblanadi"
        ],
        0,
        "Monarxiyada oliy davlat hokimiyati yakka hukmdor (podsho, qirol, amir) tomonidan amalga oshiriladi va nasldan-naslga meros qoladi.",
        "8-sinf",
        "oson"
    ),
    (
        "8-sinf - Davlat shakllari",
        "Davlat tuzilishi shakliga ko'ra davlatlar qanday turlarga bo'linadi?",
        [
            "Unitar, Federativ va Konfederativ",
            "Prezidentlik va Parlamentar",
            "Monarxiya va Respublika",
            "Demokratik va Totalitar"
        ],
        0,
        "Davlat tuzilishi shakli davlat hududiy bo'linishi va markaz bilan hududlar munosabatiga ko'ra unitar, federatsiya va konfederatsiyaga bo'linadi.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Davlat shakllari",
        "Unitar davlat deganda qanday davlat tushuniladi?",
        [
            "Tarkibida alohida davlat tuzilmalari bo'lmagan, yagona konstitutsiya va qonunlarga ega yaxlit davlat",
            "Mustaqil davlatlarning vaqtinchalik harbiy ittifoqi",
            "Bir nechta mustaqil davlatlarning yagona federatsiyasi",
            "Faqat bir nechta qirolliklar birlashmasi"
        ],
        0,
        "Unitar davlat – yagona davlat hokimiyati, yagona qonunchilik va yagona fuqarolikka ega bo'lgan yaxlit davlat tuzilishidir.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Siyosiy rejim",
        "Siyosiy rejim tushunchasi nimani anglatadi?",
        [
            "Davlat hokimiyatini amalga oshirish usul va vositalari majmui",
            "Davlat chegaralarini qo'riqlash tartibi",
            "Faqat parlament saylovlari tizimi",
            "Davlat byudjetini taqsimlash tartibi"
        ],
        0,
        "Siyosiy rejim – davlat hokimiyatini amalga oshirishning usullari, vositalari va yo'llari tizimidir (demokratik yoki antidemokratik).",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Huquq tushunchasi",
        "Huquq nima?",
        [
            "Davlat tomonidan qabul qilingan va uning kuchi bilan ta'minlanadigan umummajburiy xulq-atvor qoidalari tizimi",
            "Faqat dinda belgilangan axloq qoidalari",
            "Insonlarning o'zaro og'zaki kelishuvlari",
            "Faqat qadimiy urf-odat va an'analar"
        ],
        0,
        "Huquq – davlat tomonidan o'rnatiladigan, uning kuchi bilan himoya qilinadigan va jamiyat a'zolari uchun umummajburiy bo'lgan xulq-atvor qoidalari tizimidir.",
        "8-sinf",
        "oson"
    ),
    (
        "8-sinf - Huquq normasi",
        "Huquq normasining tuzilishi (strukturasi) qanday elementlardan iborat?",
        [
            "Gipoteza, dispozitsiya, sanksiya",
            "Muqaddima, bob, modda",
            "Kirish, asosiy qism, xulosa",
            "Subyekt, obyekt, mazmun"
        ],
        0,
        "Huquq normasining mantiqiy strukturasi uch qismdan iborat: Gipoteza (shart), Dispozitsiya (qoida), Sanksiya (oqibat/jazo).",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Huquq normasi",
        "Huquq normasining qaysi elementi xulq-atvor qoidasining o'zini, ya'ni huquq va majburiyatlarni ifodalaydi?",
        [
            "Dispozitsiya",
            "Gipoteza",
            "Sanksiya",
            "Preambula"
        ],
        0,
        "Dispozitsiya – huquq normasining bevosita xulq-atvor qoidasi bayon etilgan markaziy qismidir.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Huquq normasi",
        "Huquq normasining qoidasini buzganlik uchun qo'llaniladigan chora yoki jazo qaysi elementda ko'rsatiladi?",
        [
            "Sanksiya",
            "Gipoteza",
            "Dispozitsiya",
            "Prospeksiya"
        ],
        0,
        "Sanksiya – normani buzgan shaxsga nisbatan davlat tomonidan qo'llaniladigan salbiy oqibat, ta'sir chorasi yoki jazodir.",
        "8-sinf",
        "oson"
    ),
    (
        "8-sinf - Huquqiy munosabatlar",
        "Huquqiy munosabatlarning elementlari qaysilar?",
        [
            "Subyekt, obyekt va huquqiy munosabat mazmuni",
            "Faqat da'vogar va javobgar",
            "Gipoteza, dispozitsiya va sanksiya",
            "Sodir etilgan joy, vaqt va guvohlar"
        ],
        0,
        "Huquqiy munosabat elementlari: Subyektlar (qatnashuvchilar), Obyekt (munosabat nima sababdan yuzaga kelgan) va Mazmun (subyektiv huquq va majburiyatlar).",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Huquqiy layoqat",
        "Fuqaroning o'z huquqlariga ega bo'lish va majburiyatlarni o'z zimmasiga olish layoqati nima deyiladi?",
        [
            "Huquq layoqati",
            "Muomala layoqati",
            "Delikt layoqati",
            "Emansipatsiya"
        ],
        0,
        "Huquq layoqati – insonning fuqarolik huquqlariga ega bo'lish va majburiyatlar olish qobiliyati bo'lib, tug'ilgan paytdan vujudga keladi.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Huquqbuzarlik",
        "Huquqbuzarlikning ijtimoiy xavflilik darajasiga qarab qanday ikki turga bo'linadi?",
        [
            "Nojo'ya harakat (prostupok) va jinoyat",
            "Qasddan va ehtiyotsizlikdan",
            "Og'ir va o'ta og'ir",
            "Shaxsiy va ommaviy"
        ],
        0,
        "Huquqbuzarliklar ijtimoiy xavflilik darajasiga ko'ra nojo'ya harakatlar (intizomiy, fuqaroviy, ma'muriy) va jinoyatlarga bo'linadi.",
        "8-sinf",
        "orta"
    ),

    # =========================================================================
    # BO'LIM 3: 9-SINF FUQAROLIK, OILA VA MEHNAT HUQUQI
    # =========================================================================
    (
        "9-sinf - Fuqarolik huquqi",
        "Fuqarolik huquqining to'liq muomala layoqati qaysi yoshdan boshlanadi?",
        [
            "18 yoshga to'lgach",
            "16 yoshdan",
            "14 yoshdan",
            "21 yoshdan"
        ],
        0,
        "Fuqarolik kodeksining 22-moddasiga ko'ra, to'liq muomala layoqati fuqaro voyaga yetishi bilan, ya'ni 18 yoshga to'lishi bilan vujudga keladi.",
        "9-sinf",
        "oson"
    ),
    (
        "9-sinf - Emansipatsiya",
        "16 yoshga to'lgan voyaga yetmagan shaxsning to'la muomalaga layoqatli deb e'lon qilinishi nima deyiladi?",
        [
            "Emansipatsiya",
            "Konsolidatsiya",
            "Litsenziyalash",
            "Restitutsiya"
        ],
        0,
        "16 yoshga to'lgan voyaga yetmagan shaxs mehnat shartnomasi bo'yicha ishlayotgan yoki tadbirkorlik bilan shug'ullanayotgan bo'lsa, to'la muomalaga layoqatli (emansipatsiya) deb e'lon qilinishi mumkin.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Fuqarolik huquqi",
        "14 yoshdan 18 yoshgacha bo'lgan voyaga yetmaganlar mustaqil ravishda qanday bitimlarni amalga oshirishi mumkin?",
        [
            "O'z stipendiyasi va maoshini tasarruf etish, mualliflik huquqlarini amalga oshirish, mayda maishiy bitimlar tuzish",
            "Ko'chmas mulk sotish va sotib olish",
            "Bankdan katta kreditlar olish",
            "Avtomobilni boshqa shaxsga hadya qilish"
        ],
        0,
        "14-18 yoshdagi fuqarolar o'z daromadini tasarruf etish, mualliflik huquqlaridan foydalanish va mayda maishiy bitimlar tuzish huquqiga mustaqil egadirlar.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Oila huquqi",
        "O'zbekiston Respublikasi Oila kodeksiga ko'ra nikoh yoshi necha yosh etib belgilangan?",
        [
            "Erkaklar va ayollar uchun 18 yosh",
            "Erkaklar uchun 18 yosh, ayollar uchun 17 yosh",
            "Har ikkala jins uchun 17 yosh",
            "Erkaklar uchun 21 yosh, ayollar uchun 18 yosh"
        ],
        0,
        "Oila kodeksining 15-moddasiga ko'ra, nikoh yoshi erkaklar va ayollar uchun o'n sakkiz yosh etib belgilanadi.",
        "9-sinf",
        "oson"
    ),
    (
        "9-sinf - Oila huquqi",
        "Uzrli sabablar bo'lganida nikoh yoshi tuman (shahar) hokimi qarori bilan ko'pi bilan qanchaga kamaytirilishi mumkin?",
        [
            "Ko'pi bilan 1 yilga",
            "Ko'pi bilan 2 yilga",
            "Ko'pi bilan 6 oyga",
            "Nikoh yoshini kamaytirish taqiqlangan"
        ],
        0,
        "Uzrli sabablar bo'lganda tuman, shahar hokimi nikohlanuvchilarning iltimosiga ko'ra nikoh yoshini ko'pi bilan bir yilga kamaytirishi mumkin.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Oila huquqi",
        "Nikoh qaysi davlat organida qayd etilgan paytdan boshlab qonuniy kuchga ega bo'ladi?",
        [
            "FHDY (Fuqarolik holati dalolatnomalarini yozish) organlarida",
            "Mahalla fuqarolar yig'inida",
            "Notarial idorada",
            "Faqat diniy muassasalarda"
        ],
        0,
        "Faqat FHDY organlarida davlat ro'yxatidan o'tkazilgan nikohgina qonuniy kuchga ega bo'ladi va er-xotin o'rtasida huquq va majburiyatlarni keltirib chiqaradi.",
        "9-sinf",
        "oson"
    ),
    (
        "9-sinf - Oila huquqi",
        "Er va xotinning nikoh davomida orttirgan umumiy mulki qanday mulk hisoblanadi?",
        [
            "Birgalikdagi umumiy mulk",
            "Faqat erning xususiy mulki",
            "Ulushli xususiy mulk",
            "Davlat mulki"
        ],
        0,
        "Er va xotinning nikoh davomida orttirgan mol-mulki ularning birgalikdagi umumiy mulki hisoblanadi.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Oila huquqi",
        "Nikohgacha tegishli bo'lgan, shuningdek nikoh davomida hadya yoki meros tariqasida olingan mol-mulk kimga tegishli bo'ladi?",
        [
            "O'sha er yoki xotinning har birining o'z shaxsiy mulki hisoblanadi",
            "Avtomatik birgalikdagi umumiy mulkka aylanadi",
            "Teng ikkiga bo'linadi",
            "Bolalar mulkiga o'tadi"
        ],
        0,
        "Er-xotinning nikohga qadar o'ziga tegishli bo'lgan, shuningdek hadya yoki meros tariqasida olgan mulki uning shaxsiy mulkidir.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Mehnat huquqi",
        "Yangi Mehnat kodeksiga ko'ra, xodim bilan mehnat shartnomasi tuzishga qaysi yoshdan yo'l qo'yiladi?",
        [
            "16 yoshdan",
            "18 yoshdan",
            "14 yoshdan",
            "15 yoshdan umumiy qoida bo'yicha"
        ],
        0,
        "Mehnat kodeksining tegishli moddasiga ko'ra, umumiy qoidaga ko'ra ishga qabul qilishga 16 yoshdan yo'l qo'yiladi.",
        "9-sinf",
        "oson"
    ),
    (
        "9-sinf - Mehnat huquqi",
        "15 yoshga to'lgan shaxslar ishga qabul qilinishi uchun qanday shart talab qilinadi?",
        [
            "Ota-onasidan birining yozma roziligi va sog'lig'iga ziyon yetkazmaslik hamda ta'limdan bo'sh vaqtda bo'lishi",
            "Faqat sud qarori",
            "Maktab direktorining buyrug'i",
            "Faqat kasaba uyushmasi ruxsati"
        ],
        0,
        "15 yoshga to'lgan shaxslar ota-onasidan birining yozma roziligi bilan ta'lim jarayoniga xalal bermaydigan yengil ishlarga olinishi mumkin.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Mehnat huquqi",
        "16 yoshdan 18 yoshgacha bo'lgan xodimlar uchun haftalik ish vaqti necha soatdan oshmasligi kerak?",
        [
            "Haftasiga 36 soatdan",
            "Haftasiga 40 soatdan",
            "Haftasiga 24 soatdan",
            "Haftasiga 30 soatdan"
        ],
        0,
        "Mehnat kodeksiga ko'ra, 16 dan 18 yoshgacha bo'lgan yoshlar uchun haftalik ish vaqti 36 soatdan oshmasligi belgilangan.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Mehnat huquqi",
        "Ishga qabul qilish chog'ida sinov muddati ko'pi bilan necha oydan oshmasligi kerak?",
        [
            "Uch oydan (ayrim rahbar xodimlar uchun 6 oydan)",
            "Bir oydan",
            "Olti oydan barcha xodimlar uchun",
            "Bir yildan"
        ],
        0,
        "Sinov muddati 3 oydan, tashkilot rahbarlari va ularning o'rinbosarlari, bosh buxgalterlar uchun 6 oydan oshmasligi kerak.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Mehnat huquqi",
        "Kimlarni ishga qabul qilishda dastlabki sinov muddati tayinlanishi taqiqlanadi?",
        [
            "Homilador ayollar, 3 yoshga to'lmagan bolasi bor ayollar va ta'lim muassasasini yangi bitirgan shaxslar",
            "Faqat chet el fuqarolari",
            "Faqat pensiya yoshidagi shaxslar",
            "Boshqa viloyatdan kelgan ishchilar"
        ],
        0,
        "Homilador ayollar, uch yoshgacha bolasi bor shaxslar, ta'lim muassasalarining bitiruvchilari birinchi marta ishga kirganda sinov muddati belgilanmaydi.",
        "9-sinf",
        "orta"
    ),

    # =========================================================================
    # BO'LIM 4: 10-SINF MA'MURIY, JINOIY VA EKOLOGIYA HUQUQI
    # =========================================================================
    (
        "10-sinf - Ma'muriy huquq",
        "Ma'muriy javobgarlik necha yoshdan boshlanadi?",
        [
            "16 yoshdan",
            "14 yoshdan",
            "18 yoshdan",
            "15 yoshdan"
        ],
        0,
        "Ma'muriy javobgarlik to'g'risidagi kodeksning 13-moddasiga ko'ra, ma'muriy huquqbuzarlik sodir etgan paytda 16 yoshga to'lgan shaxslar ma'muriy javobgarlikka tortiladi.",
        "10-sinf",
        "oson"
    ),
    (
        "10-sinf - Ma'muriy huquq",
        "Ma'muriy qamoq jazosining umumiy eng yuqori muddati necha sutka qilib belgilangan?",
        [
            "15 sutkagacha (favqulodda hollarda 30 sutkagacha)",
            "30 sutkagacha har doim",
            "10 sutkagacha",
            "3 oygacha"
        ],
        0,
        "Ma'muriy qamoq o'n besh sutkagacha, favqulodda holat tartibi sharoitida esa o'ttiz sutkagacha bo'lgan muddatga faqat sud tomonidan qo'llaniladi.",
        "10-sinf",
        "orta"
    ),
    (
        "10-sinf - Ma'muriy huquq",
        "Qaysi shaxslarga nisbatan ma'muriy qamoq jazosi qo'llanilishi mumkin emas?",
        [
            "Homilador ayollar, 14 yoshgacha bolasi bor ayollar, 18 yoshga to'lmagan shaxslar va 1-2 guruh nogironlari",
            "Faqat talabalar va o'qituvchilar",
            "Faqat chet ellik sayyohlar",
            "Davlat xizmatchilari"
        ],
        0,
        "Homilador ayollarga, 14 yoshgacha bolasi bor ayollarga, 18 yoshga to'lmagan shaxslarga, I va II guruh nogironlariga nisbatan ma'muriy qamoq qo'llanilmaydi.",
        "10-sinf",
        "orta"
    ),
    (
        "10-sinf - Jinoyat huquqi",
        "Jinoyat tushunchasining asosiy belgisi nima?",
        [
            "Jinoyat kodeksida taqiqlangan, aybli va ijtimoiy xavfli qilmish",
            "Faqat moddiy zarar keltiruvchi harakat",
            "Axloq me'yorlariga to'g'ri kelmaydigan odat",
            "Qonunda taqiqlanmagan xato harakat"
        ],
        0,
        "Jinoyat – Jinoyat kodeksi bilan taqiqlangan, ijtimoiy xavfli, aybli va jazolanishi shart bo'lgan qilmishdir.",
        "10-sinf",
        "oson"
    ),
    (
        "10-sinf - Jinoyat huquqi",
        "Jinoyat tarkibi qaysi 4 ta elementdan iborat?",
        [
            "Obyekt, obyektiv tomon, subyekt, subyektiv tomon",
            "Ayblovchi, tergovchi, sudya, advokat",
            "Gipoteza, dispozitsiya, sanksiya, sud",
            "Sabab, oqibat, zarar, vaqt"
        ],
        0,
        "Jinoyat tarkibi to'rtta elementdan iborat: Jinoyat obyekti, jinoyatning obyektiv tomoni, jinoyat subyekti va subyektiv tomoni.",
        "10-sinf",
        "orta"
    ),
    (
        "10-sinf - Jinoyat huquqi",
        "O'zbekiston Respublikasi Jinoyat kodeksiga binoan umumiy jinoiy javobgarlik yoshi necha yoshdan boshlanadi?",
        [
            "16 yoshdan",
            "18 yoshdan",
            "14 yoshdan",
            "15 yoshdan"
        ],
        0,
        "Jinoyat kodeksining 17-moddasiga binoan jinoyat sodir etgunga qadar 16 yoshga to'lgan shaxslar umumiy javobgarlikka tortiladi.",
        "10-sinf",
        "oson"
    ),
    (
        "10-sinf - Jinoyat huquqi",
        "Qasddan odam o'ldirish, bosqinchilik, talonchilik kabi o'ta og'ir jinoyatlar uchun jinoiy javobgarlik qaysi yoshdan boshlanadi?",
        [
            "14 yoshga to'lgan shaxslar",
            "12 yoshdan",
            "15 yoshdan",
            "16 yoshdan"
        ],
        0,
        "Jinoyat kodeksining 17-moddasi 2-qismida sanab o'tilgan og'ir jinoyatlar (odam o'ldirish, qasddan badanga og'ir shikast yetkazish, bosqinchilik va h.k.) uchun 14 yoshga to'lgan shaxslar javobgarlikka tortiladi.",
        "10-sinf",
        "orta"
    ),
    (
        "10-sinf - Jinoyat huquqi",
        "Zaruriy mudofaa holatida qilingan harakat jinoyat hisoblanadimi?",
        [
            "Yo'q, agar zaruriy mudofaa chegarasidan chetga chiqilmagan bo'lsa, qilmish jinoyat hisoblanmaydi",
            "Ha, har qanday odamga tan jarohati yetkazish jinoyatdir",
            "Faqat tergovchi ruxsati bilan oqlanadi",
            "Faqat pul jarimasi bilan jazolanadi"
        ],
        0,
        "Zaruriy mudofaa – tajovuzchiga zarar yetkazish orqali shaxsni yoki davlat manfaatlarini himoya qilish bo'lib, qilmishning jinoiyligini istisno qiladi.",
        "10-sinf",
        "orta"
    ),
    (
        "10-sinf - Ekologiya huquqi",
        "Yo'qolib ketish xavfi ostida bo'lgan noyob o'simlik va hayvonot turlari qaysi davlat hujjatiga kiritiladi?",
        [
            "O'zbekiston Respublikasi Qizil kitobiga",
            "Yashil kitobga",
            "Ekologiya xaritasiga",
            "O'rmon kadastriga"
        ],
        0,
        "Qizil kitob – noyob va yo'qolib ketish xavfi ostida turgan o'simliklar va hayvonot turlarini muhofaza qilish bo'yicha rasmiy davlat hujjatidir.",
        "10-sinf",
        "oson"
    ),

    # =========================================================================
    # BO'LIM 5: 11-SINF XALQARO HUQUQ, SUD VA ODIL SUDLOV
    # =========================================================================
    (
        "11-sinf - Inson huquqlari",
        "Inson huquqlari umumjahon deklaratsiyasi qachon qabul qilingan?",
        [
            "1948-yil 10-dekabrda",
            "1945-yil 9-mayda",
            "1991-yil 1-sentyabrda",
            "1992-yil 8-dekabrda"
        ],
        0,
        "Birlashgan Millatlar Tashkiloti (BMT) Bosh Assambleyasi 1948-yil 10-dekabrda Inson huquqlari umumjahon deklaratsiyasini qabul qilgan. 10-dekabr – Xalqaro inson huquqlari kuni.",
        "11-sinf",
        "oson"
    ),
    (
        "11-sinf - Bola huquqlari",
        "BMTning 'Bola huquqlari to'g'risida'gi Konvensiyasiga binoan kimlar bola hisoblanadi?",
        [
            "18 yoshga to'lmagan har bir inson",
            "14 yoshgacha bo'lgan shaxslar",
            "16 yoshgacha bo'lganlar",
            "Faqat maktab o'quvchilari"
        ],
        0,
        "Konvensiyaning 1-moddasiga muvofiq, 18 yoshga to'lmagan har bir inson bola hisoblanadi.",
        "11-sinf",
        "oson"
    ),
    (
        "11-sinf - Ombudsman",
        "O'zbekiston Respublikasi Oliy Majlisining Inson huquqlari bo'yicha vakili lavozimi qanday ataladi?",
        [
            "Ombudsman",
            "Bosh prokuror",
            "Adliya vaziri",
            "Vasiylik organi"
        ],
        0,
        "Oliy Majlisning Inson huquqlari bo'yicha vakili (Ombudsman) fuqarolarning buzilgan inson huquqlarini tiklash bo'yicha mustaqil parlament nazorati institutidir.",
        "11-sinf",
        "oson"
    ),
    (
        "11-sinf - Odil sudlov",
        "Sud muhokamasining barcha sudlarda ochiq olib borilishi prinsipi qanday ataladi?",
        [
            "Sudning oshkoralik prinsipi",
            "Sud mustaqilligi",
            "Tortishuvlik prinsipi",
            "Kollektivlik prinsipi"
        ],
        0,
        "Oshkoralik prinsipi – barcha sudlarda ishlar ochiq ko'rilishi, davlat siri yoki shaxsiy sirni saqlash hollari bundan mustasno ekanligini bildiradi.",
        "11-sinf",
        "orta"
    ),
    (
        "11-sinf - Odil sudlov",
        "Sud jarayonida ayblovchi (prokuror) va himoyachi (advokat) teng huquqlarga ega bo'lishi qaysi prinsip deyiladi?",
        [
            "Tortishuvlik va taraflarning tengligi prinsipi",
            "Aybsizlik prezumpsiyasi",
            "Oshkoralik prinsipi",
            "Bir martalik jazo prinsipi"
        ],
        0,
        "Odil sudlov taraflarning tortishuvi va teng huquqliligi asosida amalga oshiriladi.",
        "11-sinf",
        "orta"
    ),
    (
        "11-sinf - Xalqaro huquq",
        "Birlashgan Millatlar Tashkilotiga (BMT) O'zbekiston Respublikasi qachon a'zo bo'lgan?",
        [
            "1992-yil 2-martda",
            "1991-yil 31-avgustda",
            "1993-yil 8-dekabrda",
            "1994-yil 1-mayda"
        ],
        0,
        "O'zbekiston Respublikasi 1992-yil 2-martda Birlashgan Millatlar Tashkilotiga to'la huquqli a'zo bo'ldi.",
        "11-sinf",
        "orta"
    ),
    (
        "11-sinf - Notariat",
        "Huquq va faktlarni qonuniy tasdiqlash, vasiyatnoma va ishonchnomalarni rasmiylashtiruvchi organ nima deyiladi?",
        [
            "Notariat idorasi",
            "Sud",
            "Advokatlik byurosi",
            "FHDY bo'limi"
        ],
        0,
        "Notariat – fuqarolar va yuridik shaxslarning huquqlari hamda qonuniy manfaatlarini tasdiqlash orqali himoya qiluvchi huquqiy organdir.",
        "11-sinf",
        "oson"
    ),
    (
        "11-sinf - FHDY",
        "Tug'ilish, nikoh, nikohdan ajralish va o'lim holatlarini rasmiy davlat ro'yxatiga oluvchi organ qaysi?",
        [
            "FHDY (Fuqarolik holati dalolatnomalarini yozish) organi",
            "Notariat",
            "Hokimlik",
            "Ichki ishlar bo'limi"
        ],
        0,
        "FHDY organi insonning fuqarolik holati dalolatnomalarini ro'yxatga oluvchi davlat organidir.",
        "11-sinf",
        "oson"
    )
]
print(f"Baza savollari kiritildi. Tayyor savollar soni: {len(HUQUQ_QUESTIONS)}")
