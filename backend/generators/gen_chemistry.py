import random
from common import make_q, insert_questions

def generate_chemistry_questions():
    questions = []

    # 1. Mol, Molyar massa va Gazlar hajmi (110 questions)
    molar_masses = [
        ("Suv (H₂O)", 18, "H: 2·1 = 2, O: 16 => M = 18 g/mol"),
        ("Karbonat angidrid (CO₂)", 44, "C: 12, O: 2·16 = 32 => M = 44 g/mol"),
        ("Metan (CH₄)", 16, "C: 12, H: 4·1 = 4 => M = 16 g/mol"),
        ("Kislorod gazi (O₂)", 32, "O: 2·16 = 32 => M = 32 g/mol"),
        ("Azot gazi (N₂)", 28, "N: 2·14 = 28 => M = 28 g/mol"),
        ("Vodorod gazi (H₂)", 2, "H: 2·1 = 2 => M = 2 g/mol"),
        ("Sulfat kislota (H₂SO₄)", 98, "H: 2, S: 32, O: 64 => M = 98 g/mol"),
        ("Osh tuzi (NaCl)", 58.5, "Na: 23, Cl: 35.5 => M = 58.5 g/mol"),
        ("Kalsiy karbonat (CaCO₃)", 100, "Ca: 40, C: 12, O: 48 => M = 100 g/mol"),
        ("Kaliy gidroksid (KOH)", 56, "K: 39, O: 16, H: 1 => M = 56 g/mol"),
        ("Natriy gidroksid (NaOH)", 40, "Na: 23, O: 16, H: 1 => M = 40 g/mol")
    ]
    for _ in range(60):
        item = random.choice(molar_masses)
        q_text = f"{item[0]} ning molyar massasini toping (g/mol)."
        ans = f"{item[1]} g/mol"
        wrongs = [f"{item[1] + 10} g/mol", f"{item[1] - 8} g/mol", f"{int(item[1] * 1.5)} g/mol"]
        exp = f"{item[0]} molyar massasi: {item[2]}."
        questions.append(make_q(3, "Boshlang'ich tushunchalar - Molyar massa", q_text, ans, wrongs, exp, "oson", "7-sinf"))

    for _ in range(50):
        # Gaz hajmi V = n * 22.4 l
        n = random.choice([0.5, 1, 2, 3, 4, 5, 10])
        V = round(n * 22.4, 1)
        if random.random() < 0.5:
            q_text = f"Normal sharoitda (n.sh.) {n} mol gaz qancha hajmni egallaydi?"
            ans = f"{V} litr"
            wrongs = [f"{round(V * 1.5, 1)} litr", f"{round(V - 11.2, 1) if V > 11.2 else 44.8} litr", f"{n * 10} litr"]
            exp = f"Normal sharoitda 1 mol har qanday gaz 22.4 litr hajm egallaydi. V = {n} · 22.4 = {V} litr."
        else:
            q_text = f"Normal sharoitda {V} litr hajm egallagan gaz necha mol bo'ladi?"
            ans = f"{n} mol"
            wrongs = [f"{n + 1} mol", f"{round(n * 2, 1)} mol", f"{round(n / 2, 1)} mol"]
            exp = f"n = V / V_m = {V} / 22.4 = {n} mol."
        questions.append(make_q(3, "Molyar hajm", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    # 2. Davriy Qonun va Atom Tuzilishi (110 questions)
    elements_data = [
        ("Vodorod (H)", 1, 1, 1, 1, "1-davr, I guruh"),
        ("Geliy (He)", 2, 4, 1, 8, "1-davr, VIII guruh (olijanob gaz)"),
        ("Uglerod (C)", 6, 12, 2, 4, "2-davr, IV guruh"),
        ("Azot (N)", 7, 14, 2, 5, "2-davr, V guruh"),
        ("Kislorod (O)", 8, 16, 2, 6, "2-davr, VI guruh"),
        ("Ftor (F)", 9, 19, 2, 7, "2-davr, VII guruh"),
        ("Natriy (Na)", 11, 23, 3, 1, "3-davr, I guruh (ishqoriy metall)"),
        ("Magniy (Mg)", 12, 24, 3, 2, "3-davr, II guruh"),
        ("Alyuminiy (Al)", 13, 27, 3, 3, "3-davr, III guruh"),
        ("Fosfor (P)", 15, 31, 3, 5, "3-davr, V guruh"),
        ("Oltingugurt (S)", 16, 32, 3, 6, "3-davr, VI guruh"),
        ("Xlor (Cl)", 17, 35.5, 3, 7, "3-davr, VII guruh"),
        ("Kaliy (K)", 19, 39, 4, 1, "4-davr, I guruh"),
        ("Kalsiy (Ca)", 20, 40, 4, 2, "4-davr, II guruh"),
        ("Temir (Fe)", 26, 56, 4, 8, "4-davr, VIII guruh (o'tish metalli)")
    ]
    for _ in range(60):
        elem = random.choice(elements_data)
        neutrons = int(elem[2]) - elem[1]
        q_text = f"{elem[0]} atomida nechta proton va elektron mavjud?"
        ans = f"{elem[1]} ta proton, {elem[1]} ta elektron"
        wrongs = [
            f"{elem[1]} ta proton, {neutrons} ta elektron",
            f"{neutrons} ta proton, {elem[1]} ta elektron",
            f"{elem[1] + 2} ta proton, {elem[1]} ta elektron"
        ]
        exp = f"Atom neytral zarracha bo'lib, tartib raqami Z = {elem[1]} proton va elektronlar soniga teng."
        questions.append(make_q(3, "Atom tuzilishi", q_text, ans, wrongs, exp, "oson", "7-sinf"))

    for _ in range(50):
        elem = random.choice(elements_data)
        neutrons = int(elem[2]) - elem[1]
        q_text = f"{elem[0]} atomining yadrosidagi neytronlar sonini toping (A_r = {int(elem[2])})."
        ans = f"{neutrons} ta"
        wrongs = [f"{elem[1]} ta", f"{int(elem[2])} ta", f"{neutrons + 2} ta"]
        exp = f"Neytronlar soni N = A - Z = {int(elem[2])} - {elem[1]} = {neutrons} ta."
        questions.append(make_q(3, "Yadro tarkibi", q_text, ans, wrongs, exp, "oson", "7-sinf"))

    # 3. Kimyoviy Bog'lanishlar (100 questions)
    bonds_data = [
        ("Osh tuzi (NaCl)", "Ion bog'lanish", ["Kovalent qutbsiz", "Kovalent qutbli", "Vodorod bog'lanish"], "Metall (Na) va nometall (Cl) orasida ion bog'lanish hosil bo'ladi."),
        ("Xlor gazi (Cl₂)", "Kovalent qutbsiz bog'lanish", ["Kovalent qutbli", "Ion bog'lanish", "Metall bog'lanish"], "Bir xil nometall atomlari o'rtasida kovalent qutbsiz bog'lanish yuzaga keladi."),
        ("Kislorod gazi (O₂)", "Kovalent qutbsiz bog'lanish", ["Kovalent qutbli", "Ion bog'lanish", "Metall bog'lanish"], "Bir xil elektromonfiylikka ega atomlar orasidagi bog'lanish kovalent qutbsizdir."),
        ("Suv (H₂O)", "Kovalent qutbli bog'lanish", ["Kovalent qutbsiz", "Ion bog'lanish", "Metall bog'lanish"], "Har xil nometall atomlari (H va O) orasida kovalent qutbli bog'lanish mavjud."),
        ("Xlorid kislota (HCl)", "Kovalent qutbli bog'lanish", ["Kovalent qutbsiz", "Ion bog'lanish", "Metall bog'lanish"], "H va Cl atomlari orasida umumiy elektron jufti xlor tomon siljigan kovalent qutbli bog'lanish bor."),
        ("Metan (CH₄)", "Kovalent qutbli bog'lanish", ["Kovalent qutbsiz", "Ion bog'lanish", "Vodorod bog'lanish"], "C va H atomlari kovalent qutbli bog'langan."),
        ("Mis bo'lagi (Cu)", "Metall bog'lanish", ["Kovalent qutbli", "Ion bog'lanish", "Vodorod bog'lanish"], "Metall kristall panjarasida musbat ionlar va erkin elektronlar orasida metall bog'lanish mavjud."),
        ("Suv molekulalari o'rtasida", "Vodorod bog'lanish", ["Ion bog'lanish", "Kovalent qutbsiz", "Metall bog'lanish"], "Bitta suv molekulasidagi vodorod bilan boshqa suv molekulasidagi kislorod orasida vodorod bog'lanish vujudga keladi.")
    ]
    for _ in range(100):
        t = random.choice(bonds_data)
        q_text = f"{t[0]} dagi kimyoviy bog'lanish turini aniqlang."
        questions.append(make_q(3, "Kimyoviy bog'lanish", q_text, t[1], t[2], t[3], "orta", "8-sinf"))

    # 4. Oksidlanish Darajasi Hisoblash (110 questions)
    ox_data = [
        ("KMnO₄ da marganesning (Mn)", "+7", ["+2", "+4", "+6"], "K (+1) + Mn + 4·(-2) = 0 => Mn = +7."),
        ("K₂Cr₂O₇ da xromning (Cr)", "+6", ["+3", "+7", "+2"], "2·(+1) + 2Cr + 7·(-2) = 0 => 2Cr = +12 => Cr = +6."),
        ("H₂SO₄ da oltingugurtning (S)", "+6", ["+4", "+2", "-2"], "2·(+1) + S + 4·(-2) = 0 => S = +6."),
        ("SO₂ da oltingugurtning (S)", "+4", ["+6", "+2", "-2"], "S + 2·(-2) = 0 => S = +4."),
        ("H₂S da oltingugurtning (S)", "-2", ["+2", "+4", "+6"], "2·(+1) + S = 0 => S = -2."),
        ("HNO₃ da azotning (N)", "+5", ["+3", "+4", "-3"], "1 + N + 3·(-2) = 0 => N = +5."),
        ("NH₃ da azotning (N)", "-3", ["+3", "+5", "0"], "N + 3·(+1) = 0 => N = -3."),
        ("CH₄ da uglerodning (C)", "-4", ["+4", "+2", "0"], "C + 4·(+1) = 0 => C = -4."),
        ("CO₂ da uglerodning (C)", "+4", ["+2", "-4", "0"], "C + 2·(-2) = 0 => C = +4."),
        ("Fe₂O₃ da temirning (Fe)", "+3", ["+2", "+6", "+1"], "2Fe + 3·(-2) = 0 => Fe = +3."),
        ("FeO da temirning (Fe)", "+2", ["+3", "+1", "+4"], "Fe + (-2) = 0 => Fe = +2.")
    ]
    for _ in range(110):
        t = random.choice(ox_data)
        q_text = f"{t[0]} oksidlanish darajasini toping."
        questions.append(make_q(3, "Oksidlanish darajasi", q_text, t[1], t[2], t[3], "orta", "8-sinf"))

    # 5. Noorganik Moddalar Sinflari (Oksid, Asos, Kislota, Tuz) (120 questions)
    inorg_data = [
        ("CaO qaysi sinfga mansub?", "Asosli oksid", ["Kislotali oksid", "Amfoter oksid", "Tuz"], "Kalsiy oksidi suv bilan ta'sirlashib ishqor hosil qiluvchi asosli oksiddir."),
        ("SO₃ qaysi sinfga mansub?", "Kislotali oksid", ["Asosli oksid", "Befarq oksid", "Asos"], "Oltingugurt (VI) oksidi suvda erib sulfat kislota hosil qiladi."),
        ("CO₂ qaysi sinfga mansub?", "Kislotali oksid", ["Asosli oksid", "Amfoter oksid", "Ishqor"], "Karbonat angidrid kislotali oksid hisoblanadi."),
        ("Al₂O₃ va ZnO qanday oksidlar?", "Amfoter oksidlar", ["Faqat asosli oksidlar", "Faqat kislotali oksidlar", "Befarq oksidlar"], "Ham kislotalar, ham asoslar bilan reaksiyaga kirishuvchi oksidlar amfoter deyiladi."),
        ("NaOH va KOH qanday moddalar?", "Ishqorlar (eruvchan asoslar)", ["Kislotalar", "Tuzlar", "Kislotali oksidlar"], "Ishqoriy metallarning suvda yaxshi eriydigan gidroksidlari ishqorlar deyiladi."),
        ("HCl va HNO₃ qanday moddalar?", "Bir negizli kislotalar", ["Ikki negizli kislotalar", "Asoslar", "Tuzlar"], "Molekulasida 1 ta vodorod atomi bo'lgan kislotalar bir negizli kislotalardir."),
        ("H₂SO₄ qanday kislota?", "Ikki negizli kuchli kislota", ["Bir negizli kislota", "Uch negizli kislota", "Kuchsiz kislota"], "Sulfat kislota 2 ta vodorod atomiga ega kuchli mineral kislotadir."),
        ("H₃PO₄ qanday kislota?", "Uch negizli o'rtacha kuchli kislota", ["Bir negizli kislota", "Ikki negizli kislota", "Asos"], "Fosfat kislota uch negizli kislotadir."),
        ("Osh tuzi (NaCl) qanday tuz?", "O'rta (normal) tuz", ["Nordon tuz", "Asosli tuz", "Qo'shaloq tuz"], "Vodorod atomlari metall bilan to'liq almashingan tuz - o'rta tuz."),
        ("NaHCO₃ (ichimlik sodasi) qanday tuz?", "Nordon tuz (gidrokarbonat)", ["O'rta tuz", "Asosli tuz", "Oddiy oksid"], "Kislota tarkibidagi vodorod to'liq almashmagan tuzlar nordon tuzlardir.")
    ]
    for _ in range(120):
        t = random.choice(inorg_data)
        questions.append(make_q(3, "Noorganik birikmalar sinflari", t[0], t[1], t[2], t[3], "oson", "8-sinf"))

    # 6. Kimyoviy Reaksiyalar va OQR (100 questions)
    rx_data = [
        ("2H₂ + O₂ → 2H₂O reaksiyasi qaysi turga kiradi?", "Birikish reaksiyasi", ["Parchalanish", "O'rin olish", "Almashinish"], "Ikki yoki undan ortiq moddadan bitta murakkab modda hosil bo'lishi birikish reaksiyasidir."),
        ("CaCO₃ → CaO + CO₂ reaksiyasi qaysi turga kiradi?", "Parchalanish reaksiyasi", ["Birikish", "O'rin olish", "Almashinish"], "Bitta murakkab moddadan bir necha modda hosil bo'lishi parchalanish reaksiyasidir."),
        ("Zn + 2HCl → ZnCl₂ + H₂↑ reaksiyasi qaysi turga kiradi?", "O'rin olish reaksiyasi", ["Birikish", "Parchalanish", "Almashinish"], "Oddiy modda atomlari murakkab moddaning bir elementini siqib chiqarishi o'rin olish reaksiyasidir."),
        ("NaOH + HCl → NaCl + H₂O reaksiyasi qaysi turga kiradi?", "Almashinish (neytrallanish) reaksiyasi", ["Birikish", "Parchalanish", "O'rin olish"], "Kislota va asos orasidagi neytrallanish reaksiyasi almashinish reaksiyasidir."),
        ("Oksidlanish-qaytarilish reaksiyasida elektron bergan modda nima bo'ladi?", "Qaytaruvchi (o'zi oksidlanadi)", ["Oksidlovchi (o'zi qaytariladi)", "Katalizator", "Indikator"], "Elektron beruvchi atom yoki ion qaytaruvchi deyiladi."),
        ("Oksidlanish-qaytarilish reaksiyasida elektron olgan modda nima bo'ladi?", "Oksidlovchi (o'zi qaytariladi)", ["Qaytaruvchi (o'zi oksidlanadi)", "Inhibitor", "Erituvchi"], "Elektron qabul qiluvchi modda oksidlovchi deb ataladi."),
        ("Issiqlik ajralib chiqishi bilan boradigan reaksiyalar qanday ataladi?", "Ekzotermik reaksiyalar (+Q)", ["Endotermik reaksiyalar (-Q)", "Katalitik", "Qaytmas"], "Issiqlik ajralishi bilan boruvchi reaksiyalar ekzotermik deyiladi."),
        ("Issiqlik yutilishi bilan boradigan reaksiyalar qanday ataladi?", "Endotermik reaksiyalar (-Q)", ["Ekzotermik reaksiyalar (+Q)", "Zanjirli", "O'z-o'zidan yonish"], "Issiqlik yutilishi bilan boruvchi reaksiyalar endotermik deyiladi.")
    ]
    for _ in range(100):
        t = random.choice(rx_data)
        questions.append(make_q(3, "Kimyoviy reaksiyalar", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 7. Eritmalar va Massa Ulushi (110 questions)
    for _ in range(110):
        m_suv = random.choice([80, 90, 180, 190, 300, 400, 450])
        m_tuz = random.choice([10, 20, 25, 50])
        m_eritma = m_suv + m_tuz
        w = round((m_tuz / m_eritma) * 100, 1)
        q_text = f"{m_tuz} g tuz {m_suv} g suvda eritildi. Hosil bo'lgan eritmadagi tuzning massa ulushini toping (%)."
        ans = f"{w}%"
        wrongs = [f"{round(w + 5, 1)}%", f"{round(w * 1.5, 1)}%", f"{round(m_tuz / m_suv * 100, 1)}%"]
        exp = f"m_eritma = {m_tuz} + {m_suv} = {m_eritma} g. ω = (m_tuz / m_eritma) · 100% = ({m_tuz} / {m_eritma}) · 100% = {w}%."
        questions.append(make_q(3, "Eritmalar - Massa ulushi", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    # 8. Elektrolitlar va pH Muhiti (100 questions)
    ph_data = [
        ("Neytral muhitda pH ko'rsatkichi nechaga teng?", "pH = 7", ["pH < 7", "pH > 7", "pH = 0"], "Sof suv va neytral eritmalar uchun pH = 7."),
        ("Kislotali muhitda pH ko'rsatkichi qanday bo'ladi?", "pH < 7", ["pH > 7", "pH = 7", "pH = 14"], "Kislotali muhitda vodorod ionlari ko'p bo'lib, pH 7 dan kichik bo'ladi."),
        ("Ishqoriy muhitda pH ko'rsatkichi qanday bo'ladi?", "pH > 7", ["pH < 7", "pH = 7", "pH = 0"], "Ishqoriy muhitda gidroksid ionlari ko'p bo'lib, pH 7 dan 14 gacha bo'ladi."),
        ("Lakmus qog'ozi kislotali muhitda qanday rangga kiradi?", "Qizil rangga", ["Ko'k rangga", "Binafsha rangga", "Sariq rangga"], "Lakmus kislotada qizaradi, ishqorda ko'karadi."),
        ("Fenolftalein indikatori ishqoriy muhitda qanday rangga kiradi?", "To'q qizil (malina) rangga", ["Rangini o'zgartirmaydi (rangsiz)", "Sariq rangga", "Ko'k rangga"], "Fenolftalein faqat ishqoriy muhitda malina rangga kiradi, kislota va neytralda rangsiz."),
        ("Metilzarg'aldoq (metiloranj) kislotali muhitda qanday rangga bo'yaladi?", "Qizil rangga", ["Sariq rangga", "Ko'k rangga", "Rangsiz"], "Metiloranj kislotada pushti-qizil, ishqorda sariq rangga ega bo'ladi."),
        ("Quyidagi moddalardan qaysi biri kuchli elektrolit hisoblanadi?", "H₂SO₄ (sulfat kislota)", ["H₂O (suv)", "CH₃COOH (sirka kislota)", "C₆H₁₂O₆ (glyukoza)"], "Mineral kuchli kislotalar, ishqorlar va deyarli barcha eruvchan tuzlar kuchli elektrolitdir.")
    ]
    for _ in range(100):
        t = random.choice(ph_data)
        questions.append(make_q(3, "Elektrolitik dissotsilanish va pH", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 9. Muhim Elementlar va Birikmalar (100 questions)
    elem_facts = [
        ("Tabiatda eng ko'p tarqalgan kimyoviy element qaysi (Koinotda)?", "Vodorod (H)", ["Kislorod (O)", "Geliy (He)", "Temir (Fe)"], "Koinot massasining qariyb 75% ini vodorod tashkil etadi."),
        ("Yer qobig'ida eng ko'p tarqalgan element qaysi?", "Kislorod (O)", ["Kremniy (Si)", "Alyuminiy (Al)", "Temir (Fe)"], "Yer qobig'ining qariyb 49% ini kislorod tashkil qiladi."),
        ("Yer qobig'ida eng ko'p tarqalgan metall qaysi?", "Alyuminiy (Al)", ["Temir (Fe)", "Kalsiy (Ca)", "Natriy (Na)"], "Alyuminiy yer qobig'idagi eng ko'p tarqalgan metall (taxminan 8%)."),
        ("Xonaki haroratda suyuq holatda bo'ladigan yagona metall qaysi?", "Simob (Hg)", ["Qo'rg'oshin (Pb)", "Galiy (Ga)", "Litiy (Li)"], "Simob - xona haroratida suyuq metall."),
        ("Xonaki haroratda suyuq holatda bo'ladigan yagona nometall qaysi?", "Brom (Br₂)", ["Xlor (Cl₂)", "Yod (I₂)", "Ftor (F₂)"], "Brom oddiy sharoitda qizil-qo'ng'ir suyuqlikdir."),
        ("Havoning asosiy tarkibiy qismi qaysi gaz?", "Azot (N₂ - taxminan 78%)", ["Kislorod (O₂)", "Karbonat angidrid (CO₂)", "Argon (Ar)"], "Atmosfera havosining 78% hajmini azot, 21% ini kislorod egallaydi."),
        ("Vodorod sulfid (H₂S) qanday hidga ega gaz?", "Sasigan tuxum hidli zaharli gaz", ["Xushbo'y gullar hidli", "Hidsiz", "Achchiq xlor hidli"], "H₂S o'ziga xos sasigan tuxum hidiga ega."),
        ("Tibbiyotda gips bog'lamlari qo'yishda qaysi tuz ishlatiladi?", "Kalsiy sulfat (CaSO₄ · 0.5H₂O)", ["Kalsiy xlorid", "Bariy sulfat", "Natriy sulfat"], "Kuydirilgan gips suv qo'shilganda qotish xususiyatiga ega.")
    ]
    for _ in range(100):
        t = random.choice(elem_facts)
        questions.append(make_q(3, "Muhim elementlar va xossalar", t[0], t[1], t[2], t[3], "oson", "9-sinf"))

    # 10. Organik Kimyo (100 questions)
    org_data = [
        ("Alkanlarning umumiy formulasini ko'rsating.", "C_n H_{2n+2}", ["C_n H_{2n}", "C_n H_{2n-2}", "C_n H_{2n-6}"], "To'yingan uglevodorodlar (alkanlar) formulasi C_n H_{2n+2}."),
        ("Alkenlarning umumiy formulasini ko'rsating.", "C_n H_{2n}", ["C_n H_{2n+2}", "C_n H_{2n-2}", "C_n H_{2n+1}OH"], "Bitta qo'shbog'li to'yinmagan uglevodorodlar - alkenlar (C_n H_{2n})."),
        ("Alkinlarning umumiy formulasini ko'rsating.", "C_n H_{2n-2}", ["C_n H_{2n+2}", "C_n H_{2n}", "C_n H_{2n-4}"], "Bitta uchbog'li to'yinmagan uglevodorodlar - alkinlar (C_n H_{2n-2}, masalan atsetilen C₂H₂)."),
        ("Tabiiy gazning asosiy qismini (90-98%) qaysi gaz tashkil qiladi?", "Metan (CH₄)", ["Etan (C₂H₆)", "Propan (C₃H₈)", "Etilen (C₂H₄)"], "Metan tabiiy gazning asosiy tarkibiy qismidir."),
        ("Tibbiyot spirtining kimyoviy formulasi qanday?", "C₂H₅OH (etanol)", ["CH₃OH (metanol)", "C₃H₇OH", "C₃H₅(OH)₃"], "Tibbiy etil spirti - etanol (C₂H₅OH)."),
        ("Kuchli zaharli xususiyatga ega bo'lib, ko'rlik va o'limga sabab bo'ladigan spirt qaysi?", "Metanol (CH₃OH - yog'och spirti)", ["Etanol", "Glitserin", "Butanol"], "Metanol o'ta xavfli texnik zaharli moddadir."),
        ("Sirka kislotaning kimyoviy formulasi qanday?", "CH₃COOH", ["HCOOH", "C₂H₅COOH", "C₆H₅COOH"], "Sirka kislota - etan kislota (CH₃COOH)."),
        ("Chumoli kislotaning formulasi qanday?", "HCOOH", ["CH₃COOH", "CH₃OH", "H₂CO₃"], "Eng oddiy bir asosli karbon kislota - chumoli kislota (HCOOH)."),
        ("Glyukozaning molekulyar formulasi qanday?", "C₆H₁₂O₆", ["C₁₂H₂₂O₁₁", "(C₆H₁₀O₅)_n", "C₆H₆"], "Glyukoza va fruktoza formulasi C₆H₁₂O₆ ga teng."),
        ("Oqsillarning monomerlari nima deb ataladi?", "Aminokislotalar", ["Glyukoza", "Nukleotidlar", "Yog' kislotalari"], "Oqsillar aminokislotalardan tashkil topgan biopolimerlardir.")
    ]
    for _ in range(100):
        t = random.choice(org_data)
        questions.append(make_q(3, "Organik kimyo asoslari", t[0], t[1], t[2], t[3], "orta", "10-sinf"))

    print(f"Generated {len(questions)} chemistry questions.")
    return questions

if __name__ == "__main__":
    qs = generate_chemistry_questions()
    cnt = insert_questions(qs)
    print(f"Successfully inserted {cnt} chemistry questions into database.")
