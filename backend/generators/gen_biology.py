import random
from common import make_q, insert_questions

def generate_biology_questions():
    questions = []

    # 1. Botanika - Organlar va To'qimalar (110 questions)
    botany_organs = [
        ("O'simliklarda suv va unda erigan mineral moddalarni ildizdan bargga qarab o'tkazuvchi to'qima qaysi?", "Ksilema (naylar)", ["Floema (elaksimon naylar)", "Qoplovchi to'qima", "Mexanik to'qima"], "Ksilema orqali suv va tuzlar yuqoriga (ildizdan bargga) o'tkaziladi."),
        ("Fotosintez natijasida hosil bo'lgan organik moddalarni bargdan boshqa organlarga o'tkazuvchi to'qima qaysi?", "Floema (elaksimon naylar)", ["Ksilema (naylar)", "Hosil qiluvchi to'qima", "Po'kak to'qimasi"], "Floema organik moddalarni yuqoridan pastga o'tkazadi."),
        ("O'simlik hujayrasining o'sishi va yangi to'qimalarning hosil bo'lishini ta'minlovchi to'qima qaysi?", "Hosil qiluvchi to'qima (meristema)", ["Mexanik to'qima", "Asosiy to'qima", "Qoplovchi to'qima"], "Meristema doimiy bo'linuvchi yosh to'qima hisoblanadi."),
        ("Fotosintez jarayoni o'simlik hujayrasining qaysi organoidida amalga oshadi?", "Xloroplastlarda", ["Mitoxondriyada", "Ribosomada", "Vakuolada"], "Fotosintez pigmenti xlorofill xloroplastlar ichida joylashgan."),
        ("Ildizning tuproqdan suv va ozuqa moddalarini so'rib oluvchi asosiy qismi qaysi?", "So'ruvchi zona (ildiz tukchalari)", ["Bo'linish zonasi", "O'sish zonasi", "Ildiz qinchasi"], "Ildiz tukchalari orqali asosiy so'rish funksiyasi bajariladi."),
        ("Gulning changchisi va urug'chisi nima vazifani bajaradi?", "Jinsiy ko'payish a'zolari", ["Faqat hasharotlarni jalb qilish", "Suv bug'latish", "Organik modda to'plash"], "Changchi va urug'chi gulning asosiy ko'payish a'zolaridir."),
        ("Barg og'izchalari asosan qanday funksiyani bajaradi?", "Gazlar almashinuvi va transpiratsiya (suv bug'latish)", ["Faqat mineral tuzlarni yutish", "O'simlikka qattiqlik berish", "Tayanch funksiyasi"], "Og'izchalar orqali CO₂ va O₂ almashinuvi hamda suv bug'lanishi sodir bo'ladi.")
    ]
    for _ in range(110):
        t = random.choice(botany_organs)
        questions.append(make_q(4, "Botanika - O'simlik to'qimalari va organlari", t[0], t[1], t[2], t[3], "oson", "5-sinf"))

    # 2. O'simliklar Sistematikasi (100 questions)
    sys_botany = [
        ("Tuban o'simliklarning yuksak o'simliklardan asosiy farqi nimada?", "Tana va to'qimalari a'zolarga (ildiz, poya, barg) ajralmagan", ["Faqat quruqlikda yashaydi", "Urug' orqali ko'payadi", "Mevalari bo'ladi"], "Tuban o'simliklar (suv o'tlari) tallom (qat-qat) tanaga ega."),
        ("Ildizga ega bo'lmagan, uning o'rniga rizooidlar orqali birikuvchi yuksak spora o'simlik qaysi?", "Yo'sinlar (masalan, funariya, sfagnum)", ["Qirqquloqlar", "Ochiq urug'lilar", "Burchoqdoshlar"], "Yo'sinlar haqiqiy ildizga ega emas, rizooidlarga ega."),
        ("Ochiq urug'li o'simliklarning asosiy vakilini ko'rsating.", "Qarag'ay, archa, qoraqarag'ay", ["Bug'doy va arpa", "Lola va nargis", "Olma va shaftoli"], "Ignabargli o'simliklar urug'lari qubbalarda ochiq joylashadi."),
        ("Ikki pallali o'simliklarning asosiy belgilarini ko'rsating.", "Urug'ida 2 ta palla, ildizi o'q ildiz, barg tomirlanishi to'rsimon", ["Urug'ida 1 ta palla, popuk ildiz", "Bargi parallel tomirlangan", "Mevasi bo'lmaydi"], "Ikki pallalilar o'q ildiz va to'rsimon tomirlangan barglarga ega."),
        ("Bug'doy, makkajo'xori, sholi qaysi oilaga mansub?", "Bug'doydoshlar (boshoqdoshlar) oilasiga", ["Ra'nodoshlar", "Burchoqdoshlar", "Karamdoshlar"], "Boshoqli don ekinlari g'alladoshlar oilasiga kiradi."),
        ("Olma, nok, shaftoli, na'matak qaysi oilaga kiradi?", "Ra'nodoshlar oilasiga", ["Gulxayridoshlar", "Sho'radoshlar", "Loladoshlar"], "Ra'nodoshlar oilasi 5 tojbargli gullarga ega mevali daraxtlarni o'z ichiga oladi.")
    ]
    for _ in range(100):
        t = random.choice(sys_botany)
        questions.append(make_q(4, "O'simliklar sistematikasi", t[0], t[1], t[2], t[3], "orta", "6-sinf"))

    # 3. Zoologiya - Umurtqasizlar (110 questions)
    invert_qs = [
        ("Soxta oyoqlari (psevdopodiyalar) yordamida harakatlanuvchi sodda bir hujayrali jonivor qaysi?", "Oddiy amyoba", ["Yashil evglena", "Tufelka (poyabzalcha)", "Volvoks"], "Amyoba soxta oyoqlari orqali harakatlanadi va ozuqani qamrab oladi (fagotsitoz)."),
        ("Xlorofill donachalariga ega bo'lib, yorug'likda fotosintez qiluvchi bir hujayrali jonivor qaysi?", "Yashil evglena", ["Amyoba", "Moxov tayoqchasi", "Bezgat plazmodiysi"], "Yashil evglena miksotrof (aralash) oziqlanadi."),
        ("Gidraning hujum va himoya vazifasini bajaruvchi maxsus hujayralari nima deb ataladi?", "Otuvchi hujayralar", ["Oraliq hujayralar", "Teri-muskul hujayralari", "Nerv hujayralari"], "Bo'shliqichlilar otuvchi hujayralari orqali o'ljasini falajlaydi."),
        ("Yomg'ir chuvalchangi qaysi chuvalchanglar tipiga mansub?", "Halqali chuvalchanglar", ["Yassi chuvalchanglar", "To'garak chuvalchanglar", "Mollyuskalar"], "Yomg'ir chuvalchangi bo'g'imlardan iborat halqali chuvalchangdir."),
        ("Bo'g'imoyoqlilarning tashqi skeleti qanday moddadan iborat?", "Xitin qobiqdan", ["Ohakdan", "Keratindan", "Kollagendan"], "Bo'g'imoyoqlilar tanasi pishiq xitin qobiq bilan himoyalangan."),
        ("O'rgimchaksimonlarning nechta yurish oyog'i mavjud?", "8 ta (4 juft)", ["6 ta (3 juft)", "10 ta (5 juft)", "12 ta"], "O'rgimchaklarda 4 juft, hasharotlarda 3 juft oyoq bo'ladi."),
        ("Hasharotlarning nechta yurish oyog'i bo'ladi?", "6 ta (3 juft)", ["8 ta (4 juft)", "4 ta", "10 ta"], "Barcha voyaga yetgan hasharotlarda 3 juft yurish oyog'i bor."),
        ("Chayon, kana va qoraqurt qaysi sinfga kiradi?", "O'rgimchaksimonlar sinfiga", ["Hasharotlar", "Qisqichbaqasimonlar", "Mollyuskalar"], "Ular o'rgimchaksimonlar sinfi vakillaridir.")
    ]
    for _ in range(110):
        t = random.choice(invert_qs)
        questions.append(make_q(4, "Zoologiya - Umurtqasizlar", t[0], t[1], t[2], t[3], "orta", "7-sinf"))

    # 4. Zoologiya - Xordalilar va Umurtqalilar (110 questions)
    vert_qs = [
        ("Baliqlarning suv oqimi yo'nalishi va bosimini sezuvchi maxsus organi nima?", "Yon chizig'i", ["Jabralari", "Dum suzgichi", "Suzgich pufagi"], "Yon chiziq a'zosi suv tebranishlari va to'lqinlarini sezadi."),
        ("Suvda va quruqda yashovchilarning (amfibiyalar) yuragi necha kamerali?", "3 kamerali (ikkita bo'lmacha, bitta qorincha)", ["2 kamerali", "4 kamerali", "1 kamerali"], "Baqa va qurbaqalarda yurak 3 kamerali bo'lib, aralash qon aylanadi."),
        ("Sudralib yuruvchilar (kaltakesak, ilon, toshbaqa) qanday nafas oladi?", "Faqat o'pka orqali", ["Teri va o'pka orqali", "Jabralar orqali", "Trakheyalar orqali"], "Sudralib yuruvchilar to'liq quruqlik hayvonlari bo'lib, o'pka orqali nafas oladi."),
        ("Qushlarning uchishiga moslashgan maxsus ko'krak suyagi o'sig'i nima deyiladi?", "Qil (to'sh toj suyagi)", ["Kurak suyagi", "Qovurg'a", "Yelka suyagi"], "Uchish muskullari qil suyagiga birikadi."),
        ("Qushlar va sut emizuvchilarning yuragi necha kamerali?", "4 kamerali (ikkita bo'lmacha, ikkita qorincha)", ["3 kamerali", "2 kamerali", "5 kamerali"], "Issiq qonli hayvonlarda yurak 4 kamerali va arterial qon venoz qondan to'liq ajralgan."),
        ("Bola tug'ib, bolasini sut bilan boquvchi yuksak umurtqalilar qaysi sinfga mansub?", "Sut emizuvchilar sinfiga", ["Qushlar", "Sudralib yuruvchilar", "Amfibiyalar"], "Sut emizuvchilar tirik tug'ish va sut bezlariga ega bo'lishi bilan ajralib turadi.")
    ]
    for _ in range(110):
        t = random.choice(vert_qs)
        questions.append(make_q(4, "Zoologiya - Umurtqalilar", t[0], t[1], t[2], t[3], "orta", "7-sinf"))

    # 5. Odam Anatomiyasi - Tayanch-harakat Sistemasi (100 questions)
    skelet_qs = [
        ("Katta yoshli odam skeletida jami nechta suyak mavjud?", "200 dan ortiq (taxminan 206 ta)", ["150 ta", "300 ta", "100 ta"], "Inson skeleti o'rtacha 206-208 ta suyakdan tashkil topgan."),
        ("Odam tanasidagi eng uzun va eng pishiq nayzasimon suyak qaysi?", "Son suyagi", ["Yelka suyagi", "Katta boldir suyagi", "Qovurg'a"], "Son suyagi inson tanasidagi eng uzun va kuchli suyakdir."),
        ("Inson umurtqa pog'onasi nechta umurtqadan iborat?", "33-34 ta umurtqadan", ["24 ta", "45 ta", "20 ta"], "Bo'yin (7), ko'krak (12), bel (5), dumg'aza (5), dum (4-5) umurtqalari bor."),
        ("Suyaklarning eniga o'sishini va sinishda bitishini ta'minlovchi qavat nima?", "Suyakusti pardasi (periost)", ["Suyak iligi", "Gialin tog'ay", "G'ovak modda"], "Suyakusti pardasining ichki qavatidagi hujayralar suyakni eniga o'stiradi."),
        ("Suyak to'qimasiga qattiqlik va elastiklik beruvchi moddalar qaysilar?", "Kalsiy/fosfor tuzlari (qattiqlik) va ossein oqsili (egiluvchanlik)", ["Faqat suv", "Faqat temir", "Kraxmal va yog'lar"], "Mineral tuzlar qattiqlik, organik ossein oqsili esa egiluvchanlik beradi.")
    ]
    for _ in range(100):
        t = random.choice(skelet_qs)
        questions.append(make_q(4, "Anatomiya - Tayanch-harakat", t[0], t[1], t[2], t[3], "oson", "8-sinf"))

    # 6. Qon va Qon Aylanish Sistemasi (110 questions)
    blood_qs = [
        ("Kislorod va karbonat angidridni tashuvchi gemoglobinga ega qon hujayralari nima?", "Eritrotsitlar (qizil qon tanachalari)", ["Leykotsitlar", "Trombotsitlar", "Qon plazmasi"], "Eritrotsitlar gemoglobin oqsili yordamida nafas gazlarini tashiydi."),
        ("Organizmga tushgan begona mikroblar va viruslarga qarshi immunitetni ta'minlovchi qon hujayralari qaysi?", "Leykotsitlar (oq qon tanachalari)", ["Eritrotsitlar", "Trombotsitlar", "Gormonlar"], "Leykotsitlar fagotsitoz va antitanalar hosil qilish orqali himoya qiladi."),
        ("Qonning ivishini (tromblar hosil bo'lishini) ta'minlovchi qon plastinkalari qaysi?", "Trombotsitlar", ["Eritrotsitlar", "Leykotsitlar", "Albuminlar"], "Trombotsitlar qon tomir jarohatlanganda qonni ivitadi."),
        ("Universal donor (har qanday guruhga quyish mumkin bo'lgan) qon guruhi qaysi?", "I guruh (0)", ["IV guruh (AB)", "II guruh (A)", "III guruh (B)"], "I guruh eritrotsitlarida agglyutinogenlar yo'qligi sababli universal donor hisoblanadi."),
        ("Universal retsipient (barcha guruhlardan qon qabul qila oladigan) qon guruhi qaysi?", "IV guruh (AB)", ["I guruh (0)", "II guruh (A)", "III guruh (B)"], "IV guruh plazmasida agglyutininlar yo'qligi sababli universal qabul qiluvchi."),
        ("Katta qon aylanish doirasi yurakning qaysi qismidan boshlanadi?", "Chap qorinchadan (aorta orqali)", ["O'ng qorinchadan", "Chap bo'lmachadan", "O'ng bo'lmachadan"], "Chap qorinchadan kislorodga boy qon butun tanaga tarqaladi."),
        ("Kichik (o'pka) qon aylanish doirasi qayerdan boshlanadi?", "O'ng qorinchadan (o'pka arteriyasi orqali)", ["Chap qorinchadan", "O'ng bo'lmachadan", "Chap bo'lmachadan"], "O'ng qorinchadan venoz qon o'pkaga gaz almashinuvi uchun haydaladi.")
    ]
    for _ in range(110):
        t = random.choice(blood_qs)
        questions.append(make_q(4, "Qon va Yurak-qon tomir sistemasi", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 7. Ichki A'zolar va Fiziologiya (120 questions)
    organ_qs = [
        ("Buyrakning eng kichik tuzilish va funksional birligi nima deb ataladi?", "Nefron", ["Neyron", "Osteon", "Miofibrilla"], "Buyrakda qonni filtrlovchi 1 milliondan ortiq nefronlar mavjud."),
        ("Nerv to'qimasining asosiy hujayrasi nima deb ataladi?", "Neyron", ["Nefron", "Akson", "Sinaps"], "Neyron nerv sistemasining tuzilish birligi bo'lib, dendrit va aksonga ega."),
        ("Qondagi qand (glyukoza) miqdorini kamaytiruvchi gormon qaysi va qayerda ishlab chiqariladi?", "Insulin (me'da osti bezida)", ["Adrenalin (buyrak usti bezida)", "Tiroksin (qalqonsimon bezda)", "Gipofiz"], "Oshqozon osti bezi beta-hujayralari insulin gormonini sintezlaydi."),
        ("Oshqozon shirasidagi oqsillarni parchalovchi asosiy ferment nima?", "Pepsin", ["Amilaza", "Lipaza", "Maltaza"], "Pepsin xlorid kislotali kislotali muhitda oqsillarni maydalaydi."),
        ("Odam organizmidagi eng yirik ichki bez va bioximik laboratoriya qaysi?", "Jigar", ["Buyrak", "Oshqozon", "Taloq"], "Jigar o't suyuqligi ishlab chiqaradi, zaharlarni zararsizlantiradi."),
        ("Nafas olish markazi bosh miyaning qaysi bo'limida joylashgan?", "Uzunchoq miyada", ["Miyachada", "Katta yarimsharlar po'stlog'ida", "Oraliq miyada"], "Uzunchoq miyada nafas, qon aylanish, himoya (aksirish, yo'tal) markazlari bor."),
        ("Harakatlarni muvofiqlashtirish va muvozanatni saqlashga javobgar miya qismi qaysi?", "Miyacha", ["Uzunchoq miya", "Gipotalamus", "Ko'prik"], "Miyacha tana muvozanatini va harakatlar aniqligini boshqaradi.")
    ]
    for _ in range(120):
        t = random.choice(organ_qs)
        questions.append(make_q(4, "Fiziologiya va Organlar sistemasi", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 8. Sitologiya va Hujayra Biologiyasi (110 questions)
    cyto_qs = [
        ("Hujayraning energetik stansiyasi (ATF sintezlanadigan organoid) qaysi?", "Mitoxondriya", ["Ribosoma", "Lizosoma", "Golji majmuasi"], "Mitoxondriyalarda hujayraviy nafas olish va ATF energiyasi hosil bo'ladi."),
        ("Hujayrada oqsil biosintezini amalga oshiruvchi membranali bo'lmagan organoid qaysi?", "Ribosomalar", ["Lizosomalar", "Mitoxondriyalar", "Sentriollar"], "Ribosomalar aminokislotalardan oqsil zanjirini sintez qiladi."),
        ("Hujayra ichida oziq moddalarni parchalovchi hazm qiluvchi organoid qaysi?", "Lizosoma", ["Vakuola", "Ribosoma", "Xloroplast"], "Lizosomalar gidrolitik fermentlarga ega bo'lib, hujayra ichi hazmini bajaradi."),
        ("Genetik axborotni saqlash va ko'payishni boshqarish markazi qaysi?", "Hujayra yadrosi (xromosomalar)", ["Sitoplazma", "Hujayra membranasi", "Sentrosoma"], "Yadroda irsiy axborot DNK molekulalarida saqlanadi."),
        ("Tana hujayralarining (somatik hujayralar) bo'linish usuli nima deb ataladi?", "Mitoz", ["Meyoz", "Amitoz", "Shizogoniya"], "Mitoz natijasida xromosomalar soni o'zgarmasdan (diploid 2n) saqlanib qoladi."),
        ("Jinsiy hujayralar (gametalar) hosil bo'lishidagi bo'linish usuli nima?", "Meyoz", ["Mitoz", "Burtiklanish", "Klonlash"], "Meyoz natijasida xromosoma to'plami ikki barobar kamayib (gaploid n) qoladi.")
    ]
    for _ in range(110):
        t = random.choice(cyto_qs)
        questions.append(make_q(4, "Sitologiya - Hujayra", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 9. Genetika va Seleksiya (100 questions)
    gen_qs = [
        ("Irsiyatning moddiy asosi va DNKning ma'lum oqsil haqida axborot saqlovchi qismi nima?", "Gen", ["Xromosoma", "Yadrocha", "Allel"], "Gen - irsiy axborotning elementar funksional birligidir."),
        ("Organizmning barcha genlari yig'indisi nima deb ataladi?", "Genotip", ["Fenotip", "Genom", "Kariotip"], "Genotip - ota-onadan olingan barcha genlar majmuidir."),
        ("Organizmning tashqi va ichki belgilari yig'indisi nima deb ataladi?", "Fenotip", ["Genotip", "Gomozigota", "Mutatsiya"], "Fenotip - genotipning tashqi muhit ta'sirida namoyon bo'lishidir."),
        ("Monoduragay chatishtirishda (Mendelning 1-qonuni) birinchi bo'g'inda (F₁) qanday qonuniyat kuzatiladi?", "Bir xillik qonuni (100% dominant belgi)", ["3:1 nisbatda ajralish", "9:3:3:1 nisbat", "Faqat retsessiv belgilar"], "Mendelning birinchi qonuni - duragaylarning bir xillik qonuni."),
        ("Mendelning ikkinchi bo'g'inda (F₂) fenotip bo'yicha ajralish nisbati qanday?", "3 : 1 (3 ta dominant, 1 ta retsessiv)", ["1 : 1", "1 : 2 : 1", "9 : 3 : 3 : 1"], "F₂ da fenotip bo'yicha 3:1, genotip bo'yicha 1:2:1 nisbatda ajralish sodir bo'ladi."),
        ("Odam tana hujayralarida nechta xromosoma mavjud?", "46 ta (23 juft)", ["48 ta", "23 ta", "44 ta"], "Odam kariotipida 22 juft autosoma va 1 juft jinsiy xromosoma (jami 46 ta) bor."),
        ("Erkaklar jinsiy xromosomasi qanday belgilanadi?", "XY", ["XX", "YY", "X0"], "Erkaklarda XY, ayollarda XX xromosomalar bo'ladi.")
    ]
    for _ in range(100):
        t = random.choice(gen_qs)
        questions.append(make_q(4, "Genetika asoslari", t[0], t[1], t[2], t[3], "qiyin", "10-sinf"))

    # 10. Evolutsiya va Ekologiya (100 questions)
    eco_qs = [
        ("Tirik organizmlarning o'zaro va tashqi muhit bilan munosabatlarini o'rganuvchi fan nima?", "Ekologiya", ["Genetika", "Anatomiya", "Embriologiya"], "Ekologiya fani biosfera va ekosistemalarni o'rganadi."),
        ("Oziq zanjirida anorganik moddalardan organik moddalar sintezlovchi avtotrof organizmlar nima deyiladi?", "Produtsentlar (o'simliklar)", ["Konsumentlar", "Redutsentlar", "Parazitlar"], "Yashil o'simliklar birlamchi mahsulot ishlab chiqaruvchi produtsentlardir."),
        ("Tayyor organik moddalar bilan oziqlanuvchi hayvonlar ekologik zanjirda kimlar?", "Konsumentlar (iste'molchilar)", ["Produtsentlar", "Redutsentlar", "Destruktorlar"], "O'txo'r va yirtqich hayvonlar konsumentlar guruhiga kiradi."),
        ("O'lik organik qoldiqlarni anorganik moddalargacha parchalovchi bakteriya va zamburug'lar nima deyiladi?", "Redutsentlar (parchalovchilar)", ["Produtsentlar", "Konsumentlar", "Yirtqichlar"], "Redutsentlar moddalar aylanishini yakunlaydi."),
        ("Turlarning kelib chiqishi va tabiiy tanlanish nazariyasi asoschisi kim?", "Charlz Darvin", ["Jan Batist Lamark", "Gregor Mendel", "Karl Linney"], "1859-yilda Darvin 'Turlarning kelib chiqishi' asarida evolutsiya mexanizmini ochib bergan."),
        ("Kamayib ketgan va yo'qolib ketish xavfi ostidagi tirik mavjudotlar ro'yxati qaysi kitobga kiritiladi?", "Qizil kitobga", ["Oq kitobga", "Yashil kitobga", "Tabiat xaritasi"], "Noyob va yo'qolish xavfidagi turlar Qizil kitobga kiritiladi.")
    ]
    for _ in range(100):
        t = random.choice(eco_qs)
        questions.append(make_q(4, "Ekologiya va Evolutsiya", t[0], t[1], t[2], t[3], "orta", "11-sinf"))

    print(f"Generated {len(questions)} biology questions.")
    return questions

if __name__ == "__main__":
    qs = generate_biology_questions()
    cnt = insert_questions(qs)
    print(f"Successfully inserted {cnt} biology questions into database.")
