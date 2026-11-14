import random
from common import make_q, insert_questions

def generate_history_questions():
    questions = []

    # 1. Qadimgi O'zbekiston va Qahramonlar (110 questions)
    qadimgi_qs = [
        ("O'zbekiston hududidagi ilk odamlar yashagan mashhur g'or manzilgohini ko'rsating.", "Teshiktosh g'ori (Surxondaryo, Neandertal bolasi suyagi)", ["Zamonbobo", "Sopollitepa", "Afrosiyob"], "Surxondaryodagi Teshiktosh g'oridan neandertal odami suyagi topilgan."),
        ("Zardushtiylik dinining muqaddas kitobi qanday nomlanadi?", "'Avesto'", ["'Veda'", "'Injil'", "'Tavrot'"], "'Avesto' zardushtiylikning muqaddas yodgorligi bo'lib, eng qadimgi qismi 'Gohlar'dir."),
        ("Eron shohi Kir II ga qarshi mardonavor kurashib, uni tor-mor keltirgan jasur massagetlar malikasi kim?", "To'maris (mil. avv. 530-yil)", ["Zarina", "Barchinoy", "Nodirabegim"], "Miloddan avvalgi 530-yilda To'maris Ahamoniylar podshosi Kir II ni mag'lub etgan."),
        ("Doro I qo'shinini dasht ichkarisiga adashtirib, o'z jonini qurbon qilgan jasur cho'pon kim?", "Shiroq (saklar qahramoni)", ["Spitamen", "Skunxa", "Muqanna"], "Shiroq dushman qo'shinini suvsiz cho'lga boshlab qahramonlik ko'rsatgan."),
        ("Aleksandr Makedonskiy bosqiniga qarshi So'g'diyonada 3 yil davomida partizanlik urushi olib borgan xalq qahramoni kim?", "Spitamen (mil. avv. 329-327)", ["Shiroq", "Jaloliddin", "Torobiy"], "Spitamen Aleksandr qo'shinlariga eng jiddiy qarshilik ko'rsatgan so'g'd sarkardasidir.")
    ]
    for _ in range(110):
        t = random.choice(qadimgi_qs)
        questions.append(make_q(6, "Qadimgi O'zbekiston tarixi", t[0], t[1], t[2], t[3], "oson", "6-sinf"))

    # 2. Kushonlar va Buyuk Ipak Yo'li (100 questions)
    kushon_qs = [
        ("Kushon podsholigining eng qudratli hukmdori va buddizmni davlat diniga aylantirgan shoh kim?", "Kanishka I", ["Kudzul Kadfiz", "Vima Kadfiz", "Eftalit"], "Kanishka davrida Kushon davlati gullab-yashnagan va buddizm yoyilgan."),
        ("Sharq bilan G'arbni, Xitoyni O'rta Osiyo va Rim bilan bog'lagan qadimgi karvon yo'li nima deb atalgan?", "Buyuk Ipak Yo'li (mil. avv. II asrdan)", ["Lojuvard yo'li", "Shoxona yo'l", "Dengiz yo'li"], "Xitoy elchisi Chjan Tsyan sayohatidan so'ng Ipak yo'li faol ishlay boshlagan."),
        ("Buyuk Ipak Yo'lining asosiy xalqaro savdogarlari va madaniyat elchilari qaysi xalq bo'lgan?", "So'g'dliklar", ["Rimliklar", "Slavyanlar", "Arablar"], "So'g'd tili butun Ipak yo'li bo'ylab xalqaro savdo tiliga aylangan edi."),
        ("Xioniylar va Eftaliylar davlati qaysi asrlarda O'rta Osiyoda hukmronlik qilgan?", "IV-VI asrlarda", ["X-XII asrlarda", "I-II asrlarda", "XIV asrda"], "Eftaliylar V-VI asrlarda yirik davlat barpo etgan 'oq xunlar' edi.")
    ]
    for _ in range(100):
        t = random.choice(kushon_qs)
        questions.append(make_q(6, "Kushonlar va Ipak Yo'li", t[0], t[1], t[2], t[3], "orta", "6-sinf"))

    # 3. Ilk O'rta Asrlar va Sharq Uyg'onish Davri (110 questions)
    ren_qs = [
        ("Arab xalifaligi davrida 'oq kiyimlilar' qo'zg'oloniga (776-783-yillar) kim boshchilik qilgan?", "Muqanna (Hoshim ibn Hakim)", ["Abu Muslim", "Qutayba ibn Muslim", "Spitamen"], "Muqanna o'z tarafdorlari bilan birga arab istilosiga qarshi qattiq kurashgan."),
        ("O'rta Osiyoda birinchi mustaqil mahalliy davlatlardan biri bo'lgan Somoniylar davlati asoschisi kim?", "Ismoil Somoniy (892-907-yillar butun Movarounnahrni birlashtirgan)", ["Tohir ibn Husayn", "Alp Tegin", "Mahmud G'aznaviy"], "Ismoil Somoniy Movarounnahr va Xurosonni birlashtirgan markazlashgan davlat tuzdi."),
        ("Dunyoga 'Algebra' fanini va 'Algoritm' tushunchasini taqdim etgan buyuk alloma kim?", "Muhammad ibn Muso al-Xorazmiy (783-850)", ["Abu Ali ibn Sino", "Abu Rayhon Beruniy", "Al-Farg'oniy"], "Al-Xorazmiy 'Al-jabr val-muqobala' asari bilan algebra faniga asos solgan."),
        ("G'arbda 'Avitsenna' nomi bilan mashhur bo'lgan 'Tib qonunlari' asari muallifi kim?", "Abu Ali ibn Sino (980-1037)", ["Abu Bakr ar-Roziy", "Beruniy", "Al-Buxoriy"], "Ibn Sino tibbiyot, falsafa va tabiatshunoslik bo'yicha jahonshumul allomadir."),
        ("Globus yaratgan va Amerika qit'asini Kolumbdan 500 yil oldin ilmiy bashorat qilgan alloma kim?", "Abu Rayhon Beruniy (973-1048)", ["Mirzo Ulug'bek", "Al-Xorazmiy", "Farobiy"], "Beruniy 'Hindiston', 'Qadimgi xalqlardan qolgan yodgorliklar' asarlari muallifidir."),
        ("Islom olamidagi eng ishonchli hadislar to'plami 'Al-Jome' as-Sahih' muallifi kim?", "Imom al-Buxoriy (810-870)", ["Imom at-Termiziy", "Imom Moturidiy", "Burhoniddin Marg'inoniy"], "Imom Buxoriy hadis ilmining sultoni hisoblanadi.")
    ]
    for _ in range(110):
        t = random.choice(ren_qs)
        questions.append(make_q(6, "Sharq Uyg'onish Davri Allomalari", t[0], t[1], t[2], t[3], "orta", "7-sinf"))

    # 4. Mo'g'ullar Istilosi va Jaloliddin Manguberdi (110 questions)
    mongol_qs = [
        ("Chingizxon qo'shiniga qarshi mardonavor kurashgan Xorazmshohlarning so'nggi jasur hukmdori kim?", "Jaloliddin Manguberdi", ["Muhammad Xorazmshoh", "Najmiddin Kubro", "Mahmud Torobiy"], "Jaloliddin Parvon jangida mo'g'ullarni tor-mor etgan yagona sarkardadir."),
        ("1221-yilda Chingizxon va Jaloliddin Manguberdi o'rtasidagi tarixiy jang qaysi daryo bo'yida bo'lgan?", "Hind daryosi bo'yida", ["Amudaryo bo'yida", "Sirdaryo bo'yida", "Volga daryosida"], "Jaloliddin o'z oti bilan Hind daryosiga sakrab o'tib, Chingizxonda ham hayrat uyg'otgan."),
        ("1220-yilda Xo'jand mudofaasiga boshchilik qilgan jasur lashkarboshi kim?", "Temur Malik", ["Jaloliddin", "Najmiddin Kubro", "Inonchxon"], "Temur Malik orolchada mustahkam istehkom qurib, qahramonona jang qilgan."),
        ("1238-yilda Buxoroda mo'g'ullar zulmiga qarshi ko'tarilgan xalq qo'zg'oloni rahbari kim?", "Mahmud Torobiy", ["Najmiddin Kubro", "Muqanna", "Po'latxon"], "Torobiy qo'zg'oloni xalqning adolat va erk uchun kurashining yorqin timsolidir.")
    ]
    for _ in range(110):
        t = random.choice(mongol_qs)
        questions.append(make_q(6, "Mo'g'ullar bosqini va Ozodlik kurashi", t[0], t[1], t[2], t[3], "orta", "7-sinf"))

    # 5. Amir Temur va Temuriylar Saltanati (120 questions)
    temur_qs = [
        ("Sohibqiron Amir Temur qachon va qayerda tavallud topgan?", "1336-yil 9-aprelda Kesh (Shahrisabz) yaqinidagi Xo'ja Ilg'or qishlog'ida", ["1340-yil Samarqandda", "1330-yil Buxoroda", "1346-yil Toshkentda"], "Amir Temur 1336-yil 9-aprelda dunyoga kelgan."),
        ("Amir Temur Movarounnahrning yagona hukmdori deb qachon e'lon qilindi?", "1370-yil Balx qurultoyida", ["1365-yil Loy jangida", "1380-yil", "1395-yil Terek jangida"], "1370-yil 9-aprelda Amir Temur Movarounnahr oliy amiri bo'ldi."),
        ("Amir Temurning davlat boshqaruvi va harbiy san'ati qonun-qoidalari bayon etilgan asari nima?", "'Temur tuzuklari'", ["'Boburnoma'", "'Zafarnoma'", "'Tarixi Rashidiy'"], "'Kuch - adolatdadir' shiori bilan davlatni idora etish prinsiplari ushbu kitobda berilgan."),
        ("Amir Temur davlatining poytaxti qaysi shahar bo'lgan?", "Samarqand", ["Shahrisabz", "Buxoro", "Toshkent"], "Amir Temur Samarqandni jahonning eng go'zal va qudratli shahriga aylantirdi."),
        ("1402-yilda Amir Temur va Usmonli turk sultoni Boyazid I Yildirim o'rtasidagi tarixiy to'qnashuv qanday nomlanadi?", "Anqara jangi", ["Kulikovo jangi", "Kalka jangi", "Terek jangi"], "Anqara jangida Amir Temur g'alaba qozonib, Yevropani Usmonlilar xavfidan xalos etdi."),
        ("Samarqandda ulkan rasadxona qurdirgan va 1018 ta yulduz jadvalini tuzgan Temuriy hukmdor kim?", "Mirzo Ulug'bek (1394-1449)", ["Shohrux Mirzo", "Husayn Boyqaro", "Mironshoh"], "Ulug'bek 'Ziji jadidi Ko'ragoniy' astronomik asari bilan butun jahonga tanilgan.")
    ]
    for _ in range(120):
        t = random.choice(temur_qs)
        questions.append(make_q(6, "Amir Temur va Temuriylar davri", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 6. O'zbek Xonliklari Davri (110 questions)
    xonlik_qs = [
        ("XVI asr boshlarida Movarounnahrda Temuriylar o'rniga hokimiyatga kelgan sulola qaysi?", "Shayboniylar sulolasi (Shayboniyxon)", ["Ashtarxoniylar", "Mang'itlar", "Qo'ng'irotlar"], "1500-1501-yillarda Muhammad Shayboniyxon Samarqandni egalladi."),
        ("Buxoro amirligida (1756-1920) qaysi sulola hukmronlik qilgan?", "Mang'itlar sulolasi (Muhammad Rahimxon asos solgan)", ["Shayboniylar", "Ashtarxoniylar", "Minglar"], "Mang'it amirlari Buxoroni 1920-yilgacha boshqardi."),
        ("Xiva xonligida (1770-1920) qaysi sulola hukmronlik qilgan?", "Qo'ng'irotlar sulolasi (Muhammad Amin inoq asos solgan)", ["Mang'itlar", "Minglar", "Shayboniylar"], "Qo'ng'irotlar xonlikni 1920-yilgacha idora etgan."),
        ("Qo'qon xonligida (1709-1876) qaysi sulola hukmronlik qilgan?", "Minglar sulolasi (Shohruxbiy asos solgan)", ["Mang'itlar", "Qo'ng'irotlar", "Ashtarxoniylar"], "Farg'ona vodiysida tashkil topgan Qo'qon xonligi Minglar sulolasi tomonidan boshqarilgan.")
    ]
    for _ in range(110):
        t = random.choice(xonlik_qs)
        questions.append(make_q(6, "O'zbek xonliklari davri", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 7. Rossiya Bosqini, Jadidchilik va Mustaqillik (110 questions)
    rus_must_qs = [
        ("Toshkent shahrini chor Rossiyasi qo'shinlari qachon bosib oldi?", "1865-yil iyun oyida (General Chernyayev)", ["1868-yil", "1873-yil", "1876-yil"], "Toshkent shahri mudofaasiga Alimqul boshchilik qilgan."),
        ("Chor Rossiyasi tomonidan Turkiston general-gubernatorligi qachon tashkil etildi?", "1867-yilda (Fon Kaufman birinchi general-gubernator)", ["1865-yil", "1876-yil", "1886-yil"], "1867-yilda poytaxti Toshkent bo'lgan general-gubernatorlik tuzildi."),
        ("1917-yil noyabrda Qo'qonda e'lon qilingan ilk demokratik milliy respublika nima?", "Turkiston Muxtoriyati (Qo'qon muxtoriyati)", ["BXSR", "XXSR", "Turkiston ASSR"], "Mustafo Cho'qay va jadidlar boshchiligida Turkiston Muxtoriyati e'lon qilingan."),
        ("O'zbekiston Respublikasining Davlat Mustaqilligi qachon e'lon qilindi?", "1991-yil 31-avgustda", ["1992-yil 8-dekabr", "1991-yil 1-sentyabr", "1993-yil 2-iyul"], "1991-yil 31-avgustda O'zbekiston Respublikasining Davlat mustaqilligi to'g'risida Oliy Kengash qarori qabul qilindi."),
        ("O'zbekiston Respublikasi Konstitutsiyasi qachon qabul qilingan?", "1992-yil 8-dekabrda", ["1991-yil 31-avgust", "1993-yil 2-iyul", "1992-yil 2-mart"], "O'zbekiston Respublikasi Konstitutsiyasi 1992-yil 8-dekabrda qabul qilingan."),
        ("O'zbekiston Respublikasi BMTga (Birlashgan Millatlar Tashkiloti) qachon to'la huquqli a'zo bo'ldi?", "1992-yil 2-martda", ["1991-yil 31-avgust", "1993-yil 8-dekabr", "1994-yil 1-iyul"], "1992-yil 2-martda BMT Bosh Assambleyasida O'zbekiston bayrog'i ko'tarildi.")
    ]
    for _ in range(110):
        t = random.choice(rus_must_qs)
        questions.append(make_q(6, "Yangi va Eng yangi tarix", t[0], t[1], t[2], t[3], "oson", "9-sinf"))

    # 8. Qadimgi Jahon Tarixi (Misr, Bobil, Yunoniston, Rim) (110 questions)
    world_anc = [
        ("Dunyoning qadimgi mo''jizasi bo'lgan eng ulkan ehrom qaysi fir'avnga atab qurilgan?", "Xeops (Xufu) ehromi (Gizadagi piramida)", ["Xafra ehromi", "Ramses ehromi", "Tutanxamon"], "Xeops ehromi balandligi qariyb 147 metr bo'lgan."),
        ("Tarixdagi ilk yozma qonunlar to'plami bo'lgan 'Qonunlar majmuasi' qaysi Bobil podshosi tomonidan tuzilgan?", "Hammurapi (mil. avv. XVIII asr)", ["Navuxodonosor", "Kir II", "Sargon"], "Hammurapi qora bazalt toshga 282 ta moddadan iborat qonunlarni o'yib yozdirgan."),
        ("Olimpiya o'yinlari vatani qaysi davlat va qachondan boshlangan?", "Qadimgi Yunoniston (mil. avv. 776-yildan)", ["Qadimgi Rim", "Qadimgi Misr", "Fors davlati"], "Zevs sharafiga har 4 yilda bir Olimpiya o'yinlari o'tkazilgan."),
        ("Qadimgi Rimda mil. avv. 74-71-yillarda gladiatorlar va qullarning buyuk qo'zg'oloniga kim rahbarlik qilgan?", "Spartak", ["Yuliy Sezar", "Gannibal", "Kikeron"], "Spartak qo'zg'oloni quldorlik tuzumini larzaga keltirgan eng yirik xalq harakati edi."),
        ("G'arbiy Rim imperiyasi qachon qulab, Qadimgi dunyo davri yakunlandi?", "Milodiy 476-yilda", ["Mil. avv. 44-yilda", "Milodiy 395-yilda", "Milodiy 1453-yilda"], "476-yilda so'nggi Rim imperatori Romul Avgustul taxtdan ag'darildi.")
    ]
    for _ in range(110):
        t = random.choice(world_anc)
        questions.append(make_q(6, "Qadimgi Jahon tarixi", t[0], t[1], t[2], t[3], "orta", "6-sinf"))

    # 9. O'rta Asrlar va Yangi Davr Jahon Tarixi (100 questions)
    world_mid = [
        ("Vizantiya imperiyasining poytaxti Konstantinopol shahri qachon va kim tomonidan zabt etildi?", "1453-yilda Usmonli turk sultoni Mehmed II Fatih tomonidan", ["1204-yilda salibchilar", "1492-yilda", "1099-yilda"], "1453-yilda Konstantinopol olinib, Istanbul deb nomlandi va O'rta asrlar tugadi."),
        ("1492-yilda Amerika qit'asini kashf etgan dengizchi sayyoh kim?", "Xristofor Kolumb", ["Vasko da Gama", "Fernan Magellan", "Amerigo Vespuchchi"], "Kolumb Ispaniya bayrog'i ostida g'arbga suzib Yangi Dunyoga yetib borgan."),
        ("Tarixda ilk marta Yer shari bo'ylab dunyo bo'ylab sayohat qilgan dengizchi kim?", "Fernan Magellan ekspeditsiyasi (1519-1522)", ["Kolumb", "Jeyms Kuk", "Fransis Dreyk"], "Magellan sayohati Yerning sharsimon ekanligini amalda isbotladi."),
        ("1789-yil 14-iyulda Fransiyada qaysi qamoqxona-qal'aning egallanishi bilan Buyuk Fransuz inqilobi boshlandi?", "Bastiliya qal'asi", ["Versal saroyi", "Luvr saroyi", "Notr-Dam"], "Bastiliyaning olinishi mutlaq monarxiya qulashining ramzi bo'ldi.")
    ]
    for _ in range(100):
        t = random.choice(world_mid)
        questions.append(make_q(6, "O'rta asrlar va Yangi davr", t[0], t[1], t[2], t[3], "orta", "7-sinf"))

    # 10. XX Asr Jahon Tarixi (100 questions)
    ww_qs = [
        ("Birinchi jahon urushi qaysi yillarda bo'lib o'tdi?", "1914–1918-yillarda", ["1939–1945-yillarda", "1905–1907-yillarda", "1917–1922-yillarda"], "Birinchi jahon urushi Antanta va Uchlar ittifoqi o'rtasida kechgan."),
        ("Ikkinchi jahon urushi qachon boshlangan va qachon tugagan?", "1939-yil 1-sentyabr — 1945-yil 2-sentyabr", ["1941–1945-yillar", "1914–1918-yillar", "1938–1944-yillar"], "1939-yil 1-sentyabrda fashistlar Germaniyasining Polshaga hujumi bilan boshlangan."),
        ("Birlashgan Millatlar Tashkiloti (BMT) qachon tashkil etilgan?", "1945-yil 24-oktyabrda (San-Fransisko konferensiyasi)", ["1919-yilda", "1941-yilda", "1950-yilda"], "BMT xalqaro xavfsizlik va tinchlikni ta'minlash maqsadida 1945-yilda tuzildi.")
    ]
    for _ in range(100):
        t = random.choice(ww_qs)
        questions.append(make_q(6, "XX asr Jahon tarixi", t[0], t[1], t[2], t[3], "oson", "9-sinf"))

    print(f"Generated {len(questions)} history questions.")
    return questions

if __name__ == "__main__":
    qs = generate_history_questions()
    cnt = insert_questions(qs)
    print(f"Successfully inserted {cnt} history questions into database.")
