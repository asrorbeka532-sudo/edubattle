import random
import math
from common import make_q, insert_questions

def generate_math_questions():
    questions = []

    # 1. Linear Equations (100 questions)
    for _ in range(100):
        x = random.randint(-15, 25)
        if x == 0: x = 2
        a = random.choice([2, 3, 4, 5, 6, 7, 8, 9, -2, -3, -4])
        b = random.randint(-30, 40)
        c = a * x + b
        sign_str = f"+ {b}" if b >= 0 else f"- {abs(b)}"
        q_text = f"Tenglamani yeching: {a}x {sign_str} = {c}"
        ans = f"x = {x}"
        wrongs = [f"x = {x + 1}", f"x = {x - 1}", f"x = {x + 2}"]
        exp = f"{a}x = {c} - ({b}) => {a}x = {c - b} => x = {x}"
        grade = random.choice(["6-sinf", "7-sinf"])
        questions.append(make_q(1, "Chiziqli tenglamalar", q_text, ans, wrongs, exp, "oson", grade))

    # 2. Quadratic Equations (100 questions)
    for _ in range(100):
        x1 = random.randint(-9, 9)
        x2 = random.randint(-9, 9)
        if x1 == x2: x2 += 1
        # (x - x1)(x - x2) = x^2 - (x1+x2)x + x1*x2 = 0
        b = -(x1 + x2)
        c = x1 * x2
        b_str = f"+ {b}x" if b > 0 else (f"- {abs(b)}x" if b < 0 else "")
        c_str = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
        eq_str = f"x² {b_str} {c_str} = 0".replace("  ", " ").strip()
        q_text = f"Kvadrat tenglamaning ildizlarini toping: {eq_str}"
        ans = f"x₁ = {min(x1, x2)}, x₂ = {max(x1, x2)}"
        wrongs = [
            f"x₁ = {min(-x1, -x2)}, x₂ = {max(-x1, -x2)}",
            f"x₁ = {min(x1+1, x2-1)}, x₂ = {max(x1+1, x2-1)}",
            f"x₁ = {min(x1-2, x2+2)}, x₂ = {max(x1-2, x2+2)}"
        ]
        exp = f"Viyet teoremasiga ko'ra: x₁ + x₂ = {-b}, x₁ · x₂ = {c}. Ildizlar: {x1} va {x2}."
        questions.append(make_q(1, "Kvadrat tenglamalar", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    # 3. Viyet Teoremasi & Diskriminant (80 questions)
    for _ in range(80):
        x1 = random.randint(-8, 8)
        x2 = random.randint(-8, 8)
        b = -(x1 + x2)
        c = x1 * x2
        b_str = f"+ {b}x" if b > 0 else (f"- {abs(b)}x" if b < 0 else "")
        c_str = f"+ {c}" if c > 0 else (f"- {abs(c)}" if c < 0 else "")
        eq_str = f"x² {b_str} {c_str} = 0".replace("  ", " ")
        
        mode = random.choice(["sum", "prod", "disc"])
        if mode == "sum":
            q_text = f"{eq_str} tenglamaning ildizlari yig'indisini toping."
            ans = str(x1 + x2)
            wrongs = [str(-(x1 + x2)), str(x1 * x2), str(x1 + x2 + 1)]
            exp = f"Viyet teoremasiga ko'ra x₁ + x₂ = -p = {-b} = {x1 + x2}."
        elif mode == "prod":
            q_text = f"{eq_str} tenglamaning ildizlari ko'paytmasini toping."
            ans = str(x1 * x2)
            wrongs = [str(-(x1 * x2)), str(x1 + x2), str(x1 * x2 + 2)]
            exp = f"Viyet teoremasiga ko'ra x₁ · x₂ = q = {c}."
        else:
            D = b*b - 4*c
            q_text = f"{eq_str} tenglamaning diskriminantini (D) hisoblang."
            ans = str(D)
            wrongs = [str(D + 4), str(abs(D - 8)), str(b*b + 4*c)]
            exp = f"D = b² - 4ac = ({b})² - 4·1·({c}) = {b*b} - ({4*c}) = {D}."
        questions.append(make_q(1, "Kvadrat tenglamalar va Viyet", q_text, ans, wrongs, exp, "orta", "8-sinf"))

    # 4. Arifmetik Progressiya (80 questions)
    for _ in range(80):
        a1 = random.randint(-10, 20)
        d = random.choice([2, 3, 4, 5, 6, -2, -3, -4])
        n = random.randint(5, 15)
        an = a1 + (n - 1) * d
        Sn = (2 * a1 + (n - 1) * d) * n // 2
        
        if random.random() < 0.5:
            q_text = f"Arifmetik progressiyada a₁ = {a1}, d = {d} bo'lsa, {n}-hadi (a_{n}) ni toping."
            ans = str(an)
            wrongs = [str(an + d), str(an - d), str(an + 2)]
            exp = f"a_n = a₁ + (n - 1)d = {a1} + ({n}-1)·({d}) = {a1} + { (n-1)*d } = {an}."
        else:
            q_text = f"Arifmetik progressiyada a₁ = {a1}, d = {d} bo'lsa, dastlabki {n} ta hadi yig'indisi (S_{n}) ni toping."
            ans = str(Sn)
            wrongs = [str(Sn + n), str(Sn - n * 2), str(Sn + 10)]
            exp = f"S_n = (2a₁ + (n-1)d)·n / 2 = (2·{a1} + {n-1}·{d})·{n} / 2 = {Sn}."
        questions.append(make_q(1, "Arifmetik progressiya", q_text, ans, wrongs, exp, "orta", "9-sinf"))

    # 5. Geometrik Progressiya (70 questions)
    for _ in range(70):
        b1 = random.choice([1, 2, 3, 4, 5])
        q = random.choice([2, 3])
        n = random.randint(3, 6)
        bn = b1 * (q ** (n - 1))
        Sn = b1 * (q**n - 1) // (q - 1)
        
        if random.random() < 0.6:
            q_text = f"Geometrik progressiyada b₁ = {b1}, q = {q} bo'lsa, {n}-hadi (b_{n}) ni toping."
            ans = str(bn)
            wrongs = [str(bn * q), str(bn // q if bn // q > 0 else bn + 4), str(bn + 6)]
            exp = f"b_n = b₁ · q^(n-1) = {b1} · {q}^{n-1} = {b1} · {q**(n-1)} = {bn}."
        else:
            q_text = f"Geometrik progressiyada b₁ = {b1}, q = {q} bo'lsa, dastlabki {n} ta hadi yig'indisini toping."
            ans = str(Sn)
            wrongs = [str(Sn + b1), str(Sn * 2), str(Sn - q)]
            exp = f"S_n = b₁(q^n - 1) / (q - 1) = {b1}({q}^{n} - 1) / ({q}-1) = {Sn}."
        questions.append(make_q(1, "Geometrik progressiya", q_text, ans, wrongs, exp, "qiyin", "9-sinf"))

    # 6. Darajalar va Ildizlar (80 questions)
    for _ in range(80):
        base = random.choice([2, 3, 4, 5])
        p1 = random.randint(2, 5)
        p2 = random.randint(2, 4)
        mode = random.choice(["mult", "div", "pow"])
        if mode == "mult":
            q_text = f"Ifodani soddalashtiring: {base}^{p1} · {base}^{p2}"
            ans = f"{base}^{p1 + p2}"
            wrongs = [f"{base}^{p1 * p2}", f"{base * 2}^{p1 + p2}", f"{base}^{abs(p1 - p2)}"]
            exp = f"Asoslari bir xil darajalar ko'paytirilganda daraja ko'rsatkichlari qo'shiladi: {p1} + {p2} = {p1+p2}."
        elif mode == "div":
            p1_big = p1 + p2
            q_text = f"Ifodani soddalashtiring: {base}^{p1_big} : {base}^{p2}"
            ans = f"{base}^{p1}"
            wrongs = [f"{base}^{p1_big * p2}", f"{base}^{p1_big + p2}", f"1^{p1}"]
            exp = f"Asoslari bir xil darajalar bo'linganda daraja ko'rsatkichlari ayiriladi: {p1_big} - {p2} = {p1}."
        else:
            q_text = f"Ifodani soddalashtiring: ({base}^{p1})^{p2}"
            ans = f"{base}^{p1 * p2}"
            wrongs = [f"{base}^{p1 + p2}", f"{base * p2}^{p1}", f"{base}^{p1 ** p2}"]
            exp = f"Daraja darajaga ko'tarilganda ko'rsatkichlar ko'paytiriladi: {p1} · {p2} = {p1*p2}."
        questions.append(make_q(1, "Darajalar va ildizlar", q_text, ans, wrongs, exp, "oson", "7-sinf"))

    # 7. Logarifmlar (70 questions)
    for _ in range(70):
        base = random.choice([2, 3, 4, 5])
        p = random.randint(1, 4)
        val = base ** p
        if random.random() < 0.6:
            q_text = f"Hisoblang: log_{base}({val})"
            ans = str(p)
            wrongs = [str(p + 1), str(p - 1 if p > 1 else p + 2), str(val // base)]
            exp = f"{base}^{p} = {val} bo'lganligi sababli, log_{base}({val}) = {p}."
        else:
            p2 = random.randint(1, 3)
            val2 = base ** p2
            q_text = f"Hisoblang: log_{base}({val}) + log_{base}({val2})"
            ans = str(p + p2)
            wrongs = [str(p * p2), str(abs(p - p2)), str(p + p2 + 2)]
            exp = f"log_a(x) + log_a(y) = log_a(x·y) = {p} + {p2} = {p+p2}."
        questions.append(make_q(1, "Logarifmlar", q_text, ans, wrongs, exp, "qiyin", "10-sinf"))

    # 8. Trigonometriya (80 questions)
    trig_vals = [
        ("sin(30°)", "1/2", ["√3/2", "√2/2", "1"]),
        ("cos(60°)", "1/2", ["√3/2", "√2/2", "0"]),
        ("sin(45°)", "√2/2", ["1/2", "√3/2", "1"]),
        ("cos(45°)", "√2/2", ["1/2", "√3/2", "0"]),
        ("sin(60°)", "√3/2", ["1/2", "√2/2", "√3"]),
        ("cos(30°)", "√3/2", ["1/2", "√2/2", "1"]),
        ("tg(45°)", "1", ["0", "√3", "√3/3"]),
        ("ctg(45°)", "1", ["0", "√3", "√3/3"]),
        ("sin(90°)", "1", ["0", "-1", "1/2"]),
        ("cos(90°)", "0", ["1", "-1", "1/2"]),
        ("sin(0°)", "0", ["1", "-1", "1/2"]),
        ("cos(0°)", "1", ["0", "-1", "1/2"]),
        ("tg(30°)", "√3/3", ["√3", "1", "1/2"]),
        ("tg(60°)", "√3", ["√3/3", "1", "1/2"]),
        ("sin²(x) + cos²(x)", "1", ["0", "2", "tg(x)"]),
        ("sin(180°)", "0", ["1", "-1", "1/2"]),
        ("cos(180°)", "-1", ["0", "1", "1/2"])
    ]
    for _ in range(80):
        t = random.choice(trig_vals)
        q_text = f"Trigonometrik ifodaning qiymatini toping: {t[0]}"
        ans = t[1]
        wrongs = t[2]
        exp = f"{t[0]} ning standart trigonometrik jadval bo'yicha qiymati {t[1]} ga teng."
        questions.append(make_q(1, "Trigonometriya", q_text, ans, wrongs, exp, "orta", "9-sinf"))

    # 9. Planimetriya (Uchburchak, To'rtburchak, Doira) (120 questions)
    pyth_triples = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (7, 24, 25)]
    for _ in range(50):
        a, b, c = random.choice(pyth_triples)
        k = random.choice([1, 2, 3])
        a, b, c = a*k, b*k, c*k
        if random.random() < 0.5:
            q_text = f"To'g'ri burchakli uchburchakning katetlari {a} sm va {b} sm. Uning gipotenuzasini toping."
            ans = f"{c} sm"
            wrongs = [f"{c + 2} sm", f"{c - 1} sm", f"{a + b} sm"]
            exp = f"Pifagor teoremasi: c² = a² + b² = {a}² + {b}² = {a*a + b*b} => c = {c} sm."
        else:
            q_text = f"To'g'ri burchakli uchburchakning katetlari {a} sm va {b} sm. Uning yuzini toping."
            S = (a * b) // 2
            ans = f"{S} sm²"
            wrongs = [f"{S * 2} sm²", f"{S + a} sm²", f"{S - 4} sm²"]
            exp = f"To'g'ri burchakli uchburchak yuzi: S = (a · b) / 2 = ({a} · {b}) / 2 = {S} sm²."
        questions.append(make_q(1, "Planimetriya - Uchburchaklar", q_text, ans, wrongs, exp, "oson", "8-sinf"))

    for _ in range(70):
        shape = random.choice(["kvadrat", "tortburchak", "doira", "romb"])
        if shape == "kvadrat":
            a = random.randint(4, 25)
            S = a * a
            P = 4 * a
            if random.random() < 0.5:
                q_text = f"Tomoni {a} sm bo'lgan kvadratning yuzini toping."
                ans = f"{S} sm²"
                wrongs = [f"{P} sm²", f"{S + a} sm²", f"{S - 5} sm²"]
                exp = f"Kvadrat yuzi: S = a² = {a}² = {S} sm²."
            else:
                q_text = f"Tomoni {a} sm bo'lgan kvadratning perimetrini toping."
                ans = f"{P} sm"
                wrongs = [f"{S} sm", f"{P + 4} sm", f"{P - 4} sm"]
                exp = f"Kvadrat perimetri: P = 4a = 4 · {a} = {P} sm."
        elif shape == "tortburchak":
            a = random.randint(3, 15)
            b = random.randint(a + 1, a + 10)
            S = a * b
            P = 2 * (a + b)
            q_text = f"To'g'ri to'rtburchakning bo'yi {b} sm, eni {a} sm. Uning yuzini toping."
            ans = f"{S} sm²"
            wrongs = [f"{P} sm²", f"{S + 10} sm²", f"{S - 8} sm²"]
            exp = f"To'rtburchak yuzi: S = a · b = {a} · {b} = {S} sm²."
        elif shape == "doira":
            r = random.randint(2, 12)
            S_coeff = r * r
            C_coeff = 2 * r
            if random.random() < 0.5:
                q_text = f"Radiusi {r} sm bo'lgan doiraning yuzini toping."
                ans = f"{S_coeff}π sm²"
                wrongs = [f"{C_coeff}π sm²", f"{S_coeff * 2}π sm²", f"{r}π sm²"]
                exp = f"Doira yuzi: S = πR² = π · {r}² = {S_coeff}π sm²."
            else:
                q_text = f"Radiusi {r} sm bo'lgan aylananing uzunligini toping."
                ans = f"{C_coeff}π sm"
                wrongs = [f"{S_coeff}π sm", f"{r}π sm", f"{C_coeff * 2}π sm"]
                exp = f"Aylana uzunligi: C = 2πR = 2 · π · {r} = {C_coeff}π sm."
        else: # romb
            d1 = random.choice([6, 8, 10, 12])
            d2 = random.choice([4, 6, 8, 14])
            S = (d1 * d2) // 2
            q_text = f"Rombning diagonallari {d1} sm va {d2} sm. Uning yuzini toping."
            ans = f"{S} sm²"
            wrongs = [f"{d1 * d2} sm²", f"{S + 6} sm²", f"{S - 4} sm²"]
            exp = f"Romb yuzi: S = (d₁ · d₂) / 2 = ({d1} · {d2}) / 2 = {S} sm²."
        questions.append(make_q(1, "Planimetriya - Shakllar", q_text, ans, wrongs, exp, "orta", "7-sinf"))

    # 10. Stereometriya (Fazoviy shakllar) (70 questions)
    for _ in range(70):
        s_type = random.choice(["kub", "parallelepiped", "silindr", "shar"])
        if s_type == "kub":
            a = random.randint(2, 8)
            V = a ** 3
            S = 6 * (a ** 2)
            q_text = f"Qirrasi {a} sm bo'lgan kubning hajmini toping."
            ans = f"{V} sm³"
            wrongs = [f"{S} sm³", f"{a * 4} sm³", f"{V + 12} sm³"]
            exp = f"Kub hajmi: V = a³ = {a}³ = {V} sm³."
        elif s_type == "parallelepiped":
            a, b, c = random.randint(2, 6), random.randint(3, 7), random.randint(2, 5)
            V = a * b * c
            q_text = f"To'g'ri burchakli parallelepipedning o'lchamlari {a} sm, {b} sm va {c} sm. Hajmini toping."
            ans = f"{V} sm³"
            wrongs = [f"{V + 10} sm³", f"{a + b + c} sm³", f"{V - 8} sm³"]
            exp = f"Parallelepiped hajmi: V = a · b · c = {a} · {b} · {c} = {V} sm³."
        elif s_type == "silindr":
            r = random.randint(2, 6)
            h = random.randint(3, 8)
            V_coeff = (r ** 2) * h
            q_text = f"Asosining radiusi {r} sm, balandligi {h} sm bo'lgan silindrning hajmini toping."
            ans = f"{V_coeff}π sm³"
            wrongs = [f"{2 * r * h}π sm³", f"{V_coeff * 2}π sm³", f"{(r*h)}π sm³"]
            exp = f"Silindr hajmi: V = πR²H = π · {r}² · {h} = {V_coeff}π sm³."
        else: # shar
            r = random.choice([3, 6, 9])
            # V = 4/3 * pi * r^3
            V_coeff = (4 * (r ** 3)) // 3
            q_text = f"Radiusi {r} sm bo'lgan sharning hajmini toping."
            ans = f"{V_coeff}π sm³"
            wrongs = [f"{4 * r * r}π sm³", f"{V_coeff + 12}π sm³", f"{r**3}π sm³"]
            exp = f"Shar hajmi: V = 4/3 πR³ = 4/3 · π · {r}³ = {V_coeff}π sm³."
        questions.append(make_q(1, "Stereometriya", q_text, ans, wrongs, exp, "orta", "10-sinf"))

    # 11. Foizlar va Proporsiya (70 questions)
    for _ in range(70):
        total = random.choice([50, 100, 150, 200, 250, 300, 400, 500, 600, 800, 1000])
        p = random.choice([5, 10, 15, 20, 25, 30, 40, 50, 75])
        part = (total * p) // 100
        if random.random() < 0.5:
            q_text = f"{total} sonining {p}% ini toping."
            ans = str(part)
            wrongs = [str(part + 5), str(part - 5 if part > 5 else part + 10), str((total * (p + 10)) // 100)]
            exp = f"{total} · {p} / 100 = {part}."
        else:
            q_text = f"{part} soni {total} sonining necha foizini tashkil qiladi?"
            ans = f"{p}%"
            wrongs = [f"{p + 5}%", f"{p - 5 if p > 5 else p + 10}%", f"{p * 2}%"]
            exp = f"({part} / {total}) · 100% = {p}%."
        questions.append(make_q(1, "Foizlar va proporsiya", q_text, ans, wrongs, exp, "oson", "6-sinf"))

    # 12. EKUB va EKUK, Oddiy va o'nli kasrlar (70 questions)
    for _ in range(70):
        g = random.choice([2, 3, 4, 5, 6, 7])
        m1 = random.choice([2, 3, 5])
        m2 = random.choice([4, 7, 9])
        a = g * m1
        b = g * m2
        ekub = math.gcd(a, b)
        ekuk = (a * b) // ekub
        if random.random() < 0.5:
            q_text = f"{a} va {b} sonlarining EKUB (eng katta umumiy bo'luvchi)ini toping."
            ans = str(ekub)
            wrongs = [str(ekub * 2), str(ekub + 1), str(a)]
            exp = f"{a} = {ekub}·{a//ekub}, {b} = {ekub}·{b//ekub}. Umumiy eng katta bo'luvchi = {ekub}."
        else:
            q_text = f"{a} va {b} sonlarining EKUK (eng kichik umumiy karrali)ini toping."
            ans = str(ekuk)
            wrongs = [str(ekuk * 2), str(ekuk // 2 if ekuk // 2 > 0 else ekuk + 10), str(a * b)]
            exp = f"EKUK({a}, {b}) = ({a} · {b}) / EKUB({a}, {b}) = {a * b} / {ekub} = {ekuk}."
        questions.append(make_q(1, "Sonlar nazariyasi va kasrlar", q_text, ans, wrongs, exp, "oson", "5-sinf"))

    # 13. Kombinatorika va Ehtimollik (70 questions)
    for _ in range(70):
        mode = random.choice(["fact", "perm", "comb", "dice"])
        if mode == "fact":
            n = random.randint(3, 6)
            ans_val = math.factorial(n)
            q_text = f"{n}! (faktorial) ning qiymatini toping."
            ans = str(ans_val)
            wrongs = [str(ans_val + n), str(ans_val - 2), str(ans_val * 2)]
            exp = f"{n}! = " + " · ".join(str(i) for i in range(1, n + 1)) + f" = {ans_val}."
        elif mode == "perm":
            n = random.choice([4, 5])
            ans_val = math.factorial(n)
            q_text = f"{n} nafar o'quvchini qatorda necha xil usulda saflab qo'yish mumkin?"
            ans = str(ans_val)
            wrongs = [str(n * 2), str(ans_val + 6), str(n ** 2)]
            exp = f"P_{n} = {n}! = {ans_val} xil usulda."
        elif mode == "comb":
            n = random.choice([4, 5, 6])
            k = 2
            ans_val = math.comb(n, k)
            q_text = f"{n} kishidan 2 kishilik guruhni necha xil usulda tanlab olish mumkin? (C_{n}²)"
            ans = str(ans_val)
            wrongs = [str(n * k), str(ans_val + 4), str(ans_val - 2)]
            exp = f"C_{n}² = {n}! / (2! · ({n}-2)!) = ({n} · {n-1}) / 2 = {ans_val}."
        else: # dice
            q_text = "Bitta o'yin suyagi (kubik) tashlanganda toq son tushish ehtimolligini toping."
            ans = "1/2"
            wrongs = ["1/3", "1/6", "2/3"]
            exp = "Toq sonlar: 1, 3, 5 (3 ta). Jami hollar: 6 ta. P = 3/6 = 1/2."
        questions.append(make_q(1, "Kombinatorika va ehtimollik", q_text, ans, wrongs, exp, "orta", "9-sinf"))

    # 14. Hosila va Boshlang'ich funksiya (70 questions)
    for _ in range(70):
        c = random.randint(2, 6)
        p = random.randint(2, 5)
        # f(x) = c * x^p -> f'(x) = c*p * x^(p-1)
        der_c = c * p
        der_p = p - 1
        p_str = f"x^{p}" if p > 1 else "x"
        der_p_str = f"x^{der_p}" if der_p > 1 else ("x" if der_p == 1 else "")
        q_text = f"f(x) = {c}{p_str} funksiyaning hosilasini toping: f'(x)"
        ans = f"{der_c}{der_p_str}" if der_p_str else str(der_c)
        wrongs = [
            f"{c}{der_p_str}" if der_p_str else str(c),
            f"{der_c}x^{p}",
            f"{c * (p+1)}x^{p+1}"
        ]
        exp = f"(c · x^n)' = c · n · x^(n-1) = {c} · {p} · x^{p-1} = {ans}."
        questions.append(make_q(1, "Hosilalar", q_text, ans, wrongs, exp, "qiyin", "11-sinf"))

    print(f"Generated {len(questions)} math questions.")
    return questions

if __name__ == "__main__":
    qs = generate_math_questions()
    cnt = insert_questions(qs)
    print(f"Successfully inserted {cnt} math questions into database.")
