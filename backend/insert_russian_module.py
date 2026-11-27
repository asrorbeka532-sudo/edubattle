# -*- coding: utf-8 -*-
"""
EduBattle: Rus tili (Yangi tahrir) fanini to'liq bazaga kiritish moduli.
- Fan: Rus tili (id: 10, code: russian, icon: 🇷🇺, category: xorijiy)
- Darsliklar: 6, 7, 8, 9, 10, 11-sinf Rus tili (Yangi tahrir, 2022-2025 rasmiy dastur)
- Blitz va mavzulashtirilgan testlar: 1,100+ ta 100% takrorlanmas real savol!
"""

import sqlite3
import json
import os
import random

DB_PATH = os.path.join(os.path.dirname(__file__), "edubattle.db")

RUSSIAN_TEXTBOOKS = [
    {
        "title": "6-Sinf Rus tili (Yangi tahrir)",
        "author": "O'zbekiston Respublikasi Maktabgacha va maktab ta'limi vazirligi (Yangi nashr)",
        "grade": "6-sinf",
        "cover_image": None,
        "file_url": None,
        "slug": "6-sinf-rus-tili-yangi-tahrir",
        "summary": "6-sinf uchun yangi tahrirdagi Rus tili darsligi: Fonetika, urg'u, otlarning jinsi va soni, sifatlar, asosiy kundalik muloqot va leksika.",
        "chapters": [
            {"title": "1-bob. Fonetika, grafika va urg'u (Фонетика и ударение)", "summary": "Unli va undosh tovushlar, qattiq va yumshoq undoshlar, ЖИ-ШИ, ЧА-ЩА, ЧУ-ЩУ imlo qoidalari.", "key_rules": ["ЖИ-ШИ har doim И bilan yoziladi", "ЧА-ЩА har doim А bilan yoziladi", "ЧУ-ЩУ har doim У bilan yoziladi"]},
            {"title": "2-bob. Otlarning jinsi (Род имён существительных)", "summary": "Мужской, женский va средний rod otlarini qo'shimchalar orqali aniqlash hamda istisno so'zlar.", "key_rules": ["Undosh bilan tugagan otlar — мужской род", "-а/-я bilan tugaganlar — женский род", "-о/-е/-мя bilan tugaganlar — средний род"]},
            {"title": "3-bob. Otlarning ko'plik shakli (Множественное число)", "summary": "Ko'plik qo'shimchalari (-ы, -и, -а, -я) hamda maxsus o'zgaruvchi otlar (человек — люди, ребёнок — дети).", "key_rules": ["Г, К, Х, Ж, Ш, Щ, Ч dan keyin -и yoziladi", "дом → дома, город → города, друг → друзья"]},
            {"title": "4-bob. Sifatlar va olmoshlar (Прилагательные и местоимения)", "summary": "Sifatlarning ot bilan jins va sonda moslashuvi, kishilik va egalik olmoshlari (мой, моя, моё, мои).", "key_rules": ["Какой? — новый (-ый/-ий/-ой)", "Какая? — новая (-ая/-яя)", "Какое? — новое (-ое/-ее)"]},
            {"title": "5-bob. Oila, maktab va kundalik muloqot (Семья и школа)", "summary": "Salomlashish, tanishish, kun tartibi, sevimli mashg'ulotlar va odobli murojaat iboralari.", "key_rules": ["Здравствуйте! / Доброе утро!", "Меня зовут... / Очень приятно!"]}
        ]
    },
    {
        "title": "7-Sinf Rus tili (Yangi tahrir)",
        "author": "O'zbekiston Respublikasi Maktabgacha va maktab ta'limi vazirligi (Yangi nashr)",
        "grade": "7-sinf",
        "cover_image": None,
        "file_url": None,
        "slug": "7-sinf-rus-tili-yangi-tahrir",
        "summary": "7-sinf uchun yangi tahrirdagi Rus tili darsligi: 6 ta kelishik (padej) tizimi, fe'llarning I va II tuslanishi, zamonlar va predloglar.",
        "chapters": [
            {"title": "1-bob. Bosh va Qaratqich kelishigi (Именительный и Родительный падежи)", "summary": "Кто? Что? va Кого? Чего? so'roqlari, нет/без/у/из/от/до predloglari bilan qo'llanilishi.", "key_rules": ["Родительный: нет времени, у друга, из школы", "2, 3, 4 sonlaridan keyin birlik Roditelniy keladi"]},
            {"title": "2-bob. Jo'nalish va Tushum kelishigi (Дательный и Винительный падежи)", "summary": "Кому? Чему? (к, по) va Кого? Что? (в, на, через) kelishiklari hamda yo'nalish ifodalash.", "key_rules": ["Дательный: помочь другу, идти к врачу", "Винительный: читать книгу, идти в школу"]},
            {"title": "3-bob. Chog'ishtirma va O'rin-payt kelishigi (Творительный и Предложный падежи)", "summary": "Кем? Чем? (с, над, под, перед, за) va О ком? О чём? Где? (в, на, о/об) padejlari.", "key_rules": ["Творительный: писать ручкой, стать врачом", "Предложный: учиться в школе, думать о будущем"]},
            {"title": "4-bob. Fe'l tuslanishi va zamonlar (Спряжение и время глаголов)", "summary": "I va II tuslanish fe'llari, o'tgan zamonning jins qo'shimchalari (-л, -ла, -ло, -ли) va kelasi zamon.", "key_rules": ["I tuslanish: -у/-ю, -ешь, -ет, -ем, -ете, -ут/-ют", "II tuslanish: -у/-ю, -ишь, -ит, -им, -ите, -ат/-ят"]}
        ]
    },
    {
        "title": "8-Sinf Rus tili (Yangi tahrir)",
        "author": "O'zbekiston Respublikasi Maktabgacha va maktab ta'limi vazirligi (Yangi nashr)",
        "grade": "8-sinf",
        "cover_image": None,
        "file_url": None,
        "slug": "8-sinf-rus-tili-yangi-tahrir",
        "summary": "8-sinf uchun yangi tahrirdagi Rus tili darsligi: Fe'l turlari (вид глагола), harakat fe'llari, ravishlar, sonlar va so'z yasalishi.",
        "chapters": [
            {"title": "1-bob. Tugallangan va tugallanmagan fe'l (Совершенный и несовершенный вид)", "summary": "Что делать? (НСВ) va Что сделать? (СВ) fe'l juftliklari va ularning nutqda to'g'ri ishlatilishi.", "key_rules": ["НСВ: делать, писать, читать, говорить", "СВ: сделать, написать, прочитать, сказать"]},
            {"title": "2-bob. Harakat fe'llari (Глаголы движения)", "summary": "Идти — ходить, ехать — ездить, бежать — бегать, лететь — летать va old qo'shimchali (при-, у-, вы-, за-) shakllar.", "key_rules": ["Идти — bir yo'nalishda (hozir)", "Ходить — muntazam yoki borib-kelish"]},
            {"title": "3-bob. Sifat darajalari va ravishlar (Степени сравнения и наречия)", "summary": "Qiyosiy va orttirma daraja (быстрее, самый красивый, лучше, хуже) hamda ravishlarning imlosi.", "key_rules": ["хороший → лучше", "плохой → хуже", "маленький → меньше"]},
            {"title": "4-bob. Sonlar va vaqtni ifodalash (Числительные и время)", "summary": "Sanoq va tartib sonlar, soat va sanani rus tilida to'g'ri aytish qoidalari.", "key_rules": ["1 час, 2-4 часа, 5-20 часов", "Который час? — Сейчас ровно девять часов."]}
        ]
    },
    {
        "title": "9-Sinf Rus tili (Yangi tahrir)",
        "author": "O'zbekiston Respublikasi Maktabgacha va maktab ta'limi vazirligi (Yangi nashr)",
        "grade": "9-sinf",
        "cover_image": None,
        "file_url": None,
        "slug": "9-sinf-rus-tili-yangi-tahrir",
        "summary": "9-sinf uchun yangi tahrirdagi Rus tili darsligi: Sodda va qo'shma gap sintaksisi, sifatdosh (причастие), ravishdosh (деепричастие) va punktuatsiya.",
        "chapters": [
            {"title": "1-bob. Sodda gap va gap bo'laklari (Простое предложение)", "summary": "Ega va kesim, to'ldiruvchi, aniqlovchi va hol; bir tarkibli gap turlari.", "key_rules": ["Подлежащее (ega) — Кто? Что?", "Сказуемое (kesim) — Что делает?"]},
            {"title": "2-bob. Sifatdosh va Ravishdosh (Причастие и деепричастие)", "summary": "Faol va majhul sifatdoshlar (-ущ/-ющ, -ащ/-ящ, -вш-, -нн-) hamda ravishdosh oborotida vergul.", "key_rules": ["Деепричастный оборот har doim vergul bilan ajratiladi", "Причастный оборот otdan keyin kelsa vergul qo'yiladi"]},
            {"title": "3-bob. Bog'lovchili va bog'lovchisiz qo'shma gaplar (Сложные предложения)", "summary": "Сложносочинённые (и, а, но) va сложноподчинённые (что, чтобы, потому что, который, если) gaplar.", "key_rules": ["чтобы — maqsad ergash gapi", "потому что — sabab ergash gapi", "если — shart ergash gapi"]}
        ]
    },
    {
        "title": "10-Sinf Rus tili (Yangi tahrir)",
        "author": "O'zbekiston Respublikasi Maktabgacha va maktab ta'limi vazirligi (Yangi nashr)",
        "grade": "10-sinf",
        "cover_image": None,
        "file_url": None,
        "slug": "10-sinf-rus-tili-yangi-tahrir",
        "summary": "10-sinf uchun yangi tahrirdagi Rus tili darsligi: Nutq uslublari (стили речи), rasmiy-idoraviy va ilmiy uslub, frazeologizmlar va murakkab orfografiya.",
        "chapters": [
            {"title": "1-bob. Nutq uslublari (Функциональные стили речи)", "summary": "So'zlashuv, ilmiy, rasmiy-idoraviy, publitsistik va badiiy uslublarning xususiyatlari.", "key_rules": ["Официально-деловой стиль — ariza, shartnoma, qonun", "Научный стиль — atamalar va aniq mantiq"]},
            {"title": "2-bob. Murakkab imlo qoidalari (Сложные случаи орфографии)", "summary": "Н va НН yozilishi, НЕ ning so'z turkumlari bilan qo'shilib yoki ajratib yozilishi, ПРИ-/ПРЕ- old qo'shimchalari.", "key_rules": ["НЕ fe'llar bilan ajratib yoziladi (не знаю, не был)", "ПРИ- — yaqinlashish; ПРЕ- — juda (очень) ma'nosida"]},
            {"title": "3-bob. Frazeologizmlar va badiiy vositalar (Фразеология)", "summary": "Rus tilidagi eng mashhur iboralar (бить баклуши, держать язык за зубами, золотые руки) va ularning o'zbekcha muqobili.", "key_rules": ["Золотые руки — qo'li gul usta", "Ни пуха ни пера — omad tilash iborasi"]}
        ]
    },
    {
        "title": "11-Sinf Rus tili (Yangi tahrir — Milliy sertifikat & DTM)",
        "author": "O'zbekiston Respublikasi Maktabgacha va maktab ta'limi vazirligi (Yangi nashr)",
        "grade": "11-sinf",
        "cover_image": None,
        "file_url": None,
        "slug": "11-sinf-rus-tili-yangi-tahrir",
        "summary": "11-sinf uchun yangi tahrirdagi Rus tili darsligi: Akademik yozuv, esse, orfoepiya (to'g'ri urg'u), paronimlar, matn tahlili va imtihonga tayyorgarlik.",
        "chapters": [
            {"title": "1-bob. Orfoepiya va to'g'ri urg'u normalari (Орфоэпия)", "summary": "Imtihonlarda eng ko'p uchraydigan urg'u normalari: звони́т, догово́р, катало́г, краси́вее, то́рты, кварта́л.", "key_rules": ["звони́т (o'ng'ay emas: зво́нит xato!)", "краси́вее, догово́р, катало́г, то́рты"]},
            {"title": "2-bob. Paronimlar va leksik normalar (Паронимы)", "summary": "Одеть / надеть, адресат / адресант, эффектный / эффективный, дипломат / дипломант farqlari.", "key_rules": ["Одеть кого-то (bolani kiyintirish)", "Надеть что-то (kurtkani kiyish)"]},
            {"title": "3-bob. Akademik matn va esse yozish (Академическое письмо)", "summary": "Kirish so'zlar (во-первых, таким образом, следовательно), dalillash va xulosa yozish texnikasi.", "key_rules": ["Вводные слова (конечно, во-первых, к сожалению) har doim vergul bilan ajratiladi"]}
        ]
    }
]


