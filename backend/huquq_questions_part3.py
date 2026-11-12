# -*- coding: utf-8 -*-
"""
Huquq fani 3-qism: Qo'shimcha 45 ta rasmiy test savollari.
Part 1 (98) + Part 2 (73) + Part 3 (45) = 216 ta rasmiy savol.
"""

HUQUQ_QUESTIONS_PART3 = [
    # --- KONSTITUTSIYA VA SAYLOV (15 ta) ---
    (
        "Konstitutsiya - Referendum",
        "Referendumda qabul qilingan qarorlar qanday yuridik kuchga ega?",
        [
            "Oliy yuridik kuchga ega bo'lib, biron-bir davlat organi tomonidan tasdiqlanishi talab etilmaydi",
            "Faqat tavsiyaviy xarakterga ega",
            "Prezident farmoni bilan tasdiqlanishi shart",
            "Faqat 1 yil davomida kuchga ega"
        ],
        0,
        "Referendum to'g'risidagi qonunga ko'ra referendumda qabul qilingan qaror oliy yuridik kuchga ega va bevosita amal qiladi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Referendum",
        "Qaysi masalalar bo'yicha referendum o'tkazilishi mumkin emas?",
        [
            "O'zbekiston Respublikasining hududiy yaxlitligini o'zgartirish, soliq va byudjet masalalari, amnistiya va afv etish",
            "Konstitutsiyaga o'zgartirish kiritish masalalari",
            "Davlat boshqaruv shaklini belgilash",
            "Ijtimoiy rivojlanish dasturlari"
        ],
        0,
        "Referendum to'g'risidagi qonunning 2-moddasiga ko'ra hududiy yaxlitlik, byudjet, soliqlar, sudlov va afv masalalari referendumga qo'yilmaydi.",
        "Konstitutsiya",
        "qiyin"
    ),
    (
        "Konstitutsiya - Saylov tizimi",
        "O'zbekiston Respublikasi Oliy Majlisi Qonunchilik palatasi deputatligiga nomzod ko'rsatish huquqiga kimlar ega?",
        [
            "Faqat qonunda belgilangan tartibda ro'yxatga olingan siyosiy partiyalar",
            "Har qanday fuqarolar guruhi o'z nomzodini to'g'ridan-to'g'ri ko'rsatishi mumkin",
            "Faqat mahalla qo'mitalari",
            "Faqat viloyat hokimlari"
        ],
        0,
        "Saylov kodeksiga binoan Qonunchilik palatasi deputatligiga nomzod ko'rsatish huquqi faqat siyosiy partiyalarga tegishlidir.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Saylov tizimi",
        "Saylovda nomzod ko'rsatishda ayollar uchun qanday gender kvotasi belgilangan?",
        [
            "Siyosiy partiyadan ko'rsatilgan nomzodlar umumiy sonining kamida 40 foizini (ilgari 30%) ayollar tashkil etishi kerak",
            "Kamida 10 foizini",
            "Kamida 50 foizini",
            "Kvota belgilanmagan"
        ],
        0,
        "Saylov kodeksiga kiritilgan yangi talabga binoan siyosiy partiyalar tomonidan ko'rsatiladigan nomzodlarning kamida 40 foizini ayollar tashkil etishi shart.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Saylov tizimi",
        "O'zbekiston Respublikasida saylovoldi tashviqoti qachon to'xtatiladi?",
        [
            "Ovoz berish kunidan bir kun oldin ('sukut kuni') va ovoz berish kunida",
            "Saylov boshlanishiga 1 soat qolganda",
            "Saylov kunining oxirida",
            "Tashviqot to'xtatilmaydi"
        ],
        0,
        "Saylov kodeksiga ko'ra ovoz berish boshlanishidan bir kun oldin har qanday saylovoldi tashviqoti to'xtatiladi ('sukut kuni').",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Senat",
        "Oliy Majlis Senatining mutlaq vakolatlariga qaysilar kiradi?",
        [
            "Konstitutsiyaviy sud, Oliy sud sudyalarini, Bosh prokuror va Davlat xavfsizlik xizmati rahbarini tasdiqlash",
            "Davlat byudjeti qonun loyihasini birinchi o'qishda qabul qilish",
            "Xalq deputatlari tuman kengashlarini tarqatib yuborish",
            "Jinoyat ishlarini ko'rib chiqish"
        ],
        0,
        "Konstitutsiyaning 95-moddasiga ko'ra Senat sud organlari rahbarlari, Bosh prokuror, elchilarni tayinlash vakolatiga ega.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Qonunchilik palatasi",
        "Oliy Majlis Qonunchilik palatasining mutlaq vakolatiga qaysi masala kiradi?",
        [
            "Davlat byudjetining ijro etilishini nazorat qilish va Bosh vazir hisobotlarini eshitish",
            "Bosh prokurorni ishdan bo'shatish",
            "Viloyat hokimlarini tayinlash",
            "Sudyalarga qasamyod qildirish"
        ],
        0,
        "Konstitutsiyaning 94-moddasiga binoan Davlat byudjeti loyihasini ko'rib chiqish va qabul qilish Qonunchilik palatasining mutlaq vakolatidir.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Prezident",
        "Prezident saylovida g'alaba qozonish uchun nomzod qancha ovoz to'plashi kerak?",
        [
            "Ovoz berishda ishtirok etgan saylovchilarning 50 foizidan ko'prog'ining (mutlaq ko'pchilik) ovozini",
            "Oddiy ko'pchilik (eng ko'p ovoz olgan shaxs)",
            "Saylovchilarning 80 foiz ovozini",
            "Barcha deputatlarning ovozini"
        ],
        0,
        "Saylov kodeksiga muvofiq nomzod ovoz berishda qatnashgan fuqarolarning yarmidan ko'pining (50% + 1) ovozini olishi shart.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Hukumat",
        "Vazirlar Mahkamasi a'zolari o'z lavozimiga qanday tasdiqlanadi?",
        [
            "Bosh vazir taqdimiga binoan Qonunchilik palatasi ma'qullaganidan so'ng Prezident tomonidan tayinlanadi",
            "Faqat Prezident yakka farmoni bilan",
            "Senat raisi buyrug'i bilan",
            "Oliy sud qarori bilan"
        ],
        0,
        "Yangi Konstitutsiyaga ko'ra Hukumat a'zolari nomzodlari Qonunchilik palatasi deputatlari tomonidan ma'qullanadi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Ombudsperson",
        "Oliy Majlisning Inson huquqlari bo'yicha vakili (Ombudsman) qaysi organ oldida hisobdordir?",
        [
            "O'zbekiston Respublikasi Oliy Majlisi palatalari oldida",
            "Prezident Administratsiyasi oldida",
            "Adliya vazirligi oldida",
            "Bosh prokuratura oldida"
        ],
        0,
        "Ombudsman o'z faoliyati to'g'risida har yili Oliy Majlis palatalariga hisobot taqdim etadi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Hisob palatasi",
        "Davlat byudjeti mablag'larining maqsadli sarflanishini nazorat qiluvchi oliy moliyaviy nazorat organi qaysi?",
        [
            "O'zbekiston Respublikasi Hisob palatasi",
            "Soliq qo'mitasi",
            "Markaziy bank",
            "Iqtisodiyot vazirligi"
        ],
        0,
        "Hisob palatasi davlat byudjeti ijrosi va moliyaviy mablag'larning sarflanishini mustaqil tekshiruvchi oliy organdir.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Sud tizimi",
        "O'zbekiston Respublikasida favqulodda sudlar tuzishga yo'l qo'yiladimi?",
        [
            "Favqulodda sudlar tuzishga yo'l qo'yilmaydi",
            "Harbiy holatda ruxsat beriladi",
            "Prezident farmoni bilan tuzilishi mumkin",
            "Favqulodda vaziyatlar vazirligi huzurida tuziladi"
        ],
        0,
        "Konstitutsiyaning 130-moddasiga ko'ra favqulodda sudlar tuzishga qat'iyan yo'l qo'yilmaydi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Fuqarolik",
        "O'zbekiston Respublikasi fuqaroligi qanday hollarda olinadi?",
        [
            "Tug'ilish bo'yicha, qabul qilinish bo'yicha, fuqarolikni tiklash yoki xalqaro shartnomalar asosida",
            "Faqat katta miqdorda sarmoya kiritish bilan",
            "Faqat qarindoshlik asosida",
            "Faqat Prezident qarindoshlariga beriladi"
        ],
        0,
        "'O'zbekiston Respublikasining fuqaroligi to'g'risida'gi Qonunga muvofiq fuqarolik tug'ilish, qabul qilish va boshqa qonuniy asoslarda olinadi.",
        "Konstitutsiya",
        "orta"
    ),
    (
        "Konstitutsiya - Mudofaa",
        "O'zbekiston Respublikasi Qurolli Kuchlari qanday maqsadda tuziladi?",
        [
            "Davlat suverenitetini, hududiy yaxlitligini, aholining tinch hayoti va xavfsizligini himoya qilish uchun",
            "Boshqa davlatlarni bosib olish uchun",
            "Faqat chegarada bojxona bojini yig'ish uchun",
            "Faqat ichki jamoat tartibini saqlash uchun"
        ],
        0,
        "Konstitutsiyaning 153-moddasiga muvofiq Qurolli Kuchlar O'zbekiston Respublikasining suverenitetini va hududiy yaxlitligini himoya qilish uchun tuziladi.",
        "Konstitutsiya",
        "oson"
    ),
    (
        "Konstitutsiya - Davlat tili",
        "Davlat tiliga hurmatsizlik qilish qanday javobgarlikka sabab bo'ladi?",
        [
            "Qonun bilan belgilangan ma'muriy javobgarlikka sabab bo'ladi",
            "Faqat jamiyat tomonidan qoralanadi",
            "Hech qanday oqibat bo'lmaydi",
            "Faqat jarima solinmaydi"
        ],
        0,
        "Davlat tili to'g'risidagi qonunchilikni buzish va unga hurmatsizlik qilish Ma'muriy javobgarlik to'g'risidagi kodeks bo'yicha jarimaga sabab bo'ladi.",
        "Konstitutsiya",
        "oson"
    ),

    # --- 8-SINF DAVLAT VA HUQUQ NAZARIYASI (10 ta) ---
    (
        "8-sinf - Huquq tizimi",
        "Bir turdagi ijtimoiy munosabatlarni tartibga soluvchi huquqiy normalar guruhi nima deyiladi?",
        [
            "Huquq instituti",
            "Huquq tizimi",
            "Huquq subyekti",
            "Yuridik fakt"
        ],
        0,
        "Huquq instituti – bitta huquq sohasi doirasidagi bir turdagi munosabatni tartibga soluvchi normalar yig'indisidir (masalan, mulk huquqi instituti, nikoh instituti).",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Huquq manbalari",
        "Davlat tomonidan rasman ma'qullangan va umummajburiy qoida sifatida qabul qilingan xalq urf-odati nima deyiladi?",
        [
            "Huquqiy odat",
            "Sud pretsedenti",
            "Shartnoma",
            "Huquqiy doktrina"
        ],
        0,
        "Huquqiy odat – uzoq vaqt davomida qo'llanilishi natijasida shakllangan va davlat tomonidan tan olingan xulq-atvor qoidasidir.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Huquqiy munosabat",
        "Huquqiy munosabatning mazmuni nimadan iborat?",
        [
            "Ishtirokchilarning subyektiv huquqlari va yuridik majburiyatlaridan",
            "Faqat moddiy buyumlardan",
            "Faqat guvohlarning gaplaridan",
            "Sud xarajatlaridan"
        ],
        0,
        "Huquqiy munosabat mazmuni – subyektning qonun bilan berilgan huquqi va uning zimmasidagi yuridik burchidir.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Qonunchilik texnikasi",
        "Normativ-huquqiy hujjatlarning moddalari, bandlari va qismlarini to'g'ri shakllantirish qoidalari nima deyiladi?",
        [
            "Qonunchilik texnikasi (Yuridik texnika)",
            "Yuridik lingvistika",
            "Sud ekspertizasi",
            "Qonuniy himoya"
        ],
        0,
        "Qonunchilik texnikasi – qonun loyihalarini aniq, ravshan va bir xil ma'noda ishlab chiqish usullari va qoidalari majmuidir.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Huquqni talqin qilish",
        "Huquq normasining asl mazmunini, maqsadini va ma'nosini tushuntirib berish faoliyati nima deyiladi?",
        [
            "Huquqni talqin qilish (interpretatsiya)",
            "Huquqni qo'llash",
            "Huquq ijodkorligi",
            "Huquqni buzish"
        ],
        0,
        "Huquqni talqin qilish – qonun normasining mazmunini aniqlash va tushuntirishdir.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Huquqiy ong",
        "Kishilarning huquqqa bo'lgan ichki hissiyotlari, tuyg'ulari va kayfiyatlari nima deb ataladi?",
        [
            "Huquqiy psixologiya",
            "Huquqiy mafkura",
            "Huquqiy fan",
            "Huquqiy axborot"
        ],
        0,
        "Huquqiy ong ikki darajadan: huquqiy psixologiya (his-tuyg'ular) va huquqiy mafkura (nazariy qarashlar) dan iborat.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Delikt qobiliyati",
        "Shaxsning sodir etgan huquqbuzarligi uchun mustaqil yuridik javobgarlikni o'z zimmasiga olish layoqati nima?",
        [
            "Delikt qobiliyati (deliktsusposobnost)",
            "Huquq layoqati",
            "Vakolat",
            "Immunitet"
        ],
        0,
        "Delikt qobiliyati – shaxsning o'z g'ayrihuquqiy qilmishlari uchun moddiy, ma'muriy yoki jinoiy javob berish qobiliyatidir.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Qonun ustuvorligi",
        "Qonun ustuvorligi (Rule of Law) nimani anglatadi?",
        [
            "Hech bir shaxs yoki idora qonundan ustun bo'la olmasligi, hamma qonun oldida javobgarligi",
            "Faqat politsiya boshlig'i qonunni o'rnatishi",
            "Har yili yangi qonunlar qabul qilinishi",
            "Qonunlarning faqat boylar uchun amal qilishi"
        ],
        0,
        "Qonun ustuvorligi jamiyatda adolat va erkinlikning eng asosiy kafolati hisoblanadi.",
        "8-sinf",
        "oson"
    ),
    (
        "8-sinf - Fuqarolik jamiyati",
        "Fuqarolik jamiyatida davlat bilan fuqaro o'rtasidagi munosabat qanday bo'ladi?",
        [
            "O'zaro tenglik, hamkorlik va o'zaro javobgarlikka asoslanadi",
            "Fuqaro davlatning so'zsiz quli bo'ladi",
            "Davlat fuqarolar hayotiga to'liq aralashadi",
            "Fuqarolar davlat soliqlaridan butunlay ozod bo'ladi"
        ],
        0,
        "Fuqarolik jamiyatida inson manfaatlari birlamchi bo'lib, davlat fuqaro oldida hisobdor bo'ladi.",
        "8-sinf",
        "orta"
    ),
    (
        "8-sinf - Davlat turlari",
        "Dunyoviy davlat deganda nima tushuniladi?",
        [
            "Davlat dindan ajratilgan, birorta din majburiy qilib o'rnatilmaydigan davlat",
            "Diniy ulamolar boshqaradigan davlat",
            "Barcha dinlarni taqiqlovchi davlat",
            "Faqat ateistlar yashaydigan davlat"
        ],
        0,
        "Dunyoviy davlatda davlat diniy ishlarga, diniy tashkilotlar esa davlat boshqaruviga aralashmaydi.",
        "8-sinf",
        "oson"
    ),

    # --- 9-SINF FUQAROLIK VA MEHNAT HUQUQI (10 ta) ---
    (
        "9-sinf - Xodimning moddiy javobgarligi",
        "Xodim korxonaga bevosita yetkazgan zarari uchun umumiy qoidaga ko'ra qanday hajmda javob beradi?",
        [
            "O'zining o'rtacha oylik ish haqi miqdorida (cheklangan moddiy javobgarlik)",
            "Korxonaning butun boyligi qiymatida",
            "Hech qanday moddiy javobgar bo'lmaydi",
            "Umrbod oyligining 90 foizi ushlab qolinadi"
        ],
        0,
        "Mehnat kodeksiga binoan, to'liq javobgarlik shartnomasi bo'lmaganda xodim o'rtacha oylik ish haqi doirasida moddiy javobgar bo'ladi.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Mehnat ta'tili",
        "Ish beruvchi xodimni uning roziligisiz mehnat ta'tilidan chaqirib olishga haqlimi?",
        [
            "Faqat xodimning yozma roziligi bilan chaqirib olishga yo'l qo'yiladi",
            "Ha, istalgan vaqtda direktor buyrug'i bilan",
            "Ta'tildan chaqirib olish mutlaqo taqiqlangan",
            "Faqat xodim xorijga ketmagan bo'lsa mumkin"
        ],
        0,
        "Mehnat kodeksining 232-moddasiga ko'ra xodimni ta'tildan chaqirib olishga faqat uning roziligi bilan ruxsat beriladi.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Mehnat nizolari",
        "Mehnat nizolari komissiyasining qaroridan norozi bo'lgan taraf qayerga murojaat qilishi mumkin?",
        [
            "Fuqarolik ishlari bo'yicha tuman (shahar) sudiga",
            "Faqat korxona direktoriga",
            "Politsiyaga",
            "FHDY organiga"
        ],
        0,
        "Xodim yoki ish beruvchi komissiya qaroridan norozi bo'lsa 10 kun ichida sudga da'vo arizasi bilan murojaat qilishi mumkin.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Ish haqi to'lash",
        "Mehnat kodeksiga ko'ra ish haqi xodimlarga qanday muddatlarda to'lanishi shart?",
        [
            "Har yarim oyda kamida bir marta (oyiga 2 marta)",
            "Yilda bir marta",
            "Har uch oyda bir marta",
            "Faqat shartnoma muddati tugaganda"
        ],
        0,
        "Ish haqi har yarim oyda kamida bir marta to'lanishi shart (avans va oylik hisob-kitob).",
        "9-sinf",
        "oson"
    ),
    (
        "9-sinf - Aliment to'lash",
        "Aliment to'lashdan qasddan bo'yin tovlagan shaxslarga nisbatan qanday jazo choralari qo'llanilishi mumkin?",
        [
            "Ma'muriy qamoq (15 sutka) va Jinoyat kodeksi bo'yicha jinoiy javobgarlik",
            "Faqat og'zaki tanbeh beriladi",
            "Hech qanday chora ko'rilmaydi",
            "Bolaning fuqaroligi bekor qilinadi"
        ],
        0,
        "Aliment to'lashdan bo'yin tovlaganlik uchun JK 122-moddasiga binoan jinoiy javobgarlik (ozodlikdan mahrum qilishgacha) nazarda tutilgan.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Da'vo arizasi",
        "Fuqarolik sudida da'vo arizasini bergan shaxs kim deb ataladi?",
        [
            "Da'vogar",
            "Javobgar",
            "Guvoh",
            "Uchinchi shaxs"
        ],
        0,
        "Da'vogar – buzilgan huquqlarini himoya qilish uchun sudga ariza bilan murojaat qilgan jismoniy yoki yuridik shaxsdir.",
        "9-sinf",
        "oson"
    ),
    (
        "9-sinf - Javobgar",
        "Suddagi da'vo talabi qaratilgan shaxs kim deb ataladi?",
        [
            "Javobgar",
            "Da'vogar",
            "Ekspert",
            "Tergovchi"
        ],
        0,
        "Javobgar – da'vogarning huquqlarini buzganlikda ayblanib sudga jalb etilgan shaxsdir.",
        "9-sinf",
        "oson"
    ),
    (
        "9-sinf - Oila huquqi",
        "Bolani farzandlikka olish qaysi organ qarori bilan amalga oshiriladi?",
        [
            "Sud qaroriga asosan",
            "Faqat mahalla fuqarolar yig'ini qarori bilan",
            "Bolalar uyi mudiri ruxsati bilan",
            "Notarius tasdig'i bilan"
        ],
        0,
        "Oila kodeksiga ko'ra bolani farzandlikka olish faqat fuqarolik ishlari bo'yicha sudning hal qiluv qarori bilan rasmiylashtiriladi.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Vasiylik va homiylik",
        "Vasiylik va homiylik kimlarga nisbatan belgilanadi?",
        [
            "14 yoshgacha bo'lgan yetimlarga – vasiylik, 14 dan 18 yoshgacha bo'lganlarga – homiylik belgilanadi",
            "Faqat nafaqa yoshidagi qariyalarga",
            "Talabalarga",
            "Chet elliklarga"
        ],
        0,
        "Oila kodeksiga ko'ra 14 yoshgacha vasiylik, 14-18 yoshdagilarga hamda muomala layoqati cheklanganlarga homiylik tayinlanadi.",
        "9-sinf",
        "orta"
    ),
    (
        "9-sinf - Mulkiy huquq",
        "Topilma (yo'qolgan buyum) topib olgan shaxs nima qilishi shart?",
        [
            "Buyum egasiga yoki tegishli organga (politsiyaga, transport ma'muriyatiga) darhol xabar berishi shart",
            "Darhol o'zlashtirib olishi mumkin",
            "Bozorga olib borib sotishi shart",
            "Tashlab yuborishi kerak"
        ],
        0,
        "Fuqarolik kodeksining 192-moddasiga binoan topilma topib olgan shaxs uni egasiga yoki huquqni muhofaza qiluvchi organga topshirishi shart.",
        "9-sinf",
        "oson"
    ),

    # --- 10-11 SINF MA'MURIY, JINOIY VA XALQARO HUQUQ (10 ta) ---
    (
        "10-sinf - Jinoiy jazolarni yengillashtiruvchi holatlar",
        "Qaysi holatlar jinoiy jazoni yengillashtiruvchi holatlar hisoblanadi?",
        [
            "Aybiga chin ko'ngildan iqror bo'lish, zararni ixtiyoriy qoplash, voyaga yetmaganlik va homiladorlik",
            "G'arazli maqsadda harakat qilish",
            "Guruh bo'lib til biriktirish",
            "Alkogolli mastlik holatida bo'lish"
        ],
        0,
        "JKning 55-moddasida jazoni yengillashtiruvchi holatlar (chin ko'ngildan pushaymonlik, zararni bartaraf etish) bayon etilgan.",
        "10-sinf",
        "orta"
    ),
    (
        "10-sinf - Jinoiy jazolarni og'irlashtiruvchi holatlar",
        "Qaysi holat jazoni og'irlashtiruvchi holat hisoblanadi?",
        [
            "Jinoyatni bir guruh shaxslar tomonidan oldindan til biriktirib sodir etilishi",
            "Shaxsning birinchi marta jinoyat sodir etishi",
            "Yetkazilgan zararni darhol to'lab berishi",
            "Jabrlanuvchi bilan yarashish"
        ],
        0,
        "JKning 56-moddasiga ko'ra guruh bo'lib yoki o'ta shafqatsizlik bilan jinoyat sodir etish jazoni og'irlashtiradi.",
        "10-sinf",
        "orta"
    ),
    (
        "10-sinf - Yarashuv instituti",
        "Ijtimoiy xavfi katta bo'lmagan yoki uncha og'ir bo'lmagan jinoyat sodir etgan shaxs jabrlanuvchi bilan yarashsa nima bo'ladi?",
        [
            "Jinoiy javobgarlikdan ozod qilinishi mumkin (JK 66-1 modda)",
            "Albatta qamoqqa olinadi",
            "Faqat ikki baravar jarima to'laydi",
            "Yarashuv jinoiy ishda hisobga olinmaydi"
        ],
        0,
        "Yarashuv instituti shaxs o'z aybini tan olib, zararni qoplagan va jabrlanuvchi bilan yarashgan taqdirda javobgarlikdan ozod qilish imkonini beradi.",
        "10-sinf",
        "orta"
    ),
    (
        "10-sinf - Ma'muriy jazo",
        "Mast holda transport vositasini boshqarganlik uchun qanday ma'muriy jazo qo'llaniladi?",
        [
            "Katta miqdorda jarima va 1,5 yildan 3 yilgacha transport vositasini boshqarish huquqidan mahrum qilish",
            "Faqat og'zaki ogohlantirish",
            "Avtomobilni tekinga davlatga berish",
            "Faqat haydovchilik guvohnomasini 1 kunga olib qo'yish"
        ],
        0,
        "MJtK 131-moddasiga ko'ra mast haydovchi BHMning 25 baravari jarima va transport boshqarish huquqidan mahrum etiladi.",
        "10-sinf",
        "orta"
    ),
    (
        "11-sinf - Ekologik ekspertiza",
        "Yangi qurilayotgan yirik sanoat korxonalari tabiatga ziyon yetkazmasligini aniqlash uchun nima o'tkaziladi?",
        [
            "Davlat ekologik ekspertizasi",
            "Sud-tibbiy ekspertizasi",
            "Faqat moliyaviy audit",
            "Kriminalistik tekshiruv"
        ],
        0,
        "Davlat ekologik ekspertizasi har qanday yirik obyekt loyihasining tabiatga ta'sirini oldindan tekshiradi.",
        "11-sinf",
        "orta"
    ),
    (
        "11-sinf - Xalqaro shartnomalar",
        "O'zbekiston Respublikasi nomidan xalqaro shartnomalarni kim imzolaydi?",
        [
            "O'zbekiston Respublikasi Prezidenti yoki uning maxsus vakolati bilan Bosh vazir yoxud Tashqi ishlar vaziri",
            "Faqat tuman hokimlari",
            "Har qanday deputat o'z xohishicha",
            "Faqat Konstitutsiyaviy sud raisi"
        ],
        0,
        "Xalqaro shartnomalar to'g'risidagi qonunga ko'ra davlat nomidan shartnomalarni oliy rahbarlar imzolashga haqlidir.",
        "11-sinf",
        "orta"
    ),
    (
        "11-sinf - Ratifikatsiya",
        "Davlatning xalqaro shartnomaga o'z roziligini parlament orqali rasman tasdiqlashi nima deyiladi?",
        [
            "Ratifikatsiya qilish",
            "Denonsatsiya qilish",
            "Veto qo'yish",
            "Litsenziyalash"
        ],
        0,
        "Ratifikatsiya – xalqaro shartnomani oliy qonun chiqaruvchi organ (parlament) tomonidan ma'qullanib, qonun qabul qilinishidir.",
        "11-sinf",
        "qiyin"
    ),
    (
        "11-sinf - Denonsatsiya",
        "Davlatning xalqaro shartnomadan qonuniy tartibda chiqishi yoki uni bekor qilishi nima deyiladi?",
        [
            "Denonsatsiya qilish",
            "Ratifikatsiya",
            "Immigratsiya",
            "Inkorporatsiya"
        ],
        0,
        "Denonsatsiya – davlatning xalqaro shartnomada belgilangan qoidalarga ko'ra undagi ishtirokini to'xtatishidir.",
        "11-sinf",
        "qiyin"
    ),
    (
        "11-sinf - Konsullik",
        "O'zbekiston Respublikasining xorijdagi fuqarolariga huquqiy yordam ko'rsatuvchi, pasport va vizalar beruvchi rasmiy muassasa nima?",
        [
            "Konsullik muassasasi (yoki Elchixona)",
            "Xorijiy bank bo'limi",
            "Bojxona posti",
            "Xalqaro sud"
        ],
        0,
        "Konsullik xorijdagi vatandoshlarning huquq va manfaatlarini himoya qiluvchi davlat organidir.",
        "11-sinf",
        "oson"
    ),
    (
        "11-sinf - Lex specialis",
        "Yuridik fanda 'Maxsus qonun umumiy qonundan ustun turadi' qoidasi lotinchada qanday ataladi?",
        [
            "Lex specialis derogat legi generali",
            "Pacta sunt servanda",
            "Dura lex, sed lex",
            "In dubio pro reo"
        ],
        0,
        "Lex specialis prinsipi – bitta munosabat bo'yicha maxsus norma umumiy normadan ustun qo'llanilishini anglatuvchi qadimiy huquqiy qoidadir.",
        "11-sinf",
        "qiyin"
    )
]
print(f"3-qism savollari tayyor: {len(HUQUQ_QUESTIONS_PART3)} ta")
