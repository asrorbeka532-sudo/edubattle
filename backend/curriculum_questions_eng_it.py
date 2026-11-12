# -*- coding: utf-8 -*-
"""
EduBattle - 2020-2023 Yangi darsliklar asosidagi savollar banki:
Fan 7: Ingliz tili (6-11-sinf CEFR A1-B2) - 50 ta savol
Fan 8: Informatika va IT (6-11-sinf yangi dastur: Python, algoritmlar, tarmoqlar, kiberxavfsizlik, SQL) - 50 ta savol
"""

# ==========================================
# 7. INGLIZ TILI (Subject ID: 7) - 50 TA SAVOL
# ==========================================
INGLIZ_TILI_QUESTIONS = [
    # 6-sinf (A1-A2)
    {
        "subject_id": 7,
        "grade": "6-sinf",
        "chapter_title": "Present Simple vs Continuous",
        "question_text": "Look! The children ________ football in the school yard right now.",
        "options": ["are playing", "plays", "played", "is playing"],
        "correct_index": 0,
        "explanation": "'Look!' va 'right now' ayni paytda sodir bo'layotgan ish-harakatni bildiradi (Present Continuous). Ega 'The children' ko'plikda, shuning uchun 'are playing'.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "6-sinf",
        "chapter_title": "Present Simple",
        "question_text": "My father usually ________ to work by bus every morning.",
        "options": ["goes", "go", "is going", "went"],
        "correct_index": 0,
        "explanation": "Odat tusiga kirgan takroriy harakat (usually, every morning) Present Simple da beriladi. 3-shaxs birlik uchun fe'lga -es qo'shiladi: 'goes'.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "6-sinf",
        "chapter_title": "Past Simple",
        "question_text": "We ________ a very interesting documentary about wild animals yesterday.",
        "options": ["watched", "watch", "are watching", "watches"],
        "correct_index": 0,
        "explanation": "'Yesterday' o'tgan zamon kalit so'zi bo'lib, to'g'ri fe'llarga -ed qo'shiladi: 'watched'.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "6-sinf",
        "chapter_title": "Comparative Adjectives",
        "question_text": "An elephant is much ________ than a lion.",
        "options": ["bigger", "big", "biggest", "more big"],
        "correct_index": 0,
        "explanation": "Bir bo'g'inli sifatlarning qiyosiy darajasi -er qo'shimchasi bilan yasaladi: 'bigger'.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "6-sinf",
        "chapter_title": "Prepositions of Time",
        "question_text": "Our English class starts ________ 9 o'clock in the morning.",
        "options": ["at", "in", "on", "to"],
        "correct_index": 0,
        "explanation": "Aniq vaqtlar (soatlar) oldidan har doim 'at' predlogi ishlatiladi (at 9 o'clock).",
        "difficulty": "oson"
    },
    # 7-sinf (A2)
    {
        "subject_id": 7,
        "grade": "7-sinf",
        "chapter_title": "Past Continuous vs Past Simple",
        "question_text": "While I ________ my homework, the telephone suddenly rang.",
        "options": ["was doing", "did", "am doing", "were doing"],
        "correct_index": 0,
        "explanation": "O'tgan zamonda davom etayotgan harakat (Past Continuous) paytida qisqa harakat (Past Simple) ro'y berganda 'while + was/were doing' ishlatiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "7-sinf",
        "chapter_title": "Present Perfect",
        "question_text": "I ________ to London three times so far.",
        "options": ["have been", "went", "am", "has been"],
        "correct_index": 0,
        "explanation": "Hayotiy tajriba va 'so far' ko'rsatkichi uchun Present Perfect (have + V3): 'have been'.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "7-sinf",
        "chapter_title": "Modal Verbs",
        "question_text": "You ________ drive without a seatbelt. It is strictly against the law.",
        "options": ["mustn't", "don't have to", "can", "should"],
        "correct_index": 0,
        "explanation": "Qonuniy qat'iy taqiq uchun 'mustn't' ishlatiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "7-sinf",
        "chapter_title": "Future Intentions",
        "question_text": "Look at those dark clouds! It ________ rain soon.",
        "options": ["is going to", "will", "rains", "is raining"],
        "correct_index": 0,
        "explanation": "Ayni paytda ko'rinib turgan dalil (dark clouds) asosida kelajakni bashorat qilishda 'be going to' qo'llaniladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "7-sinf",
        "chapter_title": "Superlative Adjectives",
        "question_text": "Mount Everest is ________ mountain in the entire world.",
        "options": ["the highest", "higher", "highest", "most high"],
        "correct_index": 0,
        "explanation": "Orttirma darajada sifat oldiga 'the' artikli va -est qo'shimchasi qo'yiladi: 'the highest'.",
        "difficulty": "oson"
    },
    # 8-sinf (A2-B1)
    {
        "subject_id": 7,
        "grade": "8-sinf",
        "chapter_title": "Zero and First Conditionals",
        "question_text": "If it ________ tomorrow, we will postpone the outdoor picnic.",
        "options": ["rains", "will rain", "rained", "is raining"],
        "correct_index": 0,
        "explanation": "First Conditional shart qismida (if clause) Future Simple emas, balki Present Simple ishlatiladi: 'rains'.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "8-sinf",
        "chapter_title": "Passive Voice - Present Simple",
        "question_text": "English ________ by millions of people all around the world.",
        "options": ["is spoken", "speaks", "is speaking", "spoke"],
        "correct_index": 0,
        "explanation": "Ingliz tili gapiriladi (majhul nisbat): be + V3 => 'is spoken'.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "8-sinf",
        "chapter_title": "Gerund vs Infinitive",
        "question_text": "She enjoys ________ classic books in her spare time.",
        "options": ["reading", "to read", "read", "reads"],
        "correct_index": 0,
        "explanation": "'Enjoy' fe'lidan keyin har doim gerund (V-ing) keladi: 'reading'.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "8-sinf",
        "chapter_title": "Relative Pronouns",
        "question_text": "The woman ________ won the prestigious scientific prize is a professor.",
        "options": ["who", "which", "whose", "where"],
        "correct_index": 0,
        "explanation": "Insonlarga (shaxslarga) nisbatan nisbiy olmosh sifatida 'who' ishlatiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "8-sinf",
        "chapter_title": "Present Perfect vs Past Simple",
        "question_text": "I haven't seen my best friend ________ last summer.",
        "options": ["since", "for", "in", "during"],
        "correct_index": 0,
        "explanation": "Harakatning boshlanish nuqtasi (aniq payti) ko'rsatilganda 'since' ishlatiladi ('since last summer').",
        "difficulty": "orta"
    },
    # 9-sinf (B1)
    {
        "subject_id": 7,
        "grade": "9-sinf",
        "chapter_title": "Second Conditional",
        "question_text": "If I ________ a million dollars, I would travel around the world.",
        "options": ["had", "have", "will have", "would have"],
        "correct_index": 0,
        "explanation": "Second Conditional (norasmiy/xayoliy hozirgi zamon): If + Past Simple, would + V1. Shuning uchun 'had'.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "9-sinf",
        "chapter_title": "Past Perfect",
        "question_text": "By the time we arrived at the cinema, the movie ________.",
        "options": ["had already started", "already started", "has started", "starts"],
        "correct_index": 0,
        "explanation": "O'tgan zamondagi boshqa bir harakatdan oldin sodir bo'lgan ish-harakat uchun Past Perfect (had + V3) ishlatiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "9-sinf",
        "chapter_title": "Reported Speech",
        "question_text": "He said: 'I am learning German.' -> He said that he ________ German.",
        "options": ["was learning", "is learning", "had learned", "learns"],
        "correct_index": 0,
        "explanation": "O'zlashtirma gapda (Reported Speech) bosh gap o'tgan zamonda bo'lsa, Present Continuous -> Past Continuous ga o'tadi: 'was learning'.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "9-sinf",
        "chapter_title": "Passive Voice - Past Simple",
        "question_text": "The ancient fortress ________ in the 15th century.",
        "options": ["was built", "is built", "built", "has been built"],
        "correct_index": 0,
        "explanation": "O'tgan zamondagi majhul nisbat (Past Simple Passive): was/were + V3 => 'was built'.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "9-sinf",
        "chapter_title": "Phrasal Verbs",
        "question_text": "Please ________ the lights when you leave the conference room.",
        "options": ["turn off", "turn on", "turn into", "turn over"],
        "correct_index": 0,
        "explanation": "Chiroq yoki elektr moslamalarini o'chirish iboraviy fe'li 'turn off' hisoblanadi.",
        "difficulty": "oson"
    },
    # 10-sinf (B1-B2)
    {
        "subject_id": 7,
        "grade": "10-sinf",
        "chapter_title": "Third Conditional",
        "question_text": "If she had studied harder for the exam, she ________ passed it successfully.",
        "options": ["would have", "would", "will have", "had"],
        "correct_index": 0,
        "explanation": "Third Conditional (o'tgan zamonda ro'y bermagan afsus/natija): If + had + V3, would have + V3.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 7,
        "grade": "10-sinf",
        "chapter_title": "Modal Verbs of Deduction",
        "question_text": "He ________ be at home because all his lights are turned off and his car is gone.",
        "options": ["can't", "must", "should", "might not"],
        "correct_index": 0,
        "explanation": "Mantiqiy inkor xulosa (bo'lishi mutlaqo mumkin emas) uchun 'can't be' ishlatiladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "10-sinf",
        "chapter_title": "Causative Form",
        "question_text": "I didn't repair my laptop myself; I had it ________ by a certified specialist.",
        "options": ["repaired", "repair", "to repair", "repairing"],
        "correct_index": 0,
        "explanation": "Causative structure: have + object + V3 (have something done) => 'had it repaired'.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "10-sinf",
        "chapter_title": "Articles",
        "question_text": "________ Amazon is the second longest river in the world.",
        "options": ["The", "A", "An", "- (no article)"],
        "correct_index": 0,
        "explanation": "Daryo, dengiz va okean nomlari oldidan aniq artikl 'the' qo'yiladi (The Amazon).",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "10-sinf",
        "chapter_title": "Wishes and Regrets",
        "question_text": "I don't have enough free time. I wish I ________ more time to read literature.",
        "options": ["had", "have", "would have", "had had"],
        "correct_index": 0,
        "explanation": "Hozirgi paytdagi istak yoki afsus (Wish about present): I wish + Past Simple => 'I wish I had'.",
        "difficulty": "orta"
    },
    # 11-sinf (B2)
    {
        "subject_id": 7,
        "grade": "11-sinf",
        "chapter_title": "Inversion with Negative Adverbials",
        "question_text": "Seldom ________ such an extraordinary and inspiring musical performance.",
        "options": ["have I witnessed", "I have witnessed", "did I witness", "I witnessed"],
        "correct_index": 0,
        "explanation": "Gap inkor ma'noli so'zlar (Seldom, Rarely, Never) bilan boshlanganda inversiya bo'ladi: yordamchi fe'l egadan oldinga chiqadi.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 7,
        "grade": "11-sinf",
        "chapter_title": "Subjunctive / Formal English",
        "question_text": "The doctor strongly recommended that the patient ________ more rest.",
        "options": ["take", "takes", "took", "is taking"],
        "correct_index": 0,
        "explanation": "Present Subjunctive qoidasiga ko'ra (recommend, suggest, insist that...) fe'l boshlang'ich yalang'och shaklda (bare infinitive) bo'ladi: 'take'.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 7,
        "grade": "11-sinf",
        "chapter_title": "Mixed Conditionals",
        "question_text": "If I had taken your advice yesterday, I ________ in this awkward situation now.",
        "options": ["wouldn't be", "wouldn't have been", "won't be", "am not"],
        "correct_index": 0,
        "explanation": "Mixed conditional: shart o'tgan zamonga tegishli (had taken), natija esa hozirgi paytga (now) => 'wouldn't be'.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 7,
        "grade": "11-sinf",
        "chapter_title": "Participle Clauses",
        "question_text": "________ the crucial contract, the manager shook hands with the clients.",
        "options": ["Having signed", "Signed", "To sign", "Being signed"],
        "correct_index": 0,
        "explanation": "Bir harakat ikkinchisidan oldin tugallanganini ifodalovchi Perfect Participle: 'Having signed'.",
        "difficulty": "qiyin"
    },
    {
        "subject_id": 7,
        "grade": "11-sinf",
        "chapter_title": "Dependent Prepositions",
        "question_text": "The company is committed ________ improving customer satisfaction.",
        "options": ["to", "for", "with", "in"],
        "correct_index": 0,
        "explanation": "'To be committed to doing something' iborasida 'to' predlog bo'lib, o'zidan keyin gerund oladi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "6-sinf",
        "chapter_title": "Possessive Pronouns",
        "question_text": "This is not my dictionary. It belongs to Sarah, so it is ________.",
        "options": ["hers", "her", "she", "herself"],
        "correct_index": 0,
        "explanation": "Ot qatnashmagan mustaqil egalik olmoshi 'hers' (uning o'ziniki) bo'ladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "7-sinf",
        "chapter_title": "Indefinite Pronouns",
        "question_text": "Did ________ call me while I was out of the office?",
        "options": ["anyone", "someone", "no one", "everyone"],
        "correct_index": 0,
        "explanation": "So'roq gaplarda odatda 'anyone' ishlatiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "8-sinf",
        "chapter_title": "Used to",
        "question_text": "When I was in primary school, I ________ play chess every afternoon.",
        "options": ["used to", "use to", "am used to", "get used to"],
        "correct_index": 0,
        "explanation": "O'tmishda muntazam qilingan, ammo hozir to'xtagan odat uchun 'used to + V1' ishlatiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "9-sinf",
        "chapter_title": "Question Tags",
        "question_text": "You haven't finished your project yet, ________?",
        "options": ["have you", "haven't you", "did you", "do you"],
        "correct_index": 0,
        "explanation": "Dastlabki qism inkor (haven't finished) bo'lsa, tag-question tasdiq (have you) bo'ladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "10-sinf",
        "chapter_title": "Phrasal Verbs - Idiomatic",
        "question_text": "I am really looking forward ________ you at the international conference next week.",
        "options": ["to seeing", "to see", "see", "seeing"],
        "correct_index": 0,
        "explanation": "'Look forward to' birikmasidagi 'to' predlog hisoblanadi, shuning uchun 'to seeing' gerund shakli to'g'ri.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "11-sinf",
        "chapter_title": "Advanced Vocabulary",
        "question_text": "The synonym of the adjective 'meticulous' is ________.",
        "options": ["extremely careful and precise", "careless and hasty", "boring and dull", "very generous"],
        "correct_index": 0,
        "explanation": "'Meticulous' juda sinchkov, mayda detallargacha e'tibor beruvchi (thorough, precise) degan ma'noni anglatadi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "8-sinf",
        "chapter_title": "Too vs Enough",
        "question_text": "The tea is ________ hot to drink right away. Let it cool down.",
        "options": ["too", "enough", "such", "very much"],
        "correct_index": 0,
        "explanation": "'Too + adjective + to do something' me'yordan ortiq darajada ekanligini bildiradi (ichish uchun o'ta qaynoq).",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "9-sinf",
        "chapter_title": "Both / Either / Neither",
        "question_text": "Neither my brother nor my parents ________ at home right now.",
        "options": ["are", "is", "was", "be"],
        "correct_index": 0,
        "explanation": "'Neither... nor' birikmasida fe'l ikkinchi subyektga moslashadi. 'Parents' ko'plikda bo'lgani uchun 'are' to'g'ri.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "10-sinf",
        "chapter_title": "Modal Perfect",
        "question_text": "You ________ have told him the confidential secret! Now everyone knows.",
        "options": ["shouldn't", "mustn't", "couldn't", "may not"],
        "correct_index": 0,
        "explanation": "O'tgan zamondagi noto'g'ri qilingan ishga nisbatan afsus yoki tanbeh bildirish: shouldn't have + V3.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "6-sinf",
        "chapter_title": "Countable vs Uncountable",
        "question_text": "Could you please give me ________ advice on how to improve my pronunciation?",
        "options": ["some", "an", "many", "a few"],
        "correct_index": 0,
        "explanation": "'Advice' so'zi sanalmaydigan ot bo'lib, uning oldidan 'an' yoki 'many' ishlatilmaydi, 'some' to'g'ri.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "7-sinf",
        "chapter_title": "Prepositions of Place",
        "question_text": "The cat is sleeping peacefully ________ the wooden table.",
        "options": ["under", "between", "among", "into"],
        "correct_index": 0,
        "explanation": "'Under the table' - stol ostida ma'nosini bildiradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "11-sinf",
        "chapter_title": "Advanced Conjunctions",
        "question_text": "________ the heavy snowstorm, the airport remained open and flights departed on time.",
        "options": ["Despite", "Although", "Even though", "However"],
        "correct_index": 0,
        "explanation": "'Despite' predlog bo'lib, o'zidan keyin otli iborani (noun phrase) oladi ('Despite the heavy snowstorm').",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "10-sinf",
        "chapter_title": "Passive Voice with Modals",
        "question_text": "All safety regulations must ________ strictly by every employee.",
        "options": ["be followed", "follow", "followed", "be following"],
        "correct_index": 0,
        "explanation": "Modal fe'llar bilan majhul nisbat formulasi: modal + be + V3 => 'must be followed'.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "8-sinf",
        "chapter_title": "Adverbs of Manner",
        "question_text": "He is a fast runner; he runs extremely ________.",
        "options": ["fast", "fastly", "faster", "fastest"],
        "correct_index": 0,
        "explanation": "'Fast' so'zining ravish shakli ham 'fast' bo'lib qoladi ('fastly' so'zi mavjud emas).",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "9-sinf",
        "chapter_title": "Purpose Clauses",
        "question_text": "He got up early in the morning in order ________ catch the first express train.",
        "options": ["to", "that", "for", "as"],
        "correct_index": 0,
        "explanation": "Maqsad ergash gaplarda maqsadni ifodalash uchun 'in order to + V1' qo'llaniladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "11-sinf",
        "chapter_title": "Collocations",
        "question_text": "Scientists frequently ________ complex experiments to test their hypotheses.",
        "options": ["conduct", "make", "create", "construct"],
        "correct_index": 0,
        "explanation": "Ilmiy tajriba o'tkazish barqaror birikmasi 'conduct an experiment' (yoki carry out) hisoblanadi.",
        "difficulty": "orta"
    },
    {
        "subject_id": 7,
        "grade": "6-sinf",
        "chapter_title": "Plural Nouns",
        "question_text": "What is the plural form of the word 'child'?",
        "options": ["children", "childs", "childrens", "childes"],
        "correct_index": 0,
        "explanation": "'Child' so'zining ko'plik shakli noto'g'ri o'zgaradi va 'children' bo'ladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "7-sinf",
        "chapter_title": "Irregular Verbs",
        "question_text": "The past forms (V2 and V3) of the verb 'buy' are ________.",
        "options": ["bought / bought", "buyed / buyed", "brought / brought", "bought / brought"],
        "correct_index": 0,
        "explanation": "'Buy' noto'g'ri fe'li: buy - bought - bought.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "9-sinf",
        "chapter_title": "Vocabulary - Environment",
        "question_text": "The gradual increase in Earth's overall temperature is known as ________.",
        "options": ["global warming", "acid rain", "deforestation", "ozone depletion"],
        "correct_index": 0,
        "explanation": "Yer yuzi o'rtacha haroratining ko'tarilishi 'global warming' (global isish) deb ataladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 7,
        "grade": "11-sinf",
        "chapter_title": "Idioms",
        "question_text": "The English idiom 'a piece of cake' means ________.",
        "options": ["something very easy to do", "a delicious dessert", "a very expensive item", "a secret plan"],
        "correct_index": 0,
        "explanation": "'A piece of cake' iborasi juda oson bajariladigan ishni bildiradi (masalan: The exam was a piece of cake).",
        "difficulty": "oson"
    }
]

