import random
from common import make_q, insert_questions

def generate_physics_questions():
    questions = []

    # 1. Kinematika (120 questions)
    for _ in range(60):
        # v = s / t
        t = random.randint(2, 10)
        v = random.choice([10, 15, 20, 25, 30, 36, 54, 72]) # km/h or m/s
        s = v * t
        if random.random() < 0.5:
            q_text = f"Jism {t} sekundda {s} metr masofani bosib o'tdi. Jismning o'rtacha tezligini toping (m/s)."
            ans = f"{v} m/s"
            wrongs = [f"{v + 5} m/s", f"{v - 5 if v > 5 else v + 10} m/s", f"{s // (t + 1)} m/s"]
            exp = f"Tezlik formulasi: v = s / t = {s} / {t} = {v} m/s."
        else:
            q_text = f"Avtomobil {v} m/s tezlik bilan tekis harakatlanib, {t} sekundda qancha masofani bosib o'tadi?"
            ans = f"{s} m"
            wrongs = [f"{s + 20} m", f"{s - 15 if s > 15 else s + 30} m", f"{v * (t - 1)} m"]
            exp = f"Masofa formulasi: s = v · t = {v} · {t} = {s} m."
        questions.append(make_q(2, "Kinematika - Tezlik va Yo'l", q_text, ans, wrongs, exp, "oson", "7-sinf"))

    for _ in range(60):
        # Tezlanish: a = (v - v0) / t, v0 = 0 -> v = a * t, s = a * t^2 / 2
        a = random.choice([2, 3, 4, 5, 6])
        t = random.choice([2, 4, 6, 8])
        v = a * t
        s = (a * (t ** 2)) // 2
        if random.random() < 0.5:
            q_text = f"Tinch holatdan {a} m/s² tezlanish bilan harakat boshlagan jismning {t} sekunddan keyingi tezligini toping."
            ans = f"{v} m/s"
            wrongs = [f"{v + a} m/s", f"{v - a if v > a else v + 4} m/s", f"{s} m/s"]
            exp = f"v = v₀ + at = 0 + {a} · {t} = {v} m/s."
        else:
            q_text = f"Boshlang'ich tezligi nolga teng bo'lgan jism {a} m/s² tezlanish bilan {t} s davomida qancha yo'l bosadi?"
            ans = f"{s} m"
            wrongs = [f"{s * 2} m", f"{v} m", f"{s + 10} m"]
            exp = f"s = at² / 2 = ({a} · {t}²) / 2 = ({a} · {t*t}) / 2 = {s} m."
        questions.append(make_q(2, "Kinematika - Tezlanish", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    # 2. Dinamika va Nyuton qonunlari (110 questions)
    for _ in range(60):
        # F = m * a
        m = random.randint(2, 25)
        a = random.choice([2, 3, 4, 5, 8, 10])
        F = m * a
        if random.random() < 0.5:
            q_text = f"Massasi {m} kg bo'lgan jismga qanday kuch ta'sir etganda u {a} m/s² tezlanish oladi?"
            ans = f"{F} N"
            wrongs = [f"{F + m} N", f"{F - a if F > a else F + 10} N", f"{m + a} N"]
            exp = f"Nyutonning 2-qonuni: F = m · a = {m} · {a} = {F} N."
        else:
            q_text = f"Massasi {m} kg bo'lgan jismga {F} N kuch ta'sir qilmoqda. Jism olgan tezlanishni toping."
            ans = f"{a} m/s²"
            wrongs = [f"{a + 2} m/s²", f"{a - 1 if a > 1 else a + 3} m/s²", f"{F // (m + 1)} m/s²"]
            exp = f"a = F / m = {F} / {m} = {a} m/s²."
        questions.append(make_q(2, "Dinamika - Nyuton qonunlari", q_text, ans, wrongs, exp, "oson", "7-sinf"))

    for _ in range(50):
        # Og'irlik kuchi F = m * g, g = 10
        m = random.choice([5, 10, 15, 20, 45, 60, 70, 80])
        F_ogirlik = m * 10
        q_text = f"Massasi {m} kg bo'lgan jismga Yer sirtida ta'sir qiluvchi og'irlik kuchini toping (g = 10 m/s²)."
        ans = f"{F_ogirlik} N"
        wrongs = [f"{m} N", f"{F_ogirlik + 50} N", f"{m * 9} N"]
        exp = f"F_og'irlik = m · g = {m} · 10 = {F_ogirlik} N."
        questions.append(make_q(2, "Dinamika - Og'irlik kuchi", q_text, ans, wrongs, exp, "oson", "7-sinf"))

    # 3. Ish, Quvvat, Energiya va Impuls (110 questions)
    for _ in range(60):
        # A = F * s, N = A / t
        F = random.choice([20, 50, 100, 200, 500])
        s = random.randint(2, 20)
        A = F * s
        t = random.choice([2, 5, 10, 20])
        N = A // t
        if random.random() < 0.5:
            q_text = f"Jismga {F} N kuch ta'sir etib, uni o'z yo'nalishida {s} m masofaga ko'chirdi. Bajarilgan ishni toping."
            ans = f"{A} J"
            wrongs = [f"{A + 100} J", f"{F + s} J", f"{A // 2} J"]
            exp = f"Bajarilgan ish: A = F · s = {F} · {s} = {A} J."
        else:
            q_text = f"{t} sekundda {A} J ish bajargan dvigatelning quvvatini toping."
            ans = f"{N} Vt"
            wrongs = [f"{N * 2} Vt", f"{N + 10} Vt", f"{A * t} Vt"]
            exp = f"Quvvat formulasi: N = A / t = {A} / {t} = {N} Vt."
        questions.append(make_q(2, "Ish va Quvvat", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    for _ in range(50):
        # Kinetik energiya: E_k = m * v^2 / 2, Impuls: p = m * v
        m = random.choice([2, 4, 6, 8, 10])
        v = random.choice([3, 4, 5, 6, 10])
        Ek = (m * (v ** 2)) // 2
        p = m * v
        if random.random() < 0.5:
            q_text = f"Massasi {m} kg, tezligi {v} m/s bo'lgan jismning kinetik energiyasini toping."
            ans = f"{Ek} J"
            wrongs = [f"{m * v} J", f"{Ek * 2} J", f"{Ek + 15} J"]
            exp = f"E_k = (m · v²) / 2 = ({m} · {v}²) / 2 = ({m} · {v*v}) / 2 = {Ek} J."
        else:
            q_text = f"Massasi {m} kg bo'lgan jism {v} m/s tezlik bilan harakatlansa, uning impulsi (harakat miqdori) qanday?"
            ans = f"{p} kg·m/s"
            wrongs = [f"{Ek} kg·m/s", f"{p + 5} kg·m/s", f"{m + v} kg·m/s"]
            exp = f"Impuls formulasi: p = m · v = {m} · {v} = {p} kg·m/s."
        questions.append(make_q(2, "Energiya va Impuls", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    # 4. Gidrostatika va Bosim (100 questions)
    for _ in range(50):
        # p = F / S
        F = random.choice([100, 200, 500, 1000, 2000])
        S = random.choice([2, 4, 5, 10]) # m^2
        p = F // S
        q_text = f"Yuzasi {S} m² bo'lgan tayanchga {F} N kuch tik ta'sir qilmoqda. Hosil bo'lgan bosimni toping."
        ans = f"{p} Pa"
        wrongs = [f"{p * 2} Pa", f"{F * S} Pa", f"{p + 50} Pa"]
        exp = f"Bosim formulasi: p = F / S = {F} / {S} = {p} Pa."
        questions.append(make_q(2, "Gidrostatika - Bosim", q_text, ans, wrongs, exp, "oson", "7-sinf"))

    for _ in range(50):
        # p = rho * g * h, rho_suv = 1000 kg/m^3, g = 10
        h = random.randint(2, 25)
        p_gidro = 1000 * 10 * h
        q_text = f"Suv tubidagi {h} m chuqurlikda gidrostatik bosim qanchaga teng? (ρ = 1000 kg/m³, g = 10 m/s²)"
        ans = f"{p_gidro} Pa"
        wrongs = [f"{p_gidro // 10} Pa", f"{p_gidro + 5000} Pa", f"{h * 1000} Pa"]
        exp = f"p = ρ · g · h = 1000 · 10 · {h} = {p_gidro} Pa (yoki {p_gidro // 1000} kPa)."
        questions.append(make_q(2, "Gidrostatik bosim", q_text, ans, wrongs, exp, "orta", "7-sinf"))

    # 5. Termodinamika va Issiqlik hodisalari (110 questions)
    for _ in range(60):
        # Q = c * m * delta_t, c_suv = 4200
        m = random.randint(1, 5)
        dt = random.choice([10, 20, 30, 40, 50])
        Q = 4200 * m * dt
        q_text = f"Massasi {m} kg bo'lgan suvni {dt} °C ga isitish uchun qancha issiqlik miqdori kerak? (c = 4200 J/(kg·°C))"
        ans = f"{Q} J"
        wrongs = [f"{Q // 2} J", f"{4200 * dt} J", f"{Q + 8400} J"]
        exp = f"Q = c · m · Δt = 4200 · {m} · {dt} = {Q} J (yoki {Q // 1000} kJ)."
        questions.append(make_q(2, "Issiqlik miqdori", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    for _ in range(50):
        # T = t + 273
        t_cels = random.choice([0, 20, 25, 27, 37, 50, 100, 127, -10, -73])
        T_kelv = t_cels + 273
        if random.random() < 0.5:
            q_text = f"{t_cels} °C harorat mutlaq harorat shkalasida (Kelvin) nechaga teng?"
            ans = f"{T_kelv} K"
            wrongs = [f"{t_cels} K", f"{T_kelv + 10} K", f"{273 - t_cels} K"]
            exp = f"T = t + 273 = {t_cels} + 273 = {T_kelv} K."
        else:
            q_text = f"{T_kelv} K harorat Selsiy (°C) shkalasida nechaga teng?"
            ans = f"{t_cels} °C"
            wrongs = [f"{t_cels + 20} °C", f"{-t_cels} °C", f"{T_kelv} °C"]
            exp = f"t = T - 273 = {T_kelv} - 273 = {t_cels} °C."
        questions.append(make_q(2, "Termodinamika - Harorat", q_text, ans, wrongs, exp, "oson", "8-sinf"))

    # 6. Elektr toki va Om qonuni (120 questions)
    for _ in range(60):
        # I = U / R
        R = random.choice([2, 4, 5, 10, 20, 25, 50])
        I = random.choice([1, 2, 3, 4, 5, 6])
        U = I * R
        if random.random() < 0.5:
            q_text = f"Qarshiligi {R} Om bo'lgan o'tkazgich uchlaridagi kuchlanish {U} V bo'lsa, undan o'tayotgan tok kuchi qancha?"
            ans = f"{I} A"
            wrongs = [f"{I + 2} A", f"{U} A", f"{I * 2} A"]
            exp = f"Zanjir qismi uchun Om qonuni: I = U / R = {U} / {R} = {I} A."
        else:
            q_text = f"Zanjirdagi tok kuchi {I} A, o'tkazgich qarshiligi {R} Om bo'lsa, undagi kuchlanishni toping."
            ans = f"{U} V"
            wrongs = [f"{R} V", f"{U + 10} V", f"{U // 2} V"]
            exp = f"Kuchlanish formulasi: U = I · R = {I} · {R} = {U} V."
        questions.append(make_q(2, "Elektr toki - Om qonuni", q_text, ans, wrongs, exp, "oson", "8-sinf"))

    for _ in range(60):
        # Ketma-ket va parallel ulash, Elektr quvvati P = U * I
        R1 = random.choice([2, 4, 6, 10])
        R2 = random.choice([3, 5, 8, 12])
        R_ket = R1 + R2
        U = random.choice([12, 24, 110, 220])
        I = random.choice([1, 2, 3, 5])
        P = U * I
        if random.random() < 0.5:
            q_text = f"Qarshiliklari {R1} Om va {R2} Om bo'lgan ikkita rezistor ketma-ket ulanganda umumiy qarshilik qancha bo'ladi?"
            ans = f"{R_ket} Om"
            wrongs = [f"{R1 * R2} Om", f"{abs(R1 - R2)} Om", f"{R_ket + 4} Om"]
            exp = f"Ketma-ket ulashda: R_um = R₁ + R₂ = {R1} + {R2} = {R_ket} Om."
        else:
            q_text = f"Kuchlanishi {U} V va tok kuchi {I} A bo'lgan elektr asbobining quvvatini toping."
            ans = f"{P} Vt"
            wrongs = [f"{P * 2} Vt", f"{U + I} Vt", f"{P // 2} Vt"]
            exp = f"Elektr quvvati: P = U · I = {U} · {I} = {P} Vt."
        questions.append(make_q(2, "Elektr zanjirlari va Quvvat", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    # 7. Elektromagnetizm va Induksiya (100 questions)
    em_qs = [
        ("Magnit maydon kuch chiziqlari qayerdan chiqib qayerga kiradi?", "Shimoliy qutbdan (N) chiqib, Janubiy qutbga (S) kiradi", ["Janubiy qutbdan chiqib Shimoliyga kiradi", "Markazdan tashqariga tarqaladi", "Faqat bir qutbda yopiq aylanadi"], "Magnit maydon kuch chiziqlari N qutbdan chiqib S qutbga kiruvchi berk chiziqlardir."),
        ("O'tkazgichdagi tokning magnit maydon yo'nalishi qaysi qoida bilan aniqlanadi?", "Burg'i (o'ng qo'l) qoidasi", ["Chap qo'l qoidasi", "Lens qoidasi", "Joul qoidasi"], "Tokli to'g'ri o'tkazgich magnit maydoni burg'i qoidasi yordamida aniqlanadi."),
        ("Magnit maydonda harakatlanayotgan zaryadli zarrachaga ta'sir qiluvchi kuch nima deb ataladi?", "Lorens kuchi", ["Amper kuchi", "Arximed kuchi", "Kulon kuchi"], "Magnit maydonda zaryadga ta'sir qiluvchi kuch - Lorens kuchi (F = qvBsinα)."),
        ("Magnit maydondagi tokli o'tkazgichga ta'sir qiluvchi kuch nima deb ataladi?", "Amper kuchi", ["Lorens kuchi", "Og'irlik kuchi", "Kulon kuchi"], "Tokli o'tkazgichga ta'sir etuvchi kuch - Amper kuchi (F = IBlsinα)."),
        ("Amper kuchi yo'nalishi qaysi qoida yordamida aniqlanadi?", "Chap qo'l qoidasi", ["O'ng qo'l qoidasi", "Burg'i qoidasi", "Inersiya qoidasi"], "Amper va Lorens kuchlarining yo'nalishi chap qo'l qoidasi bilan aniqlanadi."),
        ("Elektromagnit induksiya hodisasini kim kashf qilgan?", "Maykl Faradey (1831-yil)", ["Jeyms Maksvell", "Isaak Nyuton", "Nikola Tesla"], "1831-yilda Maykl Faradey elektromagnit induksiya qonunini kashf etgan."),
        ("Magnit oqimining Xalqaro birliklar sistemasidagi (SI) birligi nima?", "Veber (Vb)", ["Tesla (Tl)", "Genri (Gn)", "Farad (F)"], "Magnit oqimi Φ = BS bo'lib, uning birligi Veber (Vb)."),
        ("Magnit induksiyasi vektorining (B) SI dagi birligi nima?", "Tesla (Tl)", ["Veber (Vb)", "Volt (V)", "Om (Om)"], "Magnit maydon kuch xarakteristikasi bo'lgan induksiya birligi Tesla (Tl)."),
        ("G'altakning induktivlik birligi nima?", "Genri (Gn)", ["Farad (F)", "Veber (Vb)", "Kulon (Kl)"], "Induktivlik L ning o'lchov birligi Genri (Gn).")
    ]
    for _ in range(100):
        t = random.choice(em_qs)
        questions.append(make_q(2, "Elektromagnetizm", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 8. Tebranishlar, To'lqinlar va Tovush (90 questions)
    wave_qs = [
        ("Vaqt birligi (1 sekund) ichidagi to'liq tebranishlar soni nima deb ataladi?", "Tebranish chastotasi", ["Tebranish davri", "Amplituda", "To'lqin uzunligi"], "1 sekunddagi tebranishlar soni chastota (ν = 1/T) deb ataladi va Gerts (Gs) da o'lchanadi."),
        ("Bitta to'liq tebranish uchun ketgan vaqt nima deb ataladi?", "Tebranish davri", ["Chastota", "Faza", "Tezlanish"], "Bir to'liq tebranish vaqti - tebranish davri T (sekundda o'lchanadi)."),
        ("Muvozanat vaziyatidan eng katta siljish nima deb ataladi?", "Tebranish amplitudasi", ["Davr", "Chastota", "To'lqin fronti"], "Maksimal og'ish yoki siljish - amplituda (A)."),
        ("Chastotaning SI tizimidagi birligi nima?", "Gerts (Gs)", ["Sekund (s)", "Metr (m)", "Radian (rad)"], "Chastota birligi 1/s = Gerts (Gs)."),
        ("To'lqin uzunligi (λ), to'lqin tezligi (v) va davr (T) o'rtasidagi bog'lanish formulasini ko'rsating.", "λ = v · T", ["λ = v / T", "λ = v · T²", "λ = T / v"], "To'lqin bir davr ichida bosib o'tgan masofa to'lqin uzunligidir: λ = vT = v/ν."),
        ("Tovush to'lqinlari qanday to'lqin turiga kiradi?", "Bo'ylama mexanik to'lqin", ["Ko'ndalang elektromagnit to'lqin", "Faqat sirt to'lqini", "Yorug'lik to'lqini"], "Havoda tovush to'lqinlari havoning siqilishi va siyraklashishi hisobiga bo'ylama to'lqin shaklida tarqaladi."),
        ("Odam qulog'i eshita oladigan tovush chastotasi diapazoni qanday?", "16 Gs dan 20 000 Gs gacha", ["1 Gs dan 100 Gs gacha", "20 000 Gs dan yuqori", "100 Gs dan 500 Gs gacha"], "Inson qulog'i 16–20 000 Gerts oralig'idagi akustik tovushlarni eshitadi."),
        ("Chastotasi 20 000 Gerts dan yuqori bo'lgan tovush to'lqinlari nima deb ataladi?", "Ultratovush", ["Infratovush", "Gipotovush", "Rezonans"], "20 kHz dan yuqori tovushlar ultratovush, 16 Gs dan pasti esa infratovush deyiladi."),
        ("Vakuumda (havosiz fazoda) tovush tarqala oladimi?", "Yo'q, chunki tovush moddiy muhit talab qiladi", ["Ha, yorug'lik tezligida tarqaladi", "Faqat past chastotalarda tarqaladi", "Ha, 340 m/s tezlikda"], "Tovush mexanik to'lqin bo'lib, uning tarqalishi uchun moddiy zarrachalar (muhit) zarur.")
    ]
    for _ in range(90):
        t = random.choice(wave_qs)
        questions.append(make_q(2, "Tebranishlar va Tovush", t[0], t[1], t[2], t[3], "orta", "9-sinf"))

    # 9. Optika (90 questions)
    optics_qs = [
        ("Vakuumda yorug'likning tarqalish tezligi qanchaga teng?", "300 000 km/s (3 · 10⁸ m/s)", ["150 000 km/s", "340 m/s", "1 000 000 km/s"], "Yorug'likning vakuumdagi tezligi c ≈ 3 · 10⁸ m/s ga teng."),
        ("Yorug'likning qaytish qonuniga ko'ra tushish burchagi (α) va qaytish burchagi (β) qanday munosabatda bo'ladi?", "Tushish burchagi qaytish burchagiga teng (α = β)", ["α > β", "α + β = 90°", "α < β"], "Yorug'likning qaytish qonuni: tushish burchagi har doim qaytish burchagiga teng."),
        ("Linzaning optik kuchi qaysi birlikda o'lchanadi?", "Dioptriya (dptr)", ["Metr (m)", "Radian (rad)", "Lyuks (lx)"], "Optik kuch D = 1 / F bo'lib, dioptriyalarda o'lchanadi."),
        ("Fokus masofasi 0.5 m bo'lgan yig'uvchi linzaning optik kuchini toping.", "2 dptr", ["0.5 dptr", "5 dptr", "1 dptr"], "D = 1 / F = 1 / 0.5 = 2 dptr."),
        ("Fokus masofasi 0.2 m bo'lgan yupqa linzaning optik kuchini toping.", "5 dptr", ["2 dptr", "0.2 dptr", "10 dptr"], "D = 1 / F = 1 / 0.2 = 5 dptr."),
        ("Yorug'lik nurining bir muhitdan ikkinchi muhitga o'tganda yo'nalishini o'zgartirishi nima deb ataladi?", "Yorug'likning sinishi", ["Yorug'lik dispersiyasi", "Yorug'lik difraksiyasi", "Yorug'lik qutblanishi"], "Ikki shaffof muhit chegarasidan o'tishda nurning sinishi sodir bo'ladi."),
        ("Oq yorug'likning prizmadan o'tganda rang-barang spektrga ajralishi qanday hodisa?", "Yorug'lik dispersiyasi", ["Yorug'lik interferensiyasi", "To'la ichki qaytish", "Fotoeffekt"], "Yorug'lik tezligining uning to'lqin uzunligiga bog'liqligi dispersiya deyiladi (Nyuton tajribasi).")
    ]
    for _ in range(90):
        t = random.choice(optics_qs)
        questions.append(make_q(2, "Optika", t[0], t[1], t[2], t[3], "orta", "8-sinf"))

    # 10. Fizika Olimlari va SI Birliklari (100 questions)
    si_qs = [
        ("Xalqaro birliklar sistemasida (SI) kuch birligi nima?", "Nyuton (N)", ["Joul (J)", "Paskal (Pa)", "Vatt (Vt)"], "Kuch birligi ser Isaak Nyuton sharafiga Nyuton (N) deb ataladi."),
        ("SI tizimida energiya va ish birligi nima?", "Joul (J)", ["Vatt (Vt)", "Nyuton (N)", "Kaloriya (cal)"], "Ish va energiya Joul (J) da o'lchanadi."),
        ("SI tizimida bosim birligi nima?", "Paskal (Pa)", ["Bar", "Atmosfera (atm)", "Torr"], "Bosim birligi Blez Paskal sharafiga Paskal (Pa = N/m²) deb ataladi."),
        ("SI tizimida quvvat birligi nima?", "Vatt (Vt)", ["Joul (J)", "Ot kuchi", "Amper (A)"], "Quvvat Jeyms Vatt sharafiga Vatt (Vt = J/s) da o'lchanadi."),
        ("Elektr zaryadining SI dagi birligi nima?", "Kulon (Kl)", ["Amper (A)", "Volt (V)", "Farad (F)"], "Zaryad birligi Sharl Kulon sharafiga Kulon (Kl = A·s) deb nomlangan."),
        ("Elektr sig'imining birligi nima?", "Farad (F)", ["Genri (Gn)", "Om (Om)", "Volt (V)"], "Kondensator sig'imi Farad (F) da o'lchanadi."),
        ("Barcha jismlar orasidagi Butun olam tortishish qonunini kim kashf etgan?", "Isaak Nyuton", ["Galileo Galiley", "Albert Eynshteyn", "Iogann Kepler"], "1687-yilda Nyuton butun olam tortishish qonunini (F = G·m₁m₂/R²) bayon etgan."),
        ("Inersiya qonunini birinchi bo'lib eksperimental tajribalar bilan asoslagan olim kim?", "Galileo Galiley", ["Arximed", "Rene Dekart", "Nikolay Kopernik"], "Galiley nishab tekislikdagi sharchalar harakatini o'rganib inersiya tushunchasini fanga kiritgan."),
        ("Fotoeffekt qonuniyatlarini tushuntirib bergani uchun Nobel mukofotiga sazovor bo'lgan olim kim?", "Albert Eynshteyn (1921-yil)", ["Nils Bor", "Maks Plank", "Ernest Rezerford"], "Eynshteyn 1905-yilda yorug'lik kvantlari (fotonlar) orqali fotoeffekt tenglamasini yaratgan.")
    ]
    for _ in range(100):
        t = random.choice(si_qs)
        questions.append(make_q(2, "SI Birliklari va Olimlar", t[0], t[1], t[2], t[3], "oson", "Umumiy"))

    print(f"Generated {len(questions)} physics questions.")
    return questions

if __name__ == "__main__":
    qs = generate_physics_questions()
    cnt = insert_questions(qs)
    print(f"Successfully inserted {cnt} physics questions into database.")
