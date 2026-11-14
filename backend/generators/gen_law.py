import random
from common import make_q, insert_questions

def generate_law_questions():
    questions = []

    # 1. Konstitutsiyaviy Asoslar (100 questions)
    const_qs = [
        ("O'zbekiston Respublikasi Konstitutsiyasining 1-moddasiga binoan O'zbekiston qanday davlat?", "Suveren, demokratik, huquqiy, ijtimoiy va dunyoviy davlat", ["Federativ respublika", "Monarxiya", "Teokratik davlat"], "1-modda: O'zbekiston – boshqaruvning respublika shakliga ega bo'lgan suveren, demokratik, huquqiy, ijtimoiy va dunyoviy davlatdir."),
        ("O'zbekistonda davlat hokimiyatining birdan-bir manbai kim hisoblanadi?", "Xalq", ["Prezident", "Oliy Majlis", "Sudlar"], "7-modda: Xalq davlat hokimiyatining birdan-bir manbaidir."),
        ("O'zbekiston Respublikasi davlat tili qaysi til?", "O'zbek tili", ["Rus tili", "Qoraqalpoq tili", "Ingliz tili"], "4-modda: O'zbekiston Respublikasining davlat tili o'zbek tilidir."),
        ("O'zbekiston Respublikasi Konstitutsiyasi va qonunlarining ustunligi qaysi prinsip bilan belgilanadi?", "Konstitutsiya va qonun ustuvorligi prinsipi", ["Xalqaro huquq ustuvorligi", "Prezident qarorlari ustuvorligi", "Mahalliy odatlar ustuvorligi"], "15-modda: O'zbekiston Respublikasida Konstitutsiya va qonunlarning ustunligi so'zsiz tan olinadi."),
        ("Yangi tahrirdagi O'zbekiston Respublikasi Konstitutsiyasi umumxalq referendumi orqali qachon qabul qilindi?", "2023-yil 30-aprelda", ["1992-yil 8-dekabr", "2021-yil 24-oktyabr", "2017-yil 7-fevral"], "Yangi tahrirdagi Konstitutsiya 2023-yil 30-apreldagi referendumda xalq tomonidan ma'qullangan.")
    ]
    for _ in range(100):
        t = random.choice(const_qs)
        questions.append(make_q(9, "Konstitutsiya - Asosiy prinsiplar", t[0], t[1], t[2], t[3], "oson", "9-sinf"))

    # 2. Inson Huquqlari va Burchlari (110 questions)
    rights_qs = [
        ("Yashash huquqi har bir insonning qanday huquqi hisoblanadi?", "Ajralmas va uzviy shaxsiy huquqi", ["Siyosiy huquq", "Iqtisodiy huquq", "Mehnat huquqi"], "25-modda: Yashash huquqi har bir insonning ajralmas huquqidir va u qonun bilan muhofaza qilinadi."),
        ("O'zbekistonda o'lim jazosi qo'llaniladimi?", "Yo'q, O'zbekiston Respublikasida o'lim jazosi qat'iyan taqiqlanadi", ["Ha, faqat og'ir jinoyatlarga", "Harbiy holatda qo'llaniladi", "Sud hukmi bilan"], "Konstitutsiyaga binoan O'zbekistonda o'lim jazosi taqiqlangan."),
        ("Shaxsning aybi qonunda nazarda tutilgan tartibda sud tomonidan isbotlanmaguncha u aybsiz hisoblanishi nima deyiladi?", "Aybsizlik prezumpsiyasi", ["Amfibiya huquqi", "Apellyatsiya", "Kassatsiya"], "28-modda: Ayblanuvchi uning aybi qonuniy kuchga kirgan sud hukmi bilan isbotlanmaguncha aybsiz hisoblanadi."),
        ("O'zbekiston fuqarolarining asosiy konstitutsiyaviy burchlariga nimalar kiradi?", "Konstitutsiya va qonunlarga rioya etish, soliqlarni to'lash, tabiatni muhofaza qilish, Vatanni himoya qilish", ["Faqat harbiy xizmat", "Faqat soliq to'lash", "Faqat saylovda qatnashish"], "Fuqarolar qonunlarga rioya etish, belgilangan soliqlarni to'lash va Vatanni himoya qilishga majburdirlar."),
        ("O'zbekiston Respublikasida majburiy mehnat taqiqlanadimi?", "Ha, har qanday shakldagi majburiy mehnat qat'iyan taqiqlanadi", ["Faqat dam olish kunlari taqiqlanadi", "Qonun bilan ruxsat berilgan", "Faqat qishloq xo'jaligida mumkin"], "Konstitutsiyaga binoan bolalar mehnati va har qanday majburiy mehnat taqiqlangan.")
    ]
    for _ in range(110):
        t = random.choice(rights_qs)
        questions.append(make_q(9, "Inson huquqlari va burchlari", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 3. Oila, Jamiyat va Ijtimoiy Himoya (80 questions)
    family_qs = [
        ("Konstitutsiyaga ko'ra oila jamiyatning qanday bo'g'ini hisoblanadi?", "Jamiyatning asosiy bo'g'inidir va davlat himoyasidadir", ["Ixtiyoriy birlashma", "Faqat xo'jalik subyekti", "Tijorat tashkiloti"], "Oila jamiyatning asosiy bo'g'ini bo'lib, jamiyat va davlat muhofazasidadir."),
        ("Voyaga yetgan, mehnatga layoqatli farzandlar o'z ota-onalari haqida qanday burchga ega?", "G'amxo'rlik qilishga va ularni moddiy ta'minlashga majburdirlar", ["Hech qanday majburiyatga ega emas", "Faqat pensiya yoshida yordam beradi", "Ixtiyoriy qaror"], "Ota-onalar voyaga yetguniga qadar bolalarni boqishi, voyaga yetganlar esa ota-onasiga g'amxo'rlik qilishi shart."),
        ("O'zbekiston Respublikasida davlat tsenzurasi qanday tartibga solingan?", "Tsenzura qat'iyan taqiqlanadi, ommaviy axborot vositalari erkindir", ["Faqat internetda ruxsat berilgan", "Vazirliklar tomonidan nazorat qilinadi", "Cheklanmagan"], "OAV erkin va tsenzuraga yo'l qo'yilmaydi.")
    ]
    for _ in range(80):
        t = random.choice(family_qs)
        questions.append(make_q(9, "Oila va Jamiyat", t[0], t[1], t[2], t[3], "oson", "8-sinf"))

    # 4. Oliy Majlis va Qonunchilik Hokimiyati (90 questions)
    parl_qs = [
        ("O'zbekiston Respublikasi Oliy Majlisi qanday palatalardan iborat parlamentdir?", "Ikki palatali: Qonunchilik palatasi (quyi) va Senat (yuqori)", ["Bir palatali", "Uch palatali", "Prezident kengashi"], "Oliy Majlis Qonunchilik palatasi va Senatdan iborat."),
        ("O'zbekiston Respublikasi Oliy Majlisi Qonunchilik palatasida nechta deputat faoliyat yuritadi?", "150 nafar deputat", ["100 nafar", "250 nafar", "65 nafar"], "Qonunchilik palatasi 150 deputatdan iborat bo'lib, 5 yil muddatga saylanadi."),
        ("O'zbekiston Respublikasi Oliy Majlisi Senatida yangi tahrirga ko'ra nechta senator bo'ladi?", "65 nafar senator", ["100 nafar", "150 nafar", "50 nafar"], "Senat a'zolari soni 65 nafarni tashkil etadi (har bir hududdan 4 tadan va 9 nafari Prezident tomonidan tayinlanadi)."),
        ("Oliy Majlis Qonunchilik palatasi deputatligiga necha yoshdan saylanish mumkin?", "25 yoshdan kam bo'lmagan fuqarolar", ["18 yoshdan", "21 yoshdan", "35 yoshdan"], "Saylov kuni 25 yoshga to'lgan fuqarolar deputatlikka saylanish huquqiga ega."),
        ("Qonunchilik palatasi qabul qilgan qonun Senat tomonidan ma'qullangach kim tomonidan imzolanadi va e'lon qilinadi?", "O'zbekiston Respublikasi Prezidenti tomonidan", ["Bosh vazir tomonidan", "Senat Raisi tomonidan", "Oliy sud Raisi tomonidan"], "Qonun Prezident tomonidan imzolanib, rasmiy e'lon qilingach kuchga kiradi.")
    ]
    for _ in range(90):
        t = random.choice(parl_qs)
        questions.append(make_q(9, "Oliy Majlis va Qonunchilik", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 5. Prezident va Ijro Etuvchi Hokimiyat (80 questions)
    exec_qs = [
        ("O'zbekiston Respublikasi Prezidenti kim hisoblanadi?", "Davlat boshlig'i va Qurolli Kuchlar Oliy Bosh Qo'mondoni", ["Hukumat rahbari", "Parlament raisi", "Bosh qonun chiqaruvchi"], "Prezident davlat boshlig'i bo'lib, davlat hokimiyati organlarining kelishilgan holda faoliyat yuritishini ta'minlaydi."),
        ("O'zbekiston Respublikasi Prezidenti necha yil muddatga saylanadi?", "7 yil muddatga", ["5 yil muddatga", "4 yil muddatga", "6 yil muddatga"], "Yangi tahrirdagi Konstitutsiyaga ko'ra Prezident 7 yil muddatga saylanadi."),
        ("O'zbekiston Respublikasi ijro etuvchi hokimiyatining oliy organi qaysi?", "O'zbekiston Respublikasi Vazirlar Mahkamasi", ["Oliy Majlis", "Oliy sud", "Konstitutsiyaviy sud"], "Vazirlar Mahkamasi (Hukumat) ijro hokimiyatini boshqaradi, unga Bosh vazir rahbarlik qiladi.")
    ]
    for _ in range(80):
        t = random.choice(exec_qs)
        questions.append(make_q(9, "Prezident va Ijro hokimiyati", t[0], t[1], t[2], t[3], "oson", "9-sinf"))

    # 6. Sud Hokimiyati va Huquqni Muhofaza Qilish (80 questions)
    court_qs = [
        ("O'zbekiston Respublikasida sud hokimiyati qanday xususiyatga ega?", "Qonun chiqaruvchi va ijro etuvchi hokimiyatlardan mustaqil ish yuritadi", ["Hukumatga bo'ysunadi", "Hokimiyatlarga tobe", "Faqat Prezident topshirig'i bilan ishlaydi"], "Sudyalar mustaqildir, faqat Konstitutsiya va qonunga bo'ysunadilar."),
        ("Qonunlarning Konstitutsiyaga muvofiqligini ko'rib chiquvchi oliy sud organi qaysi?", "O'zbekiston Respublikasi Konstitutsiyaviy sudi", ["Oliy sud", "Harbiy sud", "Iqtisodiy sud"], "Konstitutsiyaviy sud qonunlarning Konstitutsiyaga mosligini nazorat qiladi."),
        ("Fuqarolik, jinoiy, iqtisodiy va ma'muriy sud ishlarini yuritish sohasida fuqarolik va jinoiy odil sudlovning oliy organi qaysi?", "O'zbekiston Respublikasi Oliy sudi", ["Konstitutsiyaviy sud", "Bosh prokuratura", "Adliya vazirligi"], "Oliy sud fuqarolik, jinoiy va iqtisodiy ishlarda oliy sud instantsiyasidir."),
        ("O'zbekiston Respublikasi hududida qonunlarning aniq va bir xilda ijro etilishi ustidan nazoratni kim amalga oshiradi?", "O'zbekiston Respublikasi Bosh prokurori va unga bo'ysunuvchi prokurorlar", ["Ichki ishlar vazirligi", "Adliya vazirligi", "Milliy gvardiya"], "Prokuratura qonunlarning to'g'ri va bir xil bajarilishini nazorat qiladi.")
    ]
    for _ in range(80):
        t = random.choice(court_qs)
        questions.append(make_q(9, "Sud hokimiyati", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 7. Fuqarolik Huquqi (90 questions)
    civ_qs = [
        ("Fuqaroning o'z harakatlari bilan fuqarolik huquqlariga ega bo'lish va majburiyatlar olish qobiliyati nima?", "Muomala layoqati", ["Huquq layoqati", "Immunitet", "Emansipatsiya"], "Muomala layoqati harakat qobiliyati, huquq layoqati esa huquqqa ega bo'la olish layoqatidir."),
        ("To'liq muomala layoqati necha yoshdan boshlab vujudga keladi?", "18 yoshga to'lgandan so'ng (voyaga yetganda)", ["16 yoshdan", "14 yoshdan", "21 yoshdan"], "Fuqarolik qonunchiligiga ko'ra 18 yoshga to'lgan fuqaro to'liq muomala layoqatiga ega bo'ladi."),
        ("14 yoshdan 18 yoshgacha bo'lgan voyaga yetmaganlar qanday muomala layoqatiga ega?", "Qisman (cheklangan) muomala layoqati", ["To'liq muomala layoqati", "Muomala layoqatiga ega emas", "To'liq javobgarlik"], "Ular o'z stipendiyasi va ish haqini mustaqil tasarruf eta oladi, boshqa bitimlarni esa ota-onasi roziligi bilan tuzadi."),
        ("16 yoshga to'lgan voyaga yetmagan shaxs mehnat shartnomasi bo'yicha ishlasa yoki tadbirkorlik qilsa, uni to'liq muomala layoqatli deb e'lon qilish nima deyiladi?", "Emansipatsiya", ["Reabilitatsiya", "Litsenziyalash", "Amfibiya"], "Emansipatsiya orqali 16 yoshli fuqaro to'la muomala layoqatli deb tan olinishi mumkin.")
    ]
    for _ in range(90):
        t = random.choice(civ_qs)
        questions.append(make_q(9, "Fuqarolik huquqi asoslari", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 8. Mehnat Huquqi (90 questions)
    lab_qs = [
        ("O'zbekiston Respublikasi Mehnat kodeksiga ko'ra xodimni ishga qabul qilishga necha yoshdan yo'l qo'yiladi?", "16 yoshdan (umumiy qoida)", ["18 yoshdan", "14 yoshdan", "21 yoshdan"], "Ishga qabul qilishning umumiy yoshi 16 yoshdir."),
        ("Ota-onaning (yoki ularning o'rnini bosuvchi shaxslarning) yozma roziligi bilan o'quvchilarni yengil ishlarga necha yoshdan qabul qilish mumkin?", "15 yoshdan", ["14 yoshdan", "16 yoshdan", "13 yoshdan"], "Ta'limdan bo'sh vaqtda, sog'lig'iga zarar yetkazmaydigan yengil ishlarga 15 yoshdan ruxsat beriladi."),
        ("16 yoshdan 18 yoshgacha bo'lgan xodimlar uchun haftalik qisqartirilgan ish vaqti necha soatdan oshmasligi kerak?", "Haftasiga 36 soatdan oshmasligi kerak", ["Haftasiga 40 soat", "Haftasiga 24 soat", "Haftasiga 48 soat"], "16-18 yoshlilar uchun haftalik ish vaqti maksimum 36 soat, 18 yoshdan oshganlar uchun 40 soat."),
        ("16 yoshga to'lmagan xodimlar uchun haftalik ish vaqti necha soatdan oshmasligi kerak?", "Haftasiga 24 soatdan oshmasligi kerak", ["Haftasiga 36 soat", "Haftasiga 30 soat", "Haftasiga 40 soat"], "16 yoshgacha bo'lganlar uchun haftasiga 24 soatdan oshmaydigan qisqartirilgan ish vaqti belgilanadi.")
    ]
    for _ in range(90):
        t = random.choice(lab_qs)
        questions.append(make_q(9, "Mehnat huquqi asoslari", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 9. Oila Huquqi (80 questions)
    fam_law = [
        ("O'zbekiston Respublikasi Oila kodeksiga ko'ra nikoh yoshi erkaklar va ayollar uchun necha yosh etib belgilangan?", "18 yosh", ["17 yosh", "16 yosh", "21 yosh"], "Oila kodeksiga ko'ra nikoh yoshi teng ravishda 18 yosh etib belgilangan."),
        ("Uzrli sabablar bo'lganda (homiladorlik, bola tug'ilishi) nikoh yoshi ko'pi bilan qanchaga kamaytirilishi mumkin?", "1 yilga (17 yoshgacha)", ["2 yilga", "6 oyga", "Kamaytirilmaydi"], "Tuman (shahar) hokimi qarori bilan nikoh yoshi ko'pi bilan 1 yilga kamaytirilishi mumkin."),
        ("Nikoh qaysi davlat organida qayd etilgandan so'ng qonuniy kuchga ega bo'ladi?", "FHDY (Fuqarolik holati dalolatnomalarini yozish) organida", ["Faqat diniy marosimda (nikoh o'qitilganda)", "Mahalla qo'mitasida", "Notariusda"], "Faqat FHDY organlarida ro'yxatdan o'tkazilgan nikoh qonuniy hisoblanadi.")
    ]
    for _ in range(80):
        t = random.choice(fam_law)
        questions.append(make_q(9, "Oila huquqi asoslari", t[0], t[1], t[2], t[3], "oson", "9-sinf"))

    # 10. Ma'muriy va Jinoyat Huquqi (90 questions)
    crim_qs = [
        ("Ma'muriy javobgarlikka tortish necha yoshdan boshlanadi?", "16 yoshga to'lgan shaxslar", ["14 yoshdan", "18 yoshdan", "12 yoshdan"], "Ma'muriy huquqbuzarlik sodir etgan 16 yoshga to'lgan shaxslar javobgarlikka tortiladi."),
        ("O'zbekiston Respublikasi Jinoyat kodeksiga ko'ra jinoiy javobgarlikka tortishning umumiy yoshi necha yosh?", "16 yosh", ["18 yosh", "14 yosh", "21 yosh"], "Umumiy qoidaga ko'ra jinoyat sodir etgunga qadar 16 yoshga to'lgan shaxslar javobgar bo'ladi."),
        ("O'ta og'ir jinoyatlar uchun (qasddan odam o'ldirish, bosqinchilik, terrorizm) jinoiy javobgarlik necha yoshdan belgilanadi?", "14 yoshdan", ["16 yoshdan", "12 yoshdan", "15 yoshdan"], "Alohida og'ir jinoyatlar uchun javobgarlik 14 yoshdan boshlanadi."),
        ("Jinoyat qonunida jazo tayinlashdan ko'zlangan asosiy maqsad nima?", "Mahkumni axloqan tuzatish, uning jinoiy faoliyatini davom ettirishining oldini olish va yangi jinoyatlar sodir etilishini ogohlantirish", ["Faqat qasos olish", "Faqat jarima undirish", "Faqat jamiyatdan butunlay ajratish"], "Jazo nafaqat qilmish uchun chora, balki tarbiyalash va yangi jinoyatlarning oldini olish vositasidir.")
    ]
    for _ in range(90):
        t = random.choice(crim_qs)
        questions.append(make_q(9, "Ma'muriy va Jinoyat huquqi", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    print(f"Generated {len(questions)} Law questions.")
    return questions

if __name__ == "__main__":
    qs = generate_law_questions()
    cnt = insert_questions(qs)
    print(f"Successfully inserted {cnt} Law questions into database.")
