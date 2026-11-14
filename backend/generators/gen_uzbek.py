import random
from common import make_q, insert_questions

def generate_uzbek_questions():
    questions = []

    # 1. Fonetika va Tovush o'zgarishlari (110 questions)
    fonetika_qs = [
        ("O'zbek adabiy tilida nechta unli tovush va nechta unli harf bor?", "6 ta unli tovush, 6 ta unli harf (a, o, i, u, o', e)", ["10 ta unli tovush", "8 ta unli tovush", "5 ta unli tovush"], "O'zbek tilida 6 ta unli fonema mavjud: i, e, a, o, u, o'."),
        ("Quyidagi qatorda faqat lablangan unlilar berilgan qatorni toping.", "o, u, o'", ["a, i, e", "a, o, i", "e, i, u"], "Lablangan unlilarni aytishda lablar oldinga cho'chchayadi: o, u, o'."),
        ("Qaysi so'zda tovush tushishi hodisasi yuz bergan?", "Ko'ngli (ko'ngil + i)", ["Qishloqqa", "Kitobim", "Yurakka"], "Ko'ngil so'ziga egalik qo'shimchasi qo'shilganda ikkinchi bo'g'indagi 'i' tovushi tushib qoladi."),
        ("Qaysi so'zda tovush almashinuvi (jarangsizlanish yoki jaranglilashish) yuz bergan?", "Kitobim (kitob + im)", ["Maktabga", "Daftarim", "Qalamim"], "Kitob so'zi oxiridagi 'b' jarangli undoshi o'z holicha saqlangan yoki 'yurak + im = yuragim' da k -> g almashinuvi bor."),
        ("Qaysi so'zda tovush ortishi hodisasi kuzatiladi?", "Pastqam (past + qam)", ["Aqlan", "Parvo", "Mening"], "Past + qam so'zida qo'shimcha tovush shakllanadi yoki 'u + ga = unga' da 'n' tovushi ortadi."),
        ("Quyidagi so'zlardan qaysi birida urg'u birinchi bo'g'inga tushadi?", "Hamma, barcha, doim", ["Kitobxona", "O'quvchilar", "Kelmoq"], "Gumon va belgilash olmoshlarida (hamma, barcha) hamda ba'zi ravishlarda urg'u birinchi bo'g'inga tushadi."),
        ("Quyidagi qatorda faqat jarangli undoshlar berilgan qatorni toping.", "b, d, g, z, v, j", ["p, t, k, s, f, x", "b, p, d, t", "m, n, s, t"], "b, d, g, v, z, j, g', y, l, m, n, r jarangli undoshlardir.")
    ]
    for _ in range(110):
        t = random.choice(fonetika_qs)
        questions.append(make_q(5, "Fonetika va Grafika", t[0], t[1], t[2], t[3], "oson", "5-sinf"))

    # 2. Leksikologiya va Frazeologiya (110 questions)
    leksika_qs = [
        ("'Ko'z ochib yumguncha' iborasining ma'nodoshi (sinonimi) qaysi?", "Zumdun-zumda (juda tez fursatda)", ["Katta qiyinchilik bilan", "Uzoq vaqt kutib", "G'azab bilan"], "Bu ibora ish-harakatning juda tez va lahzada sodir bo'lishini anglatadi."),
        ("'Tepasi soch tikka bo'ldi' iborasi qanday ma'noni bildiradi?", "Qattiq qo'rqdi yoki hayratlandi", ["Juda xursand bo'ldi", "Charchab uxlab qoldi", "Kasal bo'lib qoldi"], "Kutilmagan dahshat yoki kuchli qo'rquv holatini ifodalaydi."),
        ("'Oyog'ini qo'liga olib yugurdi' iborasining ma'nosi nima?", "Juda tez, shoshib qochdi/yugurdi", ["Sekin qadam tashladi", "Yiqilib tushdi", "Adashib qoldi"], "Shoshilinch va tezkor harakatni bildiradi."),
        ("Quyidagi so'z juftliklaridan qaysi biri paronim hisoblanadi?", "Asr (yuz yil) - Asir (tutqun)", ["Katta - Ulkan", "Oq - Qora", "Bosh - Oyoq"], "Talaffuzi va yozilishi yaqin, lekin ma'nosi butunlay boshqa so'zlar paronimlar deyiladi."),
        ("Quyidagi so'zlardan qaysi biri omonim (shakldosh) so'z hisoblanadi?", "O't (o'simlik, olov, harakat)", ["Qalam", "Daftar", "Kitob"], "Yozilishi va aytilishi bir xil, leksik ma'nosi turlicha bo'lgan so'z - omonim."),
        ("'Zamondosh, safdosh, maslakdosh' so'zlari qanday munosabatda?", "Sinonim (ma'nodosh) so'zlar", ["Antonim so'zlar", "Omonim so'zlar", "Paronim so'zlar"], "Bir-biriga yaqin tushunchalarni ifodalovchi so'zlar ma'nodosh so'zlardir."),
        ("'Katta zal qarsak chaldi' jumlasida ma'no ko'chishining qaysi turi qo'llangan?", "Metonimiya (idish nomining ichidagiga ko'chishi)", ["Metafora", "Sinekdoxa", "Vazifadoshlik"], "Zal qarsak chalmadi, balki zaldagi odamlar qarsak chaldi - metonimiya.")
    ]
    for _ in range(110):
        t = random.choice(leksika_qs)
        questions.append(make_q(5, "Leksikologiya va Iboralar", t[0], t[1], t[2], t[3], "orta", "6-sinf"))

    # 3. So'z Yasalishi va Tarkibi (100 questions)
    word_form = [
        ("Quyidagi so'zlardan qaysi biri yasama so'z hisoblanadi?", "Gulzor (gul + zor)", ["Gullar", "Guldan", "Gulim"], "-zor o'rin-joy otini yasovchi qo'shimchadir."),
        ("Quyidagi qo'shimchalardan qaysi biri fe'l yasovchi qo'shimcha hisoblanadi?", "-la (tuzla, oqla, ishla)", ["-chi", "-dosh", "-zor"], "-la ot va sifatlardan fe'l yasovchi eng sermahsul qo'shimchadir."),
        ("Quyidagi so'zlardan qaysi biri qo'shma so'z hisoblanadi?", "Beshburchak, temiryo'l", ["Kitobxon", "Guldon", "O'qituvchi"], "Ikki yoki undan ortiq mustaqil o'zakning birikuvidan hosil bo'lgan so'zlar qo'shma so'z deyiladi."),
        ("Qaysi qatorda juft so'z to'g'ri chiziqcha bilan yozilgan?", "Ota-ona, qovun-tarvuz", ["Otaona", "Katta-kichiklik", "Birato'la"], "Juft va takroriy so'zlar har doim chiziqcha (defis) bilan yoziladi."),
        ("Qaysi so'zda faqat so'z o'zgartiruvchi qo'shimchalar qatnashgan?", "Kitoblarimizdan (lar + imiz + dan)", ["Ishxona", "Bog'bon", "Sinfdosh"], "Ko'plik, egalik va kelishik qo'shimchalari so'z o'zgartiruvchi hisoblanadi.")
    ]
    for _ in range(100):
        t = random.choice(word_form)
        questions.append(make_q(5, "So'z tarkibi va Yasalishi", t[0], t[1], t[2], t[3], "orta", "6-sinf"))

    # 4. Morfologiya - Ot, Sifat, Son, Olmosh (110 questions)
    morph_qs = [
        ("O'zbek tilida nechta kelishik bor va qaratqich kelishigi qo'shimchasi qaysi?", "6 ta kelishik, qaratqich qo'shimchasi: -ning", ["5 ta kelishik, -ni", "7 ta kelishik, -ga", "4 ta kelishik, -da"], "O'zbek tilida 6 ta kelishik mavjud: bosh, qaratqich (-ning), tushum (-ni), jo'nalish (-ga), o'rin-payt (-da), chiqish (-dan)."),
        ("Quyidagi sifatlardan qaysi biri orttirma darajada berilgan?", "Eng chiroyli, g'oyat go'zal, qip-qizil", ["Kattaroq", "Yashilroq", "Nimrang"], "Eng, g'oyat so'zlari yoki tovush orttirish (qip-qizil) orqali orttirma daraja yasaladi."),
        ("'O'n beshtadan, uchtadan' sonlari ma'no jihatdan qaysi turga kiradi?", "Taqsim son (-tadan)", ["Chama son", "Dona son", "Tartib son"], "-tadan qo'shimchasi taqsim son yasaydi."),
        ("'Birinchidan, beshinchi sinf' so'zlaridagi son turi qaysi?", "Tartib son (-inchi, -nchi)", ["Dona son", "Jamlovchi son", "Kasr son"], "Tartib sonlar narsalarning sanoqdagi tartibini bildiradi."),
        ("'Hech kim, hech narsa, hech qachon' qanday olmoshlar hisoblanadi?", "Bo'lishsizlik olmoshlari", ["Belgilash olmoshlari", "Kishilik olmoshlari", "Gumon olmoshlari"], "Hech so'zi bilan yasalgan olmoshlar bo'lishsizlik olmoshlaridir."),
        ("'O'zim, o'zing, o'zi' olmoshlari qaysi olmosh turiga mansub?", "O'zlik olmoshi", ["Kishilik olmoshi", "Ko'rsatish olmoshi", "So'roq olmoshi"], "'O'z' so'zi egalik qo'shimchalarini olib o'zlik olmoshini hosil qiladi.")
    ]
    for _ in range(110):
        t = random.choice(morph_qs)
        questions.append(make_q(5, "Morfologiya - So'z turkumlari", t[0], t[1], t[2], t[3], "oson", "7-sinf"))

    # 5. Fe'l va Nisbatlar (110 questions)
    verb_qs = [
        ("Ish-harakatning bajaruvchisi noma'lum bo'lgan fe'l nisbati qaysi?", "Majhul nisbat (-il, -in)", ["O'zlik nisbati", "Birgalik nisbati", "Orttirma nisbat"], "Majhul nisbatda harakatning kim tomonidan bajarilgani noma'lum bo'ladi (xat yozildi, bino qurildi)."),
        ("Bajaruvchining o'z ustida bajargan harakatini ifodalovchi nisbat qaysi?", "O'zlik nisbati (-in, -il, -ish)", ["Majhul nisbat", "Orttirma nisbat", "Birgalik nisbati"], "Kiyindi, tarandi, yuvindi - o'zlik nisbatidagi fe'llardir."),
        ("Ish-harakatning birgalashib, to'dalanib bajarilishini bildiruvchi nisbat qaysi?", "Birgalik nisbati (-ish, -sh)", ["Orttirma nisbat", "Majhul nisbat", "Bosh nisbat"], "Kulishdi, yozishdi, yugurishdi - birgalik nisbatidir."),
        ("Bajaruvchi harakatni boshqa birovga bajartirganini bildiruvchi nisbat qaysi?", "Orttirma nisbat (-dir, -tir, -t, -sat, -qaz)", ["Bosh nisbat", "O'zlik nisbati", "Majhul nisbat"], "Yozdirdi, tozalattirdi, o'qitdi - orttirma nisbat shakllaridir."),
        ("Fe'lning zamon va shaxs-sonda o'zgarmaydigan funksional shakllarini toping.", "Sifatdosh, ravishdosh, harakat nomi", ["Buyruq mayli", "Shart mayli", "Xabar mayli"], "Bu shakllar fe'lning noaniq (funksional) shakllari hisoblanadi.")
    ]
    for _ in range(110):
        t = random.choice(verb_qs)
        questions.append(make_q(5, "Fe'l nisbatlari va Shakllari", t[0], t[1], t[2], t[3], "orta", "7-sinf"))

    # 6. Sintaksis va Gap bo'laklari (110 questions)
    synt_qs = [
        ("Gapning qaysi bo'lagi kim? nima? qayer? so'roqlariga javob bo'lib, harakat bajaruvchisini ko'rsatadi?", "Ega", ["Kesim", "To'ldiruvchi", "Hol"], "Ega gapning bosh bo'lagi bo'lib, harakat egasini ifodalaydi."),
        ("Gapning qaysi bo'lagi qanday? qaysi? qancha? kimning? so'roqlariga javob bo'ladi?", "Aniqlovchi", ["Hol", "To'ldiruvchi", "Kesim"], "Aniqlovchi ot yoki otlashgan so'zga bog'lanib, belgini bildiradi."),
        ("Qay tarzda? qachon? qayerda? nima uchun? kabi so'roqlarga javob bo'luvchi ikkinchi darajali bo'lak qaysi?", "Hol", ["Ega", "To'ldiruvchi", "Aniqlovchi"], "Hol fe'l-kesimga bog'lanib, ish-harakatning bajarilish belgilarini bildiradi."),
        ("O'zaro teng huquqli sodda gaplarning bog'lovchilar yordamida birikishidan hosil bo'lgan gap qanday ataladi?", "Bog'langan qo'shma gap", ["Ergashgan qo'shma gap", "Bog'lovchisiz qo'shma gap", "Uyushiq bo'lakli sodda gap"], "Teng bog'lovchilar (va, ammo, lekin, biroq) orqali bog'langan qo'shma gaplar - bog'langan qo'shma gap."),
        ("Bitta bosh va unga tobe ergash gapdan tashkil topgan qo'shma gap nima deyiladi?", "Ergashgan qo'shma gap", ["Bog'langan qo'shma gap", "Bog'lovchisiz gap", "Ajratilgan bo'lakli gap"], "Ergash gap bosh gapning biror bo'lagini yoki butun mazmunini izohlaydi.")
    ]
    for _ in range(110):
        t = random.choice(synt_qs)
        questions.append(make_q(5, "Sintaksis - Gap bo'laklari va Turlari", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 7. Mumtoz Adabiyot - Alisher Navoiy va Xamsa (120 questions)
    navoiy_qs = [
        ("Alisher Navoiyning turkiy tilda yaratgan buyuk dostoni 'Xamsa' nechta dostondan iborat?", "5 ta dostondan", ["4 ta", "7 ta", "3 ta"], "Xamsa arabcha 'beshlik' demakdir va 5 dostonni o'z ichiga oladi."),
        ("Alisher Navoiy 'Xamsa'sining birinchi (falsafiy-pandnoma) dostoni qaysi?", "'Hayrat ul-abror' ('Yaxshi kishilarning hayratlanishi')", ["'Farhod va Shirin'", "'Layli va Majnun'", "'Sab'ai sayyor'"], "'Hayrat ul-abror' 1483-yilda yozilgan birinchi doston hisoblanadi."),
        ("Navoiyning qaysi dostonida mehnat, jasorat va vatanparvarlik timsoli bo'lgan qahramon tasvirlangan?", "'Farhod va Shirin'", ["'Layli va Majnun'", "'Saddi Iskandariy'", "'Sab'ai sayyor'"], "Farhod tog'ni teshib suv chiqargan buyuk xalq qahramoni sifatida gavdalanadi."),
        ("Alisher Navoiyning qushlar tili va tasavvufiy ramzlar orqali yozilgan asari qaysi?", "'Lison ut-tayr' ('Qushlar tili')", ["'Mahbub ul-qulub'", "'Muhokamat ul-lug'atayn'", "'Majolis un-nafois'"], "'Lison ut-tayr' Farididdin Attorning 'Mantiq ut-tayr' asariga ijodiy javobdir."),
        ("Turkiy tilning forsiy tildan boy va qudratli ekanligini ilmiy isbotlab bergan Navoiy asari qaysi?", "'Muhokamat ul-lug'atayn' ('Ikki til muhokamasi')", ["'Vaqfiya'", "'Xazoyin ul-maoniy'", "'Tarixi muluki Ajam'"], "1499-yilda yozilgan bu asarda Navoiy turkiy tilning cheksiz imkoniyatlarini dalillagan."),
        ("Alisher Navoiyning hayotining so'nggi yillarida yozilgan nasriy-axloqiy asari qaysi?", "'Mahbub ul-qulub' ('Ko'ngillar sevgani')", ["'Hayrat ul-abror'", "'Boburnoma'", "'Munshaot'"], "'Mahbub ul-qulub' jamiyat tabaqalari va axloqiy fazilatlar haqidagi nasriy durdonadir.")
    ]
    for _ in range(120):
        t = random.choice(navoiy_qs)
        questions.append(make_q(5, "Alisher Navoiy merosi", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 8. Mumtoz Shoirlar: Bobur, Yassaviy, Lutfiy, Mashrab (110 questions)
    classic_qs = [
        ("Zahiriddin Muhammad Boburning butun dunyoga mashhur tarixiy-memuar asari qaysi?", "'Boburnoma' ('Vaqoe')", ["'Avesto'", "'Shajarayi turk'", "'Qutadg'u bilig'"], "'Boburnoma' jahon memuar adabiyotining eng buyuk asarlaridan biridir."),
        ("Xoja Ahmad Yassaviyning hikmatli she'rlari to'plami qanday nomlanadi?", "'Devoni hikmat'", ["'Hibat ul-haqoyiq'", "'Devonu lug'atit turk'", "'Qutadg'u bilig'"], "Yassaviy turkiy tilda sodda va ta'sirchan hikmatlar yozgan."),
        ("Turkiy tildagi ilk didaktik (ta'limiy-axloqiy) doston 'Qutadg'u bilig'ning muallifi kim?", "Yusuf Xos Hojib (1069-yil)", ["Mahmud Qoshg'ariy", "Ahmad Yugnakiy", "Al-Farg'oniy"], "'Qutadg'u bilig' - Saodatga eltuvchi bilim demakdir."),
        ("Turkiy xalqlarning ilk qomusiy lug'ati 'Devonu lug'atit turk' muallifi kim?", "Mahmud Qoshg'ariy (XI asr)", ["Yusuf Xos Hojib", "Ahmad Yassaviy", "Al-Buxoriy"], "Mahmud Qoshg'ariy turkiy qabilalar tillari va xaritasini yaratgan buyuk tilshunosdir."),
        ("Bobur lirik merosida qaysi she'riy janr alohida yuksak mahorat bilan yaratilgan?", "Ruboiylar", ["Dostonlar", "Qasidalar", "Fardlar"], "Bobur ruboiy janrining Alisher Navoiydan keyingi eng yirik ustasidir.")
    ]
    for _ in range(110):
        t = random.choice(classic_qs)
        questions.append(make_q(5, "Mumtoz adabiyot", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 9. Jadid Adabiyoti: Qodiriy, Cho'lpon, Fitrat, Behbudiy (100 questions)
    jadid_qs = [
        ("O'zbek adabiyotida birinchi milliy romanning nomi va muallifi kim?", "'O'tkan kunlar' (Abdulla Qodiriy, 1922-1926)", ["'Kecha va kunduz' (Cho'lpon)", "'Navoiy' (Oybek)", "'Padarkush' (Behbudiy)"], "Abdulla Qodiriy 'O'tkan kunlar' orqali o'zbek romanchiligiga asos soldi."),
        ("O'zbek dramaturgiyasining ilk namunasi bo'lgan 'Padarkush' dramasining muallifi kim?", "Mahmudxo'ja Behbudiy (1911-yil)", ["Abdulla Qodiriy", "Munavvarqori", "Hamza"], "Behbudiy 'Padarkush' orqali jaholat va ilmsizlik oqibatlarini ko'rsatgan."),
        ("'Go'zal', 'Binafsha', 'Ko'ngil' kabi lirik she'rlar va 'Kecha va kunduz' romani muallifi kim?", "Abdulhamid Sulaymon o'g'li Cho'lpon", ["Abdurauf Fitrat", "G'afur G'ulom", "Usmon Nosir"], "Cho'lpon milliy istiqlol va ozodlik kuychisi bo'lgan buyuk shoir va adibdir."),
        ("'Abulfayzxon' tarixiy fojiasi va 'Qiyomat' asari muallifi qaysi jadid adibi?", "Abdurauf Fitrat", ["Behbudiy", "Cho'lpon", "Avloniy"], "Fitrat o'zbek adabiyotida ilk fojiachi (tragediyanavis) hisoblanadi."),
        ("'Tarbiya biz uchun yo hayot - yo mamot, yo najot - yo halokat...' hikmati kimga tegishli?", "Abdulla Avloniy ('Turkiy guliston yoxud axloq')", ["Mahmudxo'ja Behbudiy", "Munavvarqori", "Ismoil Gasprinskiy"], "Avloniy yosh avlod ta'lim-tarbiyasini millat taqdiri deb baholagan.")
    ]
    for _ in range(100):
        t = random.choice(jadid_qs)
        questions.append(make_q(5, "Jadid adabiyoti", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 10. XX Asr va Zamonaviy Adabiyot (100 questions)
    modern_qs = [
        ("'O'zbegim' qasidasi va 'Ruhlar isyoni' dostoni muallifi, O'zbekiston Qahramoni kim?", "Erkin Vohidov", ["Abdulla Oripov", "G'afur G'ulom", "Oybek"], "Erkin Vohidov o'zbek milliy g'ururini kuylagan buyuk shoirdir."),
        ("O'zbekiston Respublikasi Davlat Madhiyasi matni muallifi, O'zbekiston Qahramoni kim?", "Abdulla Oripov", ["Erkin Vohidov", "Muhammad Yusuf", "Oybek"], "Abdulla Oripov 'O'zbekiston', 'Munojot' va Madhiyamiz muallifidir."),
        ("'Shum bola' qissasi va 'Sen yetim emassan' she'ri muallifi kim?", "G'afur G'ulom", ["Abdulla Qahhor", "Oybek", "Hamid Olimjon"], "G'afur G'ulom akademik, xalq shoiri va buyuk adibdir."),
        ("O'zbek adabiyotida kichik hikoya janrining buyuk ustasi ('Anor', 'Bemor', 'O'g'ri') kim?", "Abdulla Qahhor", ["Said Ahmad", "O'tkir Hoshimov", "Tog'ay Murod"], "Abdulla Qahhor Chexovona ixcham va teran hikoyalari bilan mashhur."),
        ("'Dunyoning ishlari' va 'Ikki eshik orasi' roman-qissalari muallifi kim?", "O'tkir Hoshimov", ["Tog'ay Murod", "Pirimqul Qodirov", "Omon Muxtor"], "O'tkir Hoshimov xalq qalbiga yaqin samimiy asarlar yozgan sevimli adibdir."),
        ("'Yulduzlar mangu yonadi', 'Otamdan qolgan dalalar' asarlari muallifi kim?", "Tog'ay Murod", ["Said Ahmad", "Shukur Xolmirzayev", "Xurshid Do'stmuhammad"], "Tog'ay Murod o'zbekona xarakter va ruhiyatni betakror ifodalagan adib.")
    ]
    for _ in range(100):
        t = random.choice(modern_qs)
        questions.append(make_q(5, "Zamonaviy o'zbek adabiyoti", t[0], t[1], t[2], t[3], "oson", "9-sinf"))

    print(f"Generated {len(questions)} Uzbek language & literature questions.")
    return questions

if __name__ == "__main__":
    qs = generate_uzbek_questions()
    cnt = insert_questions(qs)
    print(f"Successfully inserted {cnt} Uzbek questions into database.")