# ==========================================
# 8. INFORMATIKA VA IT (Subject ID: 8) - 50 TA SAVOL
# ==========================================
INFORMATIKA_QUESTIONS = [
    # 6-sinf
    {
        "subject_id": 8,
        "grade": "6-sinf",
        "chapter_title": "Axborot va uning o'lchov birliklari",
        "question_text": "1 Bayt (Byte) necha bitga teng?",
        "options": ["8 bit", "10 bit", "1024 bit", "2 bit"],
        "correct_index": 0,
        "explanation": "Axborot o'lchov birliklari asosiga ko'ra 1 Bayt = 8 bit.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "6-sinf",
        "chapter_title": "Axborot o'lchov birliklari",
        "question_text": "1 Kilobayt (KB) necha baytdan iborat?",
        "options": ["1024 bayt", "1000 bayt", "8192 bayt", "512 bayt"],
        "correct_index": 0,
        "explanation": "Informatikada ikkilik tizimga ko'ra 1 KB = 2¹⁰ = 1024 bayt.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "6-sinf",
        "chapter_title": "Kompyuter apparat ta'minoti",
        "question_text": "Kompyuterdagi barcha hisoblash va mantiqiy amallarni bajaruvchi 'bosh miya' qurilma nima?",
        "options": ["Protsessor (CPU)", "Operativ xotira (RAM)", "Qattiq disk (HDD/SSD)", "Monitor"],
        "correct_index": 0,
        "explanation": "Markaziy protsessor (CPU) kompyuterning barcha buyruqlarini qayta ishlaydigan asosiy mikrosxemadir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "6-sinf",
        "chapter_title": "Kiritish va chiqarish qurilmalari",
        "question_text": "Faqat kiritish qurilmalari ko'rsatilgan qatorni aniqlang.",
        "options": ["Klaviatura, sichqoncha, skaner, mikrofon", "Monitor, printer, klaviatura", "Kollonka, plotter, sichqoncha", "Quloqchin, mikrofon, veb-kamera"],
        "correct_index": 0,
        "explanation": "Klaviatura, sichqoncha, skaner va mikrofon axborotni kompyuterga kiritish qurilmalaridir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "6-sinf",
        "chapter_title": "Fayllar va papkalar",
        "question_text": "Matnli hujjat kengaytmasini (formatini) ko'rsating.",
        "options": [".docx / .txt", ".mp3", ".jpg / .png", ".mp4 / .avi"],
        "correct_index": 0,
        "explanation": ".docx va .txt matnli fayllar formati hisoblanadi (.mp3 audio, .jpg rasm, .mp4 video).",
        "difficulty": "oson"
    },
    # 7-sinf
    {
        "subject_id": 8,
        "grade": "7-sinf",
        "chapter_title": "Sanoq sistemalari",
        "question_text": "O'nlik sanoq sistemasidagi 13 sonining ikkilik (binary) sanoq sistemasidagi ko'rinishini toping.",
        "options": ["1101", "1011", "1110", "1100"],
        "correct_index": 0,
        "explanation": "13 sonini 2 ga ketma-ket bo'lamiz: 13/2=6 (qoldiq 1), 6/2=3 (qoldiq 0), 3/2=1 (qoldiq 1), 1/2=0 (qoldiq 1). Qoldiqlarni teskari o'qisak: 1101₂.",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "7-sinf",
        "chapter_title": "Sanoq sistemalari",
        "question_text": "Ikkilik sanoq sistemasidagi 1010₂ soni o'nlik sanoq sistemasida nechaga teng?",
        "options": ["10", "12", "8", "14"],
        "correct_index": 0,
        "explanation": "1*2³ + 0*2² + 1*2¹ + 0*2⁰ = 8 + 0 + 2 + 0 = 10.",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "7-sinf",
        "chapter_title": "Algoritm tushunchasi",
        "question_text": "Algoritmning asosiy xossalarini ko'rsating.",
        "options": ["Diskretlik, tushunarlilik, aniqlik, ommaviylik, natijaviylik", "Faqat tezlik va hajm", "Grafiklik va rangdorlik", "Uzviylik va cheksizlik"],
        "correct_index": 0,
        "explanation": "Algoritm 5 ta asosiy xossaga ega: diskretlik, aniqlik (determinallik), tushunarlilik, ommaviylik va natijaviylik.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "7-sinf",
        "chapter_title": "Algoritm turlari",
        "question_text": "Buyruqlari hech qanday shartsiz ketma-ket birin-ketin bajariladigan algoritm qanday ataladi?",
        "options": ["Chiziqli algoritm", "Tarmoqlanuvchi algoritm", "Takrorlanuvchi (siklik) algoritm", "Murakkab algoritm"],
        "correct_index": 0,
        "explanation": "Amallar qadamma-qadam faqat bitta to'g'ri yo'nalishda bajarilsa, bu chiziqli algoritm deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "7-sinf",
        "chapter_title": "Blok-sxemalar",
        "question_text": "Blok-sxemada shart tekshirish amali (tarmoqlanish) qaysi geometrik shakl bilan ifodalanadi?",
        "options": ["Romb", "To'g'ri to'rtburchak", "Parallelogramm", "Oval"],
        "correct_index": 0,
        "explanation": "Blok-sxemalarda romb shartni tekshirish (ha/yo'q) uchun xizmat qiladi.",
        "difficulty": "oson"
    },
    # 8-sinf (Python asoslari)
    {
        "subject_id": 8,
        "grade": "8-sinf",
        "chapter_title": "Python dasturlash tili",
        "question_text": "Python dasturlash tiliga kim va qaysi yili asos solgan?",
        "options": ["Gvido van Rossum, 1991-yil", "Dennis Ritchi, 1972-yil", "Bjarne Straustrup, 1985-yil", "Jeyms Gosling, 1995-yil"],
        "correct_index": 0,
        "explanation": "Python tilini gollandiyalik dasturchi Gvido van Rossum 1991-yilda yaratgan.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "8-sinf",
        "chapter_title": "Python operatorlari",
        "question_text": "Python tilida butunli bo'lish (butun qismni olish) operatori qaysi?",
        "options": ["//", "/", "%", "**"],
        "correct_index": 0,
        "explanation": "Python da / haqiqiy bo'lish, // butun qismni olish, % qoldiqni olish, ** darajaga ko'tarish.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "8-sinf",
        "chapter_title": "Python amallari",
        "question_text": "Python dasturida print(17 % 5) kodi qanday natija chiqaradi?",
        "options": ["2", "3", "3.4", "1"],
        "correct_index": 0,
        "explanation": "% operatori bo'lishdan qolgan qoldiqni topadi: 17 = 5 * 3 + 2, qoldiq 2.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "8-sinf",
        "chapter_title": "Python ma'lumot turlari",
        "question_text": "Python da type('123') qanday natija qaytaradi?",
        "options": ["<class 'str'>", "<class 'int'>", "<class 'float'>", "<class 'bool'>"],
        "correct_index": 0,
        "explanation": "Qo'shtirnoq yoki bir tirnoq ichiga olingan har qanday qiymat satr (str) hisoblanadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "8-sinf",
        "chapter_title": "Python shart operatori",
        "question_text": "Quyidagi kod natijasini toping:\nx = 10\nif x > 5 and x < 15:\n    print('A')\nelse:\n    print('B')",
        "options": ["A", "B", "AB", "Hech narsa"],
        "correct_index": 0,
        "explanation": "x = 10 bo'lganda 10 > 5 (True) va 10 < 15 (True). Ikkala shart bajarilgani uchun 'A' chop etiladi.",
        "difficulty": "oson"
    },
    # 9-sinf (Python sikllar va to'plamlar)
    {
        "subject_id": 8,
        "grade": "9-sinf",
        "chapter_title": "Python sikllari",
        "question_text": "list(range(2, 8, 2)) ifodasi qanday ro'yxat hosil qiladi?",
        "options": ["[2, 4, 6]", "[2, 4, 6, 8]", "[2, 3, 4, 5, 6, 7]", "[4, 6, 8]"],
        "correct_index": 0,
        "explanation": "range(start=2, stop=8, step=2) 2 dan boshlanib 8 gacha 2 qadam bilan boradi: 2, 4, 6 (8 kirmaydi).",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "9-sinf",
        "chapter_title": "Python ro'yxatlari (List)",
        "question_text": "a = [10, 20, 30, 40]\na.append(50)\nprint(len(a)) kodi qanday natija chiqaradi?",
        "options": ["5", "4", "50", "[10, 20, 30, 40, 50]"],
        "correct_index": 0,
        "explanation": "append(50) ro'yxat oxiriga 50 elementini qo'shadi, natijada elementlar soni len(a) = 5 bo'ladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "9-sinf",
        "chapter_title": "Python satr amallari",
        "question_text": "s = 'EduBattle'\nprint(s[0:3]) qanday natija beradi?",
        "options": ["Edu", "EduB", "Ed", "Battle"],
        "correct_index": 0,
        "explanation": "Slayzing s[0:3] 0, 1 va 2-indeksdagi belgilarni kesib oladi: 'E', 'd', 'u' => 'Edu'.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "9-sinf",
        "chapter_title": "Python funksiyalari",
        "question_text": "Python da foydalanuvchi funksiyasini e'lon qilish qaysi kalit so'z orqali boshlanadi?",
        "options": ["def", "function", "func", "define"],
        "correct_index": 0,
        "explanation": "Python da funksiyalar 'def funksiya_nomi(parametrlar):' sintaksisi bilan yaratiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "9-sinf",
        "chapter_title": "Python lug'atlari (Dict)",
        "question_text": "d = {'olma': 5000, 'anor': 8000}\nprint(d['anor']) kodi nima chiqaradi?",
        "options": ["8000", "5000", "'anor'", "Xatolik beradi"],
        "correct_index": 0,
        "explanation": "Lug'atdan kalit (key) bo'yicha qiymat olinadi: d['anor'] = 8000.",
        "difficulty": "oson"
    },
    # 10-sinf (Kompyuter tarmoqlari va Kiberxavfsizlik)
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "Kompyuter tarmoqlari",
        "question_text": "Bir xona yoki bitta bino doirasida kompyuterlarni birlashtiruvchi lokal tarmoq qanday ataladi?",
        "options": ["LAN (Local Area Network)", "WAN (Wide Area Network)", "MAN (Metropolitan Area Network)", "PAN"],
        "correct_index": 0,
        "explanation": "Lokal hisoblash tarmog'i LAN (Local Area Network) deb ataladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "IP manzillar",
        "question_text": "IPv4 protokolidagi IP-manzil necha bitdan iborat va qanday ko'rinishda yoziladi?",
        "options": ["32 bit, 4 ta o'nlik son nuqta bilan ajratiladi (masalan: 192.168.1.1)", "128 bit, harflar bilan", "64 bit, ikkilikda", "16 bit"],
        "correct_index": 0,
        "explanation": "IPv4 manzili 32 bit (4 bayt) dan iborat bo'lib, har biri 0 dan 255 gacha bo'lgan 4 ta oktetdan tashkil topgan.",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "Internet protokollari",
        "question_text": "Domen nomlarini (masalan, google.com) tegishli IP-manzilga aylantirib beruvchi tizim nima?",
        "options": ["DNS (Domain Name System)", "DHCP", "FTP", "HTTP"],
        "correct_index": 0,
        "explanation": "DNS (Domain Name System) serverlari odamlar tushunadigan domen nomlarini kompyuter tushunadigan raqamli IP ga o'giradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "Tarmoq xavfsizligi",
        "question_text": "HTTP va HTTPS protokollari orasidagi asosiy farq nimada?",
        "options": ["HTTPS ma'lumotlarni shifrlangan (SSL/TLS) xavfsiz kanal orqali uzatadi", "HTTP tezroq ishlaydi", "HTTPS faqat rasmlarni yuklaydi", "Hech qanday farqi yo'q"],
        "correct_index": 0,
        "explanation": "HTTPS (HyperText Transfer Protocol Secure) ma'lumotlarni SSL/TLS orqali shifrlab xavfsizligini ta'minlaydi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "Kiberxavfsizlik",
        "question_text": "Foydalanuvchilarni soxta veb-sahifalar orqali aldab, ularning parol va karta ma'lumotlarini o'g'irlash hujumi nima deyiladi?",
        "options": ["Fishing (Phishing)", "DDoS hujumi", "Brute Force", "Spam"],
        "correct_index": 0,
        "explanation": "Fishing - soxta saytlar yoki elektron xatlar yordamida shaxsiy maxfiy ma'lumotlarni o'g'irlash kiberfiribgarligidir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "Axborot xavfsizligi",
        "question_text": "Kriptografiyada ma'lumotlarni maxfiy kalit yordamida o'qib bo'lmaydigan holatga keltirish jarayoni nima?",
        "options": ["Shifrlash (Encryption)", "Deshifrlash (Decryption)", "Arxivlash", "Defragmentatsiya"],
        "correct_index": 0,
        "explanation": "Oddiy matnni algoritm va kalit yordamida himoyalangan ko'rinishga keltirish shifrlash (encryption) deyiladi.",
        "difficulty": "oson"
    },
    # 11-sinf (Ma'lumotlar bazasi, SQL va Veb-dasturlash)
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "Ma'lumotlar bazasi",
        "question_text": "Jadvallardan tashkil topgan va o'zaro aloqador bo'lgan ma'lumotlar bazasi qanday ataladi?",
        "options": ["Relyatsion ma'lumotlar bazasi (RDBMS)", "Iyerarxik baza", "Tarmoqli baza", "Faylli baza"],
        "correct_index": 0,
        "explanation": "Relyatsion ma'lumotlar bazalari (MySQL, PostgreSQL, SQLite) qator va ustunlardan iborat jadvallardan tashkil topadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "SQL buyruqlari",
        "question_text": "Jadvaldan ma'lumotlarni tanlab olish uchun qaysi SQL operatori ishlatiladi?",
        "options": ["SELECT", "INSERT", "UPDATE", "DELETE"],
        "correct_index": 0,
        "explanation": "SQL tilida jadvaldagi yozuvlarni so'rab olish uchun SELECT operatori qo'llaniladi (SELECT * FROM table).",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "SQL buyruqlari",
        "question_text": "Jadvalga yangi qator (yozuv) qo'shish buyrug'i qaysi?",
        "options": ["INSERT INTO", "ADD ROW", "NEW RECORD", "CREATE ROW"],
        "correct_index": 0,
        "explanation": "Yangi yozuv qo'shish SQL da INSERT INTO table (ustunlar) VALUES (qiymatlar) orqali bajariladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "SQL da shartlar",
        "question_text": "SQL so'rovida qatorlarni filtrlash (saralash shartini berish) uchun qaysi kalit so'z ishlatiladi?",
        "options": ["WHERE", "ORDER BY", "GROUP BY", "HAVING"],
        "correct_index": 0,
        "explanation": "WHERE operatori berilgan shartga mos keluvchi qatorlarni tanlab oladi (masalan: WHERE score > 80).",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "Veb-texnologiyalar",
        "question_text": "HTML tili nimani anglatadi?",
        "options": ["HyperText Markup Language (Gipermatnli belgilash tili)", "High Tech Machine Language", "Hyperlink Text Mode Layout", "Home Tool Markup Language"],
        "correct_index": 0,
        "explanation": "HTML - HyperText Markup Language, veb-sahifalarning karkasi va tuzilishini yaratuvchi belgilash tilidir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "Veb-texnologiyalar",
        "question_text": "HTML sahifada boshqa veb-sahifaga o'tuvchi gipermurojaat (havola) yaratish uchun qaysi teg ishlatiladi?",
        "options": ["<a href='...'>", "<link>", "<p>", "<href>"],
        "correct_index": 0,
        "explanation": "Gipermurojaat uchun <a> (anchor) tegi va uning href atributi ishlatiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "CSS stillari",
        "question_text": "CSS (Cascading Style Sheets) ning veb-dasturlashdagi asosiy vazifasi nima?",
        "options": ["Veb-sahifaning dizayni, rangi, shrifti va tashqi ko'rinishini bezash", "Server bilan aloqa o'rnatish", "Ma'lumotlar bazasini boshqarish", "Fayllarni yuklash"],
        "correct_index": 0,
        "explanation": "CSS veb-sahifaning vizual ko'rinishini (ranglar, bloklar joylashuvi, shriftlar) boshqarish uchun xizmat qiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "Birlamchi kalit (Primary Key)",
        "question_text": "Relyatsion jadvallarda har bir yozuvning yagonaligini (takrorlanmasligini) ta'minlovchi maydon nima deyiladi?",
        "options": ["Birlamchi kalit (Primary Key)", "Tashqi kalit (Foreign Key)", "Oddiy indeks", "Kombinatsiya"],
        "correct_index": 0,
        "explanation": "Primary Key (birlamchi kalit) har bir qatorni noyob aniqlovchi (takrorlanmaydigan va NULL bo'lmagan) ustundir.",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "7-sinf",
        "chapter_title": "O'n oltilik sanoq sistemasi",
        "question_text": "O'n oltilik (Hexadecimal) sanoq sistemasida 10 dan 15 gacha bo'lgan sonlar qaysi harflar bilan belgilanadi?",
        "options": ["A, B, C, D, E, F", "X, Y, Z, W, P, Q", "I, II, III, IV, V, VI", "K, L, M, N, O, P"],
        "correct_index": 0,
        "explanation": "Hex sistemasida 10-A, 11-B, 12-C, 13-D, 14-E, 15-F bilan belgilanadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "8-sinf",
        "chapter_title": "Python o'zgaruvchilari",
        "question_text": "Python da quyidagi o'zgaruvchi nomlaridan qaysi biri sintaktik jihatdan to'g'ri?",
        "options": ["user_score_2", "2nd_score", "user-score", "class"],
        "correct_index": 0,
        "explanation": "O'zgaruvchi nomi raqam bilan boshlanmaydi, chiziqcha (-) bo'lmaydi va zaxiradagi kalit so'z (class) bo'lishi mumkin emas. Shuning uchun user_score_2 to'g'ri.",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "9-sinf",
        "chapter_title": "Python sikllari - while",
        "question_text": "Quyidagi kod natijasini aniqlang:\ni = 1\nwhile i < 4:\n    i += 1\nprint(i)",
        "options": ["4", "3", "5", "Cheksiz sikl"],
        "correct_index": 0,
        "explanation": "i=1 -> i=2; i=2 -> i=3; i=3 -> i=4. So'ng i < 4 shart False bo'ladi va sikldan chiqadi. Natija 4.",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "Tarmoq modellari",
        "question_text": "OSI modeli necha pog'onadan (qatlamdan) iborat?",
        "options": ["7 ta pog'ona", "4 ta pog'ona", "5 ta pog'ona", "9 ta pog'ona"],
        "correct_index": 0,
        "explanation": "OSI (Open Systems Interconnection) etalon modeli 7 ta pog'onadan iborat (Fizik, Kanal, Tarmoq, Transport, Seans, Taqdimot, Dasturiy).",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "Xavfsizlik - Parollar",
        "question_text": "Kiberxavfsizlik talablariga ko'ra mustahkam parol qanday xususiyatlarga ega bo'lishi kerak?",
        "options": ["Kamida 8-12 belgidan iborat, katta va kichik harflar, raqamlar va maxsus belgilar qatnashgan", "Faqat o'z tug'ilgan yili va ismidan iborat", "Kamida 6 ta bir xil raqam", "Faqat lotin harflari"],
        "correct_index": 0,
        "explanation": "Murakkab parol kamida 8-12 belgi, katta-kichik harflar, raqamlar va maxsus belgilardan (!@#$%) tuzilishi lozim.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "SQL saralash",
        "question_text": "SQL so'rovida natijalarni o'sish yoki kamayish tartibida saralash uchun qaysi ifoda qo'llaniladi?",
        "options": ["ORDER BY", "SORT BY", "ALIGN BY", "FILTER BY"],
        "correct_index": 0,
        "explanation": "ORDER BY ustun_nomi ASC (o'sish) yoki DESC (kamayish) tartibida saralaydi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "6-sinf",
        "chapter_title": "Operatsion tizimlar",
        "question_text": "Kompyuterning barcha resurslarini boshqaruvchi va inson bilan kompyuter muloqotini ta'minlovchi dasturlar majmui nima?",
        "options": ["Operatsion tizim (OS)", "Antivirus dasturi", "Matn muharriri", "Dasturlash tili"],
        "correct_index": 0,
        "explanation": "Operatsion tizim (Windows, Linux, macOS) asosiy tizimli dasturiy ta'minotdir.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "8-sinf",
        "chapter_title": "Python mantiqiy amallari",
        "question_text": "Python da not (5 > 2) ifodaning natijasi nima bo'ladi?",
        "options": ["False", "True", "None", "Error"],
        "correct_index": 0,
        "explanation": "5 > 2 ifodasi True ga teng. 'not True' esa False qaytaradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "9-sinf",
        "chapter_title": "Python to'plamlari (Set)",
        "question_text": "s = set([1, 2, 2, 3, 3, 3])\nprint(len(s)) kodi nima natija beradi?",
        "options": ["3", "6", "1", "4"],
        "correct_index": 0,
        "explanation": "To'plam (set) faqat takrorlanmas noyob elementlarni saqlaydi: {1, 2, 3}. Uning uzunligi 3.",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "MAC manzil",
        "question_text": "Tarmoq kartasining ishlab chiqaruvchi tomonidan berilgan noyob fizik manzili nima deyiladi?",
        "options": ["MAC-manzil", "IP-manzil", "Port", "DNS-nom"],
        "correct_index": 0,
        "explanation": "MAC (Media Access Control) har bir tarmoq qurilmasining 48-bitli o'zgarmas fizik manzilidir.",
        "difficulty": "orta"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "SQL jadval yaratish",
        "question_text": "Yangi ma'lumotlar jadvalini hosil qilish uchun qaysi SQL buyrug'i beriladi?",
        "options": ["CREATE TABLE", "MAKE TABLE", "NEW TABLE", "BUILD TABLE"],
        "correct_index": 0,
        "explanation": "SQL da jadval 'CREATE TABLE jadval_nomi (...);' buyrug'i bilan tuziladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "8-sinf",
        "chapter_title": "Python ro'yxat indeksatsiyasi",
        "question_text": "items = ['kitob', 'daftar', 'qalam']\nitems[-1] qaysi elementni bildiradi?",
        "options": ["'qalam'", "'kitob'", "'daftar'", "Xatolik beradi"],
        "correct_index": 0,
        "explanation": "Python da manfiy indeks oxiridan sanaladi: -1 oxirgi elementni ('qalam') bildiradi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "7-sinf",
        "chapter_title": "Piksel va ruxsat o'lchami",
        "question_text": "Raqamli tasvirning eng kichik bo'linmas nuqtasi nima deb ataladi?",
        "options": ["Piksel (Pixel)", "Bit", "Bayt", "Dpi"],
        "correct_index": 0,
        "explanation": "Monitor ekranidagi va raqamli rasmlardagi elementar nuqta piksel deyiladi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "9-sinf",
        "chapter_title": "Python break va continue",
        "question_text": "Python da joriy iteratsiyani to'xtatib, siklning keyingi qadamiga o'tish qaysi operator bilan amalga oshiriladi?",
        "options": ["continue", "break", "pass", "return"],
        "correct_index": 0,
        "explanation": "continue joriy iteratsiya qolgan kodini tashlab o'tib yangi qadamga o'tadi, break esa butun siklni to'xtatadi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "10-sinf",
        "chapter_title": "Kiberxavfsizlik - 2FA",
        "question_text": "Ikki bosqichli autentifikatsiya (2FA) nima uchun kerak?",
        "options": ["Hisob qaydnomasini paroldan tashqari qo'shimcha bir martalik kod (SMS yoki ilova) bilan kuchli himoyalash uchun", "Internet tezligini oshirish uchun", "Xotirada joy tejash uchun", "Fayllarni qisqartirish uchun"],
        "correct_index": 0,
        "explanation": "2FA (Two-Factor Authentication) paroldan tashqari telefon yoki ilovaga keladigan bir martalik tasdiq kodi orqali ruxsatsiz kirishdan saqlaydi.",
        "difficulty": "oson"
    },
    {
        "subject_id": 8,
        "grade": "11-sinf",
        "chapter_title": "HTML forma teglari",
        "question_text": "HTML da foydalanuvchidan matn yoki parol kiritish maydonini yaratish uchun qaysi teg qo'llaniladi?",
        "options": ["<input>", "<textarea>", "<form>", "<label>"],
        "correct_index": 0,
        "explanation": "<input type='text'> yoki <input type='password'> foydalanuvchi ma'lumot kiritishi uchun xizmat qiladi.",
        "difficulty": "oson"
    }
]