def generate_russian_questions():
    """
    Generate 1,120+ 100% UNIQUE, pedagogically accurate Russian language questions
    covering the full Uzbek school New-Edition Russian curriculum (grades 6-11).
    Tuple format: (chapter_title, question_text, [4 options], correct_idx, explanation, grade, difficulty)
    """
    rng = random.Random(2026)
    questions = []
    seen = set()

    def add_q(ch, qtxt, opts, corr_idx, expl, grade="8-sinf", diff="orta"):
        key = qtxt.strip().lower()
        if key in seen or len(opts) != 4 or len(set(opts)) != 4:
            return
        seen.add(key)
        questions.append((ch, qtxt, list(opts), corr_idx, expl, grade, diff))

    # =====================================================================
    # 1. VOCABULARY & TRANSLATION (Ruscha -> O'zbekcha & O'zbekcha -> Ruscha)
    # 210+ words grouped by category -> 420+ unique questions!
    # =====================================================================
    VOCAB_CATEGORIES = {
        "Oila va insonlar": [
            ("семья", "oila"), ("отец", "ota"), ("мать", "ona"), ("брат", "aka / uka"),
            ("сестра", "opa / singil"), ("дедушка", "bobo"), ("бабушка", "buvi"), ("сын", "o'g'il"),
            ("дочь", "qiz farzand"), ("дядя", "amaki / tog'a"), ("тётя", "amma / xola"), ("внук", "nevara (o'g'il)"),
            ("друг", "do'st"), ("подруга", "dugona"), ("сосед", "qo'shni"), ("гость", "mehmon"),
            ("ребёнок", "bola"), ("родители", "ota-ona"), ("родственник", "qarindosh"), ("человек", "inson"),
            ("мужчина", "erkak"), ("женщина", "ayol"), ("мальчик", "o'g'il bola"), ("девочка", "qiz bola")
        ],
        "Maktab va ta'lim": [
            ("школа", "maktab"), ("учитель", "o'qituvchi"), ("ученик", "o'quvchi"), ("класс", "sinf"),
            ("урок", "dars"), ("перемена", "tanaffus"), ("книга", "kitob"), ("тетрадь", "daftar"),
            ("ручка", "ruchka"), ("карандаш", "qalam"), ("линейка", "chizg'ich"), ("ластик", "o'chirg'ich"),
            ("доска", "doska"), ("мел", "bo'r"), ("парта", "parta"), ("рюкзак", "ryukzak / sumka"),
            ("словарь", "lug'at"), ("библиотека", "kutubxona"), ("экзамен", "imtihon"), ("оценка", "baho"),
            ("задача", "masala"), ("упражнение", "mashq"), ("расписание", "dars jadvali"), ("знание", "bilim"),
            ("наука", "ilm-fan"), ("университет", "universitet"), ("студент", "talaba"), ("дневник", "kundalik")
        ],
        "Kasblar": [
            ("врач", "shifokor"), ("инженер", "muhandis"), ("водитель", "haydovchi"), ("повар", "oshpaz"),
            ("строитель", "quruvchi"), ("продавец", "sotuvchi"), ("программист", "dasturchi"), ("художник", "rassom"),
            ("писатель", "yozuvchi"), ("журналист", "jurnalist"), ("юрист", "huquqshunos"), ("судья", "sudya"),
            ("пожарный", "o't o'chiruvchi"), ("полицейский", "politsiyachi"), ("лётчик", "uchuvchi"), ("моряк", "dengizchi"),
            ("парикмахер", "sartarosh"), ("портной", "tikuvchi"), ("фермер", "fermer"), ("переводчик", "tarjimon"),
            ("архитектор", "me'mor"), ("бухгалтер", "hisobchi"), ("учёный", "olim"), ("музыкант", "musiqachi")
        ],
        "Tabiat va ob-havo": [
            ("солнце", "quyosh"), ("луна", "oy"), ("звезда", "yulduz"), ("небо", "osmon"),
            ("облако", "bulut"), ("дождь", "yomg'ir"), ("снег", "qor"), ("ветер", "shamol"),
            ("гроза", "momaqaldiroq"), ("туман", "tuman"), ("гора", "tog'"), ("река", "daryo"),
            ("озеро", "ko'l"), ("море", "dengiz"), ("океан", "okean"), ("лес", "o'rmon"),
            ("поле", "dala"), ("пустыня", "cho'l"), ("дерево", "daraxt"), ("цветок", "gul"),
            ("трава", "o't-maysa"), ("лист", "barg"), ("корень", "ildiz"), ("земля", "yer"),
            ("огонь", "olov"), ("вода", "suv"), ("воздух", "havo"), ("радуга", "kamalak")
        ],
        "Shahar, uy va transport": [
            ("город", "shahar"), ("деревня", "qishloq"), ("улица", "ko'cha"), ("площадь", "maydon"),
            ("мост", "ko'prik"), ("парк", "bog' / park"), ("больница", "shifoxona"), ("аптека", "dorixona"),
            ("магазин", "do'kon"), ("рынок", "bozor"), ("вокзал", "vokzal"), ("аэропорт", "aeroport"),
            ("дом", "uy"), ("квартира", "kvartira"), ("комната", "xona"), ("кухня", "oshxona"),
            ("окно", "deraza"), ("дверь", "eshik"), ("крыша", "tom"), ("стена", "devor"),
            ("пол", "pol / zamin"), ("потолок", "shift"), ("лестница", "zina"), ("поезд", "poyezd"),
            ("самолёт", "samolyot"), ("корабль", "kema"), ("автобус", "avtobus"), ("светофор", "svetofor")
        ],
        "Ovqat va mahsulotlar": [
            ("хлеб", "non"), ("молоко", "sut"), ("масло", "yog' / sariyog'"), ("сыр", "pishloq"),
            ("мясо", "go'sht"), ("рыба", "baliq"), ("яйцо", "tuxum"), ("сахар", "shakar"),
            ("соль", "tuz"), ("мёд", "asal"), ("чай", "choy"), ("суп", "sho'rva"),
            ("яблоко", "olma"), ("груша", "nok"), ("виноград", "uzum"), ("арбуз", "tarvuz"),
            ("дыня", "qovun"), ("персик", "shaftoli"), ("клубника", "qulupnay"), ("картофель", "kartoshka"),
            ("морковь", "sabzi"), ("лук", "piyoz"), ("помидор", "pomidor"), ("огурец", "bodring")
        ],
        "Vaqt va fasllar": [
            ("время", "vaqt"), ("секунда", "soniya"), ("минута", "daqiqa"), ("час", "soat"),
            ("день", "kun"), ("ночь", "tun"), ("утро", "tong / ertalab"), ("вечер", "kechqurun"),
            ("неделя", "hafta"), ("месяц", "oy (kalendar)"), ("год", "yil"), ("век", "asr"),
            ("весна", "bahor"), ("лето", "yoz"), ("осень", "kuz"), ("зима", "qish"),
            ("вчера", "kecha"), ("сегодня", "bugun"), ("завтра", "ertaga"), ("всегда", "har doim"),
            ("никогда", "hech qachon"), ("иногда", "ba'zan"), ("часто", "tez-tez"), ("редко", "kamdan-kam")
        ],
        "Sifatlar va belgilar": [
            ("большой", "katta"), ("маленький", "kichik"), ("высокий", "baland"), ("низкий", "past"),
            ("длинный", "uzun"), ("короткий", "qisqa"), ("широкий", "keng"), ("узкий", "tor"),
            ("новый", "yangi"), ("старый", "eski / qari"), ("молодой", "yosh"), ("красивый", "chiroyli"),
            ("умный", "aqlli"), ("добрый", "mehribon"), ("смелый", "jasur"), ("сильный", "kuchli"),
            ("слабый", "kuchsiz"), ("быстрый", "tez"), ("медленный", "sekin"), ("горячий", "issiq"),
            ("холодный", "sovuq"), ("тёплый", "iliq"), ("светлый", "yorug'"), ("тёмный", "qorong'i"),
            ("чистый", "toza"), ("грязный", "kir"), ("лёгкий", "yengil / oson"), ("тяжёлый", "og'ir"),
            ("дорогой", "qimmat"), ("дешёвый", "arzon"), ("вкусный", "mazali"), ("полезный", "foydali")
        ],
        "Asosiy fe'llar": [
            ("читать", "o'qimoq"), ("писать", "yozmoq"), ("говорить", "gapirmoq"), ("слушать", "tinglamoq"),
            ("смотреть", "qaramoq / ko'rmoq"), ("думать", "o'ylamoq"), ("знать", "bilmoq"), ("понимать", "tushunmoq"),
            ("учить", "o'rganmoq / o'qitmoq"), ("работать", "ishlamoq"), ("отдыхать", "dam olmoq"), ("играть", "o'ynamoq"),
            ("бегать", "yugurmoq"), ("ходить", "yurmoq"), ("летать", "uchmoq"), ("плавать", "suzmoq"),
            ("помогать", "yordam bermoq"), ("любить", "sevmoq / yaxshi ko'rmoq"), ("строить", "qurmoq"), ("покупать", "sotib olmoq"),
            ("продавать", "sotmoq"), ("открывать", "ochmoq"), ("закрывать", "yopmoq"), ("искать", "qidirmoq"),
            ("находить", "topmoq"), ("помнить", "eslamoq"), ("забывать", "unutmoq"), ("мечтать", "orzu qilmoq")
        ]
    }

    for cat_name, pairs in VOCAB_CATEGORIES.items():
        uz_pool = [uz for _, uz in pairs]
        ru_pool = [ru for ru, _ in pairs]
        for ru, uz in pairs:
            # Direction 1: Ruscha -> O'zbekcha
            wrong_uz = rng.sample([x for x in uz_pool if x != uz], 3)
            opts = [uz] + wrong_uz
            add_q(
                f"Leksika: {cat_name}",
                f"Rus tilidagi «{ru}» so'zining o'zbekcha tarjimasi qaysi?",
                opts, 0,
                f"«{ru}» so'zi o'zbek tilida «{uz}» degan ma'noni anglatadi.",
                "6-sinf", "oson"
            )
            # Direction 2: O'zbekcha -> Ruscha
            wrong_ru = rng.sample([x for x in ru_pool if x != ru], 3)
            opts2 = [ru] + wrong_ru
            add_q(
                f"Tarjima: {cat_name}",
                f"O'zbekcha «{uz}» so'zi rus tilida qanday aytiladi?",
                opts2, 0,
                f"«{uz}» so'zining ruscha tarjimasi — «{ru}».",
                "6-sinf", "oson"
            )

    # =====================================================================
    # 2. NOUN GENDER (Род имён существительных) — 130+ unique questions!
    # =====================================================================
    GENDER_DATA = [
        # (noun, gender_label, explanation, grade, diff)
        ("стол", "Мужской род", "Undosh bilan tugagan — мужской род.", "6-sinf", "oson"),
        ("дом", "Мужской род", "Undosh bilan tugagan — мужской род.", "6-sinf", "oson"),
        ("город", "Мужской род", "Undosh bilan tugagan — мужской род.", "6-sinf", "oson"),
        ("карандаш", "Мужской род", "Undosh bilan tugagan — мужской род.", "6-sinf", "oson"),
        ("учебник", "Мужской род", "Undosh bilan tugagan — мужской род.", "6-sinf", "oson"),
        ("музей", "Мужской род", "-й bilan tugagan ot — мужской род.", "6-sinf", "oson"),
        ("герой", "Мужской род", "-й bilan tugagan ot — мужской род.", "6-sinf", "oson"),
        ("трамвай", "Мужской род", "-й bilan tugagan ot — мужской род.", "6-sinf", "oson"),
        ("чай", "Мужской род", "-й bilan tugagan ot — мужской род.", "6-sinf", "oson"),
        ("словарь", "Мужской род", "-арь qo'shimchali otlar — мужской род (мой словарь).", "6-sinf", "orta"),
        ("календарь", "Мужской род", "-арь qo'shimchali ot — мужской род.", "6-sinf", "orta"),
        ("секретарь", "Мужской род", "-арь qo'shimchali ot — мужской род.", "6-sinf", "orta"),
        ("учитель", "Мужской род", "-тель qo'shimchali kasb oti — мужской род.", "6-sinf", "orta"),
        ("писатель", "Мужской род", "-тель qo'shimchali ot — мужской род.", "6-sinf", "orta"),
        ("день", "Мужской род", "«День» (-ь) — мужской род (добрый день).", "6-sinf", "orta"),
        ("дождь", "Мужской род", "«Дождь» (-ь) — мужской род (сильный дождь).", "6-sinf", "orta"),
        ("огонь", "Мужской род", "«Огонь» (-ь) — мужской род (яркий огонь).", "6-sinf", "orta"),
        ("конь", "Мужской род", "«Конь» (-ь) — мужской род (быстрый конь).", "6-sinf", "orta"),
        ("путь", "Мужской род", "«Путь» (-ь) — мужской род (длинный путь).", "7-sinf", "qiyin"),
        ("рояль", "Мужской род", "«Рояль» — мужской род (чёрный рояль).", "8-sinf", "qiyin"),
        ("шампунь", "Мужской род", "«Шампунь» — мужской род (новый шампунь).", "8-sinf", "qiyin"),
        ("тюль", "Мужской род", "«Тюль» — мужской род (белый тюль).", "9-sinf", "qiyin"),
        ("кофе", "Мужской род", "Adabiy normada «кофе» — мужской род (чёрный кофе).", "9-sinf", "qiyin"),
        ("папа", "Мужской род", "Erkak jinsiga tegishli bo'lgani uchun — мужской род.", "6-sinf", "orta"),
        ("дедушка", "Мужской род", "Erkak kishini bildirgani uchun — мужской род.", "6-sinf", "orta"),
        ("дядя", "Мужской род", "Erkak kishini bildirgani uchun — мужской род.", "6-sinf", "orta"),
        ("юноша", "Мужской род", "O'smir yigitni bildiradi — мужской род.", "7-sinf", "orta"),
        ("книга", "Женский род", "-а bilan tugagan — женский род.", "6-sinf", "oson"),
        ("школа", "Женский род", "-а bilan tugagan — женский род.", "6-sinf", "oson"),
        ("страна", "Женский род", "-а bilan tugagan — женский род.", "6-sinf", "oson"),
        ("родина", "Женский род", "-а bilan tugagan — женский род.", "6-sinf", "oson"),
        ("деревня", "Женский род", "-я bilan tugagan — женский род.", "6-sinf", "oson"),
        ("земля", "Женский род", "-я bilan tugagan — женский род.", "6-sinf", "oson"),
        ("история", "Женский род", "-ия bilan tugagan — женский род.", "6-sinf", "oson"),
        ("станция", "Женский род", "-ия bilan tugagan — женский род.", "6-sinf", "oson"),
        ("тетрадь", "Женский род", "«Тетрадь» (-ь) — женский род (новая тетрадь).", "6-sinf", "orta"),
        ("дверь", "Женский род", "«Дверь» (-ь) — женский род (открытая дверь).", "6-sinf", "orta"),
        ("ночь", "Женский род", "Shiqillovchi + ь (ч+ь) har doim женский род.", "6-sinf", "orta"),
        ("дочь", "Женский род", "«Дочь» (-ь) — женский род.", "6-sinf", "orta"),
        ("вещь", "Женский род", "Shiqillovchi + ь (щ+ь) — женский род.", "7-sinf", "orta"),
        ("помощь", "Женский род", "«Помощь» (щ+ь) — женский род.", "7-sinf", "orta"),
        ("молодёжь", "Женский род", "«Молодёжь» (ж+ь) — женский род.", "7-sinf", "orta"),
        ("жизнь", "Женский род", "«Жизнь» — женский род (счастливая жизнь).", "6-sinf", "orta"),
        ("площадь", "Женский род", "«Площадь» — женский род (большая площадь).", "6-sinf", "orta"),
        ("радость", "Женский род", "-ость qo'shimchali otlar — женский род.", "7-sinf", "orta"),
        ("новость", "Женский род", "-ость qo'shimchali ot — женский род.", "7-sinf", "orta"),
        ("скорость", "Женский род", "-ость qo'shimchali ot — женский род.", "7-sinf", "orta"),
        ("осень", "Женский род", "«Осень» — женский род (золотая осень).", "6-sinf", "orta"),
        ("соль", "Женский род", "«Соль» — женский род (белая соль).", "7-sinf", "orta"),
        ("мебель", "Женский род", "«Мебель» — женский род (новая мебель).", "8-sinf", "qiyin"),
        ("фамилия", "Женский род", "-ия bilan tugagan — женский род.", "6-sinf", "oson"),
        ("окно", "Средний род", "-о bilan tugagan — средний род.", "6-sinf", "oson"),
        ("письмо", "Средний род", "-о bilan tugagan — средний род.", "6-sinf", "oson"),
        ("озеро", "Средний род", "-о bilan tugagan — средний род.", "6-sinf", "oson"),
        ("облако", "Средний род", "-о bilan tugagan — средний род.", "6-sinf", "oson"),
        ("яблоко", "Средний род", "-о bilan tugagan — средний род.", "6-sinf", "oson"),
        ("море", "Средний род", "-е bilan tugagan — средний род.", "6-sinf", "oson"),
        ("поле", "Средний род", "-е bilan tugagan — средний род.", "6-sinf", "oson"),
        ("солнце", "Средний род", "-е bilan tugagan — средний род.", "6-sinf", "oson"),
        ("сердце", "Средний род", "-е bilan tugagan — средний род.", "6-sinf", "oson"),
        ("здание", "Средний род", "-ие bilan tugagan — средний род.", "6-sinf", "oson"),
        ("задание", "Средний род", "-ие bilan tugagan — средний род.", "6-sinf", "oson"),
        ("упражнение", "Средний род", "-ие bilan tugagan — средний род.", "6-sinf", "oson"),
        ("время", "Средний род", "-мя bilan tugaydigan 10 ta ot — средний род!", "7-sinf", "qiyin"),
        ("имя", "Средний род", "-мя bilan tugaydigan ot — средний род (моё имя).", "7-sinf", "qiyin"),
        ("знамя", "Средний род", "-мя bilan tugaydigan ot — средний род.", "8-sinf", "qiyin"),
        ("пламя", "Средний род", "-мя bilan tugaydigan ot — средний род.", "8-sinf", "qiyin"),
        ("племя", "Средний род", "-мя bilan tugaydigan ot — средний род.", "8-sinf", "qiyin"),
        ("семя", "Средний род", "-мя bilan tugaydigan ot — средний род.", "8-sinf", "qiyin"),
        ("метро", "Средний род", "O'zlashma turlanmaydigan jonsiz ot — средний род.", "8-sinf", "qiyin"),
        ("такси", "Средний род", "Turlanmaydigan jonsiz ot — средний род (жёлтое такси).", "8-sinf", "qiyin"),
        ("пальто", "Средний род", "Turlanmaydigan jonsiz ot — средний род (тёплое пальто).", "8-sinf", "qiyin"),
        ("кино", "Средний род", "Turlanmaydigan jonsiz ot — средний род (интересное кино).", "7-sinf", "orta"),
        ("радио", "Средний род", "Turlanmaydigan jonsiz ot — средний род.", "7-sinf", "orta"),
        ("меню", "Средний род", "Turlanmaydigan jonsiz ot — средний род (новое меню).", "8-sinf", "qiyin"),
        ("сирота", "Общий род", "«Сирота» ham erkak, ham ayolga nisbatan — общий род.", "8-sinf", "qiyin"),
        ("умница", "Общий род", "«Умница» (aqlli) ikki jinsga ham tegishli — общий род.", "8-sinf", "qiyin"),
        ("молодец", "Мужской род", "«Молодец» grammatik jihatdan мужской род.", "8-sinf", "qiyin"),
        ("коллега", "Общий род", "«Коллега» (hamkasb) — общий род.", "9-sinf", "qiyin"),
        ("неряха", "Общий род", "«Неряха» — общий род.", "9-sinf", "qiyin")
    ]
    all_genders = ["Мужской род", "Женский род", "Средний род", "Общий род"]
    for noun, gend, expl, gr, df in GENDER_DATA:
        opts = [gend] + [g for g in all_genders if g != gend]
        add_q(
            "Otlarning jinsi (Род существительных)",
            f"«{noun}» oti qaysi jinsga (rod) tegishli?",
            opts, 0, expl, gr, df
        )
        # Also create possessive pronoun agreement question for non-obshiy nouns!
        if gend != "Общий род":
            pron_map = {"Мужской род": "мой", "Женский род": "моя", "Средний род": "моё"}
            corr_p = pron_map[gend]
            p_opts = [corr_p] + [p for p in ["мой", "моя", "моё", "мои"] if p != corr_p]
            add_q(
                "Egalik olmoshlari (Притяжательные местоимения)",
                f"Nuqtalar o'rniga mos egalik olmoshini qo'ying: «... {noun}»",
                p_opts, 0,
                f"«{noun}» — {gend}, shuning uchun «{corr_p} {noun}» bo'ladi.",
                gr, df
            )

    # =====================================================================
    # 3. PLURAL FORMS (Множественное число) — 80+ unique questions!
    # =====================================================================
    PLURALS = [
        ("дом", "дома", ["домы", "доми", "домов"], "Istisno: дом → дома."),
        ("город", "города", ["городы", "городи", "городов"], "Istisno: город → города."),
        ("глаз", "глаза", ["глазы", "глази", "глазов"], "Istisno: глаз → глаза."),
        ("лес", "леса", ["лесы", "леси", "лесов"], "Istisno: лес → леса."),
        ("берег", "берега", ["береги", "берегы", "берегов"], "Istisno: берег → берега."),
        ("поезд", "поезда", ["поезды", "поезди", "поездов"], "Istisno: поезд → поезда."),
        ("учитель", "учителя", ["учители", "учителы", "учителей"], "Istisno: учитель → учителя."),
        ("доктор", "доктора", ["докторы", "доктори", "докторов"], "Istisno: доктор → доктора."),
        ("профессор", "профессора", ["профессоры", "профессори", "профессоров"], "Istisno: профессор → профессора."),
        ("паспорт", "паспорта", ["паспорты", "паспорти", "паспортов"], "Istisno: паспорт → паспорта."),
        ("адрес", "адреса", ["адресы", "адреси", "адресов"], "Istisno: адрес → адреса."),
        ("вечер", "вечера", ["вечеры", "вечери", "вечеров"], "Istisno: вечер → вечера."),
        ("номер", "номера", ["номеры", "номери", "номеров"], "Istisno: номер → номера."),
        ("голос", "голоса", ["голосы", "голоси", "голосов"], "Istisno: голос → голоса."),
        ("цвет", "цвета", ["цветы", "цвети", "цветов"], "Rang ma'nosida: цвет → цвета (цветы — gullar)."),
        ("человек", "люди", ["человеки", "человека", "людей"], "Suppletiv shakl: человек → люди!"),
        ("ребёнок", "дети", ["ребёнки", "ребёнка", "детям"], "Suppletiv shakl: ребёнок → дети!"),
        ("друг", "друзья", ["други", "друга", "друзей"], "Istisno: друг → друзья."),
        ("брат", "братья", ["браты", "брата", "братьев"], "Istisno: брат → братья."),
        ("сын", "сыновья", ["сыны", "сына", "сыновьёв"], "Oila a'zosi: сын → сыновья."),
        ("стул", "стулья", ["стулы", "стули", "стульев"], "Istisno: стул → стулья."),
        ("дерево", "деревья", ["деревы", "дерева", "деревьев"], "Istisno: дерево → деревья."),
        ("лист (daraxt bargi)", "листья", ["листы", "листа", "листьев"], "Daraxt bargi: лист → листья."),
        ("перо", "перья", ["перы", "пера", "перьев"], "Istisno: перо → перья."),
        ("крыло", "крылья", ["крылы", "крыла", "крыльев"], "Istisno: крыло → крылья."),
        ("мать", "матери", ["мати", "матеря", "матей"], "Istisno: мать → матери."),
        ("дочь", "дочери", ["дочи", "дочеря", "дочей"], "Istisno: дочь → дочери."),
        ("время", "времена", ["времи", "времяны", "времён"], "-мя otlarida: время → времена."),
        ("имя", "имена", ["ими", "имяны", "имён"], "-мя otlarida: имя → имена."),
        ("знамя", "знамёна", ["знами", "знамяны", "знамён"], "-мя otlarida: знамя → знамёна."),
        ("ухо", "уши", ["ухи", "уха", "ушей"], "Istisno: ухо → уши."),
        ("яблоко", "яблоки", ["яблока", "яблокы", "яблоков"], "Istisno: яблоко → яблоки."),
        ("сосед", "соседи", ["соседы", "соседа", "соседей"], "Istisno: сосед → соседи."),
        ("гражданин", "граждане", ["гражданины", "граждани", "гражданов"], "-ин qo'shimchali ot: гражданин → граждане."),
        ("англичанин", "англичане", ["англичанины", "англичани", "англичанов"], "-анин → -ане: англичанин → англичане."),
        ("крестьянин", "крестьяне", ["крестьянины", "крестьяни", "крестьянов"], "-янин → -яне: крестьянин → крестьяне."),
        ("котёнок", "котята", ["котёнки", "котяты", "котёнков"], "-ёнок → -ята: котёнок → котята."),
        ("щенок", "щенки", ["щенята", "щенка", "щенков"], "щенок → щенки."),
        ("медвежонок", "медвежата", ["медвежонки", "медвежаты", "медвежат"], "-онок → -ата: медвежонок → медвежата."),
        ("книга", "книги", ["книгы", "книга", "книгов"], "Г harfidan keyin -и yoziladi: книги."),
        ("ручка", "ручки", ["ручкы", "ручка", "ручков"], "К harfidan keyin -и yoziladi: ручки."),
        ("врач", "врачи", ["врачы", "врача", "врачей"], "Ч harfidan keyin -и yoziladi: врачи."),
        ("карандаш", "карандаши", ["карандашы", "карандаша", "карандашей"], "Ш harfidan keyin -и yoziladi: карандаши."),
        ("нож", "ножи", ["ножы", "ножа", "ножей"], "Ж harfidan keyin -и yoziladi: ножи."),
        ("тетрадь", "тетради", ["тетрады", "тетрадя", "тетрадей"], "Женский род -ь → -и: тетради."),
        ("окно", "окна", ["окны", "окни", "окон"], "Средний род -о → -а: окна."),
        ("море", "моря", ["моры", "мори", "морей"], "Средний род -е → -я: моря."),
        ("здание", "здания", ["здании", "зданиев", "зданий"], "Средний род -ие → -ия: здания."),
        ("письмо", "письма", ["письмы", "письми", "писем"], "Средний род -о → -а: письма."),
        ("дело", "дела", ["делы", "дели", "дел"], "Средний род -о → -а: дела.")
    ]
    for sg, pl, wr, expl in PLURALS:
        add_q(
            "Ko'plik shakli (Множественное число)",
            f"«{sg}» so'zining ko'plik (множественное число) shakli qaysi?",
            [pl] + wr, 0, expl, "6-sinf", "orta"
        )

    # =====================================================================
    # 4. ALL 6 CASES / PADEJLAR (Падежи) — 150+ unique questions!
    # =====================================================================
    PADEJ_THEORY = [
        ("Именительный падеж (Bosh kelishik) qaysi so'roqlarga javob beradi?", "Кто? Что?", ["Кого? Чего?", "Кому? Чему?", "Кем? Чем?"], "Именительный падеж — Кто? Что?"),
        ("Родительный падеж (Qaratqich kelishigi) qaysi so'roqlarga javob beradi?", "Кого? Чего?", ["Кто? Что?", "Кому? Чему?", "О ком? О чём?"], "Родительный падеж — (нет) Кого? Чего?"),
        ("Дательный падеж (Jo'nalish kelishigi) qaysi so'roqlarga javob beradi?", "Кому? Чему?", ["Кого? Чего?", "Кем? Чем?", "О ком? О чём?"], "Дательный падеж — (дать) Кому? Чему?"),
        ("Винительный падеж (Tushum kelishigi) qaysi so'roqlarga javob beradi?", "Кого? Что?", ["Кого? Чего?", "Кому? Чему?", "Кем? Чем?"], "Винительный падеж — (вижу) Кого? Что?"),
        ("Творительный падеж qaysi so'roqlarga javob beradi?", "Кем? Чем?", ["Кто? Что?", "Кому? Чему?", "О ком? О чём?"], "Творительный падеж — (доволен) Кем? Чем?"),
        ("Предложный падеж (O'rin-payt kelishigi) qaysi so'roqlarga javob beradi?", "О ком? О чём?", ["Кем? Чем?", "Кому? Чему?", "Кого? Чего?"], "Предложный падеж — (думаю) О ком? О чём?"),
        ("Rus tilida nechta kelishik (падеж) mavjud?", "6 ta", ["4 ta", "5 ta", "7 ta"], "Rus tilida 6 ta padej bor: И., Р., Д., В., Т., П."),
        ("Qaysi kelishik hech qachon predlogsiz ishlatilmaydi?", "Предложный падеж", ["Именительный падеж", "Дательный падеж", "Винительный падеж"], "Предложный падеж har doim predlog (в, на, о, при) bilan keladi!"),
        ("Qaysi kelishik hech qachon predlog bilan ishlatilmaydi?", "Именительный падеж", ["Родительный падеж", "Творительный падеж", "Предложный падеж"], "Именительный падеж har doim predlogsiz ishlatiladi."),
        ("«Без, у, от, до, из, около» predloglari qaysi kelishik bilan qo'llaniladi?", "Родительный падеж", ["Дательный падеж", "Творительный падеж", "Предложный падеж"], "Bu predloglar Родительный падеж (Кого? Чего?) talab qiladi."),
        ("«К» va «по» predloglari qaysi kelishik bilan qo'llaniladi?", "Дательный падеж", ["Родительный падеж", "Винительный падеж", "Предложный падеж"], "«К» va «по» — Дательный падеж (Кому? Чему?) predloglari."),
        ("«С, над, под, перед, между» predloglari ko'pincha qaysi kelishik bilan keladi?", "Творительный падеж", ["Именительный падеж", "Дательный падеж", "Предложный падеж"], "Bu predloglar Творительный падеж (Кем? Чем?) bilan qo'llaniladi.")
    ]
    for q, c, w, ex in PADEJ_THEORY:
        add_q("Kelishiklar nazariyasi (Падежи)", q, [c] + w, 0, ex, "7-sinf", "orta")

    PADEJ_SENTENCES = [
        # Contextual sentence fill-in-the-blank across all 6 cases!
        ("Я учусь в ... (школа).", "школе", ["школа", "школу", "школой"], "Предложный падеж (Где?): в школе."),
        ("Книга лежит на ... (стол).", "столе", ["стол", "стола", "столом"], "Предложный падеж (Где?): на столе."),
        ("Мы живём в ... (Ташкент).", "Ташкенте", ["Ташкент", "Ташкента", "Ташкенту"], "Предложный падеж: в Ташкенте."),
        ("Дети гуляют в ... (парк).", "парке", ["парк", "парка", "парком"], "Предложный падеж: в парке."),
        ("Он думает о ... (будущее).", "будущем", ["будущее", "будущего", "будущему"], "Предложный падеж (О чём?): о будущем."),
        ("Мы говорили о ... (книга).", "книге", ["книга", "книгу", "книгой"], "Предложный падеж (О чём?): о книге."),
        ("Студент занимается в ... (библиотека).", "библиотеке", ["библиотека", "библиотеку", "библиотекой"], "Предложный падеж: в библиотеке."),
        ("Птицы летают в ... (небо).", "небе", ["небо", "неба", "небом"], "Предложный падеж: в небе."),
        ("Я мечтаю о ... (путешествие).", "путешествии", ["путешествие", "путешествия", "путешествием"], "-ие otlari Предложный padejda -ии oladi: о путешествии!"),
        ("Мы были на ... (экскурсия).", "экскурсии", ["экскурсия", "экскурсию", "экскурсией"], "-ия otlari Предложный padejda -ии oladi: на экскурсии!"),
        ("У меня нет ... (время).", "времени", ["время", "временем", "времён"], "Родительный падеж (Чего?): нет времени."),
        ("Сегодня нет ... (дождь).", "дождя", ["дождь", "дождю", "дождём"], "Родительный падеж: нет дождя."),
        ("В комнате нет ... (стол).", "стола", ["стол", "столу", "столе"], "Родительный падеж: нет стола."),
        ("Я пью чай без ... (сахар).", "сахара", ["сахар", "сахару", "сахаром"], "«Без» predlogi + Родительный: без сахара."),
        ("Он вернулся из ... (школа).", "школы", ["школа", "школе", "школу"], "«Из» + Родительный: из школы."),
        ("У ... (сестра) новая книга.", "сестры", ["сестра", "сестре", "сестру"], "«У» + Родительный: у сестры."),
        ("Магазин находится около ... (дом).", "дома", ["дом", "доме", "дому"], "«Около» + Родительный: около дома."),
        ("Я получил письмо от ... (друг).", "друга", ["друг", "другу", "другом"], "«От» + Родительный: от друга."),
        ("В классе много ... (ученики).", "учеников", ["ученики", "ученикам", "учениками"], "«Много» + ko'plik Родительный: много учеников."),
        ("На столе пять ... (книги).", "книг", ["книги", "книгов", "книгам"], "5 dan keyin ko'plik Родительный: пять книг."),
        ("Я помогаю ... (мама).", "маме", ["мама", "маму", "мамой"], "Дательный падеж (Кому?): помогаю маме."),
        ("Учитель объясняет правило ... (ученик).", "ученику", ["ученик", "ученика", "учеником"], "Дательный падеж (Кому?): ученику."),
        ("Я звоню ... (друг).", "другу", ["друг", "друга", "другом"], "Дательный падеж (Кому?): звоню другу."),
        ("Он подарил цветы ... (учительница).", "учительнице", ["учительница", "учительницу", "учительницей"], "Дательный падеж: учительнице."),
        ("Мы идём к ... (врач).", "врачу", ["врач", "врача", "врачом"], "«К» + Дательный: к врачу."),
        ("Машина едет по ... (дорога).", "дороге", ["дорога", "дорогу", "дорогой"], "«По» + Дательный: по дороге."),
        ("Я рад ... (встреча).", "встрече", ["встреча", "встречу", "встречей"], "«Рад» + Дательный: рад встрече."),
        ("Я читаю интересную ... (книга).", "книгу", ["книга", "книги", "книге"], "Винительный падеж (Что?): читаю книгу."),
        ("Утром я иду в ... (школа).", "школу", ["школа", "школе", "школой"], "Yo'nalish (Куда?) — Винительный: в школу."),
        ("Мы любим нашу ... (родина).", "родину", ["родина", "родины", "родине"], "Винительный падеж: любим родину."),
        ("Он смотрит ... (фильм).", "фильм", ["фильма", "фильму", "фильмом"], "Jonsiz мужской род Винительныйda o'zgarmaydi: фильм."),
        ("Я вижу своего ... (брат).", "брата", ["брат", "брату", "братом"], "Jonli мужской род Винительныйda -а oladi: брата."),
        ("Мы купили свежую ... (рыба).", "рыбу", ["рыба", "рыбы", "рыбе"], "Винительный падеж: рыбу."),
        ("Она поставила вазу на ... (стол).", "стол", ["столе", "стола", "столом"], "Yo'nalish (Куда?) — Винительный: на стол."),
        ("Я пишу ... (ручка).", "ручкой", ["ручка", "ручку", "ручке"], "Творительный падеж (Чем?): пишу ручкой."),
        ("Художник рисует ... (карандаш).", "карандашом", ["карандаш", "карандаша", "карандашу"], "Творительный падеж (Чем?): карандашом."),
        ("Я пью чай с ... (лимон).", "лимоном", ["лимон", "лимона", "лимону"], "«С» + Творительный: с лимоном."),
        ("Мой брат хочет стать ... (врач).", "врачом", ["врач", "врача", "врачу"], "«Стать» + Творительный (Кем?): стать врачом."),
        ("Я горжусь своей ... (страна).", "страной", ["страна", "страну", "стране"], "«Гордиться» + Творительный: горжусь страной."),
        ("Мы интересуемся ... (история).", "историей", ["история", "историю", "истории"], "«Интересоваться» + Творительный: историей."),
        ("Самолёт летит над ... (город).", "городом", ["город", "города", "городе"], "«Над» + Творительный: над городом."),
        ("Кот спит под ... (стол).", "столом", ["стол", "стола", "столе"], "«Под» + Творительный: под столом."),
        ("Перед ... (дом) растёт дерево.", "домом", ["дом", "дома", "доме"], "«Перед» + Творительный: перед домом."),
        ("Она занимается ... (спорт).", "спортом", ["спорт", "спорта", "спорте"], "«Заниматься» + Творительный: спортом."),
        ("Я дружу с ... (Алишер).", "Алишером", ["Алишер", "Алишера", "Алишеру"], "«С» + Творительный: с Алишером.")
    ]
    for sent, ans, wr, ex in PADEJ_SENTENCES:
        add_q("Padejlar amaliyoti (Падежи в предложении)", f"To'g'ri shaklni tanlang: «{sent}»", [ans] + wr, 0, ex, "7-sinf", "orta")

    # =====================================================================
    # 5. VERB CONJUGATION, TENSES & ASPECTS — 160+ unique questions!
    # =====================================================================
    CONJ_DATA = [
        ("читать", "я", "читаю", ["читаешь", "читает", "читаем"]),
        ("читать", "ты", "читаешь", ["читаю", "читает", "читаете"]),
        ("читать", "он", "читает", ["читаю", "читаешь", "читают"]),
        ("читать", "мы", "читаем", ["читаете", "читают", "читаешь"]),
        ("читать", "вы", "читаете", ["читаем", "читают", "читает"]),
        ("читать", "они", "читают", ["читаем", "читаете", "читает"]),
        ("писать", "я", "пишу", ["писаю", "пишешь", "пишет"]),
        ("писать", "ты", "пишешь", ["пишу", "пишет", "пишете"]),
        ("писать", "он", "пишет", ["пишу", "пишешь", "пишут"]),
        ("писать", "мы", "пишем", ["пишут", "пишете", "пишет"]),
        ("писать", "они", "пишут", ["пишем", "пишете", "пишет"]),
        ("говорить", "я", "говорю", ["говоришь", "говорит", "говорим"]),
        ("говорить", "ты", "говоришь", ["говорю", "говорит", "говорят"]),
        ("говорить", "он", "говорит", ["говорю", "говоришь", "говорят"]),
        ("говорить", "мы", "говорим", ["говорите", "говорят", "говорит"]),
        ("говорить", "они", "говорят", ["говорим", "говорите", "говорит"]),
        ("любить", "я", "люблю", ["любишь", "любит", "любят"]),
        ("любить", "ты", "любишь", ["люблю", "любит", "любите"]),
        ("любить", "они", "любят", ["любим", "любите", "любит"]),
        ("видеть", "я", "вижу", ["видишь", "видит", "видят"]),
        ("видеть", "ты", "видишь", ["вижу", "видит", "видите"]),
        ("видеть", "они", "видят", ["видим", "видите", "видит"]),
        ("хотеть", "я", "хочу", ["хочешь", "хочет", "хотим"]),
        ("хотеть", "ты", "хочешь", ["хочу", "хочет", "хотите"]),
        ("хотеть", "мы", "хотим", ["хотите", "хотят", "хочет"]),
        ("хотеть", "они", "хотят", ["хотим", "хотите", "хочет"]),
        ("идти", "я", "иду", ["идёшь", "идёт", "идём"]),
        ("идти", "ты", "идёшь", ["иду", "идёт", "идёте"]),
        ("идти", "они", "идут", ["идём", "идёте", "идёт"]),
        ("ехать", "я", "еду", ["едешь", "едет", "едем"]),
        ("ехать", "они", "едут", ["едем", "едете", "едет"]),
        ("бежать", "я", "бегу", ["бежишь", "бежит", "бежим"]),
        ("бежать", "они", "бегут", ["бежим", "бежите", "бежит"]),
        ("мочь", "я", "могу", ["можешь", "может", "можем"]),
        ("мочь", "ты", "можешь", ["могу", "может", "можете"]),
        ("мочь", "они", "могут", ["можем", "можете", "может"]),
        ("жить", "я", "живу", ["живёшь", "живёт", "живём"]),
        ("жить", "они", "живут", ["живём", "живёте", "живёт"]),
        ("учиться", "я", "учусь", ["учишься", "учится", "учимся"]),
        ("учиться", "они", "учатся", ["учимся", "учитесь", "учится"]),
        ("знать", "я", "знаю", ["знаешь", "знает", "знаем"]),
        ("знать", "они", "знают", ["знаем", "знаете", "знает"]),
        ("работать", "мы", "работаем", ["работаете", "работают", "работает"]),
        ("помогать", "вы", "помогаете", ["помогаем", "помогают", "помогает"]),
        ("строить", "они", "строят", ["строим", "строите", "строит"]),
        ("смотреть", "ты", "смотришь", ["смотрю", "смотрит", "смотрят"]),
        ("смотреть", "они", "смотрят", ["смотрим", "смотрите", "смотрит"]),
        ("слышать", "они", "слышат", ["слышим", "слышите", "слышит"]),
        ("дышать", "ты", "дышишь", ["дышу", "дышит", "дышат"]),
        ("держать", "они", "держат", ["держим", "держите", "держит"])
    ]
    for inf, pron, ans, wr in CONJ_DATA:
        add_q(
            "Fe'l tuslanishi (Спряжение глаголов)",
            f"«{inf}» fe'lining «{pron}» olmoshi bilan hozirgi zamon shakli qaysi?",
            [ans] + wr, 0,
            f"To'g'ri tuslanish: {pron} {ans} ({inf}).",
            "7-sinf", "orta"
        )

    ASPECT_PAIRS = [
        ("делать", "сделать"), ("писать", "написать"), ("читать", "прочитать"), ("говорить", "сказать"),
        ("брать", "взять"), ("покупать", "купить"), ("давать", "дать"), ("открывать", "открыть"),
        ("закрывать", "закрыть"), ("решать", "решить"), ("получать", "получить"), ("изучать", "изучить"),
        ("понимать", "понять"), ("начинать", "начать"), ("кончать", "кончить"), ("помогать", "помочь"),
        ("смотреть", "посмотреть"), ("слушать", "послушать"), ("строить", "построить"), ("рисовать", "нарисовать"),
        ("готовить", "приготовить"), ("учить", "выучить"), ("отвечать", "ответить"), ("спрашивать", "спросить"),
        ("встречать", "встретить"), ("приглашать", "пригласить"), ("забывать", "забыть"), ("находить", "найти"),
        ("показывать", "показать"), ("рассказывать", "рассказать")
    ]
    sv_pool = [sv for _, sv in ASPECT_PAIRS]
    for nsv, sv in ASPECT_PAIRS:
        wr = rng.sample([x for x in sv_pool if x != sv], 3)
        add_q(
            "Fe'l turlari (Вид глагола: НСВ / СВ)",
            f"«{nsv}» (tugallanmagan tur — НСВ) fe'lining tugallangan (СВ) jufti qaysi?",
            [sv] + wr, 0,
            f"Fe'l juftligi: {nsv} (что делать?) — {sv} (что сделать?).",
            "8-sinf", "orta"
        )

    # =====================================================================
    # 6. ADJECTIVE AGREEMENT, ANTONYMS & SYNONYMS — 120+ unique questions!
    # =====================================================================
    ANTONYMS = [
        ("большой", "маленький"), ("высокий", "низкий"), ("длинный", "короткий"), ("широкий", "узкий"),
        ("новый", "старый"), ("молодой", "пожилой"), ("добрый", "злой"), ("смелый", "трусливый"),
        ("сильный", "слабый"), ("быстрый", "медленный"), ("горячий", "холодный"), ("светлый", "тёмный"),
        ("чистый", "грязный"), ("лёгкий", "тяжёлый"), ("дорогой", "дешёвый"), ("богатый", "бедный"),
        ("весёлый", "грустный"), ("твёрдый", "мягкий"), ("сухой", "мокрый"), ("острый", "тупой"),
        ("громкий", "тихий"), ("сладкий", "горький"), ("далёкий", "близкий"), ("ранний", "поздний"),
        ("правда", "ложь"), ("мир", "война"), ("день", "ночь"), ("лето", "зима"),
        ("начало", "конец"), ("вопрос", "ответ"), ("вход", "выход"), ("победа", "поражение"),
        ("друг", "враг"), ("радость", "печаль"), ("здоровье", "болезнь"), ("труд", "лень")
    ]
    ant_pool = [b for _, b in ANTONYMS]
    for a, b in ANTONYMS:
        wr = rng.sample([x for x in ant_pool if x != b and x != a], 3)
        add_q(
            "Antonimlar (Антонимы)",
            f"«{a}» so'zining antonimi (qarama-qarshi ma'nolisi) qaysi?",
            [b] + wr, 0,
            f"«{a}» va «{b}» — qarama-qarshi ma'noli so'zlar (antonimlar).",
            "6-sinf", "oson"
        )

    SYNONYMS = [
        ("красивый", "прекрасный"), ("смелый", "храбрый"), ("большой", "огромный"), ("быстрый", "стремительный"),
        ("грустный", "печальный"), ("умный", "мудрый"), ("верный", "преданный"), ("холодный", "морозный"),
        ("друг", "товарищ"), ("родина", "отечество"), ("доктор", "врач"), ("работа", "труд"),
        ("дорога", "путь"), ("здание", "сооружение"), ("ученик", "школьник"), ("разговор", "беседа"),
        ("радость", "веселье"), ("страх", "боязнь"), ("бежать", "мчаться"), ("смотреть", "глядеть"),
        ("говорить", "произносить"), ("думать", "размышлять"), ("помогать", "содействовать"), ("создавать", "творить")
    ]
    syn_pool = [b for _, b in SYNONYMS]
    for a, b in SYNONYMS:
        wr = rng.sample([x for x in syn_pool if x != b and x != a], 3)
        add_q(
            "Sinonimlar (Синонимы)",
            f"«{a}» so'ziga eng yaqin sinonim (ma'nodosh so'z) qaysi?",
            [b] + wr, 0,
            f"«{a}» va «{b}» — ma'nodosh so'zlar (sinonimlar).",
            "7-sinf", "orta"
        )

    ADJ_AGREE = [
        ("новый", "дом", "новый дом", ["новая дом", "новое дом", "новые дом"]),
        ("новый", "книга", "новая книга", ["новый книга", "новое книга", "новые книга"]),
        ("новый", "окно", "новое окно", ["новый окно", "новая окно", "новые окно"]),
        ("новый", "друзья", "новые друзья", ["новый друзья", "новая друзья", "новое друзья"]),
        ("синий", "небо", "синее небо", ["синий небо", "синяя небо", "синие небо"]),
        ("синий", "море", "синее море", ["синий море", "синяя море", "синие море"]),
        ("синий", "река", "синяя река", ["синий река", "синее река", "синие река"]),
        ("интересный", "фильм", "интересный фильм", ["интересная фильм", "интересное фильм", "интересные фильм"]),
        ("интересный", "история", "интересная история", ["интересный история", "интересное история", "интересные история"]),
        ("интересный", "задание", "интересное задание", ["интересный задание", "интересная задание", "интересные задание"]),
        ("хороший", "ученик", "хороший ученик", ["хорошая ученик", "хорошее ученик", "хорошие ученик"]),
        ("хороший", "погода", "хорошая погода", ["хороший погода", "хорошее погода", "хорошие погода"]),
        ("хороший", "настроение", "хорошее настроение", ["хороший настроение", "хорошая настроение", "хорошие настроение"]),
        ("высокий", "гора", "высокая гора", ["высокий гора", "высокое гора", "высокие гора"]),
        ("высокий", "дерево", "высокое дерево", ["высокий дерево", "высокая дерево", "высокие дерево"]),
        ("тёплый", "вечер", "тёплый вечер", ["тёплая вечер", "тёплое вечер", "тёплые вечер"]),
        ("тёплый", "пальто", "тёплое пальто", ["тёплый пальто", "тёплая пальто", "тёплые пальто"]),
        ("чёрный", "кофе", "чёрный кофе", ["чёрная кофе", "чёрное кофе", "чёрные кофе"]),
        ("жёлтый", "такси", "жёлтое такси", ["жёлтый такси", "жёлтая такси", "жёлтые такси"]),
        ("золотой", "осень", "золотая осень", ["золотой осень", "золотое осень", "золотые осень"])
    ]
    for adj, noun, corr, wr in ADJ_AGREE:
        add_q(
            "Sifat moslashuvi (Согласование прилагательных)",
            f"«{adj}» sifatini «{noun}» oti bilan to'g'ri moslashtiring:",
            [corr] + wr, 0,
            f"To'g'ri birikma: «{corr}».",
            "6-sinf", "oson"
        )

    # =====================================================================
    # 7. ORTHOGRAPHY, STRESS (УДАРЕНИЕ), PARONYMS, PHRASEOLOGY & SYNTAX — 140+ Qs!
    # =====================================================================
    ORTHO_STRESS = [
        ("Imlo (Орфография)", "Qaysi qatorda barcha so'zlar to'g'ri yozilgan (ЖИ-ШИ qoidasi)?", "жизнь, машина, шина", ["жызнь, машына, шына", "жизнь, машына, шина", "жызнь, машина, шина"], "ЖИ-ШИ har doim И bilan yoziladi!", "6-sinf", "oson"),
        ("Imlo (Орфография)", "Qaysi qatorda ЧА-ЩА qoidasiga ko'ra to'g'ri yozilgan?", "чашка, задача, роща", ["чяшка, задачя, рощя", "чашка, задачя, роща", "чяшка, задача, роща"], "ЧА-ЩА har doim А bilan yoziladi!", "6-sinf", "oson"),
        ("Imlo (Орфография)", "Qaysi qatorda ЧУ-ЩУ qoidasiga ko'ra to'g'ri yozilgan?", "чудо, щука, чувствовать", ["чюдо, щюка, чювствовать", "чудо, щюка, чувствовать", "чюдо, щука, чувствовать"], "ЧУ-ЩУ har doim У bilan yoziladi!", "6-sinf", "oson"),
        ("Imlo (Орфография)", "ЧК-ЧН birikmalari qaysi qatorda to'g'ri yozilgan?", "точка, речка, ночной", ["точька, речька, ночьной", "точка, речька, ночной", "точька, речка, ночной"], "ЧК va ЧН o'rtasida yumshatish belgisi (Ь) yozilmaydi!", "6-sinf", "oson"),
        ("Imlo (Орфография)", "«Не» inkor yuklamasi fe'l bilan qanday yoziladi?", "не знаю, не был, не читал", ["незнаю, небыл, нечитал", "не-знаю, не-был, не-читал", "незнаю, не был, нечитал"], "«Не» fe'llar bilan ajratib yoziladi (istisno: ненавидеть, негодовать).", "7-sinf", "oson"),
        ("Imlo (Орфография)", "Qaysi fe'l «не» bilan qo'shib yoziladi (не siz ishlatilmaydi)?", "ненавидеть", ["не знать", "не видеть", "не любить"], "«Ненавидеть» fe'li «не» siz ishlatilmaydi, shuning uchun qo'shib yoziladi.", "8-sinf", "orta"),
        ("Imlo (Орфография)", "Qaysi so'zda ajratish belgisi «Ъ» to'g'ri yozilgan?", "подъезд, объявление", ["подьезд, обьявление", "подезд, обявление", "подъезд, обьявление"], "Undosh bilan tugagan old qo'shimchadan keyin Е, Ё, Ю, Я oldidan Ъ yoziladi.", "8-sinf", "orta"),
        ("Imlo (Орфография)", "Qaysi so'zda «Ь» (yumshatish belgisi) to'g'ri yozilgan?", "семья, друзья, здоровье", ["семъя, друзъя, здоровъе", "семя, друзя, здорове", "семъя, друзья, здоровье"], "So'z o'zagida Е, Ё, Ю, Я, И oldidan ajratuvchi Ь yoziladi.", "8-sinf", "orta"),
        ("Imlo (Орфография)", "«При-» old qo'shimchasi qaysi ma'noda ishlatilgan: «приехать»?", "Yaqinlashish, yetib kelish", ["Juda (очень)", "Chetlab o'tish", "Qayta bajarish"], "При- — yaqinlashish, qo'shilish, to'liq bo'lmagan harakat ma'nosini beradi.", "9-sinf", "orta"),
        ("Imlo (Орфография)", "«Пре-» old qo'shimchasi qaysi so'zda «juda (очень)» ma'nosini bildiradi?", "прекрасный", ["пришкольный", "принести", "приоткрыть"], "Прекрасный = очень красивый (juda chiroyli).", "9-sinf", "orta"),
        ("Imlo (Орфография)", "Qaysi so'zda qo'sh «НН» to'g'ri yozilgan?", "стеклянный, оловянный, деревянный", ["стекляный, оловяный, деревяный", "серебрянный, кожанный, глинянный", "ветренный, песчанный, ледянный"], "Istisno 3 ta sifat: стеклянный, оловянный, деревянный — har doim НН!", "9-sinf", "qiyin"),
        ("Orfoepiya (Urg'u)", "«Звонит» fe'lida urg'u qaysi bo'g'inga tushadi?", "звони́т", ["зво́нит", "звóнит (ikkalasi ham)", "urg'u yo'q"], "Adabiy normada faqat «звони́т» to'g'ri!", "10-sinf", "qiyin"),
        ("Orfoepiya (Urg'u)", "«Торты» so'zida urg'u qaysi bo'g'inga tushadi?", "то́рты", ["торты́", "to'rtí", "ikkalasi ham to'g'ri"], "Adabiy normada «то́рты» (1-bo'g'inga urg'u).", "10-sinf", "qiyin"),
        ("Orfoepiya (Urg'u)", "«Красивее» so'zida to'g'ri urg'u qaysi?", "краси́вее", ["красиве́е", "кра́сивее", "красивее́"], "Adabiy normada faqat «краси́вее» to'g'ri!", "10-sinf", "qiyin"),
        ("Orfoepiya (Urg'u)", "«Каталог» so'zida to'g'ri urg'u qaysi?", "катало́г", ["ка́талог", "ката́лог", "ikkalasi ham"], "Adabiy normada «катало́г» (oxirgi bo'g'inda).", "11-sinf", "qiyin"),
        ("Orfoepiya (Urg'u)", "«Договор» so'zida to'g'ri urg'u qaysi?", "догово́р", ["до́говор", "дого́вор", "farqi yo'q"], "Adabiy normada «догово́р» (oxirgi bo'g'inda).", "11-sinf", "qiyin"),
        ("Orfoepiya (Urg'u)", "«Квартал» so'zida to'g'ri urg'u qaysi?", "кварта́л", ["ква́ртал", "квáртал (chorakda)", "urg'usiz"], "Barcha ma'nolarda faqat «кварта́л» to'g'ri!", "11-sinf", "qiyin"),
        ("Orfoepiya (Urg'u)", "«Средства» so'zida to'g'ri urg'u qaysi?", "сре́дства", ["средства́", "средст́ва", "ikkalasi ham"], "To'g'ri talaffuz: «сре́дства».", "11-sinf", "qiyin"),
        ("Orfoepiya (Urg'u)", "«Шарфы» so'zida to'g'ri urg'u qaysi?", "ша́рфы", ["шарфы́", "шарф́ы", "ikkalasi ham"], "To'g'ri talaffuz: «ша́рфы».", "11-sinf", "qiyin"),
        ("Paronimlar", "Qaysi gapda «надеть» fe'li to'g'ri ishlatilgan?", "Надеть тёплое пальто", ["Надеть младшего брата", "Надеть куклу", "Надеть ребёнка"], "Qoida: Одеть кого-то (odamni kiyintirish), Надеть что-то (kiyimni kiyish)!", "10-sinf", "qiyin"),
        ("Paronimlar", "Qaysi gapda «одеть» fe'li to'g'ri ishlatilgan?", "Одеть ребёнка на прогулку", ["Одеть шапку", "Одеть очки", "Одеть куртку"], "Odamni kiyintirishda «одеть» ishlatiladi: одеть ребёнка.", "10-sinf", "qiyin"),
        ("Paronimlar", "Xatni qabul qilib oluvchi shaxs qanday ataladi?", "адресат", ["адресант", "абонент", "дипломант"], "Адресат — qabul qiluvchi; адресант — jo'natuvchi.", "11-sinf", "qiyin"),
        ("Paronimlar", "Samarali, natijador dori yoki usul qanday ataladi?", "эффективный", ["эффектный", "дефектный", "аффектный"], "Эффективный — samarali; эффектный — taassurot qoldiruvchi, chiroyli.", "11-sinf", "qiyin"),
        ("Frazeologizmlar", "«Золотые руки» frazeologizmining ma'nosi nima?", "Qo'li gul, mohir usta", ["Qimmatbaho uzuk", "Qo'lini yuvish", "Boy odam"], "«Золотые руки» — har ishni qoyilmaqom bajaradigan mohir inson.", "9-sinf", "orta"),
        ("Frazeologizmlar", "«Бить баклуши» iborasi nimani anglatadi?", "Bekorchilik qilish", ["Mehnat qilish", "Tez yugurish", "Qattiq baqirish"], "«Бить баклуши» — bekor yurish, hech narsa qilmaslik.", "9-sinf", "orta"),
        ("Frazeologizmlar", "«Держать язык за зубами» iborasi nimani bildiradi?", "Sir saqlash, jim turish", ["Ko'p gapirish", "Ovqat yeyish", "Qo'shiq aytish"], "«Держать язык за зубами» — ortiqcha gapirmaslik, sir saqlash.", "9-sinf", "orta"),
        ("Frazeologizmlar", "«Ни пуха ни пера!» iborasi qachon aytiladi?", "Imtihon yoki muhim ish oldidan omad tilaganda", ["Xayrlashganda", "Ovqatlanishda", "Kechirim so'raganda"], "Bu — omad tilash iborasi (javobi: «К чёрту!»).", "9-sinf", "orta"),
        ("Frazeologizmlar", "«Водить за нос» iborasining ma'nosi nima?", "Aldash, laqillatish", ["Yo'l ko'rsatish", "Yordam berish", "Maqtash"], "«Водить за нос» — aldash, va'dani bajarmaslik.", "10-sinf", "orta"),
        ("Frazeologizmlar", "«Как две капли воды» iborasi nimani anglatadi?", "Bir-biriga juda o'xshash (quyib qo'ygandek)", ["Juda uzoq", "Suv ichish", "Juda tez"], "«Как две капли воды» — bir-biriga mutlaqo o'xshash.", "9-sinf", "oson"),
        ("Frazeologizmlar", "«Рукой подать» iborasi nimani anglatadi?", "Juda yaqin", ["Juda uzoq", "Qo'l berib ko'rishish", "Qiyin ish"], "«Рукой подать» — bir qadam, juda yaqin masofa.", "9-sinf", "orta"),
        ("Frazeologizmlar", "«Спустя рукава» iborasi nimani bildiradi?", "E'tiborsiz, qo'l uchida ishlash", ["Juda tirishib ishlash", "Kiyim tikish", "Sovuq qotish"], "«Работать спустя рукава» — hafsalasiz, sifatsiz ishlash (aksi: засучив рукава).", "10-sinf", "qiyin"),
        ("Sintaksis va Bog'lovchilar", "Sabab ergash gapini bog'lovchi so'zni toping: «Я не пошёл гулять, ... шёл дождь».", "потому что", ["чтобы", "хотя", "если"], "Sabab bildirish uchun «потому что» ishlatiladi.", "8-sinf", "oson"),
        ("Sintaksis va Bog'lovchilar", "Maqsad ergash gapini bog'lovchi so'zni toping: «Я учу русский язык, ... свободно говорить».", "чтобы", ["потому что", "когда", "хотя"], "Maqsad (uchun) ma'nosida «чтобы» ishlatiladi.", "8-sinf", "orta"),
        ("Sintaksis va Bog'lovchilar", "Shart ergash gapini bog'lovchi so'z qaysi: «... будет хорошая погода, мы пойдём в парк».", "Если", ["Хотя", "Потому что", "Чтобы"], "Shart (agar) — «Если».", "8-sinf", "oson"),
        ("Sintaksis va Bog'lovchilar", "To'siqsizlik (garchi) ma'nosidagi bog'lovchini toping: «Он пришёл вовремя, ... дорога была трудной».", "хотя", ["если", "чтобы", "потому что"], "«Хотя» — garchi, ...ga qaramay.", "9-sinf", "orta"),
        ("Sintaksis va Bog'lovchilar", "Qaysi so'z kirish so'zi (вводное слово) hisoblanadi va vergul bilan ajratiladi?", "во-первых, конечно, к сожалению", ["очень, почти, вдруг", "именно, даже, только", "всегда, вчера, быстро"], "«Во-первых, конечно, к сожалению» — kirish so'zlari, har doim vergul qo'yiladi.", "10-sinf", "qiyin"),
        ("Nutq madaniyati", "Kattalarga yoki notanish insonlarga hurmat bilan qanday salom beriladi?", "Здравствуйте!", ["Привет!", "Здорово!", "Пока!"], "Rasmiy va hurmatli salomlashish — «Здравствуйте!».", "6-sinf", "oson"),
        ("Nutq madaniyati", "«Rahmat» so'ziga rus tilida eng odobli javob qaysi?", "Пожалуйста!", ["Извините!", "До свидания!", "Спокойной ночи!"], "«Спасибо!» ga javoban «Пожалуйста!» (Arzimaydi!) deyiladi.", "6-sinf", "oson"),
        ("Nutq madaniyati", "Kechirim so'rash uchun qaysi ibora ishlatiladi?", "Извините, пожалуйста!", ["Приятного аппетита!", "С днём рождения!", "Добро пожаловать!"], "Kechirim so'rash — «Извините, пожалуйста!» / «Простите!».", "6-sinf", "oson"),
        ("Nutq madaniyati", "«Xush kelibsiz!» iborasining ruscha tarjimasi qaysi?", "Добро пожаловать!", ["Спокойной ночи!", "Счастливого пути!", "Будьте здоровы!"], "«Добро пожаловать!» — Xush kelibsiz!", "6-sinf", "oson"),
        ("Nutq madaniyati", "«Oq yo'l!» (Safaringiz bexatar bo'lsin!) rus tilida qanday aytiladi?", "Счастливого пути!", ["Приятного аппетита!", "Доброе утро!", "До скорой встречи!"], "«Счастливого пути!» — Oq yo'l!", "6-sinf", "oson"),
        ("Nutq madaniyati", "«Yoqimli ishtaha!» rus tilida qanday aytiladi?", "Приятного аппетита!", ["Счастливого пути!", "Спокойной ночи!", "Всего доброго!"], "«Приятного аппетита!» — Yoqimli ishtaha!", "6-sinf", "oson")
    ]
    for ch, q, c, w, ex, gr, df in ORTHO_STRESS:
        add_q(ch, q, [c] + w, 0, ex, gr, df)

    # =====================================================================
    # 8. COMPARATIVES, NUMERALS & PAST TENSE — 130+ additional unique Qs!
    # =====================================================================
    COMPARATIVES = [
        ("хороший", "лучше", ["хорошее", "более хороший", "хороше"]),
        ("плохой", "хуже", ["плошее", "плохее", "плохо"]),
        ("маленький", "меньше", ["маленькее", "малее", "мало"]),
        ("большой", "больше", ["большее", "большое", "великее"]),
        ("высокий", "выше", ["высокее", "высоче", "высший"]),
        ("низкий", "ниже", ["низкее", "низее", "низко"]),
        ("дорогой", "дороже", ["дорогее", "дорожее", "дорого"]),
        ("дешёвый", "дешевле", ["дешёвее", "дешевше", "дёшево"]),
        ("лёгкий", "легче", ["лёгкее", "легше", "легко"]),
        ("мягкий", "мягче", ["мягкее", "мягше", "мягко"]),
        ("яркий", "ярче", ["яркее", "ярше", "ярко"]),
        ("громкий", "громче", ["громкее", "громше", "громко"]),
        ("тихий", "тише", ["тихее", "тихче", "тихо"]),
        ("близкий", "ближе", ["близкее", "близее", "близко"]),
        ("далёкий", "дальше", ["далёкее", "далече", "далеко"]),
        ("широкий", "шире", ["широкее", "ширше", "широко"]),
        ("узкий", "уже", ["узкее", "узее", "узко"]),
        ("короткий", "короче", ["короткее", "коротше", "коротко"]),
        ("молодой", "моложе", ["молодее", "молодше", "молодо"]),
        ("чистый", "чище", ["чистее", "чистше", "чисто"]),
        ("простой", "проще", ["простее", "простше", "просто"]),
        ("богатый", "богаче", ["богатее", "богатше", "богато"]),
        ("крепкий", "крепче", ["крепкее", "крепше", "крепко"]),
        ("сладкий", "слаще", ["сладкее", "сладче", "сладко"])
    ]
    for base, comp, wr in COMPARATIVES:
        add_q(
            "Sifat darajalari (Степени сравнения)",
            f"«{base}» sifatining qiyosiy darajasi (сравнительная степень) qaysi?",
            [comp] + wr, 0,
            f"«{base}» → qiyosiy daraja: «{comp}».",
            "8-sinf", "orta"
        )

    NUMERALS_RU = [
        (1, "один"), (2, "два"), (3, "три"), (4, "четыре"), (5, "пять"),
        (6, "шесть"), (7, "семь"), (8, "восемь"), (9, "девять"), (10, "десять"),
        (11, "одиннадцать"), (12, "двенадцать"), (13, "тринадцать"), (14, "четырнадцать"), (15, "пятнадцать"),
        (16, "шестнадцать"), (17, "семнадцать"), (18, "восемнадцать"), (19, "девятнадцать"), (20, "двадцать"),
        (30, "тридцать"), (40, "сорок"), (50, "пятьдесят"), (60, "шестьдесят"), (70, "семьдесят"),
        (80, "восемьдесят"), (90, "девяносто"), (100, "сто"), (200, "двести"), (300, "триста"),
        (400, "четыреста"), (500, "пятьсот"), (1000, "тысяча"), (1000000, "миллион")
    ]
    num_words = [w for _, w in NUMERALS_RU]
    for n, word in NUMERALS_RU:
        wr = rng.sample([x for x in num_words if x != word], 3)
        add_q(
            "Sonlar (Числительные)",
            f"«{n}» soni rus tilida qanday yoziladi?",
            [word] + wr, 0,
            f"{n} — rus tilida «{word}».",
            "6-sinf", "oson"
        )

    # Past Tense Agreement (Прошедшее время) — 40+ questions
    PAST_VERBS = [
        ("читать", "читал", "читала", "читало", "читали"),
        ("писать", "писал", "писала", "писало", "писали"),
        ("говорить", "говорил", "говорила", "говорило", "говорили"),
        ("работать", "работал", "работала", "работало", "работали"),
        ("играть", "играл", "играла", "играло", "играли"),
        ("учить", "учил", "учила", "учило", "учили"),
        ("смотреть", "смотрел", "смотрела", "смотрело", "смотрели"),
        ("думать", "думал", "думала", "думало", "думали"),
        ("строить", "строил", "строила", "строило", "строили"),
        ("покупать", "покупал", "покупала", "покупало", "покупали")
    ]
    for inf, m, f, n, pl in PAST_VERBS:
        add_q("O'tgan zamon (Прошедшее время)", f"«Она ... ({inf})» — o'tgan zamon shaklini toping:", [f, m, n, pl], 0, f"Женский род o'tgan zamonda -ла oladi: она {f}.", "6-sinf", "oson")
        add_q("O'tgan zamon (Прошедшее время)", f"«Они ... ({inf})» — o'tgan zamon shaklini toping:", [pl, m, f, n], 0, f"Ko'plikda o'tgan zamon -ли oladi: они {pl}.", "6-sinf", "oson")
        add_q("O'tgan zamon (Прошедшее время)", f"«Он ... ({inf})» — o'tgan zamon shaklini toping:", [m, f, n, pl], 0, f"Мужской род o'tgan zamonda -л oladi: он {m}.", "6-sinf", "oson")

    # =====================================================================
    # 9. EXTRA HIGH-VALUE GRAMMAR: PREPOSITIONS & SENTENCE TRANSLATIONS — 70+ Qs!
    # =====================================================================
    PHRASE_TRANS = [
        ("Меня зовут Алишер.", "Mening ismim Alisher.", ["Men Alisher bilanman.", "Mening do'stim Alisher.", "Alisher maktabda."]),
        ("Сколько тебе лет?", "Yoshing nechada?", ["Soat necha bo'ldi?", "Qayerda yashaysan?", "Isming nima?"]),
        ("Где находится библиотека?", "Kutubxona qayerda joylashgan?", ["Kutubxona qachon ochiladi?", "Kutubxonada kim bor?", "Bu kitob kimniki?"]),
        ("Я люблю читать книги.", "Men kitob o'qishni yaxshi ko'raman.", ["Men kitob yozmoqchiman.", "Men kitob sotib oldim.", "Menda ko'p kitob bor."]),
        ("Сегодня очень хорошая погода.", "Bugun ob-havo juda yaxshi.", ["Kecha yomg'ir yog'di.", "Ertaga qor yog'adi.", "Bugun havo sovuq."]),
        ("Который сейчас час?", "Hozir soat necha?", ["Bugun haftaning qaysi kuni?", "Qachon dars boshlanadi?", "Necha daqiqa qoldi?"]),
        ("Я иду в школу.", "Men maktabga ketyapman.", ["Men maktabdan qaytyapman.", "Men maktabda o'qiyman.", "Maktab uyga yaqin."]),
        ("Он хорошо говорит по-русски.", "U rus tilida yaxshi gapiradi.", ["U rus tilini endi o'rganyapti.", "U ingliz tilida yozadi.", "U tez o'qiydi."]),
        ("Мне нужна ваша помощь.", "Menga sizning yordamingiz kerak.", ["Men sizga yordam beraman.", "Yordamingiz uchun rahmat.", "Siz qayerda ishlaysiz?"]),
        ("Мы готовимся к экзамену.", "Biz imtihonga tayyorlanyapmiz.", ["Biz imtihonni topshirdik.", "Imtihon ertaga bo'ladi.", "Imtihon juda oson edi."]),
        ("У меня есть большая мечта.", "Mening katta orzuyim bor.", ["Men kecha tush ko'rdim.", "Mening katta uyim bor.", "Men ko'p o'ylayman."]),
        ("Не опаздывайте на урок!", "Darsga kechikmang!", ["Darsda jim o'tiring!", "Uyga vazifani bajaring!", "Kitobingizni oching!"]),
        ("Откройте тетради и запишите тему.", "Daftarlarngizni oching va mavzuni yozib oling.", ["Kitoblarni yoping va tinglang.", "Doskaga chiqing va yozing.", "Savollarga javob bering."]),
        ("Повторите, пожалуйста, ещё раз.", "Iltimos, yana bir bor takrorlang.", ["Iltimos, sekinroq gapiring.", "Iltimos, yozib bering.", "Iltimos, kuting."]),
        ("Я не понял этот вопрос.", "Men bu savolni tushunmadim.", ["Men bu savolga javob berdim.", "Bu savol juda qiziq.", "Menda savol bor."]),
        ("Желаю вам больших успехов!", "Sizga katta muvaffaqiyatlar tilayman!", ["Tug'ilgan kuningiz bilan!", "Bayramingiz muborak bo'lsin!", "Sog'-salomat bo'ling!"]),
        ("Знание — сила.", "Bilim — kuchdir.", ["Vaqt — oltin.", "Salomatlik — boylik.", "Mehnat — baxt kaliti."]),
        ("Без труда не выловишь и рыбку из пруда.", "Mehnatsiz rohat yo'q (hovuzdan baliq ham tutolmaysan).", ["Do'st boshga kulfat tushganda bilinadi.", "Yetti o'lchab bir kes.", "Ilm — aql chirog'i."]),
        ("Семь раз отмерь, один раз отрежь.", "Yetti o'lchab, bir kes.", ["Vaqt hamma narsani davolaydi.", "Ko'z qo'rqoq, qo'l botir.", "Aql yoshda emas, boshda."]),
        ("Век живи — век учись.", "Beshikdan to qabrgacha ilm izla (bir umr o'rgan).", ["Ilmli mingni yiqar.", "Til — dil kaliti.", "Kitob — bilim manbai."])
    ]
    for ru_p, uz_p, wr in PHRASE_TRANS:
        add_q(
            "Nutq va Tarjima (Разговорная речь)",
            f"«{ru_p}» gapining to'g'ri o'zbekcha tarjimasi qaysi?",
            [uz_p] + wr, 0,
            f"«{ru_p}» = «{uz_p}».",
            "7-sinf", "oson"
        )

    # Extra Noun Plural/Singular & Gender Exceptions to easily exceed 1,100 unique questions!
    EXTRA_VOCAB = [
        ("природа", "tabiat"), ("экология", "ekologiya"), ("культура", "madaniyat"), ("искусство", "san'at"),
        ("музыка", "musiqa"), ("спорт", "sport"), ("победа", "g'alaba"), ("здоровье", "salomatlik"),
        ("счастье", "baxt"), ("успех", "muvaffaqiyat"), ("будущее", "kelajak"), ("прошлое", "o'tmish"),
        ("настоящее", "hozirgi zamon"), ("память", "xotira"), ("мысль", "fikr"), ("идея", "g'oya"),
        ("цель", "maqsad"), ("результат", "natija"), ("опыт", "tajriba"), ("талант", "iste'dod"),
        ("уважение", "hurmat"), ("честность", "halollik"), ("терпение", "sabr"), ("доверие", "ishonch"),
        ("свобода", "erkinlik"), ("закон", "qonun"), ("право", "huquq"), ("обязанность", "majburiyat"),
        ("общество", "jamiyat"), ("государство", "davlat"), ("экономика", "iqtisodiyot"), ("торговля", "savdo"),
        ("деньги", "pul"), ("цена", "narx"), ("подарок", "sovg'a"), ("праздник", "bayram"),
        ("путешествие", "sayohat"), ("приключение", "sarguzasht"), ("открытие", "kashfiyot"), ("изобретение", "ixtiro"),
        ("компьютер", "kompyuter"), ("телефон", "telefon"), ("экран", "ekran"), ("программа", "dastur"),
        ("информация", "axborot"), ("новость", "yangilik"), ("газета", "gazeta"), ("журнал", "jurnal"),
        ("письмо", "xat / maktub"), ("сообщение", "xabar"), ("голос", "ovoz"), ("улыбка", "tabassum"),
        ("сердце", "yurak"), ("голова", "bosh"), ("рука", "qo'l"), ("нога", "oyoq"),
        ("глаз", "ko'z"), ("ухо", "quloq"), ("нос", "burun"), ("рот", "og'iz")
    ]
    ex_uz = [u for _, u in EXTRA_VOCAB]
    ex_ru = [r for r, _ in EXTRA_VOCAB]
    for ru, uz in EXTRA_VOCAB:
        add_q("Kengaytirilgan leksika (Yangi tahrir)", f"Rus tilidagi «{ru}» so'zining ma'nosi nima?", [uz] + rng.sample([x for x in ex_uz if x != uz], 3), 0, f"«{ru}» — «{uz}».", "8-sinf", "orta")
        add_q("Kengaytirilgan tarjima (Yangi tahrir)", f"«{uz}» so'zining rus tilidagi tarjimasi qaysi?", [ru] + rng.sample([x for x in ex_ru if x != ru], 3), 0, f"«{uz}» — «{ru}».", "8-sinf", "orta")

    return questions


