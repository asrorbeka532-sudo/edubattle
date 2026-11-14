import random
from common import make_q, insert_questions

def generate_cs_questions():
    questions = []

    # 1. Axborot o'lchov birliklari (110 questions)
    for _ in range(60):
        # 1 KB = 1024 B, 1 MB = 1024 KB
        unit_pairs = [
            ("1 Bayt", "8 bit", ["10 bit", "4 bit", "16 bit"], "1 Bayt = 8 bitdan iborat eng kichik adreslanadigan xotira birligidir."),
            ("1 Kilobayt (KB)", "1024 bayt", ["1000 bayt", "512 bayt", "2048 bayt"], "1 KB = 2¹⁰ = 1024 bayt."),
            ("1 Megabayt (MB)", "1024 Kilobayt (KB)", ["1000 KB", "1024 Bayt", "2048 KB"], "1 MB = 1024 KB = 2²⁰ bayt."),
            ("1 Gigabayt (GB)", "1024 Megabayt (MB)", ["1000 MB", "1024 KB", "512 MB"], "1 GB = 1024 MB = 2³⁰ bayt."),
            ("1 Terabayt (TB)", "1024 Gigabayt (GB)", ["1000 GB", "1024 MB", "512 GB"], "1 TB = 1024 GB = 2⁴⁰ bayt.")
        ]
        u = random.choice(unit_pairs)
        q_text = f"Axborot o'lchov birliklarida {u[0]} nechaga teng?"
        questions.append(make_q(8, "Axborot o'lchov birliklari", q_text, u[1], u[2], u[3], "oson", "5-sinf"))

    for _ in range(50):
        val = random.choice([2, 3, 4, 5, 8, 10])
        kb = val * 1024
        q_text = f"{val} Megabayt (MB) necha Kilobayt (KB) bo'ladi?"
        ans = f"{kb} KB"
        wrongs = [f"{val * 1000} KB", f"{kb // 2} KB", f"{kb + 512} KB"]
        exp = f"{val} MB = {val} · 1024 = {kb} KB."
        questions.append(make_q(8, "Axborot miqdori hisoblash", q_text, ans, wrongs, exp, "orta", "6-sinf"))

    # 2. Sanoq Sistemalari (110 questions)
    bin_numbers = [
        (1, "1"), (2, "10"), (3, "11"), (4, "100"), (5, "101"),
        (6, "110"), (7, "111"), (8, "1000"), (9, "1001"), (10, "1010"),
        (11, "1011"), (12, "1100"), (13, "1101"), (14, "1110"), (15, "1111"),
        (16, "10000"), (20, "10100"), (32, "100000")
    ]
    for _ in range(60):
        dec, b_val = random.choice(bin_numbers)
        if random.random() < 0.5:
            q_text = f"O'nlik sanoq sistemasidagi {dec} soni ikkilik sanoq sistemasida qanday yoziladi?"
            ans = b_val
            wrongs = [f"{b_val}0", f"{b_val[:-1]}0" if len(b_val) > 1 else "10", f"1{b_val}"]
            exp = f"{dec} ni ketma-ket 2 ga bo'lgandagi qoldiqlarni teskari yozish orqali: {b_val}₂ hosil bo'ladi."
        else:
            q_text = f"Ikkilik sanoq sistemasidagi {b_val}₂ soni o'nlik sanoq sistemasida nechaga teng?"
            ans = str(dec)
            wrongs = [str(dec + 1), str(dec - 1 if dec > 1 else dec + 2), str(dec * 2)]
            exp = f"{b_val}₂ ning o'nlik ekvivalenti: {dec}₁₀."
        questions.append(make_q(8, "Sanoq sistemalari", q_text, ans, wrongs, exp, "orta", "7-sinf"))

    for _ in range(50):
        hex_data = [
            (10, "A"), (11, "B"), (12, "C"), (13, "D"), (14, "E"), (15, "F"), (16, "10"), (255, "FF")
        ]
        dec, h_val = random.choice(hex_data)
        q_text = f"O'nlik sanoq sistemasidagi {dec} soni 16 lik (o'n oltilik) sanoq sistemasida qanday belgilanadi?"
        ans = h_val
        wrongs = [chr(ord(h_val[0]) + 1) if h_val.isalpha() else "1F", "G", "0A"]
        exp = f"16 lik sanoq sistemasida 10-15 sonlari A, B, C, D, E, F harflari bilan belgilanadi: {dec} = {h_val}."
        questions.append(make_q(8, "O'n oltilik sanoq sistemasi", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    # 3. Kompyuter Apparat Ta'minoti (Hardware) (100 questions)
    hw_qs = [
        ("Kompyuterning asosiy 'miyasi' - amallarni bajaruvchi va hisob-kitob qiluvchi qurilma nima?", "Markaziy protsessor (CPU)", ["Tezkor xotira (RAM)", "Qattiq disk (SSD)", "Ona plata (Motherboard)"], "CPU (Central Processing Unit) barcha buyruqlar va arifmetik-mantiqiy amallarni bajaradi."),
        ("Kompyuter o'chirilganda undagi barcha axborotlar o'chib ketadigan vaqtinchalik tezkor xotira nima?", "Tezkor xotira (RAM / OZU)", ["Doimiy xotira (ROM)", "Qattiq disk (HDD)", "Fleshka"], "RAM uchuvchan xotira bo'lib, kompyuter o'chishi bilan tozalanadi."),
        ("Kompyuterning barcha ichki qismlarini (CPU, RAM, videokarta) o'zaro bog'lab turuvchi asosiy plata nima?", "Ona plata (Motherboard)", ["Quvvat bloki", "Kuler (ventilyator)", "Shina"], "Ona plata kompyuterning barcha qismlarini bog'lovchi poydevordir."),
        ("Axborotlarni uzoq muddat ishonchli saqlash uchun xizmat qiluvchi zamonaviy tezkor saqlash qurilmasi qaysi?", "SSD disk (Solid State Drive)", ["RAM", "Kesh xotira", "Registr"], "SSD mikrosxemalar asosida ishlaydigan zamonaviy va tezkor diskdir."),
        ("Faqat kiritish qurilmalari berilgan qatorni toping.", "Klaviatura, sichqoncha, skaner, mikrofon", ["Monitor, printer, kolonka", "Protsessor, RAM, ona plata", "Fleshka, quloqchin, proyektor"], "Klaviatura, sichqoncha, skaner kompyuterga ma'lumot kiritadi.")
    ]
    for _ in range(100):
        t = random.choice(hw_qs)
        questions.append(make_q(8, "Hardware - Apparat ta'minoti", t[0], t[1], t[2], t[3], "oson", "6-sinf"))

    # 4. Operatsion Tizimlar va Fayllar (100 questions)
    os_qs = [
        ("Kompyuter uskunalari bilan foydalanuvchi va amaliy dasturlar o'rtasida muloqotni ta'minlovchi tizimli dasturiy ta'minot nima?", "Operatsion tizim (OT / OS)", ["Antivirus", "Matn muharriri", "Dasturlash tili"], "Operatsion tizim (Windows, Linux, macOS) kompyuterning butun faoliyatini boshqaradi."),
        ("Ochiq kodli (Open Source) va bepul tarqatiluvchi mashhur operatsion tizim qaysi?", "Linux (Ubuntu, Debian, Fedora)", ["Windows", "macOS", "MS-DOS"], "Linux ochiq kodli tizim bo'lib, uning kodi hamma uchun ochiq."),
        ("Matnli hujjatlarning rasmiy kengaytmasini ko'rsating.", ".docx yoki .txt", [".mp3", ".exe", ".jpg"], ".docx (Word) va .txt matnli fayl kengaytmalaridir."),
        ("Grafik tasvir (rasm) fayllarining kengaytmasini toping.", ".jpg, .png, .gif, .bmp", [".mp4, .avi", ".exe, .bat", ".docx, .pdf"], "Bular rasm va tasvirlarning formatlaridir."),
        ("Bajariluvchi dasturiy fayl kengaytmasini ko'rsating.", ".exe (Executable)", [".mp3", ".jpg", ".txt"], ".exe - Windows tizimida dasturlarni ishga tushiruvchi fayl kengaytmasi."),
        ("Arxivlangan (siqilgan) fayllar kengaytmasi qaysi?", ".zip yoki .rar", [".docx", ".html", ".mp4"], "Fayllar hajmini kamaytirish uchun ZIP va RAR arxivatorlaridan foydalaniladi.")
    ]
    for _ in range(100):
        t = random.choice(os_qs)
        questions.append(make_q(8, "Operatsion tizimlar va Fayllar", t[0], t[1], t[2], t[3], "oson", "7-sinf"))

    # 5. MS Excel va Amaliy Dasturlar (110 questions)
    excel_qs = [
        ("MS Excel jadvalida sonlarning yig'indisini hisoblovchi standart funksiya qaysi?", "=SUM() (yoki =СУММ())", ["=AVERAGE()", "=COUNT()", "=MAX()"], "SUM funksiyasi berilgan katakchalar diapazonidagi sonlarni qo'shadi."),
        ("MS Excelda sonlarning o'rtacha arifmetik qiymatini hisoblovchi funksiya qaysi?", "=AVERAGE() (yoki =СРЗНАЧ())", ["=SUM()", "=MIN()", "=IF()"], "AVERAGE ko'rsatilgan diapazondagi sonlarning o'rtacha qiymatini hisoblaydi."),
        ("MS Excel formulalar har doim qaysi belgi bilan boshlanadi?", "= (tenglik belgisi)", ["+", "#", "$"], "Excelda har qanday hisoblash formulasi '=' bilan boshlanadi."),
        ("Excelda mutlaq (o'zgarmas) katakcha manzilini belgilash uchun qaysi belgidan foydalaniladi?", "$ (dollar belgisi, masalan $A$1)", ["#", "@", "%"], "$ belgisi nusxa ko'chirilganda katakcha manzilining siljimasligini ta'minlaydi."),
        ("Excelda berilgan diapazondagi eng katta va eng kichik sonni topuvchi funksiyalar qaysilar?", "=MAX() va =MIN()", ["=SUM() va =COUNT()", "=UPPER() va =LOWER()", "=TOP() va =BOT()"], "MAX - maksimum, MIN - minimum sonni aniqlaydi.")
    ]
    for _ in range(110):
        t = random.choice(excel_qs)
        questions.append(make_q(8, "MS Excel va Jadval protsessorlari", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 6. Kompyuter Tarmoqlari va Internet (110 questions)
    net_qs = [
        ("Bitta xona, bino yoki tashkilot doirasidagi kompyuterlarni birlashtiruvchi tarmoq qanday ataladi?", "LAN (Mahalliy / Local Area Network)", ["WAN (Global tarmoq)", "MAN (Shahar tarmog'i)", "PAN"], "LAN cheklangan hududiy kompyuter tarmog'idir."),
        ("Butun dunyo bo'ylab millionlab kompyuterlarni bog'lovchi global kompyuter tarmog'i nima?", "Internet (WAN)", ["Intranet", "LAN", "Bluetooth"], "Internet butun jahon kompyuter tarmog'idir."),
        ("Tarmoqdagi har bir qurilmaning o'ziga xos takrorlanmas raqamli manzili nima?", "IP-manzil (masalan, 192.168.1.1)", ["URL manzil", "Domen nomi", "Elektron pochta"], "IP (Internet Protocol) manzil kompyuterning tarmoqdagi unikal identifikatoridir."),
        ("Veb-sahifalarni ko'rish va Internetda ishlash uchun mo'ljallangan dastur nima deb ataladi?", "Veb-brauzer (Google Chrome, Firefox, Safari)", ["Qidiruv tizimi", "Operatsion tizim", "Antivirus"], "Brauzer veb-sahifalar kodini o'qib, ekranda ko'rsatib beradi."),
        ("Xavfsiz va shifrlangan ma'lumot uzatuvchi veb-protokolni ko'rsating.", "HTTPS (Port 443)", ["HTTP (Port 80)", "FTP", "Telnet"], "HTTPS protokoli SSL/TLS shifrlash orqali xavfsizlikni ta'minlaydi.")
    ]
    for _ in range(110):
        t = random.choice(net_qs)
        questions.append(make_q(8, "Tarmoqlar va Internet", t[0], t[1], t[2], t[3], "oson", "8-sinf"))

    # 7. Kiberxavfsizlik (100 questions)
    sec_qs = [
        ("Foydalanuvchilarni aldamchi havolalar orqali login va parollarini o'g'irlash xuruji nima deyiladi?", "Fishing (Phishing)", ["Spam", "DDoS hujumi", "Troya"], "Fishing soxta veb-sahifalar orqali shaxsiy ma'lumotlarni o'g'irlashdir."),
        ("O'zini foydali dastur niqobi ostida ko'rsatib, tizimga yashirincha zarar keltiruvchi dastur qaysi?", "Troya oti (Trojan)", ["Fishing", "Xaker", "Kuki (Cookie)"], "Troya dasturlari foydali dastur ko'rinishida yashirinadi."),
        ("Xavfsiz va mustahkam parolda nimalar bo'lishi tavsiya etiladi?", "Katta va kichik harflar, sonlar hamda maxsus belgilar (@, #, $) kamida 8-12 belgi", ["Faqat tug'ilgan sana", "Faqat 12345678", "Faqat foydalanuvchi ismi"], "Kuchli parollar turli registrli harflar, raqamlar va belgilarni o'z ichiga olishi shart."),
        ("Akkaunt xavfsizligini oshirish uchun paroldan tashqari telefonga SMS kod kelishi nima deyiladi?", "Ikki bosqichli autentifikatsiya (2FA)", ["Bir martalik parol", "Biometriya", "Shifrlash"], "2FA paroldan tashqari ikkinchi xavfsizlik qatlamini yaratadi.")
    ]
    for _ in range(100):
        t = random.choice(sec_qs)
        questions.append(make_q(8, "Kiberxavfsizlik asoslari", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 8. Algoritmlar Nazariyasi (110 questions)
    algo_qs = [
        ("Algoritmning natijaga erishish va chekli sondagi qadamlardan iborat bo'lish xossasi nima?", "Natijaviylik (cheklilik)", ["Diskretlik", "Tushunarlilik", "Ommaviylik"], "Har qanday algoritm chekli qadamdan so'ng natija berishi kerak."),
        ("Algoritmning alohida-alohida, ketma-ket bajariluvchi qadamlarga bo'linish xossasi nima?", "Diskretlik", ["Aniqlik", "Ommaviylik", "Natijaviylik"], "Diskretlik - algoritmning bo'laklardan iborat bo'lishidir."),
        ("Algoritmning bitta emas, balki bir turdagi barcha masalalarga qo'llana olish xossasi nima?", "Ommaviylik", ["Tushunarlilik", "Diskretlik", "Natijaviylik"], "Ommaviylik har xil boshlang'ich ma'lumotlar bilan ishlash imkonini beradi."),
        ("Blok-sxemada shart tekshirish (tarmoqlanish) amali qaysi geometrik shakl bilan belgilanadi?", "Romb shakli bilan", ["To'rtburchak", "Oval", "Parallelogramm"], "Romb shart tekshirish va ikki yo'ldan birini tanlashni ifodalaydi."),
        ("Blok-sxemada ma'lumotlarni kiritish va chiqarish qaysi shakl orqali ifodalanadi?", "Parallelogramm bilan", ["Oval", "Romb", "To'rtburchak"], "Parallelogramm kiritish/chiqarish amalini ko'rsatadi."),
        ("Blok-sxemaning boshlanishi va tugashini bildiruvchi shakl nima?", "Oval (yoki burchaklari yumaloqlangan to'rtburchak)", ["Romb", "Aylana", "Uchburchak"], "Oval har doim algoritm boshlanishi va tugashini belgilaydi.")
    ]
    for _ in range(110):
        t = random.choice(algo_qs)
        questions.append(make_q(8, "Algoritmlar nazariyasi", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 9. Dasturlash - Python Asoslari (120 questions)
    python_qs = [
        ("Python tilida konsolga (ekranga) matn chiqaruvchi standart funksiya qaysi?", "print()", ["input()", "echo()", "write()"], "print() matn yoki o'zgaruvchilarni ekranga chiqaradi."),
        ("Python tilida foydalanuvchidan ma'lumot kiritishni qabul qiluvchi funksiya qaysi?", "input()", ["scan()", "get()", "read()"], "input() konsoldan kiritilgan ma'lumotni satr (str) sifatida o'qiydi."),
        ("Quyidagi kod natijasini toping: print(type(5.5))", "<class 'float'>", ["<class 'int'>", "<class 'str'>", "<class 'bool'>"], "5.5 o'nlik kasr son bo'lib, float toifasiga kiradi."),
        ("Python tilida butun sonlar qaysi ma'lumot toifasiga mansub?", "int (integer)", ["float", "str", "bool"], "Butun sonlar int toifasida saqlanadi."),
        ("Python tilida butun qismli bo'lish operatori qaysi?", "// (ikkita qiyshiq chiziq)", ["/", "%", "**"], "// bo'lishda faqat butun qismni oladi (masalan 7 // 2 = 3)."),
        ("Python tilida qoldiqni hisoblash operatori qaysi?", "% (foiz belgisi)", ["//", "/", "**"], "7 % 3 = 1 (7 ni 3 ga bo'lgandagi qoldiq 1)."),
        ("Python tilida darajaga ko'tarish operatori qaysi?", "** (ikkita yulduzcha)", ["^", "*", "pow"], "2 ** 3 = 8 (2 ning kubi 8)."),
        ("Python tilida ro'yxat (list) elementlari qaysi qavslar ichida yoziladi?", "[ ] (to'rtburchak qavslar)", ["{ }", "( )", "< >"], "Ro'yxatlar to'rtburchak qavslar [1, 2, 3] bilan belgilanadi."),
        ("Ro'yxat oxiriga yangi element qo'shish metodi qaysi?", "append()", ["add()", "insert()", "push()"], "my_list.append(item) elementni ro'yxat oxiriga joylaydi."),
        ("Satr yoki ro'yxatning uzunligini (elementlar sonini) aniqlovchi funksiya qaysi?", "len()", ["size()", "count()", "length()"], "len() elementlar sonini qaytaradi.")
    ]
    for _ in range(120):
        t = random.choice(python_qs)
        questions.append(make_q(8, "Dasturlash - Python asoslari", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 10. Veb Texnologiyalar va Sun'iy Intellekt (100 questions)
    web_ai_qs = [
        ("Veb-sahifaning strukturasini (karkasini) yaratuvchi gipermatnli belgilash tili nima?", "HTML (HyperText Markup Language)", ["CSS", "JavaScript", "Python"], "HTML sahifa tuzilishini yaratadi."),
        ("Veb-sahifaga dizayn, ranglar, shriftlar va chiroyli ko'rinish beruvchi texnologiya nima?", "CSS (Cascading Style Sheets)", ["HTML", "SQL", "PHP"], "CSS veb-sahifaning tashqi uslubini belgilaydi."),
        ("Veb-sahifaga interaktivlik, dinamika va harakat qo'shuvchi dasturlash tili qaysi?", "JavaScript (JS)", ["HTML", "CSS", "C++"], "JavaScript brauzer ichida dinamik amallarni bajaradi."),
        ("HTML tilida boshqa sahifaga havola (link) yaratuvchi teg qaysi?", "<a> tegi (href atributi bilan)", ["<p>", "<img>", "<div>"], "<a href='...'>Havola</a> orqali o'tish ta'minlanadi."),
        ("Kompyuterlarga insondek mustaqil o'rganish va qaror qabul qilish imkonini beruvchi soha nima?", "Sun'iy intellekt (AI) va Mashinaviy o'rganish (ML)", ["Kriptografiya", "Grafika", "Web dizayn"], "Sun'iy intellekt inson aql-zakovatini modellashtiruvchi zamonaviy IT sohasidir.")
    ]
    for _ in range(100):
        t = random.choice(web_ai_qs)
        questions.append(make_q(8, "Web va Zamonaviy texnologiyalar", t[0], t[1], t[2], t[3], "oson", "10-sinf"))

    print(f"Generated {len(questions)} Computer Science questions.")
    return questions

if __name__ == "__main__":
    qs = generate_cs_questions()
    cnt = insert_questions(qs)
    print(f"Successfully inserted {cnt} CS questions into database.")