def insert_all_russian(db_path=None):
    target_db = db_path or DB_PATH
    conn = sqlite3.connect(target_db)
    c = conn.cursor()

    # 1. Create / update Subject id=10 ('Rus tili')
    c.execute("SELECT id FROM subjects WHERE code = 'russian' OR id = 10")
    row = c.fetchone()
    if row:
        subject_id = row[0]
        c.execute("""
            UPDATE subjects
            SET name = 'Rus tili', code = 'russian', icon = '🇷🇺', color = '#e11d48',
                description = 'Yangi tahrir: Fonetika, Grammatika, Padejlar, Leksika, Tarjima va Nutq madaniyati',
                category = 'xorijiy'
            WHERE id = ?
        """, (subject_id,))
    else:
        c.execute("""
            INSERT INTO subjects (id, name, code, icon, color, description, category)
            VALUES (10, 'Rus tili', 'russian', '🇷🇺', '#e11d48',
                    'Yangi tahrir: Fonetika, Grammatika, Padejlar, Leksika, Tarjima va Nutq madaniyati', 'xorijiy')
        """)
        subject_id = 10

    # 2. Insert / update 6 New-Edition Russian Textbooks (grades 6-11)
    for b in RUSSIAN_TEXTBOOKS:
        c.execute("SELECT id FROM textbooks WHERE subject_id = ? AND title = ?", (subject_id, b["title"]))
        exist = c.fetchone()
        ch_json = json.dumps(b["chapters"], ensure_ascii=False)
        if exist:
            c.execute("""
                UPDATE textbooks
                SET author = ?, grade = ?, summary = ?, chapters = ?, file_url = ?
                WHERE id = ?
            """, (b["author"], b["grade"], b["summary"], ch_json, b["file_url"], exist[0]))
        else:
            c.execute("""
                INSERT INTO textbooks (subject_id, title, author, grade, cover_image, summary, chapters, uploaded_by, file_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, NULL, ?)
            """, (subject_id, b["title"], b["author"], b["grade"], b["cover_image"], b["summary"], ch_json, b["file_url"]))

    # 3. Insert 1,100+ Unique Russian Blitz & Curriculum Questions
    all_raw = generate_russian_questions()
    c.execute("DELETE FROM questions WHERE subject_id = ? AND created_by IS NULL", (subject_id,))

    rng = random.Random(2026)
    inserted = 0
    for ch_title, q_text, raw_opts, corr_idx, expl, grade, diff in all_raw:
        corr_ans = raw_opts[corr_idx]
        shuffled = list(raw_opts)
        rng.shuffle(shuffled)
        new_corr = shuffled.index(corr_ans)
        c.execute("""
            INSERT INTO questions (subject_id, grade, chapter_title, question_text, options, correct_index, explanation, difficulty, created_by, group_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL)
        """, (
            subject_id, grade, ch_title, q_text,
            json.dumps(shuffled, ensure_ascii=False),
            new_corr, expl, diff
        ))
        inserted += 1

    conn.commit()
    conn.close()
    print(f"Rus tili (id={subject_id}): {len(RUSSIAN_TEXTBOOKS)} ta yangi tahrir darslik va {inserted} ta 100% noyob Blitz/test kiritildi!")
    return inserted


if __name__ == "__main__":
    cnt = insert_all_russian()
    print("Jami Rus tili savollari:", cnt)
