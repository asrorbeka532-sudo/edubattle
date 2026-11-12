// ================= GLOBAL BACKEND TUNNEL INTERCEPTOR =================
const BACKEND_TUNNEL_URL = 'https://edubattle-backend-x0v2.onrender.com';

(function() {
  const origFetch = window.fetch;
  window.fetch = async function(input, init) {
    let url = typeof input === 'string' ? input : (input && input.url ? input.url : '');
    if (url.startsWith('/api/') || url.startsWith('/uploads/')) {
      try {
        const res = await origFetch(input, init);
        const isHtml404 = res.status === 404 && (res.headers.get('content-type') || '').includes('text/html');
        if (!isHtml404 && res.status !== 502 && res.status !== 503) {
          return res;
        }
      } catch (err) {
        console.warn("Relative fetch error, fallback to tunnel:", err);
      }
      const directUrl = BACKEND_TUNNEL_URL + url;
      return origFetch(directUrl, init);
    }
    return origFetch(input, init);
  };
})();


const DEFAULT_TEXTBOOKS = [{"id": 1, "title": "6-sinf Matematika Darsligi", "author": "M. Mirzaahmedov", "grade": "6-sinf", "subject_id": 1, "subject_name": "Matematika", "subject_icon": "📐", "file_url": "/uploads/textbooks/matematika_6_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 6-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 2, "title": "8-sinf Geometriya Darsligi", "author": "A. Rahimov", "grade": "8-sinf", "subject_id": 1, "subject_name": "Matematika", "subject_icon": "📐", "file_url": "/uploads/textbooks/geometriya_8_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 8-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 5, "title": "11-sinf Matematika (2-qism)", "author": "Sh. Alimov", "grade": "11-sinf", "subject_id": 1, "subject_name": "Matematika", "subject_icon": "📐", "file_url": "/uploads/textbooks/matematika_2qism_11_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 11-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 6, "title": "7-sinf Kimyo Darsligi", "author": "I. Asqarov", "grade": "7-sinf", "subject_id": 3, "subject_name": "Kimyo", "subject_icon": "🧪", "file_url": "/uploads/textbooks/kimyo_7_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 7-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 7, "title": "8-sinf Kimyo Darsligi", "author": "I. Asqarov", "grade": "8-sinf", "subject_id": 3, "subject_name": "Kimyo", "subject_icon": "🧪", "file_url": "/uploads/textbooks/kimyo_8_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 8-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 8, "title": "9-sinf Kimyo Darsligi", "author": "I. Asqarov", "grade": "9-sinf", "subject_id": 3, "subject_name": "Kimyo", "subject_icon": "🧪", "file_url": "/uploads/textbooks/kimyo_9_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 9-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 10, "title": "9-sinf Biologiya Darsligi", "author": "A. Zikiryayev", "grade": "9-sinf", "subject_id": 4, "subject_name": "Biologiya", "subject_icon": "🧬", "file_url": "/uploads/textbooks/biologiya_9_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 9-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 12, "title": "11-sinf Biologiya Darsligi", "author": "A. G'ofurov", "grade": "11-sinf", "subject_id": 4, "subject_name": "Biologiya", "subject_icon": "🧬", "file_url": "/uploads/textbooks/biologiya_11_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 11-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 13, "title": "6-sinf Ona tili Darsligi", "author": "N. Mahmudov", "grade": "6-sinf", "subject_id": 5, "subject_name": "Ona tili va Adabiyot", "subject_icon": "📚", "file_url": "/uploads/textbooks/ona_tili_6_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 6-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 14, "title": "7-sinf Ona tili Darsligi", "author": "N. Mahmudov", "grade": "7-sinf", "subject_id": 5, "subject_name": "Ona tili va Adabiyot", "subject_icon": "📚", "file_url": "/uploads/textbooks/ona_tili_7_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 7-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 15, "title": "8-sinf Ona tili Darsligi", "author": "N. Mahmudov", "grade": "8-sinf", "subject_id": 5, "subject_name": "Ona tili va Adabiyot", "subject_icon": "📚", "file_url": "/uploads/textbooks/ona_tili_8_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 8-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 16, "title": "9-sinf Ona tili Darsligi", "author": "N. Mahmudov", "grade": "9-sinf", "subject_id": 5, "subject_name": "Ona tili va Adabiyot", "subject_icon": "📚", "file_url": "/uploads/textbooks/ona_tili_9_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 9-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 19, "title": "6-sinf Qadimgi dunyo tarixi", "author": "A. Sagdullayev", "grade": "6-sinf", "subject_id": 6, "subject_name": "Tarix", "subject_icon": "🏛️", "file_url": "/uploads/textbooks/qadimgi_dunyo_tarixi_6_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 6-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 20, "title": "7-sinf O'zbekiston tarixi", "author": "Q. Rajabov", "grade": "7-sinf", "subject_id": 6, "subject_name": "Tarix", "subject_icon": "🏛️", "file_url": "/uploads/textbooks/ozbekiston_tarixi_7_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 7-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 25, "title": "10-sinf O'zbekiston tarixi", "author": "Q. Rajabov", "grade": "10-sinf", "subject_id": 6, "subject_name": "Tarix", "subject_icon": "🏛️", "file_url": "/uploads/textbooks/ozbekiston_tarixi_10_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 10-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 27, "title": "10-sinf Davlat va huquq asoslari", "author": "O'. Tojixonov", "grade": "10-sinf", "subject_id": 6, "subject_name": "Tarix", "subject_icon": "🏛️", "file_url": "/uploads/textbooks/davlat_va_huquq_asoslari_10_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 10-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 29, "title": "11-sinf O'zbekiston tarixi", "author": "Q. Rajabov", "grade": "11-sinf", "subject_id": 6, "subject_name": "Tarix", "subject_icon": "🏛️", "file_url": "/uploads/textbooks/ozbekiston_tarixi_11_uzb.pdf", "summary": "O'zbekiston Respublikasi Xalq ta'limi vazirligi tomonidan tasdiqlangan rasmiy umumta'lim maktabi 11-sinf darsligi.", "uploader_name": null, "chapters": [{"title": "1-bob. Kirish va asosiy tushunchalar", "summary": "Mavzu bo'yicha fundamental bilimlar va amaliy qoidalar."}, {"title": "2-bob. Asosiy bo'lim va masalalar", "summary": "Nazariy qoidalar va misollar yechimi."}, {"title": "3-bob. Mustahkamlash va xulosalar", "summary": "Mavzuni to'liq takrorlash va testlarga tayyorgarlik."}]}, {"id": 33, "title": "O'zbekiston Respublikasi Konstitutsiyasi (Yangi tahrir)", "author": "Oliy Majlis va O'zbekiston xalqi", "grade": "Barcha sinflar", "subject_id": 9, "subject_name": "Huquq", "subject_icon": "⚖️", "file_url": "/uploads/textbooks/ozbekiston_respublikasi_konstitutsiyasi_yangi_tahrir.pdf", "summary": "2023-yil 30-apreldagi referendumda umumxalq ovozi bilan qabul qilingan yangi tahrirdagi O'zbekiston Respublikasi Konstitutsiyasi. 6 bo'lim, 27 bob va 155 moddadan iborat oliy yuridik kuchga ega Bosh qomus.", "uploader_name": null, "chapters": [{"title": "1-bo'lim. Asosiy prinsiplar (1-18 moddalar)", "summary": "Davlat suvereniteti, xalq hokimiyatchiligi, Konstitutsiya va qonun ustunligi hamda tinchliksevar tashqi siyosat."}, {"title": "2-bo'lim. Inson va fuqaroning asosiy huquqlari, erkinliklari va burchlari (19-64 moddalar)", "summary": "Fuqarolik, shaxsiy, siyosiy, iqtisodiy, ijtimoiy, madaniy va ekologik huquqlar hamda konstitutsiyaviy burchlar."}, {"title": "3-bo'lim. Jamiyat va shaxs (65-82 moddalar)", "summary": "Bozor iqtisodiyoti asoslari, jamoat birlashmalari, erkin OAV, oila va yoshlarni har tomonlama qo'llab-quvvatlash."}, {"title": "4-bo'lim. Ma'muriy-hududiy va davlat tuzilishi (83-90 moddalar)", "summary": "Hududiy yaxlitlik va Qoraqalpog'iston Respublikasining Konstitutsiyaviy maqomi."}, {"title": "5-bo'lim. Davlat hokimiyatining tashkil etilishi (91-153 moddalar)", "summary": "Oliy Majlis Qonunchilik palatasi va Senati, Prezident, Vazirlar Mahkamasi, Mahalliy hokimiyat, Mustaqil Sud hokimiyati va Prokuratura."}, {"title": "6-bo'lim. Konstitutsiyaga o'zgartirish kiritish tartibi (154-155 moddalar)", "summary": "Konstitutsiyaga tuzatishlar kiritish va boshqaruv shakli hamda hududiy yaxlitlikning daxlsizligi."}]}, {"id": 34, "title": "8-sinf Davlat va huquq asoslari", "author": "A. Saidov, V. Qo'chqorov", "grade": "8-sinf", "subject_id": 9, "subject_name": "Huquq", "subject_icon": "⚖️", "file_url": "/uploads/textbooks/davlat_va_huquq_asoslari_8_uzb.pdf", "summary": "Umumta'lim maktablarining 8-sinfi uchun darslik: Davlatning kelib chiqishi, suverenitet, boshqaruv va davlat tuzilishi shakllari, huquq normalari strukturasi, yuridik faktlar va huquqiy madaniyat.", "uploader_name": null, "chapters": [{"title": "1-bob. Davlat tushunchasi va belgilari", "summary": "Davlatning kelib chiqishi nazariyalari, ommaviy hokimiyat, davlat suvereniteti va uning asosiy vazifalari."}, {"title": "2-bob. Davlat shakllari va siyosiy rejimlar", "summary": "Monarxiya va respublika, unitar va federatsiya, demokratik va antidemokratik siyosiy rejimlar."}, {"title": "3-bob. Huquq tushunchasi va huquqiy normalar", "summary": "Huquq va axloq munosabati, gipoteza, dispozitsiya, sanksiya va huquq manbalari."}, {"title": "4-bob. Huquqiy munosabatlar va qonuniylik", "summary": "Huquqiy munosabat elementlari, yuridik faktlar (voqea va harakat), huquqiy ong va huquqiy madaniyat."}]}, {"id": 35, "title": "9-sinf Davlat va huquq asoslari", "author": "A. Saidov, U. Tojixonov", "grade": "9-sinf", "subject_id": 9, "subject_name": "Huquq", "subject_icon": "⚖️", "file_url": "/uploads/textbooks/davlat_va_huquq_asoslari_9_uzb.pdf", "summary": "Umumta'lim maktablarining 9-sinfi uchun darslik: Fuqarolik huquqi, muomala layoqati, emansipatsiya, mulkdorlik huquqi, Oila huquqi va nikoh munosabatlari, yangi Mehnat kodeksi asoslari.", "uploader_name": null, "chapters": [{"title": "1-bob. Fuqarolik huquqi asoslari", "summary": "Huquq layoqati va muomala layoqati, emansipatsiya, mulk huquqi, oldi-sotdi va hadya shartnomalari, da'vo muddatlari."}, {"title": "2-bob. Oila huquqi va nikoh munosabatlari", "summary": "Nikoh yoshi, nikoh tuzish tartibi, nikoh shartnomasi, er-xotin mulki, aliment munosabatlari va farzandlikka olish."}, {"title": "3-bob. Yangi Mehnat kodeksi asoslari", "summary": "Mehnat shartnomasi tuzish, sinov muddati, haftalik ish vaqti, ta'tillar va mehnat intizomi choralari."}, {"title": "4-bob. Voyaga yetmaganlarning mehnat huquqlari", "summary": "15-18 yoshli o'smirlarning qisqartirilgan ish vaqti, taqiqlangan ishlar va majburiy tibbiy ko'riklar."}]}, {"id": 36, "title": "10-sinf Davlat va huquq asoslari", "author": "O'. Tojixonov, A. Saidov", "grade": "10-sinf", "subject_id": 9, "subject_name": "Huquq", "subject_icon": "⚖️", "file_url": "/uploads/textbooks/davlat_va_huquq_asoslari_10_uzb.pdf", "summary": "Umumta'lim maktablarining 10-sinfi uchun darslik: Ma'muriy huquq, ma'muriy javobgarlik va jazo turlari, Jinoyat huquqi, jinoyat tarkibi, jinoiy javobgarlik yoshi hamda Ekologiya huquqi.", "uploader_name": null, "chapters": [{"title": "1-bob. Ma'muriy huquq va javobgarlik", "summary": "Ma'muriy huquqbuzarlik tushunchasi, 16 yoshdan javobgarlik, ma'muriy jarimalar va 15 sutkagacha ma'muriy qamoq."}, {"title": "2-bob. Jinoyat huquqi asoslari", "summary": "Jinoyat toifalari, jinoyat tarkibining 4 elementi (obyekt, obyektiv tomon, subyekt, subyektiv tomon), qasd va ehtiyotsizlik."}, {"title": "3-bob. Jinoiy javobgarlik va jazo tizimi", "summary": "14 va 16 yoshdan javobgarlik, zaruriy mudofaa, jinoiy ishtirokchilik turlari, ozodlikdan mahrum qilish va umrbod qamoq cheklovlari."}, {"title": "4-bob. Ekologiya huquqi va atrof-muhit muhofazasi", "summary": "Tabiatni muhofaza qilish to'g'risidagi qonun, Qizil kitob, tabiiy resurslar va ekologik huquqbuzarliklar uchun javobgarlik."}]}, {"id": 37, "title": "11-sinf Davlat va huquq asoslari", "author": "A. Saidov, B. Ahmedov", "grade": "11-sinf", "subject_id": 9, "subject_name": "Huquq", "subject_icon": "⚖️", "file_url": "/uploads/textbooks/davlat_va_huquq_asoslari_11_uzb.pdf", "summary": "Umumta'lim maktablarining 11-sinfi uchun darslik: Xalqaro huquq, Inson huquqlari umumjahon deklaratsiyasi, Sud hokimiyati va odil sudlov kafolatlari, Prokuratura va Advokatura institutlari.", "uploader_name": null, "chapters": [{"title": "1-bob. Xalqaro huquq va inson huquqlari", "summary": "BMT Nizomi, Inson huquqlari umumjahon deklaratsiyasi (1948), Bola huquqlari to'g'risidagi konvensiya va xalqaro gumanitar huquq."}, {"title": "2-bob. Sud hokimiyati va odil sudlov", "summary": "Konstitutsiyaviy sud, Oliy sud, sudyalarning mustaqilligi, sud ochiqligi (oshkoraligi) va sud qarorlarining majburiyligi."}, {"title": "3-bob. Prokuratura va tergov organlari", "summary": "Qonunlar ijrosi ustidan Bosh prokuror nazorati, davlat ayblovi va sud qarorlari ijrosi (MIB)."}, {"title": "4-bob. Advokatura va fuqarolik institutlari", "summary": "Professional yuridik yordam, advokatlik siri, Ombudsman, Bolalar ombudsmani va Korrupsiyaga qarshi kurashish agentligi."}]}];
// ========================================================
// EDUBATTLE - CORE APP LOGIC (STRICT ROLE ENFORCEMENT & TARIFFS)
// ========================================================

const state = {
  currentUser: null,
  subjects: [],
  textbooks: [],
  activeSubject: null,
  activeGrade: null,
  currentView: 'home',
  selectedPaymentProvider: 'click',
  selectedPaymentPlan: 'student_pro',
  proPrice: 29000,
  audioEnabled: true,
  audioCtx: null
};

// ----------------- AUDIO SYNTHESIZER -----------------
function initAudio() {
  if (!state.audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (AudioContext) state.audioCtx = new AudioContext();
  }
}

function playSound(type) {
  if (!state.audioEnabled) return;
  try {
    initAudio();
    if (!state.audioCtx) return;
    if (state.audioCtx.state === 'suspended') state.audioCtx.resume();

    const ctx = state.audioCtx;
    const now = ctx.currentTime;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);

    if (type === 'correct') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(587.33, now);
      osc.frequency.setValueAtTime(880, now + 0.1);
      gain.gain.setValueAtTime(0.12, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
      osc.start(now);
      osc.stop(now + 0.35);
    } else if (type === 'wrong') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(140, now);
      gain.gain.setValueAtTime(0.12, now);
      gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
      osc.start(now);
      osc.stop(now + 0.25);
    } else if (type === 'victory') {
      [523.25, 659.25, 783.99, 1046.50].forEach((freq, idx) => {
        const o = ctx.createOscillator();
        const g = ctx.createGain();
        o.type = 'sine';
        o.frequency.setValueAtTime(freq, now + idx * 0.08);
        g.gain.setValueAtTime(0.12, now + idx * 0.08);
        g.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.25);
        o.connect(g);
        g.connect(ctx.destination);
        o.start(now + idx * 0.08);
        o.stop(now + idx * 0.08 + 0.25);
      });
    } else if (type === 'click') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(650, now);
      gain.gain.setValueAtTime(0.03, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
      osc.start(now);
      osc.stop(now + 0.04);
    }
  } catch (e) {}
}

function toggleAudio() {
  state.audioEnabled = !state.audioEnabled;
  const audioIcon = document.getElementById('audioIcon');
  if (audioIcon) audioIcon.textContent = state.audioEnabled ? '🔊' : '🔇';
  const headerBtn = document.getElementById('headerAudioBtn');
  if (headerBtn) headerBtn.title = state.audioEnabled ? "Ovoz: Yoqilgan / Sound ON" : "Ovoz: O'chirilgan / Sound OFF";
}

// ----------------- NAVIGATION HISTORY & BACK BUTTON -----------------
const navigationHistory = [];

// ----------------- STRICT ROLE-BASED ROUTER & ACCESS GUARD -----------------
const TEACHER_ALLOWED_VIEWS = ['teacher', 'teacher-students', 'textbooks', 'profile', 'blitz'];
const STUDENT_ALLOWED_VIEWS = ['home', 'blitz', 'textbooks', 'battle', 'friends', 'profile'];

function enforceRoleGuard(targetView) {
  const user = state.currentUser;
  const role = user ? user.role : 'guest';

  // Guest users (not logged in): can only view home, textbooks, profile/auth
  if (!user) {
    if (targetView === 'teacher' || targetView === 'teacher-students' || targetView === 'friends' || targetView === 'battle') {
      openAuthModal();
      return null;
    }
    return targetView;
  }

  // TEACHER: strictly allowed teacher views only. NEVER leak into student home, battle, or friends!
  if (role === 'teacher') {
    if (!TEACHER_ALLOWED_VIEWS.includes(targetView)) {
      console.warn(`[RoleGuard] O'qituvchi o'quvchi bo'limiga ('${targetView}') o'ta olmaydi. O'qituvchi kabinetiga yo'naltirildi.`);
      return 'teacher';
    }
    return targetView;
  }

  // STUDENT: strictly allowed student views only. NEVER leak into teacher management portal!
  if (role === 'student') {
    if (!STUDENT_ALLOWED_VIEWS.includes(targetView)) {
      console.warn(`[RoleGuard] O'quvchi o'qituvchi boshqaruviga ('${targetView}') o'ta olmaydi. Asosiy sahifaga yo'naltirildi.`);
      return 'home';
    }
    return targetView;
  }

  // ADMIN: can access all views
  return targetView;
}

function goBackHistory() {
  playSound('click');
  // 1. If any modal is active, close it
  const activeModal = document.querySelector('.modal-backdrop.active');
  if (activeModal) {
    activeModal.classList.remove('active');
    return;
  }

  // 2. If chat modal open
  const chatModal = document.getElementById('friendChatModal');
  if (chatModal && chatModal.classList.contains('active')) {
    closeFriendChatModal();
    return;
  }

  // 3. Pop previous view from history stack and validate against role guard!
  while (navigationHistory.length > 0) {
    const prevView = navigationHistory.pop();
    const safeView = enforceRoleGuard(prevView);
    if (safeView && safeView !== state.currentView) {
      navigateTo(safeView, true);
      return;
    }
  }

  // Fallback to role's home view
  const homeView = (state.currentUser && state.currentUser.role === 'teacher') ? 'teacher' : 'home';
  navigateTo(homeView, true);
}

function updateBackBtnVisibility(currentView) {
  const backBtn = document.getElementById('appGlobalBackBtn');
  if (!backBtn) return;
  const homeView = (state.currentUser && state.currentUser.role === 'teacher') ? 'teacher' : 'home';
  if (currentView !== homeView || navigationHistory.length > 0) {
    backBtn.style.display = 'inline-flex';
  } else {
    backBtn.style.display = 'none';
  }
}

function handleBrandClick() {
  playSound('click');
  if (state.currentUser && state.currentUser.role === 'teacher') {
    navigateTo('teacher');
  } else {
    navigateTo('home');
  }
}

function handleHeaderProClick() {
  playSound('click');
  if (state.currentUser && state.currentUser.role === 'admin') {
    window.location.href = '/admin-portal.html';
  } else if (state.currentUser && state.currentUser.role === 'teacher') {
    alert("👨‍🏫 Siz o'qituvchisiz! O'qituvchi kabineti orqali sinflar, testlar va darsliklarni boshqarishingiz mumkin.");
  } else {
    openPaymentModal('student_pro');
  }
}

function updateBottomNavForRole(role) {
  const nav = document.getElementById('mainBottomNav');
  if (!nav) return;

  const tHome = (typeof t === 'function') ? t('nav_home', 'Asosiy') : 'Asosiy';
  const tLib = (typeof t === 'function') ? t('nav_library', 'Kutubxona') : 'Kutubxona';
  const tBattle = (typeof t === 'function') ? t('nav_battle', 'Batl') : 'Batl';
  const tFriends = (typeof t === 'function') ? t('nav_friends', 'Do\'stlar') : 'Do\'stlar';
  const tProfile = (typeof t === 'function') ? t('nav_profile', 'Profil') : 'Profil';
  const tDashboard = (typeof t === 'function') ? t('nav_dashboard', 'Kabinet') : 'Kabinet';
  const tNewSub = (typeof t === 'function') ? t('nav_new_subject', 'Yangi Fan') : 'Yangi Fan';
  const tQuiz = (typeof t === 'function') ? t('nav_quiz', 'Viktorina') : 'Viktorina';
  const tStudents = (typeof t === 'function') ? t('nav_students', 'O\'quvchilar') : 'O\'quvchilar';

  if (role === 'admin') {
    nav.innerHTML = `
      <button class="nav-tab active" id="navTab_home" onclick="navigateTo('home')">
        <span style="font-size:16px;">🏠</span>
        <span>${tHome}</span>
      </button>
      <button class="nav-tab" id="navTab_textbooks" onclick="navigateTo('textbooks')">
        <span style="font-size:16px;">📚</span>
        <span>${tLib}</span>
      </button>
      <button class="nav-tab" id="navTab_adminAddSub" onclick="openAddSubjectModal()">
        <span style="font-size:16px;">➕</span>
        <span>${tNewSub}</span>
      </button>
      <button class="nav-tab" id="navTab_teacher" onclick="navigateTo('teacher')">
        <span style="font-size:16px;">👨‍🏫</span>
        <span>${tDashboard}</span>
      </button>
      <button class="nav-tab" id="navTab_profile" onclick="navigateTo('profile')">
        <span style="font-size:16px;">👑</span>
        <span>Admin</span>
      </button>
    `;
  } else if (role === 'teacher') {
    nav.innerHTML = `
      <button class="nav-tab active" id="navTab_teacher" onclick="navigateTo('teacher')">
        <span style="font-size:16px;">👨‍🏫</span>
        <span>${tDashboard}</span>
      </button>
      <button class="nav-tab" id="navTab_textbooks" onclick="navigateTo('textbooks')">
        <span style="font-size:16px;">📚</span>
        <span>${tLib}</span>
      </button>
      <button class="nav-tab" id="navTab_teacherQuiz" onclick="openCreateQuizModal()">
        <span style="font-size:16px;">⚡</span>
        <span>${tQuiz}</span>
      </button>
      <button class="nav-tab" id="navTab_teacher-students" onclick="navigateTo('teacher-students')">
        <span style="font-size:16px;">👥</span>
        <span>${tStudents}</span>
      </button>
      <button class="nav-tab" id="navTab_profile" onclick="navigateTo('profile')">
        <span style="font-size:16px;">👤</span>
        <span>${tProfile}</span>
      </button>
    `;
  } else {
    nav.innerHTML = `
      <button class="nav-tab active" id="navTab_home" onclick="navigateTo('home')">
        <span style="font-size:16px;">🏠</span>
        <span>${tHome}</span>
      </button>
      <button class="nav-tab" id="navTab_textbooks" onclick="navigateTo('textbooks')">
        <span style="font-size:16px;">📚</span>
        <span>${tLib}</span>
      </button>
      <button class="nav-tab" id="navTab_battle" onclick="navigateTo('battle')">
        <span style="font-size:16px;">⚔️</span>
        <span>${tBattle}</span>
      </button>
      <button class="nav-tab" id="navTab_friends" onclick="navigateTo('friends')">
        <span style="font-size:16px;">👥</span>
        <span>${tFriends}</span>
      </button>
      <button class="nav-tab" id="navTab_profile" onclick="navigateTo('profile')">
        <span style="font-size:16px;">👤</span>
        <span>${tProfile}</span>
      </button>
    `;
  }
}

// ----------------- NAVIGATION & STRICT ROLE ROUTING -----------------
function navigateTo(viewName, isBack = false) {
  playSound('click');

  // Enforce absolute role guard: prevents students from seeing teacher sections, and teachers from entering student home/battle
  const safeView = enforceRoleGuard(viewName);
  if (!safeView) return;
  viewName = safeView;

  if (!isBack && state.currentView && state.currentView !== viewName) {
    if (enforceRoleGuard(state.currentView) === state.currentView) {
      navigationHistory.push(state.currentView);
      if (navigationHistory.length > 20) navigationHistory.shift();
    }
  }

  state.currentView = viewName;

  document.querySelectorAll('.view-section').forEach(sec => sec.classList.remove('active'));
  const targetSec = document.getElementById(`view-${viewName}`);
  if (targetSec) targetSec.classList.add('active');

  // Bottom nav tab styling
  document.querySelectorAll('.bottom-nav .nav-tab').forEach(b => b.classList.remove('active'));
  const activeTab = document.getElementById(`navTab_${viewName}`);
  if (activeTab) activeTab.classList.add('active');

  updateBackBtnVisibility(viewName);

  if (viewName === 'teacher' && typeof loadTeacherPortalData === 'function') {
    loadTeacherPortalData();
  }
  if (viewName === 'teacher-students' && typeof loadTeacherAllStudents === 'function') {
    loadTeacherAllStudents();
  }
  if (viewName === 'textbooks' && typeof loadLibraryBooks === 'function') {
    loadLibraryBooks();
  }
  if (viewName === 'friends' && typeof loadMyFriendsList === 'function') {
    loadMyFriendsList();
  }
  if (viewName === 'profile') {
    applyTheme(document.documentElement.getAttribute('data-theme') || 'dark');
  }
  if (viewName === 'blitz') {
    if (typeof initBlitzView === 'function') initBlitzView();
  } else if (typeof blitzTickerInterval !== 'undefined' && blitzTickerInterval) {
    clearInterval(blitzTickerInterval);
    blitzTickerInterval = null;
  }
  if (viewName === 'home') {
    if (typeof updateHomeDailyLimitBadge === 'function') updateHomeDailyLimitBadge();
  }
}

function switchDeviceMode(mode) {
  // Deprecated: Layout is now fully universal & responsive automatically across all screen sizes
}

// ----------------- THEME MANAGEMENT (LIGHT / DARK) -----------------
function initTheme() {
  const savedTheme = localStorage.getItem('edubattle_theme') || 'dark';
  applyTheme(savedTheme);
}

function toggleTheme() {
  if (typeof playSound === 'function') playSound('click');
  const current = document.documentElement.getAttribute('data-theme') || 'dark';
  const newTheme = current === 'dark' ? 'light' : 'dark';
  applyTheme(newTheme);
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  try {
    localStorage.setItem('edubattle_theme', theme);
  } catch (e) {}

  // Update browser mobile header color
  const metaTheme = document.querySelector('meta[name="theme-color"]');
  if (metaTheme) {
    metaTheme.setAttribute('content', theme === 'dark' ? '#090a0f' : '#f4f6fa');
  }

  // Update header button icon & tooltip
  const iconEl = document.getElementById('themeIcon');
  if (iconEl) iconEl.textContent = theme === 'dark' ? '🌙' : '☀️';

  const btnEl = document.getElementById('headerThemeBtn');
  if (btnEl) {
    btnEl.title = theme === 'dark' 
      ? "Rejim: Qorong'u (Yorug' rejimga o'tish)" 
      : "Rejim: Yorug' (Qorong'u rejimga o'tish)";
  }

  // Update profile settings card
  const pIconEl = document.getElementById('profileThemeIcon');
  if (pIconEl) pIconEl.textContent = theme === 'dark' ? '🌙' : '☀️';

  const pSubEl = document.getElementById('profileThemeSubtitle');
  if (pSubEl) {
    if (theme === 'dark') {
      pSubEl.textContent = typeof t === 'function' ? t('theme_dark', "Qorong'u rejim (Dark Mode)") : "Qorong'u rejim (Dark Mode)";
    } else {
      pSubEl.textContent = typeof t === 'function' ? t('theme_light', "Yorug' rejim (Light Mode)") : "Yorug' rejim (Light Mode)";
    }
  }

  const pBtnEl = document.getElementById('profileThemeToggleBtn');
  if (pBtnEl) {
    pBtnEl.textContent = theme === 'dark' ? "Yorug' rejimga o'tish ☀️" : "Qorong'u rejimga o'tish 🌙";
  }
}

// Ensure theme elements update immediately on script load
if (typeof window !== 'undefined') {
  initTheme();
}

// ----------------- APP INIT & PERSISTED SESSION (TOKEN-BASED) -----------------
async function initApp() {
  try {
    initTheme();
    loadTariffs();

    // 0. Telegram Mini App (Web App) initialization
    if (window.Telegram && window.Telegram.WebApp) {
      try {
        const tg = window.Telegram.WebApp;
        tg.ready();
        try { tg.expand(); } catch (e) {}
        try { if (typeof tg.enableClosingConfirmation === 'function') tg.enableClosingConfirmation(); } catch (e) {}
        try { if (typeof tg.setHeaderColor === 'function') tg.setHeaderColor('#090a0f'); } catch (e) {}
        try { if (typeof tg.setBackgroundColor === 'function') tg.setBackgroundColor('#090a0f'); } catch (e) {}
        document.body.classList.add('telegram-webapp-mode');

        const urlParams = new URLSearchParams(window.location.search);
        const urlRole = urlParams.get('role') || 'student';
        const tgUser = tg.initDataUnsafe?.user;
        if (tgUser) {
          let loggedIn = false;
          try {
            const tgLoginRes = await fetch('/api/auth/telegram-webapp-login', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                id: tgUser.id,
                first_name: tgUser.first_name,
                last_name: tgUser.last_name,
                username: tgUser.username,
                language_code: tgUser.language_code,
                role: urlRole
              })
            });
            if (tgLoginRes.ok) {
              const authData = await tgLoginRes.json();
              if (authData.user) {
                state.currentUser = authData.user;
                localStorage.setItem('edubattle_user', JSON.stringify(authData.user));
                if (authData.token) localStorage.setItem('edubattle_token', authData.token);
                loggedIn = true;
              }
            }
          } catch (authErr) {
            console.warn("Telegram webapp auth backend offline:", authErr);
          }
          if (!loggedIn && !localStorage.getItem('edubattle_user')) {
            const tgFullName = [tgUser.first_name, tgUser.last_name].filter(Boolean).join(' ') || tgUser.username || "Telegram Foydalanuvchi";
            const generatedEB = "EB-" + Math.floor(10000 + Math.random() * 90000);
            const localUser = {
              id: tgUser.id,
              username: generatedEB,
              full_name: tgFullName,
              role: urlRole,
              school_lyceum: 'EduBattle Online Maktab',
              grade: urlRole === 'teacher' ? 'Oliy toifa' : '9-sinf',
              xp: 0,
              coins: 0,
              streak: 1,
              is_pro: urlRole === 'teacher' ? 1 : 0,
              grade_score: 0
            };
            state.currentUser = localUser;
            localStorage.setItem('edubattle_user', JSON.stringify(localUser));
          }
        }
      } catch (tgErr) {
        console.warn("Telegram WebApp initialization error:", tgErr);
      }
    }

    // 1. Fetch subjects (with offline & CDN fallback)
    try {
      const subRes = await fetch('/api/subjects');
      if (subRes.ok) {
        state.subjects = await subRes.json();
      }
    } catch (e) {
      console.warn("Could not fetch subjects from API:", e);
    }
    if (!state.subjects || state.subjects.length === 0) {
      state.subjects = [
        { id: 1, name: "Matematika & Algebra", icon: "📐", category: "aniq" },
        { id: 2, name: "Fizika", icon: "⚡", category: "aniq" },
        { id: 3, name: "Kimyo", icon: "🧪", category: "tabiiy" },
        { id: 4, name: "Biologiya", icon: "🧬", category: "tabiiy" },
        { id: 5, name: "Informatika & IT", icon: "💻", category: "aniq" },
        { id: 6, name: "Ona tili va Adabiyot", icon: "📖", category: "ijtimoiy" },
        { id: 7, name: "Ingliz tili", icon: "🇬🇧", category: "ijtimoiy" },
        { id: 8, name: "Tarix", icon: "🏛️", category: "ijtimoiy" },
        { id: 9, name: "Huquq", icon: "⚖️", category: "ijtimoiy" }
      ];
    }
    renderHomeSubjects();
    populateSubjectSelects();

    // 2. Check saved user session token
    const token = localStorage.getItem('edubattle_token');
    const saved = localStorage.getItem('edubattle_user');
    
    if (token) {
      try {
        const meRes = await fetch(`/api/auth/me?token=${encodeURIComponent(token)}`);
        if (meRes.ok) {
          const meData = await meRes.json();
          state.currentUser = meData.user;
          localStorage.setItem('edubattle_user', JSON.stringify(meData.user));
        } else {
          localStorage.removeItem('edubattle_token');
          state.currentUser = null;
        }
      } catch (e) {
        state.currentUser = saved ? JSON.parse(saved) : null;
      }
    } else if (saved) {
      try {
        const u = JSON.parse(saved);
        const res = await fetch(`/api/users/${u.id}`);
        if (res.ok) state.currentUser = await res.json();
        else state.currentUser = u;
      } catch (e) {
        state.currentUser = null;
      }
    }

    if (!state.currentUser) {
      if (window.Telegram && window.Telegram.WebApp) {
        const localUser = {
          id: Math.floor(Math.random() * 899999) + 100000,
          username: "EB-" + Math.floor(10000 + Math.random() * 90000),
          full_name: "EduBattle O'quvchi",
          role: 'student',
          school_lyceum: 'EduBattle Online Maktab',
          grade: '9-sinf',
          xp: 0,
          coins: 0,
          streak: 1,
          is_pro: 0,
          grade_score: 0
        };
        state.currentUser = localUser;
        localStorage.setItem('edubattle_user', JSON.stringify(localUser));
        updateHeaderAndProfileUI();
        updateBottomNavForRole('student');
        navigateTo('home', true);
      } else {
        openAuthModal();
      }
    } else {
      if (state.currentUser.lang && typeof setAppLanguage === 'function') {
        setAppLanguage(state.currentUser.lang);
      }
      updateHeaderAndProfileUI();
      updateBottomNavForRole(state.currentUser.role);
      
      // If user registered as teacher, direct them properly to their teacher cabinet!
      if (state.currentUser.role === 'teacher') {
        navigateTo('teacher', true);
      } else {
        navigateTo('home', true);
      }
    }

    // 3. Textbooks & leaderboard
    await loadTextbooks();
    await loadHomeLeaderboard();

    // 4. Start automatic real-time sync
    startRealTimeSync();
  } catch (err) {
    console.error(err);
  }
}

// ----------------- ADMIN FAN QO'SHISH (ADD SUBJECT) -----------------
function openAddSubjectModal() {
  playSound('click');
  if (!state.currentUser || state.currentUser.role !== 'admin') {
    alert("Yangi fan qo'shish faqat administrator uchun ruxsat etilgan!");
    return;
  }
  const nameInput = document.getElementById('newSubjectName');
  if (nameInput) nameInput.value = '';
  const descInput = document.getElementById('newSubjectDesc');
  if (descInput) descInput.value = '';
  document.getElementById('addSubjectModal').classList.add('active');
}

async function submitAddNewSubject() {
  playSound('click');
  if (!state.currentUser || state.currentUser.role !== 'admin') {
    alert("Faqat administrator yangi fan qo'shishi mumkin!");
    return;
  }
  const name = (document.getElementById('newSubjectName').value || '').trim();
  const icon = (document.getElementById('newSubjectIcon').value || '📚').trim();
  const category = (document.getElementById('newSubjectCategory').value || 'Aniqlik').trim();
  const desc = (document.getElementById('newSubjectDesc').value || '').trim();

  if (!name) {
    alert("Iltimos, fan nomini kiriting!");
    return;
  }

  try {
    const res = await fetch('/api/admin/add-subject', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        admin_id: state.currentUser.id,
        name: name,
        icon: icon,
        category: category,
        description: desc
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('victory');
      alert(`🎉 Yangi fan ("${name}") muvaffaqiyatli qo'shildi va darhol barcha o'quvchi va ustozlarga taqdim etildi!`);
      closeModal('addSubjectModal');
      await refreshRealTimeData(true);
    } else {
      playSound('wrong');
      alert(data.detail || "Fanni qo'shishda xatolik yuz berdi!");
    }
  } catch (err) {
    alert("Serverga ulanishda xatolik!");
  }
}

// ----------------- REAL-TIME REVISION SYNC ENGINE -----------------
let lastKnownRevision = null;
let realTimeSyncInterval = null;

async function checkRealTimeSync() {
  try {
    const res = await fetch('/api/sync/state');
    if (!res.ok) return;
    const data = await res.json();
    if (lastKnownRevision === null) {
      lastKnownRevision = data.revision;
      return;
    }
    if (data.revision > lastKnownRevision) {
      lastKnownRevision = data.revision;
      await refreshRealTimeData(false);
    }
  } catch (e) {
    // silently ignore network blip
  }
}

async function refreshRealTimeData(force = false) {
  try {
    // 1. Refresh subjects list
    const subRes = await fetch('/api/subjects');
    if (subRes.ok) {
      state.subjects = await subRes.json();
      renderHomeSubjects();
      populateSubjectSelects();
    }

    // 2. Refresh library books
    if (typeof loadLibraryBooks === 'function') {
      await loadLibraryBooks();
    }

    // 3. Refresh user-specific views
    if (state.currentUser) {
      if (state.currentUser.role === 'teacher') {
        if (typeof loadTeacherGroups === 'function') loadTeacherGroups();
        if (typeof loadTeacherQuizzes === 'function') loadTeacherQuizzes();
        if (typeof loadTeacherStudentsList === 'function') loadTeacherStudentsList();
      } else if (state.currentUser.role === 'student') {
        if (typeof loadStudentJoinedGroups === 'function') loadStudentJoinedGroups();
        // Update student score/xp silently
        fetch(`/api/users/${state.currentUser.id}`)
          .then(r => r.json())
          .then(u => {
            if (u && !u.detail && u.role === 'student') {
              state.currentUser = u;
              localStorage.setItem('edubattle_user', JSON.stringify(u));
              updateHeaderAndProfileUI();
            }
          }).catch(() => {});
      }
    }

    // 4. Refresh leaderboard
    if (typeof loadHomeLeaderboard === 'function') {
      loadHomeLeaderboard();
    }
  } catch (err) {
    console.error("RealTimeData refresh error:", err);
  }
}

function startRealTimeSync() {
  if (realTimeSyncInterval) clearInterval(realTimeSyncInterval);
  checkRealTimeSync();
  realTimeSyncInterval = setInterval(checkRealTimeSync, 2500);
}

// ----------------- AUTHENTICATION -----------------
function openAuthModal() {
  const el = document.getElementById('authModal');
  if (el) el.classList.add('active');
  switchAuthTab('login');
}

function switchAuthTab(tab) {
  playSound('click');
  const btnLogin = document.getElementById('tabBtnLogin');
  const btnRegister = document.getElementById('tabBtnRegister');
  const btnForgot = document.getElementById('tabBtnForgot');
  const formLogin = document.getElementById('authLoginForm');
  const formRegister = document.getElementById('authRegisterForm');
  const formForgot = document.getElementById('authForgotForm');

  if (btnLogin) btnLogin.classList.remove('active');
  if (btnRegister) btnRegister.classList.remove('active');
  if (btnForgot) btnForgot.classList.remove('active');

  if (formLogin) formLogin.style.display = 'none';
  if (formRegister) formRegister.style.display = 'none';
  if (formForgot) formForgot.style.display = 'none';

  if (tab === 'login') {
    if (btnLogin) btnLogin.classList.add('active');
    if (formLogin) formLogin.style.display = 'block';
  } else if (tab === 'register') {
    if (btnRegister) btnRegister.classList.add('active');
    if (formRegister) formRegister.style.display = 'block';
    const userField = document.getElementById('regUsername');
    if (userField && !userField.value) {
      generateNewAutoLogin();
    }
  } else if (tab === 'forgot') {
    if (btnForgot) btnForgot.classList.add('active');
    if (formForgot) formForgot.style.display = 'block';
  }
}

async function generateNewAutoLogin() {
  const userField = document.getElementById('regUsername');
  if (!userField) return;
  userField.value = "Generatsiya...";
  try {
    const res = await fetch('/api/auth/generate-login');
    const data = await res.json();
    if (data && data.login) {
      userField.value = data.login;
    }
  } catch(e) {
    userField.value = "EB-" + Math.floor(10000 + Math.random() * 90000);
  }
}

async function requestTelegramOtp(purpose) {
  playSound('click');
  let inputVal = '';
  let statusEl = null;
  let groupEl = null;

  if (purpose === 'register') {
    inputVal = (document.getElementById('regTelegramUser')?.value || '').trim();
    statusEl = document.getElementById('regOtpStatusMsg');
    groupEl = document.getElementById('regOtpInputGroup');
  } else {
    inputVal = (document.getElementById('forgotUsername')?.value || '').trim();
    statusEl = document.getElementById('forgotOtpStatusMsg');
    groupEl = document.getElementById('forgotPasswordFields');
  }

  if (statusEl) {
    statusEl.innerHTML = '<span style="color:#00f0ff;">⏳ Telegram kod so\'ralmoqda...</span>';
  }

  try {
    const res = await fetch('/api/auth/telegram-otp/request', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        telegram: inputVal,
        login: inputVal,
        purpose: purpose,
        website_url: ''
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('correct');
      if (groupEl) groupEl.style.display = 'block';
      if (statusEl) {
        if (data.sent_direct) {
          statusEl.innerHTML = '<span style="color:var(--accent-green); font-weight:700;">✅ Kod Telegram akkauntingizga yuborildi!</span>';
        } else {
          statusEl.innerHTML = `<span style="color:#24A1DE;">✈️ <a href="${data.bot_url}" target="_blank" style="color:#00f0ff; font-weight:800; text-decoration:underline;">@${data.bot_username}</a> ga kiring va <b>"🔑 Tasdiqlash kodi"</b> tugmasini bosing!</span>`;
        }
      }
    } else {
      playSound('wrong');
      if (statusEl) {
        statusEl.innerHTML = `<span style="color:var(--accent-red);">${data.detail || data.message || "Xatolik yuz berdi"}</span>`;
      }
    }
  } catch(e) {
    if (statusEl) {
      statusEl.innerHTML = '<span style="color:var(--accent-red);">Server bilan aloqa uzildi.</span>';
    }
  }
}

async function submitResetPassword() {
  playSound('click');
  const login = (document.getElementById('forgotUsername')?.value || '').trim();
  const code = (document.getElementById('forgotOtpCode')?.value || '').trim();
  const newPassword = (document.getElementById('forgotNewPassword')?.value || '').trim();
  const honeypot = (document.getElementById('forgotWebsiteUrl')?.value || '').trim();

  if (!login || !code || !newPassword) {
    alert("Iltimos, barcha maydonlarni to'ldiring!");
    return;
  }

  if (newPassword.length < 4) {
    alert("Yangi parol kamida 4 ta belgidan iborat bo'lishi kerak!");
    return;
  }

  try {
    const res = await fetch('/api/auth/reset-password', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        login: login,
        code: code,
        new_password: newPassword,
        website_url: honeypot
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('victory');
      alert("🎉 Parolingiz muvaffaqiyatli yangilandi!\nEndi yangi parolingiz bilan tizimga kiring.");
      switchAuthTab('login');
      const loginUserEl = document.getElementById('loginUsername');
      if (loginUserEl) loginUserEl.value = login;
      const loginPassEl = document.getElementById('loginPassword');
      if (loginPassEl) loginPassEl.value = newPassword;
    } else {
      playSound('wrong');
      alert(data.detail || "Tiklash kodi noto'g'ri yoki eskirgan!");
    }
  } catch(e) {
    alert("Serverga ulanishda xatolik!");
  }
}

let selectedRegRole = 'student';
function selectRegRole(role) {
  playSound('click');
  selectedRegRole = role;
  const choiceStudent = document.getElementById('roleChoiceStudent');
  const choiceTeacher = document.getElementById('roleChoiceTeacher');
  const studentExtra = document.getElementById('studentExtraFields');

  if (role === 'student') {
    choiceStudent.classList.add('active');
    choiceTeacher.classList.remove('active');
    studentExtra.style.display = 'block';
  } else {
    choiceTeacher.classList.add('active');
    choiceStudent.classList.remove('active');
    studentExtra.style.display = 'none';
  }
}

async function submitLogin() {
  const username = (document.getElementById('loginUsername').value || '').trim();
  const password = (document.getElementById('loginPassword').value || '').trim();
  const honeypot = (document.getElementById('loginWebsiteUrl')?.value || '').trim();

  if (!username) {
    alert("Iltimos, foydalanuvchi nomini kiriting!");
    return;
  }

  try {
    const res = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password, website_url: honeypot })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('correct');
      navigationHistory.length = 0;
      state.currentUser = data.user;
      if (data.token) localStorage.setItem('edubattle_token', data.token);
      localStorage.setItem('edubattle_user', JSON.stringify(data.user));
      if (data.user && data.user.lang && typeof setAppLanguage === 'function') {
        setAppLanguage(data.user.lang);
      }
      closeModal('authModal');
      updateHeaderAndProfileUI();
      updateBottomNavForRole(data.user.role);

      if (data.user.role === 'teacher') {
        navigateTo('teacher', true);
      } else {
        navigateTo('home', true);
      }
    } else {
      playSound('wrong');
      alert(data.detail || "Login yoki parol noto'g'ri!");
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik!");
  }
}

async function submitRegister() {
  const fullName = (document.getElementById('regFullName').value || '').trim();
  const username = (document.getElementById('regUsername').value || '').trim();
  const password = (document.getElementById('regPassword').value || '').trim();
  const school = (document.getElementById('regSchool').value || '').trim();
  const grade = document.getElementById('regGrade').value;
  const verificationCode = (document.getElementById('regOtpCode')?.value || '').trim();
  const telegram = (document.getElementById('regTelegramUser')?.value || '').trim();
  const honeypot = (document.getElementById('regWebsiteUrl')?.value || '').trim();

  if (!fullName) {
    alert("Iltimos, ism va familiyangizni kiriting!");
    return;
  }

  if (password.length < 4) {
    alert("Parol kamida 4 ta belgidan iborat bo'lishi kerak!");
    return;
  }

  try {
    const res = await fetch('/api/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        full_name: fullName,
        username: username,
        password: password,
        role: selectedRegRole,
        school_lyceum: school || 'Maktab / Litsey',
        grade: selectedRegRole === 'student' ? grade : 'Oliy toifa',
        verification_code: verificationCode,
        telegram: telegram,
        website_url: honeypot
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('victory');
      navigationHistory.length = 0;
      const assignedLogin = data.auto_login || username;
      alert(`🎉 TABRIKLAYMIZ!\n\nSizning shaxsiy Tizim ID (Loginingiz): ${assignedLogin}\nParolingiz: ${password}\n\nUshbu ID va parolni eslab qoling, tizimga kirish uchun kerak bo'ladi!`);
      state.currentUser = data.user;
      if (data.token) localStorage.setItem('edubattle_token', data.token);
      localStorage.setItem('edubattle_user', JSON.stringify(data.user));
      if (data.user && data.user.lang && typeof setAppLanguage === 'function') {
        setAppLanguage(data.user.lang);
      }
      closeModal('authModal');
      updateHeaderAndProfileUI();
      updateBottomNavForRole(data.user.role);

      if (data.user.role === 'teacher') navigateTo('teacher', true);
      else navigateTo('home', true);
    } else {
      playSound('wrong');
      alert(data.detail || "Ro'yxatdan o'tishda xatolik yuz berdi!");
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik!");
  }
}

function logoutCurrentUser() {
  if (confirm("Haqiqatan ham profilingizdan chiqmoqchimisiz?")) {
    playSound('click');
    localStorage.removeItem('edubattle_token');
    localStorage.removeItem('edubattle_user');
    state.currentUser = null;
    navigationHistory.length = 0;
    state.currentView = 'home';
    document.querySelectorAll('.modal-backdrop').forEach(m => m.classList.remove('active'));
    updateBottomNavForRole('student');
    navigateTo('home', true);
    openAuthModal();
  }
}

function updateHeaderAndProfileUI() {
  const u = state.currentUser;
  if (!u) return;

  const isTeacher = (u.role === 'teacher');
  const isAdmin = (u.role === 'admin');
  let roleText = (typeof t === 'function') ? t('role_student', "O'quvchi") : "O'quvchi";
  if (isAdmin) roleText = (typeof t === 'function') ? t('role_admin', "Administrator") : "Administrator";
  else if (isTeacher) roleText = (typeof t === 'function') ? t('role_teacher', "O'qituvchi") : "O'qituvchi";

  // Header UI
  document.getElementById('headerRoleBadge').textContent = roleText;
  document.getElementById('headerUserAvatar').textContent = isAdmin ? '👑' : (isTeacher ? '👨‍🏫' : '👨‍🎓');
  if (isAdmin) {
    document.getElementById('headerProPill').textContent = '⚡ Admin Boshqaruv';
  } else if (isTeacher) {
    document.getElementById('headerProPill').textContent = '👨‍🏫 ' + ((typeof t === 'function') ? t('nav_dashboard', "Kabinet") : "Kabinet");
  } else {
    document.getElementById('headerProPill').textContent = u.is_pro ? '💎 PRO' : `💎 PRO: ${(state.proPrice || 29000).toLocaleString()} so'm`;
  }

  // Home Screen
  const greetingWord = (typeof t === 'function') ? t('greeting_default', "Salom") : "Salom";
  document.getElementById('homeGreetingName').textContent = `${greetingWord}, ${u.full_name.split(' ')[0]}`;
  document.getElementById('homeGreetingMeta').textContent = `${u.school_lyceum || 'Maktab/Litsey'} • ${u.grade || ''}`;
  document.getElementById('homeUserTag').textContent = roleText;
  const homeCoinsEl = document.getElementById('homeCoinsText');
  if (homeCoinsEl) homeCoinsEl.textContent = (u.coins || 0).toLocaleString();

  // Profile Screen
  document.getElementById('profileFullName').textContent = u.full_name;
  document.getElementById('profileSchoolGrade').textContent = `${u.school_lyceum || ''} • ${u.grade || ''}`;
  document.getElementById('profileBigAvatar').textContent = isAdmin ? '👑' : (isTeacher ? '👨‍🏫' : '👨‍🎓');

  // Display Official User EB- ID in Profile (Always guaranteed EB-XXXXX format)
  let userEBId = (u.username && u.username.startsWith('EB-')) ? u.username : (u.eb_id && u.eb_id.startsWith('EB-') ? u.eb_id : null);
  if (!userEBId) {
    const rawNum = u.id ? Math.abs(parseInt(u.id, 10)) : 0;
    const ebNum = (rawNum && !isNaN(rawNum)) ? ((rawNum * 1337 + 12345) % 90000 + 10000) : Math.floor(10000 + Math.random() * 90000);
    userEBId = 'EB-' + ebNum;
    u.username = userEBId;
    u.eb_id = userEBId;
    try { localStorage.setItem('edubattle_user', JSON.stringify(u)); } catch(e){}
  }
  const idEl = document.getElementById('profileUserIdDisplay');
  if (idEl) idEl.textContent = userEBId;
  const loginEl = document.getElementById('profileUserLogin');
  if (loginEl) loginEl.textContent = userEBId;
  const teacherIdPill = document.getElementById('teacherIdPill');
  if (teacherIdPill) teacherIdPill.textContent = `ID: ${userEBId}`;
  const payModalUserId = document.getElementById('payModalUserId');
  if (payModalUserId) payModalUserId.textContent = userEBId;

  // Toggle Profile Stats & Teacher Switcher: TEACHERS & ADMINS DO NOT HAVE STUDENT GRADES!
  const studentStatsRow = document.getElementById('studentProfileStatsRow');
  const teacherStatsRow = document.getElementById('teacherProfileStatsRow');
  const studentDiaryBox = document.getElementById('profileStudentDiaryBox');
  const teacherDirectAccessBox = document.getElementById('teacherDirectAccessBox');
  const teacherSwitchPromptBox = document.getElementById('teacherSwitchPromptBox');
  if (isTeacher || isAdmin) {
    if (teacherDirectAccessBox) teacherDirectAccessBox.style.display = 'block';
    if (teacherSwitchPromptBox) teacherSwitchPromptBox.style.display = 'none';
  } else {
    if (teacherDirectAccessBox) teacherDirectAccessBox.style.display = 'none';
    if (teacherSwitchPromptBox) teacherSwitchPromptBox.style.display = 'block';
  }

  if (isTeacher || isAdmin) {
    if (studentStatsRow) studentStatsRow.style.display = 'none';
    if (teacherStatsRow) teacherStatsRow.style.display = 'flex';
  } else {
    if (studentStatsRow) studentStatsRow.style.display = 'flex';
    if (teacherStatsRow) teacherStatsRow.style.display = 'none';

    const streakEl = document.getElementById('profileStreak');
    if (streakEl) streakEl.textContent = `${u.streak || 1} kun`;

    const profileCoinsEl = document.getElementById('profileCoins');
    if (profileCoinsEl) profileCoinsEl.textContent = `${(u.coins || 0).toLocaleString()} 🪙`;
  }

  // Pro Plan vs Teacher Free Perks Card
  const proPromoCard = document.getElementById('proPromotionCard');
  if (proPromoCard) proPromoCard.style.display = (isTeacher || isAdmin) ? 'none' : 'block';

  const teacherPerksCard = document.getElementById('teacherFreePerksCard');
  if (teacherPerksCard) teacherPerksCard.style.display = isTeacher ? 'block' : 'none';

  // Kutubxona teacher & admin buttons
  const teacherSubjectToggle = document.getElementById('btnTeacherSubjectToggle');
  if (teacherSubjectToggle) teacherSubjectToggle.style.display = (isTeacher || isAdmin) ? 'inline-block' : 'none';

  const uploadBookBtn = document.getElementById('btnUploadBookKutubxona');
  if (uploadBookBtn) uploadBookBtn.style.display = (isTeacher || isAdmin) ? 'inline-block' : 'none';

  // Admin Add Subject buttons
  const homeAddSubjectBtn = document.getElementById('btnHomeAddSubject');
  if (homeAddSubjectBtn) homeAddSubjectBtn.style.display = isAdmin ? 'inline-block' : 'none';

  const adminAddSubjectBtn = document.getElementById('btnAdminAddSubject');
  if (adminAddSubjectBtn) adminAddSubjectBtn.style.display = isAdmin ? 'inline-block' : 'none';

  // Hide/Show Student group join box
  const joinBox = document.getElementById('studentJoinGroupBox');
  if (joinBox) joinBox.style.display = (isTeacher || isAdmin) ? 'none' : 'block';

  const homeGroupBox = document.getElementById('homeGroupJoinCard');
  if (homeGroupBox) homeGroupBox.style.display = (isTeacher || isAdmin) ? 'none' : 'block';

  const teacherAccessBox = document.getElementById('teacherDirectAccessBox');
  if (teacherAccessBox) teacherAccessBox.style.display = (isTeacher || isAdmin) ? 'block' : 'none';

  if (!isTeacher && !isAdmin) {
    loadStudentJoinedGroups();
  }
}

// ----------------- SUBJECTS & TOPICS / TESTS -----------------
function renderHomeSubjects() {
  const container = document.getElementById('homeSubjectsGrid');
  if (!container) return;

  container.innerHTML = state.subjects.map(s => {
    const safeName = (s.name || '').replace(/'/g, "\\'");
    return `
      <div class="subject-tile" onclick="openSubjectTestsModal(${s.id}, '${safeName}', '${s.icon}')">
        <div class="subject-tile-header">
          <span class="subject-tile-icon">${s.icon}</span>
          <span class="tag tag-subtle">Mavzular ➔</span>
        </div>
        <div>
          <div class="subject-tile-title">${s.name}</div>
          <div class="subject-tile-desc">${s.category === 'aniq' ? 'Aniq fanlar' : 'Ijtimoiy & tabiiy'}</div>
        </div>
      </div>
    `;
  }).join('');
}

let activeSubjectQuizzes = [];

async function openSubjectTestsModal(subjectId, subjectName, subjectIcon) {
  playSound('click');
  state.activeSubject = { id: subjectId, name: subjectName, icon: subjectIcon };
  
  const titleEl = document.getElementById('subjModalTitle');
  const iconEl = document.getElementById('subjModalIcon');
  if (titleEl) titleEl.textContent = subjectName;
  if (iconEl) iconEl.textContent = subjectIcon;

  openModal('subjectTestsModal');
  await loadSubjectQuizzes(subjectId);
}

async function loadSubjectQuizzes(subjectId) {
  const listEl = document.getElementById('subjectTestsList');
  const badgeEl = document.getElementById('subjTestsCountBadge');
  if (listEl) {
    listEl.innerHTML = `
      <div style="text-align:center; padding:30px; color:var(--text-muted);">
        <div class="spinner" style="margin:0 auto 10px;"></div>
        Yuklanmoqda...
      </div>`;
  }

  try {
    const res = await fetch(`/api/subject-quizzes/${subjectId}`);
    if (!res.ok) throw new Error("Yuklab bo'lmadi");
    const quizzes = await res.json();
    activeSubjectQuizzes = quizzes || [];
    if (badgeEl) badgeEl.textContent = `Mavjud testlar: ${activeSubjectQuizzes.length} ta`;
    renderSubjectTestsList(activeSubjectQuizzes);
  } catch (err) {
    console.error(err);
    if (listEl) {
      listEl.innerHTML = `
        <div style="text-align:center; padding:20px; color:var(--accent-red);">
          ⚠️ Testlarni yuklashda xatolik yuz berdi.
        </div>`;
    }
  }
}

function renderSubjectTestsList(quizzes) {
  const listEl = document.getElementById('subjectTestsList');
  if (!listEl) return;

  if (!quizzes || quizzes.length === 0) {
    listEl.innerHTML = `
      <div style="text-align:center; padding:36px 16px; background:rgba(255,255,255,0.02); border-radius:12px; border:1px dashed rgba(255,255,255,0.1);">
        <span style="font-size:36px; display:block; margin-bottom:8px;">📝</span>
        <h4 style="font-size:14px; font-weight:800; color:var(--text-primary); margin-bottom:4px;">Ushbu fanga hali test kiritilmagan</h4>
        <p style="font-size:12px; color:var(--text-muted); margin-bottom:14px;">
          "Yangi Test / Mavzu Qo'shish" tugmasi orqali o'zingiz istagan mavzu va testlarni kiriting!
        </p>
        <button class="btn btn-green btn-sm" onclick="openCreateSubjectQuizModal()" style="font-weight:700;">
          ➕ Birinchi Testni Qo'shish
        </button>
      </div>`;
    return;
  }

  listEl.innerHTML = quizzes.map(q => `
    <div class="minimal-card" style="padding:12px 14px; margin-bottom:0; display:flex; justify-content:space-between; align-items:center; gap:10px;">
      <div style="flex:1; min-width:0;">
        <div style="display:flex; align-items:center; gap:6px; margin-bottom:4px; flex-wrap:wrap;">
          <span style="font-size:11px; font-weight:800; color:var(--accent-green); background:rgba(16,185,129,0.1); padding:2px 6px; border-radius:4px;">
            ${q.grade || 'Barchasi'}
          </span>
          <span style="font-size:11px; color:var(--text-muted);">⏱ ${Math.round((q.time_limit_sec || 600) / 60)} daq</span>
          <span style="font-size:11px; color:var(--text-muted);">❓ ${q.question_count || 0} ta savol</span>
        </div>
        <h4 style="font-size:13px; font-weight:800; color:var(--text-primary); margin:0; word-break:break-word;">
          ${q.title}
        </h4>
        ${q.description ? `<p style="font-size:11px; color:var(--text-muted); margin:3px 0 0; text-overflow:ellipsis; overflow:hidden; white-space:nowrap;">${q.description}</p>` : ''}
      </div>
      <div style="display:flex; align-items:center; gap:6px;">
        <button class="btn btn-green btn-sm" onclick="startSelectedSubjectQuiz(${q.id})" style="font-weight:800; font-size:11px; padding:6px 12px; white-space:nowrap;">
          🚀 Boshlash
        </button>
        <button class="btn btn-outline btn-sm" onclick="deleteSubjectQuiz(${q.id}, event)" style="padding:6px 8px; color:var(--accent-red); border-color:rgba(239,68,68,0.3);" title="O'chirish">
          🗑
        </button>
      </div>
    </div>
  `).join('');
}

function openCreateSubjectQuizModal() {
  playSound('click');
  const subj = state.activeSubject;
  if (!subj) return;

  document.getElementById('createQuizHeaderTitle').textContent = `${subj.icon} ${subj.name} — Yangi Test Yaratish`;
  document.getElementById('newQuizTitle').value = '';
  document.getElementById('newQuizGrade').value = 'Barchasi';
  document.getElementById('newQuizTimeLimit').value = '10';
  document.getElementById('newQuizDescription').value = '';

  const listEl = document.getElementById('quizQuestionsBuilderList');
  if (listEl) listEl.innerHTML = '';
  addQuestionItemToBuilder(); // Add first blank question
  openModal('createSubjectQuizModal');
}

function addQuestionItemToBuilder(qData = null) {
  const listEl = document.getElementById('quizQuestionsBuilderList');
  if (!listEl) return;

  const qIdx = listEl.children.length;
  const qNum = qIdx + 1;

  const qCard = document.createElement('div');
  qCard.className = 'minimal-card builder-question-card';
  qCard.style.padding = '12px';
  qCard.style.background = 'rgba(255,255,255,0.03)';
  qCard.style.border = '1px solid rgba(255,255,255,0.08)';

  qCard.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
      <span style="font-size:12px; font-weight:800; color:var(--accent-green);">${qNum}-Savol</span>
      <button type="button" class="btn btn-outline btn-sm" onclick="removeQuestionItemFromBuilder(this)" style="padding:2px 8px; font-size:11px; color:var(--accent-red); border-color:rgba(239,68,68,0.3);">
        🗑 O'chirish
      </button>
    </div>
    <div style="margin-bottom:8px;">
      <textarea class="input-field q-text" rows="2" placeholder="Savol matnini kiriting..." style="width:100%; font-size:12px; resize:vertical;">${qData ? qData.question_text || '' : ''}</textarea>
    </div>
    <div style="font-size:11px; font-weight:700; color:var(--text-muted); margin-bottom:4px;">Javob variantlari (To'g'ri javobni tanlang):</div>
    <div style="display:flex; flex-direction:column; gap:6px; margin-bottom:8px;">
      ${['A', 'B', 'C', 'D'].map((letter, optIdx) => `
        <div style="display:flex; align-items:center; gap:8px;">
          <label style="display:flex; align-items:center; gap:4px; font-weight:800; font-size:12px; color:var(--text-primary); cursor:pointer;">
            <input type="radio" name="correct_radio_${qNum}" value="${optIdx}" ${optIdx === (qData ? (qData.correct_index || 0) : 0) ? 'checked' : ''} style="cursor:pointer;" />
            ${letter})
          </label>
          <input type="text" class="input-field q-opt-${optIdx}" placeholder="${letter} varianti matni" value="${qData && qData.options && qData.options[optIdx] ? qData.options[optIdx] : ''}" style="flex:1; margin-bottom:0; font-size:12px; padding:6px 10px;" />
        </div>
      `).join('')}
    </div>
    <div>
      <input type="text" class="input-field q-expl" placeholder="Izoh / Tushuntirish (ixtiyoriy)" value="${qData ? qData.explanation || '' : ''}" style="margin-bottom:0; font-size:11px; padding:4px 8px; width:100%;" />
    </div>
  `;

  listEl.appendChild(qCard);
}

function removeQuestionItemFromBuilder(btn) {
  const card = btn.closest('.builder-question-card');
  if (card) card.remove();
}

async function saveSubjectQuizFromBuilder() {
  playSound('click');
  const subj = state.activeSubject;
  if (!subj) {
    alert("Fan tanlanmagan!");
    return;
  }

  const title = (document.getElementById('newQuizTitle').value || '').trim();
  const grade = document.getElementById('newQuizGrade').value || 'Barchasi';
  const timeLimitMins = parseInt(document.getElementById('newQuizTimeLimit').value || '10', 10);
  const description = (document.getElementById('newQuizDescription').value || '').trim();

  if (!title) {
    alert("Iltimos, test yoki mavzu nomini kiriting!");
    return;
  }

  const listEl = document.getElementById('quizQuestionsBuilderList');
  const cards = listEl.querySelectorAll('.builder-question-card');
  if (cards.length === 0) {
    alert("Iltimos, kamida 1 ta savol qo'shing!");
    return;
  }

  const questions = [];
  for (let i = 0; i < cards.length; i++) {
    const card = cards[i];
    const qText = (card.querySelector('.q-text').value || '').trim();
    if (!qText) {
      alert(`Iltimos, ${i + 1}-savol matnini kiriting!`);
      return;
    }

    const options = [
      (card.querySelector('.q-opt-0').value || '').trim(),
      (card.querySelector('.q-opt-1').value || '').trim(),
      (card.querySelector('.q-opt-2').value || '').trim(),
      (card.querySelector('.q-opt-3').value || '').trim()
    ].filter(Boolean);

    if (options.length < 2) {
      alert(`Iltimos, ${i + 1}-savol uchun kamida 2 ta variant kiriting!`);
      return;
    }

    const checkedRadio = card.querySelector(`input[name^="correct_radio_"]:checked`);
    const correctIdx = checkedRadio ? parseInt(checkedRadio.value, 10) : 0;
    const expl = (card.querySelector('.q-expl').value || '').trim();

    questions.push({
      question_text: qText,
      options: options,
      correct_index: correctIdx,
      explanation: expl
    });
  }

  try {
    const payload = {
      subject_id: subj.id,
      title: title,
      grade: grade,
      description: description,
      time_limit_sec: timeLimitMins * 60,
      questions: questions,
      author_id: state.currentUser ? state.currentUser.id : null
    };

    const res = await fetch('/api/subject-quizzes/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    if (!res.ok) {
      alert(data.detail || "Xatolik yuz berdi!");
      return;
    }

    alert("✅ Test muvaffaqiyatli saqlandi!");
    closeModal('createSubjectQuizModal');
    await loadSubjectQuizzes(subj.id);
  } catch (err) {
    console.error(err);
    alert("Tarmoq xatosi: testni saqlab bo'lmadi.");
  }
}

async function deleteSubjectQuiz(quizId, event) {
  if (event) event.stopPropagation();
  if (!confirm("Haqiqatan ham ushbu testni o'chirmoqchimisiz?")) return;

  try {
    const res = await fetch(`/api/subject-quizzes/${quizId}`, { method: 'DELETE' });
    if (res.ok) {
      if (state.activeSubject) {
        await loadSubjectQuizzes(state.activeSubject.id);
      }
    } else {
      alert("Testni o'chirib bo'lmadi.");
    }
  } catch (err) {
    console.error(err);
  }
}

async function startSelectedSubjectQuiz(quizId) {
  playSound('click');
  closeModal('subjectTestsModal');

  try {
    const res = await fetch(`/api/subject-quizzes/quiz/${quizId}`);
    if (!res.ok) {
      alert("Test savollari topilmadi!");
      return;
    }
    const quiz = await res.json();
    if (!quiz.questions || quiz.questions.length === 0) {
      alert("Ushbu testda hali savollar yo'q!");
      return;
    }

    startSubjectQuiz(quiz.subject_id, quiz.title, quiz.questions);
  } catch (err) {
    console.error(err);
  }
}

function openSubjectGradeSelector(subjectId, subjectName, subjectIcon) {
  openSubjectTestsModal(subjectId, subjectName, subjectIcon);
}

function selectGradeAndOpen(gradeName) {
  playSound('click');
  state.activeGrade = gradeName;
  closeModal('gradeSelectorModal');
  openSelectedGradeQuiz();
}

async function openSelectedGradeBookReader() {
  navigateTo('textbooks');
}

async function openSelectedGradeQuiz() {
  playSound('click');
  const subjectId = state.activeSubject ? state.activeSubject.id : null;
  const grade = state.activeGrade;
  const title = `${state.activeSubject ? state.activeSubject.name : 'Fan'} — ${grade}`;

  try {
    let url = `/api/questions?subject_id=${subjectId}&count=5`;
    if (grade) url += `&grade=${encodeURIComponent(grade)}`;
    const res = await fetch(url);
    const questions = await res.json();
    if (!questions || questions.length === 0) {
      alert(`⚠️ ${title} uchun hozircha testlar kiritilmagan.`);
      return;
    }

    startSubjectQuiz(subjectId, title, questions);
  } catch (e) {
    console.error(e);
  }
}

function startBattleForSelectedGrade() {
  playSound('click');
  const sel = document.getElementById('battleSubjectSelect');
  if (sel && state.activeSubject) sel.value = state.activeSubject.id;
  navigateTo('battle');
}

function openSubjectAllBooks() {
  playSound('click');
  closeModal('gradeSelectorModal');
  loadTextbooks(state.activeSubject.id, null);
  navigateTo('textbooks');
}

function populateSubjectSelects() {
  const optionsHtml = state.subjects.map(s => `<option value="${s.id}">${s.icon} ${s.name}</option>`).join('');
  ['battleSubjectSelect', 'newGroupSubject', 'newQuizSubjectSelect', 'quizBotSubjectSelect', 'uploadBookSubjectSelect', 'newQuestionSubjectSelect', 'gradeSubjectSelect'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.innerHTML = optionsHtml;
  });
  renderLibrarySubjectChips();
}

async function openMyGradesModal() {
  playSound('click');
  if (!state.currentUser) {
    openAuthModal();
    return;
  }
  if (typeof openStudentGradesHistoryModal === 'function') {
    openStudentGradesHistoryModal(state.currentUser.id, state.currentUser.full_name);
  }
}

// ----------------- KUTUBXONA (MAKTAB & LITSEY) -----------------
let currentLibraryGrade = 'barchasi';
let currentLibrarySubjectId = null;
let teacherFilterOnlyMine = false;

function renderLibrarySubjectChips() {
  const container = document.getElementById('librarySubjectChips');
  if (!container || !state.subjects) return;

  let html = `<button class="subject-chip ${currentLibrarySubjectId === null ? 'active' : ''}" onclick="selectLibrarySubject(null, this)">Barchasi</button>`;
  html += state.subjects.map(s => `
    <button class="subject-chip ${currentLibrarySubjectId === s.id ? 'active' : ''}" onclick="selectLibrarySubject(${s.id}, this)">
      ${s.icon} ${s.name}
    </button>
  `).join('');
  container.innerHTML = html;
}

function selectLibraryGrade(grade, el) {
  playSound('click');
  currentLibraryGrade = grade;
  document.querySelectorAll('#libraryGradePills .grade-pill').forEach(b => b.classList.remove('active'));
  if (el) el.classList.add('active');
  loadLibraryBooks();
}

function selectLibrarySubject(subId, el) {
  playSound('click');
  currentLibrarySubjectId = subId;
  document.querySelectorAll('#librarySubjectChips .subject-chip').forEach(b => b.classList.remove('active'));
  if (el) el.classList.add('active');
  loadLibraryBooks();
}

function toggleTeacherLibraryFilter() {
  playSound('click');
  teacherFilterOnlyMine = !teacherFilterOnlyMine;
  const btn = document.getElementById('btnTeacherSubjectToggle');
  if (btn) {
    btn.textContent = teacherFilterOnlyMine ? "👨‍🏫 Mening fanim" : "🌐 Barcha fanlar";
    btn.classList.toggle('active', teacherFilterOnlyMine);
  }
  loadLibraryBooks();
}

function onLibrarySearchInput(val) {
  renderBooksList(state.textbooks);
}

async function loadLibraryBooks() {
  const container = document.getElementById('booksListContainer');
  if (!container) return;

  let books = [];
  try {
    let url = '/api/library?';
    const params = [];
    if (currentLibrarySubjectId) params.push(`subject_id=${currentLibrarySubjectId}`);
    if (currentLibraryGrade && currentLibraryGrade !== 'barchasi') params.push(`grade=${encodeURIComponent(currentLibraryGrade)}`);
    if (teacherFilterOnlyMine && state.currentUser && state.currentUser.role === 'teacher') {
      params.push(`teacher_id=${state.currentUser.id}`);
    }
    url += params.join('&');

    const res = await fetch(url);
    if (res.ok) {
      books = await res.json();
    }
  } catch (e) {
    // API not reachable, fallback to bundled textbooks
  }

  if (!books || books.length === 0) {
    books = DEFAULT_TEXTBOOKS.filter(b => {
      if (currentLibrarySubjectId && b.subject_id !== currentLibrarySubjectId) return false;
      if (currentLibraryGrade && currentLibraryGrade !== 'barchasi' && b.grade !== currentLibraryGrade) return false;
      return true;
    });
  }

  state.textbooks = books;
  renderBooksList(books);
}

function renderBooksList(books) {
  const container = document.getElementById('booksListContainer');
  if (!container) return;

  const searchVal = (document.getElementById('librarySearchInput')?.value || '').toLowerCase().trim();
  const filtered = (books || []).filter(b => {
    if (!searchVal) return true;
    return (b.title && b.title.toLowerCase().includes(searchVal)) ||
           (b.author && b.author.toLowerCase().includes(searchVal)) ||
           (b.subject_name && b.subject_name.toLowerCase().includes(searchVal));
  });

  if (filtered.length === 0) {
    container.innerHTML = `
      <div class="minimal-card" style="text-align:center; padding:24px 14px;">
        <div style="font-size:32px; margin-bottom:8px;">📚</div>
        <h4 style="font-size:14px; font-weight:700; color:var(--text-primary);">Darslik topilmadi</h4>
        <p style="color:var(--text-muted); font-size:11px; margin-top:4px;">
          Tanlangan filtr bo'yicha hozircha kitob mavjud emas.
          ${state.currentUser && state.currentUser.role === 'teacher' ? '<br><button class="btn btn-red btn-sm" style="margin-top:10px;" onclick="openTeacherUploadBookModal()">➕ Darslik yuklash</button>' : ''}
        </p>
      </div>
    `;
    return;
  }

  container.innerHTML = filtered.map(b => `
    <div class="minimal-card" style="cursor:pointer; margin-bottom:10px;" onclick="openBookModal(${b.id})">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:4px;">
        <div>
          <span style="font-size:16px; margin-right:4px;">${b.subject_icon || '📖'}</span>
          <span style="font-size:11px; font-weight:700; color:var(--accent-red);">${b.subject_name || 'Fan'}</span>
        </div>
        <span class="tag tag-subtle">${b.grade}</span>
      </div>
      <h4 style="font-size:14px; font-weight:800; color:var(--text-primary); margin:4px 0;">${escapeHtml(b.title)}</h4>
      <div style="font-size:11px; color:var(--text-muted); margin-bottom:6px;">
        Muallif: <b style="color:var(--text-secondary);">${escapeHtml(b.author || 'Ustoz')}</b>
        ${b.file_url ? ' • <span class="tag tag-green" style="font-size:9px;">📄 PDF Kitob</span>' : ''}
        ${b.uploader_name ? ` • Yuklovchi: <span style="color:var(--accent-green);">${escapeHtml(b.uploader_name)}</span>` : ''}
      </div>
      <p style="font-size:11px; color:var(--text-secondary); line-height:1.4; margin-bottom:10px;">${escapeHtml(b.summary || '')}</p>
      <div style="display:flex; gap:6px;">
        <button class="btn ${b.file_url ? 'btn-red' : 'btn-outline'} btn-sm" style="flex:1;">📖 ${b.file_url ? 'Kitobni O\'qish (PDF)' : 'Darslikni O\'qish'}</button>
        <button class="btn btn-green btn-sm" onclick="event.stopPropagation(); startSubjectQuiz(${b.subject_id}, '${escapeHtml(b.title)}')" style="flex:1;">📝 Test Ishlash</button>
      </div>
    </div>
  `).join('');
}

async function loadTextbooks(subjectId = null, grade = null) {
  if (subjectId) currentLibrarySubjectId = subjectId;
  if (grade) currentLibraryGrade = grade;
  renderLibrarySubjectChips();
  await loadLibraryBooks();
}

async function openBookModal(bookId) {
  playSound('click');
  try {
    let b = (state.textbooks || []).find(x => x.id === bookId) || DEFAULT_TEXTBOOKS.find(x => x.id === bookId);

    try {
      const res = await fetch(`/api/textbooks/${bookId}`);
      if (res.ok) {
        const fetchedB = await res.json();
        if (fetchedB && fetchedB.title) b = fetchedB;
      }
    } catch (apiErr) {}

    if (!b) return;

    const hasPdf = Boolean(b.file_url);

    let pdfSection = '';
    if (hasPdf) {
      pdfSection = `
        <div style="margin-bottom:14px; background:var(--bg-card); border-radius:10px; border:1px solid var(--border-card); overflow:hidden;">
          <div style="display:flex; justify-content:space-between; align-items:center; padding:10px 14px; background:var(--bg-card-hover); border-bottom:1px solid var(--border-card); flex-wrap:wrap; gap:8px;">
            <div style="font-size:13px; font-weight:800; color:var(--text-primary); display:flex; align-items:center; gap:6px;">
              <span>📄 Rasmiy PDF Kitob</span>
              <span class="tag tag-green" style="font-size:10px;">To'liq nusxa</span>
            </div>
            <div style="display:flex; gap:8px;">
              <button onclick="openOrDownloadPdf('${b.file_url}', '${escapeHtml(b.title)}')" class="btn btn-sm btn-red" style="font-size:12px; padding:6px 14px; font-weight:800;">
                ↗️ PDF O'qish (To'liq ekran)
              </button>
              <button onclick="openOrDownloadPdf('${b.file_url}', '${escapeHtml(b.title)}')" class="btn btn-sm btn-outline" style="font-size:12px; padding:6px 14px; font-weight:700;">
                📥 Yuklab olish
              </button>
            </div>
          </div>
          <iframe 
            src="${b.file_url}#toolbar=1" 
            style="width:100%; height:68vh; min-height:420px; border:none; display:block;"
            title="${escapeHtml(b.title)}"
          ></iframe>
        </div>
      `;
    }

    document.getElementById('bookModalContent').innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; flex-wrap:wrap; gap:8px;">
        <div>
          <span class="tag tag-subtle">${b.grade}</span>
          <h3 style="font-size:17px; font-weight:800; margin-top:4px;">${escapeHtml(b.title)}</h3>
          <p style="font-size:12px; color:var(--text-muted); margin:0;">Muallif: <b style="color:var(--text-secondary);">${escapeHtml(b.author)}</b></p>
        </div>
        ${hasPdf ? `
          <div style="display:flex; gap:6px;">
            <button onclick="openOrDownloadPdf('${b.file_url}', '${escapeHtml(b.title)}')" class="btn btn-red btn-sm" style="font-weight:700;">
              📖 O'qish
            </button>
            <button onclick="openOrDownloadPdf('${b.file_url}', '${escapeHtml(b.title)}')" class="btn btn-outline btn-sm" style="font-weight:700;">
              📥 Yuklab olish
            </button>
          </div>
        ` : ''}
      </div>

      ${pdfSection}

      <div class="minimal-card" style="margin-bottom:10px;">
        <h5 style="font-size:11px; color:var(--accent-red); margin-bottom:4px;">Tavsif:</h5>
        <p style="font-size:11px; line-height:1.5; color:var(--text-secondary);">${b.summary}</p>
      </div>

      <h4 style="font-size:12px; font-weight:800; margin-bottom:8px;">📖 Boblar:</h4>
      ${(b.chapters || []).map(ch => `
        <div class="minimal-card" style="padding:10px; margin-bottom:6px;">
          <h5 style="font-size:12px; font-weight:700; color:var(--text-primary); margin-bottom:4px;">${ch.title}</h5>
          <p style="font-size:11px; color:var(--text-secondary); line-height:1.4; margin-bottom:4px;">${ch.summary}</p>
        </div>
      `).join('')}

      <button class="btn btn-red" onclick="closeModal('bookModal'); startSubjectQuiz(${b.subject_id}, '${b.title}')" style="margin-top:10px; width:100%;">
        🎯 Ushbu Darslik Bo'yicha Test Yechish
      </button>
    `;

    document.getElementById('bookModal').classList.add('active');
  } catch (e) {
    console.error("Error opening book modal:", e);
  }
}


// ----------------- SOLO TEST PRACTICE -----------------
let soloTestSession = { questions: [], currentIndex: 0, score: 0, correctCount: 0, startTime: null };

async function startSubjectQuiz(subjectId, title, loadedQuestions = null) {
  playSound('click');

  // Enforce Daily Test Limit for Free Students (2 tests/day)
  const user = state.currentUser;
  const isTeacher = user && (user.role === 'teacher' || user.role === 'admin');
  const isPro = user && (user.is_pro === 1 || user.is_pro === true);

  if (user && !isTeacher && !isPro) {
    try {
      const limitRes = await fetch(`/api/user-test-limit/${user.id}`);
      if (limitRes.ok) {
        const limitData = await limitRes.json();
        if (limitData.allowed === false) {
          openModal('proLimitModal');
          return;
        }
      }
    } catch (e) {
      console.warn("Could not check daily limit:", e);
    }
  }

  try {
    let qList = loadedQuestions;
    if (!qList) {
      const res = await fetch(`/api/questions?subject_id=${subjectId}&count=5`);
      qList = await res.json();
    }
    if (!qList || qList.length === 0) {
      alert(`⚠️ ${title} bo'yicha rasmiy testlar hali kiritilmagan.`);
      return;
    }

    soloTestSession = {
      questions: qList,
      currentIndex: 0,
      score: 0,
      correctCount: 0,
      startTime: Date.now()
    };

    renderSoloTestQuestion();
    document.getElementById('soloTestModal').classList.add('active');
  } catch (e) {
    console.error(e);
  }
}

function renderSoloTestQuestion() {
  const session = soloTestSession;
  const q = session.questions[session.currentIndex];
  const container = document.getElementById('soloTestModalContent');

  container.innerHTML = `
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
      <span class="tag tag-subtle">Savol ${session.currentIndex + 1} / ${session.questions.length}</span>
      <span style="font-size:12px; font-weight:800; color:var(--accent-red);">${session.score} ball</span>
    </div>

    <div style="font-size:14px; font-weight:700; line-height:1.4; margin-bottom:14px; color:var(--text-primary);">
      ${q.question_text}
    </div>

    <div id="soloOptionsContainer">
      ${(q.options || []).map((opt, idx) => `
        <button class="quiz-option-btn" onclick="checkSoloAnswer(${idx})">
          <span style="color:var(--accent-red); font-weight:800;">${['A', 'B', 'C', 'D'][idx]})</span>
          <span>${opt}</span>
        </button>
      `).join('')}
    </div>

    <div id="soloExplanationBox" style="display:none; margin-top:12px;" class="minimal-card highlight-green">
      <h5 style="font-size:11px; font-weight:700; color:var(--accent-green); margin-bottom:3px;">💡 Izoh:</h5>
      <p id="soloExplanationText" style="font-size:11px; line-height:1.4; color:var(--text-secondary);"></p>
      <button class="btn btn-red btn-sm" onclick="advanceSoloTest()" style="margin-top:8px;">Keyingi Savol ➔</button>
    </div>
  `;
}

function checkSoloAnswer(chosenIdx) {
  const session = soloTestSession;
  const q = session.questions[session.currentIndex];
  const isCorrect = (chosenIdx === q.correct_index);

  document.querySelectorAll('#soloOptionsContainer .quiz-option-btn').forEach((btn, idx) => {
    btn.disabled = true;
    if (idx === q.correct_index) btn.classList.add('correct');
    else if (idx === chosenIdx && !isCorrect) btn.classList.add('wrong');
  });

  if (isCorrect) {
    playSound('correct');
    session.score += 20;
    session.correctCount += 1;
  } else {
    playSound('wrong');
  }

  const explBox = document.getElementById('soloExplanationBox');
  document.getElementById('soloExplanationText').textContent = q.explanation || "To'g'ri javob belgilandi.";
  explBox.style.display = 'block';
}

async function advanceSoloTest() {
  playSound('click');
  const session = soloTestSession;
  session.currentIndex += 1;

  if (session.currentIndex >= session.questions.length) {
    const timeSpent = Math.floor((Date.now() - session.startTime) / 1000);
    playSound('victory');

    try {
      const res = await fetch('/api/submit-test', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: state.currentUser ? state.currentUser.id : 1,
          score: session.score,
          total_questions: session.questions.length,
          correct_count: session.correctCount,
          time_spent_sec: timeSpent
        })
      });
      const data = await res.json();

      if (data.new_coins !== undefined && state.currentUser) {
        state.currentUser.coins = data.new_coins;
        state.currentUser.xp = 0;
        localStorage.setItem('edubattle_user', JSON.stringify(state.currentUser));
        updateHeaderAndProfileUI();
        updateHomeDailyLimitBadge();
        if (data.coins_earned > 0) showCoinRewardPopup(data.coins_earned);
      }

      document.getElementById('soloTestModalContent').innerHTML = `
        <div style="text-align:center; padding:16px 0;">
          <div style="font-size:36px; margin-bottom:6px;">🎉</div>
          <h3 style="font-size:16px; font-weight:800; color:var(--text-primary);">Test Yakunlandi!</h3>
          <p style="font-size:11px; color:var(--text-muted); margin-top:2px;">Natija: ${session.correctCount} / ${session.questions.length} to'g'ri</p>

          <div class="minimal-card highlight-green" style="margin:14px 0;">
            <div style="font-size:16px; font-weight:900; color:#f59e0b;">+${data.coins_earned || 0} 🪙 Tanga yutib oldingiz!</div>
            <div style="font-size:12px; color:var(--text-primary); margin-top:4px;">Jami Tangalaringiz: <b style="color:#f59e0b;">${((data.new_coins !== undefined) ? data.new_coins : (state.currentUser?.coins || 0)).toLocaleString()} 🪙</b></div>
          </div>

          <button class="btn btn-red" onclick="closeModal('soloTestModal'); refreshCurrentUserData();">Bosh Sahifaga Qaytish</button>
        </div>
      `;
    } catch (e) {}
  } else {
    renderSoloTestQuestion();
  }
}

async function refreshCurrentUserData() {
  if (state.currentUser) {
    const res = await fetch(`/api/users/${state.currentUser.id}`);
    if (res.ok) {
      state.currentUser = await res.json();
      localStorage.setItem('edubattle_user', JSON.stringify(state.currentUser));
      updateHeaderAndProfileUI();
    }
  }
}

// ----------------- TARIFF & PAYMENT (TELEGRAM BOT PRO) -----------------

async function loadTariffs() {
  try {
    const res = await fetch('/api/tariffs');
    if (res.ok) {
      const tariffs = await res.json();
      const proPlan = tariffs.find(t => t.id === 'student_pro') || tariffs[0];
      if (proPlan && proPlan.amount) {
        state.proPrice = proPlan.amount;
        window.edubattleProPrice = proPlan.amount;
        applyDynamicTariffPrice(proPlan.amount);
      }
    }
  } catch (e) {
    console.warn("Dynamic tariffs fallback:", e);
  }
}

function applyDynamicTariffPrice(amount) {
  state.proPrice = amount;
  window.edubattleProPrice = amount;
  const formatted = `${Number(amount).toLocaleString()} so'm`;

  const modalPrice = document.getElementById('payModalPrice');
  if (modalPrice) modalPrice.textContent = Number(amount).toLocaleString();

  document.querySelectorAll('.dynamic-pro-price').forEach(el => {
    el.textContent = formatted;
  });
  const promoBtn = document.querySelector('#proPromotionCard button');
  if (promoBtn) promoBtn.textContent = `💎 PRO Tarifiga Ulanish (${formatted})`;
  const promoTag = document.querySelector('#proPromotionCard .tag-red');
  if (promoTag) promoTag.textContent = `${formatted} / oy`;

  if (state.currentUser && !state.currentUser.is_pro && state.currentUser.role !== 'teacher' && state.currentUser.role !== 'admin') {
    const headerPill = document.getElementById('headerProPill');
    if (headerPill) headerPill.textContent = `💎 PRO: ${formatted}`;
  }
}

function openPaymentModal(planId = 'student_pro') {
  playSound('click');
  if (state.currentUser && state.currentUser.role === 'teacher') {
    alert("👨‍🏫 Siz o'qituvchisiz! O'qituvchilar uchun barcha imkoniyatlar 100% bepul.");
    return;
  }

  state.selectedPaymentPlan = 'student_pro';

  const userLoginEl = document.getElementById('payModalUserId');
  if (userLoginEl) {
    userLoginEl.textContent = state.currentUser ? (state.currentUser.username || `ID: ${state.currentUser.id}`) : "Tizimga kirmagan";
  }

  const modal = document.getElementById('paymentModal');
  if (modal) modal.classList.add('active');
}

function redirectToTelegramProPayment() {
  playSound('click');
  let url = 'https://t.me/edubattleuz_bot?start=buy_pro';
  if (state.currentUser && state.currentUser.id) {
    url += `_${state.currentUser.id}`;
  }
  window.open(url, '_blank');
}

function selectPaymentProvider(provider) {
  playSound('click');
}

async function submitRealPayment() {
  redirectToTelegramProPayment();
}

// ----------------- LEADERBOARD (HAFTALIK VA UMUMIY TANGALAR) -----------------
let currentHomeLbPeriod = 'weekly';
let currentModalLbPeriod = 'weekly';

async function loadHomeLeaderboard(period = currentHomeLbPeriod) {
  currentHomeLbPeriod = period;
  const container = document.getElementById('homeLeaderboardList');
  if (!container) return;

  const uid = state.currentUser ? state.currentUser.id : '';
  try {
    const res = await fetch(`/api/leaderboard?period=${period}${uid ? '&user_id=' + uid : ''}`);
    const data = await res.json();
    const list = Array.isArray(data) ? data : (data.leaderboard || []);
    const top3 = list.slice(0, 3);
    const medals = ['🥇', '🥈', '🥉'];
    const rankBadges = ['lb-rank-1', 'lb-rank-2', 'lb-rank-3'];
    const cardTopClasses = ['is-top-1', 'is-top-2', 'is-top-3'];

    if (!top3 || top3.length === 0) {
      container.innerHTML = '<div style="text-align:center; padding:12px; color:var(--text-muted); font-size:11px;">Hozircha ma\'lumotlar yo\'q</div>';
      return;
    }

    container.innerHTML = top3.map((student, idx) => {
      const coinsVal = period === 'weekly' ? (student.weekly_coins !== undefined ? student.weekly_coins : student.coins) : (student.total_coins !== undefined ? student.total_coins : student.coins);
      const isMe = state.currentUser && state.currentUser.id === student.id;
      return `
        <div class="lb-item-card ${cardTopClasses[idx] || ''} ${isMe ? 'is-me' : ''}">
          <div style="display:flex; align-items:center; gap:8px; min-width:0;">
            <div class="lb-rank-badge ${rankBadges[idx] || 'lb-rank-other'}">${medals[idx]}</div>
            <span style="font-size:16px;">${student.avatar || '👤'}</span>
            <div style="min-width:0;">
              <div style="font-size:12px; font-weight:800; color:#fff; display:flex; align-items:center; gap:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                <span>${student.full_name || student.username}</span>
                ${student.is_pro ? '<span class="pro-tag-mini" style="font-size:8px; padding:1px 4px;">PRO</span>' : ''}
                ${isMe ? '<span style="font-size:9px; color:#6366f1; font-weight:800;">(Siz)</span>' : ''}
              </div>
              <div style="font-size:10px; color:var(--text-muted); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                ${student.school_lyceum || 'Maktab'} • ${student.grade || ''}
              </div>
            </div>
          </div>
          <div class="lb-coins-badge">
            <span>🪙</span>
            <span>${(coinsVal || 0).toLocaleString()}</span>
          </div>
        </div>
      `;
    }).join('');
  } catch (e) {
    console.warn("loadHomeLeaderboard error:", e);
  }
}

function switchHomeLeaderboardPeriod(period) {
  playSound('click');
  currentHomeLbPeriod = period;
  
  const btnWeekly = document.getElementById('homeLbSwitch_weekly');
  const btnAllTime = document.getElementById('homeLbSwitch_all_time');
  const subLabel = document.getElementById('homeLeaderboardSub');

  if (btnWeekly) btnWeekly.classList.toggle('active', period === 'weekly');
  if (btnAllTime) btnAllTime.classList.toggle('active', period === 'all_time');

  if (subLabel) {
    subLabel.textContent = period === 'weekly' 
      ? '⚡ Haftalik eng ko\'p tanga to\'plaganlar' 
      : '🌐 Barcha to\'plangan umumiy tangalar';
  }

  loadHomeLeaderboard(period);
}

async function showLeaderboardModal(period = 'weekly') {
  playSound('click');
  currentModalLbPeriod = period;
  const modal = document.getElementById('leaderboardModal');
  if (modal) modal.classList.add('active');

  const btnWeekly = document.getElementById('modalLbSwitch_weekly');
  const btnAllTime = document.getElementById('modalLbSwitch_all_time');
  const subLabel = document.getElementById('modalLeaderboardSub');

  if (btnWeekly) btnWeekly.classList.toggle('active', period === 'weekly');
  if (btnAllTime) btnAllTime.classList.toggle('active', period === 'all_time');

  if (subLabel) {
    subLabel.textContent = period === 'weekly' 
      ? '⚡ Bu hafta davomida to\'plangan tangalar' 
      : '🌐 Platforma bo\'yicha barcha umumiy tangalar';
  }

  loadModalLeaderboard(period);
}

function switchModalLeaderboardPeriod(period) {
  playSound('click');
  currentModalLbPeriod = period;

  const btnWeekly = document.getElementById('modalLbSwitch_weekly');
  const btnAllTime = document.getElementById('modalLbSwitch_all_time');
  const subLabel = document.getElementById('modalLeaderboardSub');

  if (btnWeekly) btnWeekly.classList.toggle('active', period === 'weekly');
  if (btnAllTime) btnAllTime.classList.toggle('active', period === 'all_time');

  if (subLabel) {
    subLabel.textContent = period === 'weekly' 
      ? '⚡ Bu hafta davomida to\'plangan tangalar' 
      : '🌐 Platforma bo\'yicha barcha umumiy tangalar';
  }

  loadModalLeaderboard(period);
}

async function loadModalLeaderboard(period = currentModalLbPeriod) {
  const listContainer = document.getElementById('fullLeaderboardList');
  const userRankBanner = document.getElementById('modalUserRankBanner');
  const userRankName = document.getElementById('modalUserRankName');
  const userRankMeta = document.getElementById('modalUserRankMeta');
  const userRankCoins = document.getElementById('modalUserRankCoins');
  const userRankAvatar = document.getElementById('modalUserRankAvatar');

  if (!listContainer) return;
  listContainer.innerHTML = '<div style="text-align:center; padding:24px; color:var(--text-muted); font-size:12px;">Reyting yuklanmoqda...</div>';

  const uid = state.currentUser ? state.currentUser.id : '';
  try {
    const res = await fetch(`/api/leaderboard?period=${period}${uid ? '&user_id=' + uid : ''}`);
    const data = await res.json();
    const list = Array.isArray(data) ? data : (data.leaderboard || []);
    const userRank = data.user_rank;

    // Render User Pinned Rank Banner
    if (userRankBanner && state.currentUser) {
      userRankBanner.style.display = 'flex';
      if (userRankAvatar) userRankAvatar.textContent = state.currentUser.avatar || '👤';
      if (userRankName) {
        userRankName.innerHTML = `${state.currentUser.full_name || state.currentUser.username} <span style="color:#6366f1; font-weight:800;">(#${userRank ? userRank.rank : '-'})</span>`;
      }
      if (userRankMeta) {
        userRankMeta.textContent = period === 'weekly'
          ? `Haftalik: #${userRank ? userRank.rank : '-'} o'rin | Jami: ${(state.currentUser.coins || 0).toLocaleString()} 🪙`
          : `Umumiy: #${userRank ? userRank.rank : '-'} o'rin | Tangalar: ${(state.currentUser.coins || 0).toLocaleString()} 🪙`;
      }
      if (userRankCoins) {
        const uCoins = userRank ? (period === 'weekly' ? userRank.weekly_coins : userRank.total_coins) : (state.currentUser.coins || 0);
        userRankCoins.innerHTML = `<span>🪙</span> <span>${(uCoins || 0).toLocaleString()}</span>`;
      }
    } else if (userRankBanner) {
      userRankBanner.style.display = 'none';
    }

    if (!list || list.length === 0) {
      listContainer.innerHTML = '<div style="text-align:center; padding:24px; color:var(--text-muted); font-size:12px;">Hozircha reyting mavjud emas.</div>';
      return;
    }

    const medals = ['🥇', '🥈', '🥉'];
    const rankBadges = ['lb-rank-1', 'lb-rank-2', 'lb-rank-3'];
    const cardTopClasses = ['is-top-1', 'is-top-2', 'is-top-3'];

    listContainer.innerHTML = list.map((s, idx) => {
      const rankNum = s.rank || (idx + 1);
      const isTop3 = idx < 3;
      const rankIcon = isTop3 ? medals[idx] : `#${rankNum}`;
      const badgeClass = isTop3 ? rankBadges[idx] : 'lb-rank-other';
      const cardClass = isTop3 ? cardTopClasses[idx] : '';
      const isMe = state.currentUser && state.currentUser.id === s.id;
      const coinsVal = period === 'weekly' ? (s.weekly_coins !== undefined ? s.weekly_coins : s.coins) : (s.total_coins !== undefined ? s.total_coins : s.coins);

      return `
        <div class="lb-item-card ${cardClass} ${isMe ? 'is-me' : ''}">
          <div style="display:flex; align-items:center; gap:8px; min-width:0;">
            <div class="lb-rank-badge ${badgeClass}">${rankIcon}</div>
            <span style="font-size:18px;">${s.avatar || '👤'}</span>
            <div style="min-width:0;">
              <div style="font-size:12px; font-weight:800; color:#fff; display:flex; align-items:center; gap:4px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                <span>${s.full_name || s.username}</span>
                ${s.is_pro ? '<span class="pro-tag-mini" style="font-size:8px; padding:1px 4px;">PRO</span>' : ''}
                ${isMe ? '<span style="font-size:9px; color:#6366f1; font-weight:800;">(Siz)</span>' : ''}
              </div>
              <div style="font-size:10px; color:var(--text-muted); white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">
                ${s.school_lyceum || 'Maktab'} • ${s.grade || ''}
              </div>
            </div>
          </div>
          <div style="display:flex; flex-direction:column; align-items:flex-end; gap:2px;">
            <div class="lb-coins-badge">
              <span>🪙</span>
              <span>${(coinsVal || 0).toLocaleString()}</span>
            </div>
          </div>
        </div>
      `;
    }).join('');
  } catch (e) {
    console.warn("loadModalLeaderboard error:", e);
    listContainer.innerHTML = '<div style="text-align:center; padding:24px; color:#ef4444; font-size:12px;">Reytingni yuklashda xatolik yuz berdi.</div>';
  }
}

function openAppDownloadModal() {
  window.open('https://t.me/edubattleuz_bot', '_blank');
}

function openModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.add('active');
}

function closeModal(id) {
  const el = document.getElementById(id);
  if (el) el.classList.remove('active');
}

// ----------------- STUDENT JOIN TEACHER GROUP & MANAGE GROUPS -----------------
function studentJoinGroupFromHome() {
  const input = document.getElementById('homeJoinGroupCodeInput');
  const code = (input ? input.value : '').trim();
  studentJoinGroup(code);
}

async function studentJoinGroup(customCode) {
  playSound('click');
  if (!state.currentUser) {
    alert("Guruhga a'zo bo'lish uchun avval akkauntingizga kiring!");
    openAuthModal();
    return;
  }

  const profileInput = document.getElementById('joinGroupCodeInput');
  const homeInput = document.getElementById('homeJoinGroupCodeInput');
  const code = (customCode || (profileInput ? profileInput.value : '') || (homeInput ? homeInput.value : '')).trim().toUpperCase();

  if (!code) {
    alert("Iltimos, ustozingiz bergan Guruh Kodi / Parolini kiriting! (Masalan: MATH9A)");
    if (homeInput) homeInput.focus();
    return;
  }

  try {
    const res = await fetch('/api/student/join-group', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        student_id: state.currentUser.id,
        invite_code: code
      })
    });

    const data = await res.json();
    if (res.ok && data.success) {
      playSound('victory');
      alert(`🎉 Tabriklaymiz!\n${data.message}`);
      if (profileInput) profileInput.value = '';
      if (homeInput) homeInput.value = '';
      loadStudentJoinedGroups();
    } else {
      playSound('wrong');
      alert(data.detail || "Guruh topilmadi!");
    }
  } catch (e) {
    alert("Guruhga ulanishda server xatosi!");
  }
}

async function loadStudentJoinedGroups() {
  if (!state.currentUser || state.currentUser.role === 'teacher') return;
  const homeContainer = document.getElementById('homeJoinedGroupsContainer');
  const profileContainer = document.getElementById('profileJoinedGroupsContainer');

  try {
    const res = await fetch(`/api/student/${state.currentUser.id}/groups`);
    if (!res.ok) return;
    const groups = await res.json();

    if (!groups || groups.length === 0) {
      if (homeContainer) homeContainer.innerHTML = '';
      if (profileContainer) {
        profileContainer.innerHTML = `
          <div style="font-size:10px; color:var(--text-muted); text-align:center; padding:6px 0;">
            Hozircha hech qaysi ustoz guruhiga a'zo emassiz.
          </div>
        `;
      }
      return;
    }

    const html = `
      <div style="display:flex; flex-direction:column; gap:6px;">
        ${groups.map(g => `
          <div style="background:rgba(16,185,129,0.08); border:1px solid rgba(16,185,129,0.3); border-radius:8px; padding:8px 10px; display:flex; justify-content:space-between; align-items:center;">
            <div>
              <div style="font-size:12px; font-weight:800; color:var(--text-primary);">${escapeHtml(g.group_name)}</div>
              <div style="font-size:10px; color:var(--text-muted); margin-top:2px;">
                Ustoz: <b style="color:var(--text-secondary);">${escapeHtml(g.teacher_name)}</b> • ${escapeHtml(g.subject_name || 'Fan')}
              </div>
            </div>
            <span class="tag tag-green" style="font-size:10px;">A'zosiz ✅</span>
          </div>
        `).join('')}
      </div>
    `;

    if (homeContainer) homeContainer.innerHTML = html;
    if (profileContainer) profileContainer.innerHTML = html;
  } catch (e) {
    console.warn("Could not load student groups:", e);
  }
}

// ========================================================
// DO'STLAR (FRIENDS & DIRECT CHAT SYSTEM)
// ========================================================

let friendSearchTimeout = null;

function onSearchFriendsInput(val) {
  if (friendSearchTimeout) clearTimeout(friendSearchTimeout);
  friendSearchTimeout = setTimeout(() => {
    searchFriendsManual();
  }, 350);
}

async function searchFriendsManual() {
  const query = (document.getElementById('friendSearchInput').value || '').trim();
  const resultsContainer = document.getElementById('friendSearchResults');
  if (!resultsContainer) return;

  if (!query) {
    resultsContainer.style.display = 'none';
    resultsContainer.innerHTML = '';
    return;
  }

  const currentUserId = state.currentUser ? state.currentUser.id : 0;
  try {
    const res = await fetch(`/api/friends/search?q=${encodeURIComponent(query)}&current_user_id=${currentUserId}`);
    const results = await res.json();
    
    resultsContainer.style.display = 'block';

    if (!results || results.length === 0) {
      resultsContainer.innerHTML = `
        <div style="padding:12px; text-align:center; color:var(--text-muted); font-size:11px;">
          "${query}" bo'yicha foydalanuvchilar topilmadi. Login ID ni to'g'ri yozganingizga ishonch hosil qiling.
        </div>
      `;
      return;
    }

    resultsContainer.innerHTML = `
      <div style="font-size:11px; font-weight:700; color:var(--text-muted); margin-bottom:8px;">Qidiruv natijalari:</div>
      <div style="display:flex; flex-direction:column; gap:8px;">
        ${results.map(user => {
          let actionButtons = '';
          if (user.friend_status === 'friends') {
            actionButtons = `
              <button class="btn btn-outline btn-sm" onclick="openFriendChat(${user.id}, '${escapeHtml(user.full_name)}', '${escapeHtml(user.username)}')">
                💬 Chat
              </button>
              <button class="btn btn-red btn-sm" onclick="inviteFriendDirectly(${user.id}, '${escapeHtml(user.full_name)}')">
                ⚔️ Batl
              </button>
            `;
          } else if (user.friend_status === 'pending_sent') {
            actionButtons = `
              <button class="btn btn-outline btn-sm" onclick="sendFriendRequestAction(${user.id})" style="font-size:11px; color:#f59e0b; border-color:#f59e0b;">
                ⏳ Kutilmoqda ✕
              </button>
            `;
          } else if (user.friend_status === 'pending_received') {
            actionButtons = `
              <button class="btn btn-green btn-sm" onclick="respondFriendRequestAction(${user.id}, 'accept')">
                ✅ Qabul qilish
              </button>
              <button class="btn btn-outline btn-sm" onclick="respondFriendRequestAction(${user.id}, 'reject')">
                ✕
              </button>
            `;
          } else {
            actionButtons = `
              <button class="btn btn-red btn-sm" onclick="sendFriendRequestAction(${user.id})">
                ➕ Do'stlik so'rovi
              </button>
            `;
          }

          return `
            <div class="minimal-card" style="padding:10px 12px; margin-bottom:0; display:flex; align-items:center; justify-content:space-between; gap:10px;">
              <div style="display:flex; align-items:center; gap:10px; overflow:hidden;">
                <div style="width:36px; height:36px; border-radius:50%; background:var(--bg-elevated); border:1px solid var(--border-card); display:flex; align-items:center; justify-content:center; font-size:16px; flex-shrink:0;">
                  ${user.role === 'teacher' ? '👨‍🏫' : '👨‍🎓'}
                </div>
                <div style="overflow:hidden;">
                  <div style="font-size:13px; font-weight:700; color:var(--text-primary); white-space:nowrap; text-overflow:ellipsis; overflow:hidden;">
                    ${escapeHtml(user.full_name)} ${user.is_pro ? '<span class="tag tag-red" style="font-size:8px; padding:2px 5px;">PRO</span>' : ''}
                  </div>
                  <div style="font-size:10px; color:var(--text-muted);">
                    @${escapeHtml(user.username)} • ${escapeHtml(user.school_lyceum || 'Maktab')} • ${user.grade || ''}
                  </div>
                </div>
              </div>

              <div style="display:flex; gap:6px; flex-shrink:0;">
                ${actionButtons}
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  } catch (e) {
    resultsContainer.style.display = 'block';
    resultsContainer.innerHTML = `<div style="color:var(--accent-red); font-size:11px; padding:8px;">Qidirishda xatolik yuz berdi</div>`;
  }
}

async function loadMyFriendsList() {
  const container = document.getElementById('myFriendsListContainer');
  const reqContainer = document.getElementById('friendRequestsContainer');
  const badge = document.getElementById('friendsCountBadge');
  if (!container) return;

  if (!state.currentUser) {
    container.innerHTML = `
      <div class="minimal-card" style="text-align:center; padding:18px;">
        <p style="color:var(--text-muted); font-size:12px;">Do'stlar va xabarlarni ko'rish uchun avval tizimga kiring.</p>
        <button class="btn btn-red btn-sm" style="margin-top:8px;" onclick="openAuthModal()">Kirish ➔</button>
      </div>
    `;
    if (reqContainer) reqContainer.innerHTML = '';
    if (badge) badge.textContent = '0 ta do\'st';
    return;
  }

  try {
    // 1. Fetch accepted friends
    const friendsRes = await fetch(`/api/friends/${state.currentUser.id}`);
    const friends = await friendsRes.json();

    // 2. Fetch pending requests
    const reqRes = await fetch(`/api/friends/requests/${state.currentUser.id}`);
    const requestsData = await reqRes.json();
    const incomingReqs = requestsData.incoming || [];
    const outgoingReqs = requestsData.outgoing || [];

    if (badge) badge.textContent = `${friends.length} ta do'st`;

    // 3. Render Incoming Requests block if any
    if (reqContainer) {
      if (incomingReqs.length > 0) {
        reqContainer.innerHTML = `
          <div class="minimal-card highlight-green" style="padding:12px; margin-bottom:12px; border:1px solid #10b981;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
              <div style="display:flex; align-items:center; gap:6px;">
                <span style="font-size:16px;">🔔</span>
                <h4 style="font-size:13px; font-weight:800; color:var(--text-primary); margin:0;">
                  Kelgan Do'stlik So'rovlari (${incomingReqs.length})
                </h4>
              </div>
              <span class="tag tag-green" style="font-size:10px;">Tasdiqlash kutilmoqda</span>
            </div>
            <div style="display:flex; flex-direction:column; gap:8px;">
              ${incomingReqs.map(r => `
                <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(0,0,0,0.3); padding:8px 10px; border-radius:8px;">
                  <div style="display:flex; align-items:center; gap:8px;">
                    <div style="width:34px; height:34px; border-radius:50%; background:var(--bg-elevated); display:flex; align-items:center; justify-content:center; font-size:16px;">
                      ${r.role === 'teacher' ? '👨‍🏫' : '👨‍🎓'}
                    </div>
                    <div>
                      <div style="font-size:12px; font-weight:700; color:var(--text-primary);">${escapeHtml(r.full_name)}</div>
                      <div style="font-size:10px; color:var(--text-muted);">@${escapeHtml(r.username)} • ${escapeHtml(r.grade || '')} • ${(r.coins || 0).toLocaleString()} 🪙</div>
                    </div>
                  </div>
                  <div style="display:flex; gap:6px;">
                    <button class="btn btn-green btn-sm" onclick="respondFriendRequestAction(${r.requester_id}, 'accept')" style="padding:4px 10px; font-weight:700; font-size:11px;">
                      ✅ Qabul
                    </button>
                    <button class="btn btn-outline btn-sm" onclick="respondFriendRequestAction(${r.requester_id}, 'reject')" style="padding:4px 8px; font-size:11px; color:var(--text-muted);">
                      ❌ Rad
                    </button>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>
        `;
      } else if (outgoingReqs.length > 0) {
        reqContainer.innerHTML = `
          <div class="minimal-card" style="padding:10px 12px; margin-bottom:12px; font-size:11px; color:var(--text-secondary);">
            <span style="color:#f59e0b; font-weight:700;">⏳ Yuborilgan so'rovlar (${outgoingReqs.length}):</span>
            ${outgoingReqs.map(o => `
              <span style="display:inline-flex; align-items:center; gap:4px; background:rgba(255,255,255,0.06); padding:2px 8px; border-radius:12px; margin:4px 4px 0 0;">
                @${escapeHtml(o.username)}
                <span style="cursor:pointer; color:var(--text-muted); font-weight:800;" onclick="sendFriendRequestAction(${o.target_id})" title="So'rovni bekor qilish">✕</span>
              </span>
            `).join('')}
          </div>
        `;
      } else {
        reqContainer.innerHTML = '';
      }
    }

    // 4. Render Accepted Friends
    if (!friends || friends.length === 0) {
      container.innerHTML = `
        <div class="minimal-card" style="text-align:center; padding:24px 14px;">
          <div style="font-size:36px; margin-bottom:8px;">👥</div>
          <h4 style="font-size:14px; font-weight:800; color:var(--text-primary);">Do'stlaringiz hali yo'q</h4>
          <p style="color:var(--text-muted); font-size:11px; margin-top:4px; line-height:1.5;">
            Sinfdoshlaringiz va do'stlaringizni Login ID orqali qidiring va do'stlik so'rovi yuboring.<br>
            Ular qabul qilgach, bemalol jonli xabarlashishingiz va intellektual batllar o'ynashingiz mumkin!
          </p>
        </div>
      `;
      return;
    }

    container.innerHTML = `
      <div style="display:flex; flex-direction:column; gap:8px;">
        ${friends.map(f => `
          <div class="minimal-card" style="padding:12px; margin-bottom:0; display:flex; align-items:center; justify-content:space-between; gap:10px;">
            <div style="display:flex; align-items:center; gap:10px; overflow:hidden; cursor:pointer;" onclick="openFriendChat(${f.id}, '${escapeHtml(f.full_name)}', '${escapeHtml(f.username)}')">
              <div style="position:relative; flex-shrink:0;">
                <div style="width:40px; height:40px; border-radius:50%; background:var(--bg-elevated); border:1px solid var(--border-card); display:flex; align-items:center; justify-content:center; font-size:18px;">
                  ${f.role === 'teacher' ? '👨‍🏫' : '👨‍🎓'}
                </div>
                <span style="position:absolute; bottom:0; right:0; width:9px; height:9px; border-radius:50%; background:#10b981; border:2px solid var(--bg-surface);"></span>
              </div>
              <div style="overflow:hidden;">
                <div style="font-size:13px; font-weight:800; color:var(--text-primary); white-space:nowrap; text-overflow:ellipsis; overflow:hidden;">
                  ${escapeHtml(f.full_name)} ${f.is_pro ? '<span class="tag tag-red" style="font-size:8px; padding:1px 5px;">PRO</span>' : ''}
                </div>
                <div style="font-size:10px; color:var(--text-muted);">
                  @${escapeHtml(f.username)} • ${escapeHtml(f.school_lyceum || 'Maktab')} • <span style="color:#f59e0b; font-weight:700;">${(f.coins || 0).toLocaleString()} 🪙</span>
                </div>
              </div>
            </div>

            <div style="display:flex; gap:6px; flex-shrink:0;">
              <button class="btn btn-outline btn-sm" title="Xabar yozish" style="font-weight:700;" onclick="openFriendChat(${f.id}, '${escapeHtml(f.full_name)}', '${escapeHtml(f.username)}')">
                💬 Chat
              </button>
              <button class="btn btn-red btn-sm" title="Batlga taklif qilish" style="font-weight:700;" onclick="inviteFriendDirectly(${f.id}, '${escapeHtml(f.full_name)}')">
                ⚔️ Batl
              </button>
              <button class="btn btn-outline btn-sm" title="Do'stlikni bekor qilish" style="color:var(--text-muted); padding:4px 6px;" onclick="removeFriendPrompt(${f.id}, '${escapeHtml(f.full_name)}')">
                ✕
              </button>
            </div>
          </div>
        `).join('')}
      </div>
    `;
  } catch (e) {
    container.innerHTML = `<div style="color:var(--accent-red); font-size:11px; padding:12px;">Do'stlar ro'yxatini yuklashda xatolik!</div>`;
  }
}

async function sendFriendRequestAction(targetId) {
  playSound('click');
  if (!state.currentUser) {
    alert("Iltimos, avval tizimga kiring!");
    openAuthModal();
    return;
  }

  try {
    const res = await fetch('/api/friends/send-request', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: state.currentUser.id,
        target_id: targetId
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      playSound('correct');
      loadMyFriendsList();
      const searchInput = document.getElementById('friendSearchInput');
      if (searchInput && searchInput.value.trim()) {
        searchFriendsManual();
      }
    } else {
      alert(data.detail || "So'rov yuborishda xatolik!");
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik!");
  }
}

async function respondFriendRequestAction(requesterId, action) {
  playSound(action === 'accept' ? 'victory' : 'click');
  if (!state.currentUser) return;

  try {
    const res = await fetch('/api/friends/respond-request', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: state.currentUser.id,
        requester_id: requesterId,
        action: action
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      loadMyFriendsList();
      const searchInput = document.getElementById('friendSearchInput');
      if (searchInput && searchInput.value.trim()) {
        searchFriendsManual();
      }
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik!");
  }
}

async function removeFriendPrompt(friendId, friendName) {
  if (!confirm(`${friendName} bilan do'stlikni bekor qilmoqchimisiz?`)) return;
  playSound('click');
  if (!state.currentUser) return;

  try {
    const res = await fetch('/api/friends/remove', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: state.currentUser.id,
        friend_id: friendId
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      loadMyFriendsList();
    }
  } catch (e) {}
}

async function toggleFollowFriend(targetId) {
  return sendFriendRequestAction(targetId);
}

// ----------------- DIRECT MESSENGER CHAT & BATTLE INVITES -----------------

function openFriendChat(friendId, friendName, friendUsername) {
  playSound('click');
  if (!state.currentUser) {
    alert("Suhbatlashish uchun avval tizimga kiring!");
    openAuthModal();
    return;
  }

  state.activeFriendChat = {
    id: friendId,
    name: friendName,
    username: friendUsername
  };

  document.getElementById('chatFriendName').textContent = friendName;
  document.getElementById('chatFriendMeta').textContent = `@${friendUsername} • Hozir tarmoqda`;

  const modal = document.getElementById('friendChatModal');
  modal.classList.add('active');

  loadFriendChatMessages();

  if (state.chatPollInterval) clearInterval(state.chatPollInterval);
  state.chatPollInterval = setInterval(loadFriendChatMessages, 2000);

  setTimeout(() => {
    const input = document.getElementById('chatMessageInput');
    if (input) input.focus();
  }, 200);
}

function closeFriendChatModal() {
  if (state.chatPollInterval) {
    clearInterval(state.chatPollInterval);
    state.chatPollInterval = null;
  }
  state.activeFriendChat = null;
  closeModal('friendChatModal');
}

async function loadFriendChatMessages() {
  if (!state.activeFriendChat || !state.currentUser) return;
  const container = document.getElementById('chatMessagesContainer');
  if (!container) return;

  try {
    const res = await fetch(`/api/chat/messages?user_id=${state.currentUser.id}&friend_id=${state.activeFriendChat.id}`);
    const messages = await res.json();

    if (!messages || messages.length === 0) {
      container.innerHTML = `
        <div style="text-align:center; color:var(--text-muted); font-size:12px; margin:auto 0; padding:24px 10px;">
          <div style="font-size:32px; margin-bottom:8px;">💬</div>
          <b>Xabarlar tarixi hozircha bo'sh</b><br>
          <span style="font-size:11px;">Birinchi bo'lib salom yozing yoki do'stingizni Batlga chaqiring!</span>
        </div>
      `;
      return;
    }

    const isNearBottom = (container.scrollHeight - container.scrollTop - container.clientHeight) < 70;

    container.innerHTML = messages.map(m => {
      const isMe = (m.sender_id === state.currentUser.id);
      
      let battleBlock = '';
      if (m.battle_room_code) {
        battleBlock = `
          <div style="margin-top:8px; padding:10px; background:rgba(0,0,0,0.6); border:1px solid #10b981; border-radius:8px; text-align:center;">
            <div style="font-size:10px; color:#10b981; text-transform:uppercase; font-weight:800; letter-spacing:1px;">⚔️ Intellektual Batl Taklifi!</div>
            <div style="font-size:16px; font-weight:900; color:#fff; font-family:monospace; margin:4px 0;">${m.battle_room_code}</div>
            <button class="btn btn-green btn-sm" style="width:100%; margin-top:4px; font-weight:800; font-size:11px;" onclick="joinBattleFromChat('${m.battle_room_code}')">
              🚀 Batlga Kirish ➔
            </button>
          </div>
        `;
      }

      const timeStr = (m.created_at || '').split(' ')[1] ? (m.created_at.split(' ')[1]).substring(0, 5) : '';

      return `
        <div style="display:flex; justify-content:${isMe ? 'flex-end' : 'flex-start'}; margin-bottom:4px;">
          <div style="max-width:82%; padding:9px 12px; border-radius:14px; font-size:13px; line-height:1.4; word-break:break-word; box-shadow:0 2px 6px rgba(0,0,0,0.3);
            ${isMe 
              ? 'background:linear-gradient(135deg, #059669, #10b981); color:#fff; border-bottom-right-radius:3px;' 
              : 'background:var(--bg-elevated); color:var(--text-primary); border:1px solid var(--border-card); border-bottom-left-radius:3px;'}">
            <div>${escapeHtml(m.message || '')}</div>
            ${battleBlock}
            <div style="font-size:10px; color:${isMe ? 'rgba(255,255,255,0.8)' : 'var(--text-muted)'}; text-align:right; margin-top:4px; display:flex; justify-content:flex-end; align-items:center; gap:3px;">
              <span>${timeStr}</span>
              ${isMe ? '<span style="font-size:11px;">✓✓</span>' : ''}
            </div>
          </div>
        </div>
      `;
    }).join('');

    if (isNearBottom) {
      container.scrollTop = container.scrollHeight;
    }
  } catch (e) {}
}

async function sendQuickChatMessage(text) {
  if (!state.activeFriendChat || !state.currentUser) return;
  const input = document.getElementById('chatMessageInput');
  if (input) input.value = text;
  submitFriendChatForm();
}

async function submitFriendChatForm(e) {
  if (e) e.preventDefault();
  if (!state.activeFriendChat || !state.currentUser) return;

  const input = document.getElementById('chatMessageInput');
  const text = (input.value || '').trim();
  if (!text) return;

  input.value = '';
  playSound('pop');

  try {
    const res = await fetch('/api/chat/send', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        sender_id: state.currentUser.id,
        receiver_id: state.activeFriendChat.id,
        message: text
      })
    });
    const data = await res.json();
    if (res.ok && data.success) {
      loadFriendChatMessages();
      setTimeout(() => {
        const c = document.getElementById('chatMessagesContainer');
        if (c) c.scrollTop = c.scrollHeight;
      }, 80);
    }
  } catch (e) {
    alert("Xabar yuborishda xatolik!");
  }
}

async function inviteActiveFriendToBattle() {
  if (!state.activeFriendChat || !state.currentUser) return;
  playSound('click');

  try {
    const res = await fetch('/api/battle/create-room', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        host_id: state.currentUser.id,
        host_name: state.currentUser.full_name,
        subject_id: 1,
        mode: '1v1',
        max_players: 2
      })
    });
    const data = await res.json();
    if (data.success) {
      const roomCode = data.room_code;
      // Send chat message with the battle code
      await fetch('/api/chat/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sender_id: state.currentUser.id,
          receiver_id: state.activeFriendChat.id,
          message: `⚔️ Sizni 1v1 bellashuvga taklif qildim! Xona kodi: ${roomCode}`,
          battle_room_code: roomCode
        })
      });
      loadFriendChatMessages();

      if (confirm(`⚔️ Batl xonasi yaratildi: ${roomCode}!\nTaklif do'stingizga yuborildi. Siz ham hozir xonaga kirasizmi?`)) {
        closeFriendChatModal();
        navigateTo('battle');
        battleState.isHost = true;
        connectToBattleWebSocket(roomCode);
      }
    }
  } catch (e) {
    alert("Batl yaratishda xatolik!");
  }
}

async function inviteFriendDirectly(friendId, friendName) {
  if (!state.currentUser) {
    alert("Iltimos, avval tizimga kiring!");
    openAuthModal();
    return;
  }
  playSound('click');

  try {
    const res = await fetch('/api/battle/create-room', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        host_id: state.currentUser.id,
        host_name: state.currentUser.full_name,
        subject_id: 1,
        mode: '1v1',
        max_players: 2
      })
    });
    const data = await res.json();
    if (data.success) {
      const roomCode = data.room_code;
      await fetch('/api/chat/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sender_id: state.currentUser.id,
          receiver_id: friendId,
          message: `⚔️ Sizni 1v1 bellashuvga taklif qildim! Xona kodi: ${roomCode}`,
          battle_room_code: roomCode
        })
      });

      alert(`⚔️ ${friendName} do'stingizga taklif yuborildi! Xona kodi: ${roomCode}`);
      navigateTo('battle');
      battleState.isHost = true;
      connectToBattleWebSocket(roomCode);
    }
  } catch (e) {
    alert("Batl yaratishda xatolik!");
  }
}

function joinBattleFromChat(roomCode) {
  closeFriendChatModal();
  navigateTo('battle');
  battleState.isHost = false;
  connectToBattleWebSocket(roomCode);
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// ================= STUDENT TEST RUNNER & ACCESS =================
let activeQuizRunnerSession = null;

async function startStudentQuizWithCredentials() {
  playSound('click');
  const pinInput = document.getElementById('quickQuizPinInput');
  const passInput = document.getElementById('quickQuizPasscodeInput');

  const pinCode = (pinInput ? pinInput.value : '').trim().toUpperCase();
  const passcode = (passInput ? passInput.value : '').trim();

  if (!pinCode) {
    alert("Iltimos, ustoz bergan Test KODI (Login/PIN)ni kiriting! Masalan: MATH-739");
    if (pinInput) pinInput.focus();
    return;
  }

  if (!passcode) {
    alert("Iltimos, Test PAROLIni kiriting! Masalan: 4821");
    if (passInput) passInput.focus();
    return;
  }

  await verifyAndLaunchQuiz(pinCode, passcode);
}

function promptQuizAccess() {
  playSound('click');
  const pinCode = prompt("Ustozingiz bergan Test KODI (Login/PIN)ni kiriting:\n(Masalan: MATH-739 yoki QZ-102)");
  if (!pinCode) return;
  const passcode = prompt(`"${pinCode.toUpperCase()}" testi uchun PAROLni kiriting:`);
  if (!passcode) return;
  verifyAndLaunchQuiz(pinCode.trim().toUpperCase(), passcode.trim());
}

async function verifyAndLaunchQuiz(pinCode, passcode) {
  try {
    const res = await fetch('/api/quiz/verify-access', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        pin_code: pinCode,
        passcode: passcode
      })
    });

    const data = await res.json();
    if (!res.ok) {
      playSound('wrong');
      alert(data.detail || "Testga kirishda xatolik! Kod yoki parolni tekshiring.");
      return;
    }

    if (data.quiz) {
      openQuizBotRunner(data.quiz);
    }
  } catch (e) {
    alert("Test tizimiga ulanishda server xatosi!");
  }
}

function openQuizBotRunner(quiz) {
  playSound('click');
  if (!quiz || !quiz.questions || quiz.questions.length === 0) {
    alert("Ushbu testda hali savollar mavjud emas!");
    return;
  }

  activeQuizRunnerSession = {
    quizId: quiz.id,
    title: quiz.title || 'Viktorina',
    pinCode: quiz.pin_code,
    questions: quiz.questions,
    currentIndex: 0,
    score: 0,
    correctCount: 0,
    wrongCount: 0,
    timeLimitSec: quiz.time_limit_sec || 30,
    timeLeft: quiz.time_limit_sec || 30,
    timerInterval: null,
    autoAdvanceTimeout: null,
    answered: false,
    startTime: Date.now()
  };

  document.getElementById('quizRunnerPinBadge').textContent = `KOD: ${quiz.pin_code}`;
  document.getElementById('quizRunnerTopicLabel').textContent = quiz.title;
  document.getElementById('quizBotRunnerActiveState').style.display = 'flex';
  document.getElementById('quizBotRunnerFinishState').style.display = 'none';

  document.getElementById('quizBotRunnerModal').classList.add('active');
  renderQuizRunnerCurrentQuestion();
}

function renderQuizRunnerCurrentQuestion() {
  if (!activeQuizRunnerSession) return;
  if (activeQuizRunnerSession.timerInterval) clearInterval(activeQuizRunnerSession.timerInterval);
  if (activeQuizRunnerSession.autoAdvanceTimeout) clearTimeout(activeQuizRunnerSession.autoAdvanceTimeout);

  const total = activeQuizRunnerSession.questions.length;
  if (activeQuizRunnerSession.currentIndex >= total) {
    finishQuizRunnerSession();
    return;
  }

  activeQuizRunnerSession.answered = false;
  const q = activeQuizRunnerSession.questions[activeQuizRunnerSession.currentIndex];

  document.getElementById('quizRunnerProgressText').textContent = `Savol ${activeQuizRunnerSession.currentIndex + 1} / ${total}`;
  document.getElementById('quizRunnerQuestionText').textContent = q.question_text;
  
  // Hide explanation and next button
  document.getElementById('quizRunnerExplanationBox').style.display = 'none';
  document.getElementById('quizRunnerNextBtnContainer').style.display = 'none';

  // Render options
  const listEl = document.getElementById('quizRunnerOptionsList');
  const letters = ['A', 'B', 'C', 'D', 'E', 'F'];
  const opts = q.options || [];

  listEl.innerHTML = opts.map((opt, idx) => `
    <button class="quiz-runner-option-btn" id="quizRunnerBtn_${idx}" onclick="answerQuizRunnerQuestion(${idx})">
      <span style="font-weight:800; color:var(--text-muted); width:24px;">${letters[idx] || (idx+1)})</span>
      <span style="flex:1;">${escapeHtml(opt)}</span>
      <span class="quiz-runner-status-icon" id="quizRunnerIcon_${idx}" style="font-size:16px;"></span>
    </button>
  `).join('');

  // Start countdown timer
  activeQuizRunnerSession.timeLeft = activeQuizRunnerSession.timeLimitSec;
  const timerNum = document.getElementById('quizRunnerTimerNum');
  timerNum.textContent = activeQuizRunnerSession.timeLeft;

  activeQuizRunnerSession.timerInterval = setInterval(() => {
    activeQuizRunnerSession.timeLeft -= 1;
    timerNum.textContent = activeQuizRunnerSession.timeLeft;

    if (activeQuizRunnerSession.timeLeft <= 0) {
      clearInterval(activeQuizRunnerSession.timerInterval);
      answerQuizRunnerQuestion(-1); // Timed out
    }
  }, 1000);
}

function answerQuizRunnerQuestion(choiceIdx) {
  if (!activeQuizRunnerSession || activeQuizRunnerSession.answered) return;
  activeQuizRunnerSession.answered = true;
  if (activeQuizRunnerSession.timerInterval) clearInterval(activeQuizRunnerSession.timerInterval);

  const q = activeQuizRunnerSession.questions[activeQuizRunnerSession.currentIndex];
  const correctIdx = typeof q.correct_index === 'number' ? q.correct_index : 0;
  const isCorrect = (choiceIdx === correctIdx);

  // Disable all option buttons
  const opts = q.options || [];
  opts.forEach((_, idx) => {
    const btn = document.getElementById(`quizRunnerBtn_${idx}`);
    if (btn) btn.disabled = true;
  });

  // Highlight chosen and correct options
  const correctBtn = document.getElementById(`quizRunnerBtn_${correctIdx}`);
  const correctIcon = document.getElementById(`quizRunnerIcon_${correctIdx}`);
  if (correctBtn) {
    correctBtn.classList.add('correct');
    if (correctIcon) correctIcon.textContent = '✅';
  }

  if (isCorrect) {
    playSound('correct');
    activeQuizRunnerSession.correctCount += 1;
  } else {
    playSound('wrong');
    activeQuizRunnerSession.wrongCount += 1;
    if (choiceIdx >= 0) {
      const chosenBtn = document.getElementById(`quizRunnerBtn_${choiceIdx}`);
      const chosenIcon = document.getElementById(`quizRunnerIcon_${choiceIdx}`);
      if (chosenBtn) {
        chosenBtn.classList.add('wrong');
        if (chosenIcon) chosenIcon.textContent = '❌';
      }
    }
  }

  // Explanation Bubble
  const expl = (q.explanation || '').trim();
  if (expl) {
    const explBox = document.getElementById('quizRunnerExplanationBox');
    const explText = document.getElementById('quizRunnerExplanationText');
    explText.textContent = expl;
    explBox.style.display = 'block';
  }

  // Show "Keyingi Savol ➔" button
  const nextBtnContainer = document.getElementById('quizRunnerNextBtnContainer');
  if (nextBtnContainer) nextBtnContainer.style.display = 'block';

  // Auto-advance after delay
  const delay = expl ? 2600 : 1800;
  activeQuizRunnerSession.autoAdvanceTimeout = setTimeout(() => {
    quizRunnerAdvanceNext();
  }, delay);
}

function quizRunnerAdvanceNext() {
  if (!activeQuizRunnerSession) return;
  if (activeQuizRunnerSession.autoAdvanceTimeout) clearTimeout(activeQuizRunnerSession.autoAdvanceTimeout);
  activeQuizRunnerSession.currentIndex += 1;
  renderQuizRunnerCurrentQuestion();
}

async function finishQuizRunnerSession() {
  if (!activeQuizRunnerSession) return;
  if (activeQuizRunnerSession.timerInterval) clearInterval(activeQuizRunnerSession.timerInterval);
  if (activeQuizRunnerSession.autoAdvanceTimeout) clearTimeout(activeQuizRunnerSession.autoAdvanceTimeout);

  const total = activeQuizRunnerSession.questions.length;
  const correct = activeQuizRunnerSession.correctCount;
  const wrong = activeQuizRunnerSession.wrongCount;
  const scorePct = total > 0 ? Math.round((correct / total) * 100) : 0;
  const timeSpentSec = Math.round((Date.now() - activeQuizRunnerSession.startTime) / 1000);

  // Submit to server
  try {
    await fetch('/api/quiz/submit-result', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        student_id: state.currentUser ? state.currentUser.id : null,
        quiz_id: activeQuizRunnerSession.quizId,
        correct_count: correct,
        total_questions: total,
        time_spent_sec: timeSpentSec
      })
    });
  } catch (e) {
    console.warn("Could not submit quiz result to server:", e);
  }

  // Determine Letter Grade
  let gradeLetter = "5 (A'lo) ⭐⭐⭐⭐⭐";
  let gradeColor = "var(--accent-green)";
  let emoji = "🏆";
  if (scorePct >= 86) {
    gradeLetter = "5 (A'lo) ⭐⭐⭐⭐⭐";
    gradeColor = "#10b981";
    emoji = "🥇";
  } else if (scorePct >= 71) {
    gradeLetter = "4 (Yaxshi) ⭐⭐⭐⭐";
    gradeColor = "#3b82f6";
    emoji = "🥈";
  } else if (scorePct >= 56) {
    gradeLetter = "3 (Qoniqarli) ⭐⭐⭐";
    gradeColor = "#f59e0b";
    emoji = "🥉";
  } else {
    gradeLetter = "2 (Qoniqarsiz) ⚠️";
    gradeColor = "#e11d48";
    emoji = "📚";
  }

  document.getElementById('quizRunnerFinishEmoji').textContent = emoji;
  document.getElementById('quizRunnerScoreNumber').textContent = `${scorePct} / 100`;
  const gradeBadge = document.getElementById('quizRunnerGradeBadge');
  gradeBadge.textContent = gradeLetter;
  gradeBadge.style.color = gradeColor;

  document.getElementById('quizRunnerCorrectCount').textContent = correct;
  document.getElementById('quizRunnerWrongCount').textContent = wrong;
  document.getElementById('quizRunnerTimeSpent').textContent = `${timeSpentSec}s`;

  document.getElementById('quizBotRunnerActiveState').style.display = 'none';
  document.getElementById('quizBotRunnerFinishState').style.display = 'block';

  playSound('victory');

  // Refresh user profile/stats if student is logged in
  if (state.currentUser) {
    fetch(`/api/user/${state.currentUser.id}`)
      .then(r => r.json())
      .then(u => {
        if (u && !u.detail) {
          state.currentUser = u;
          localStorage.setItem('edubattle_user', JSON.stringify(u));
          updateUIForUser();
        }
      }).catch(() => {});
  }
}

function exitQuizBotRunner() {
  if (activeQuizRunnerSession && activeQuizRunnerSession.timerInterval) {
    clearInterval(activeQuizRunnerSession.timerInterval);
  }
  if (activeQuizRunnerSession && activeQuizRunnerSession.autoAdvanceTimeout) {
    clearTimeout(activeQuizRunnerSession.autoAdvanceTimeout);
  }
  activeQuizRunnerSession = null;
  closeModal('quizBotRunnerModal');
}

function showQuizLeaderboardFromRunner() {
  if (!activeQuizRunnerSession) return;
  const qId = activeQuizRunnerSession.quizId;
  closeModal('quizBotRunnerModal');
  if (typeof showQuizLeaderboard === 'function') {
    showQuizLeaderboard(qId);
  }
}

if (document.readyState === 'loading') {
  window.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}


// ----------------- COPY USER ID HELPER -----------------
function copyMyUserId() {
  if (!state.currentUser) return;
  const u = state.currentUser;
  let userEBId = (u.username && u.username.startsWith('EB-')) ? u.username : (u.eb_id && u.eb_id.startsWith('EB-') ? u.eb_id : null);
  if (!userEBId) {
    const rawNum = u.id ? Math.abs(parseInt(u.id, 10)) : 0;
    const ebNum = (rawNum && !isNaN(rawNum)) ? ((rawNum * 1337 + 12345) % 90000 + 10000) : Math.floor(10000 + Math.random() * 90000);
    userEBId = 'EB-' + ebNum;
  }
  try {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(userEBId);
    }
  } catch (e) {}

  const idEl = document.getElementById('profileUserIdDisplay');
  if (idEl) {
    const orig = idEl.textContent;
    idEl.textContent = 'Nusxalandi! ✓';
    setTimeout(() => { idEl.textContent = orig; }, 1500);
  }
  const teacherIdPill = document.getElementById('teacherIdPill');
  if (teacherIdPill) {
    const origT = teacherIdPill.textContent;
    teacherIdPill.textContent = 'Nusxalandi! ✓';
    setTimeout(() => { teacherIdPill.textContent = origT; }, 1500);
  }
}

// ----------------- TEACHER & STUDENT ROLE SWITCHERS -----------------
async function switchToTeacherRole() {
  playSound('click');
  if (!state.currentUser) return;
  state.currentUser.role = 'teacher';
  state.currentUser.is_pro = 1;
  localStorage.setItem('edubattle_user', JSON.stringify(state.currentUser));
  
  try {
    if (state.currentUser.id) {
      await fetch('/api/user/role', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: state.currentUser.id, role: 'teacher' })
      });
    }
  } catch (e) {}
  
  updateHeaderAndProfileUI();
  updateBottomNavForRole('teacher');
  navigateTo('teacher', true);
  showToast("👨‍🏫 O'qituvchi Kabineti faollashtirildi! Xush kelibsiz, Ustoz!");
}

async function switchToStudentRole() {
  playSound('click');
  if (!state.currentUser) return;
  state.currentUser.role = 'student';
  localStorage.setItem('edubattle_user', JSON.stringify(state.currentUser));
  
  try {
    if (state.currentUser.id) {
      await fetch('/api/user/role', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ user_id: state.currentUser.id, role: 'student' })
      });
    }
  } catch (e) {}
  
  updateHeaderAndProfileUI();
  updateBottomNavForRole('student');
  navigateTo('home', true);
  showToast("👨‍🎓 O'quvchi rejimiga o'tildi.");
}

function openOrDownloadPdf(pdfUrl, bookTitle) {
  if (typeof playSound === 'function') playSound('click');
  const fullUrl = pdfUrl.startsWith('http') ? pdfUrl : (window.location.origin + pdfUrl);
  if (window.Telegram && window.Telegram.WebApp && typeof window.Telegram.WebApp.openLink === 'function') {
    window.Telegram.WebApp.openLink(fullUrl);
    return;
  }
  const a = document.createElement('a');
  a.href = fullUrl;
  a.download = (bookTitle || 'darslik').replace(/[^a-zA-Z0-9_-]/g, '_') + '.pdf';
  a.target = '_blank';
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    if (a.parentNode) a.parentNode.removeChild(a);
  }, 500);
}


// ========================================================
// JONLI GLOBAL BLITZ TURNIR & KUNLIK TEST LIMITI MODULE
// ========================================================

let activeBlitzSubjectId = 1;
let blitzTickerInterval = null;
let currentBlitzSecondsLeft = 60;
let currentBlitzMinuteEpoch = 0;
let currentBlitzQuestionData = null;

const BLITZ_SUBJECTS = [
  { id: 1, name: "Matematika", icon: "📐" },
  { id: 2, name: "Fizika", icon: "⚡" },
  { id: 3, name: "Kimyo", icon: "🧪" },
  { id: 4, name: "Biologiya", icon: "🧬" },
  { id: 5, name: "Ona tili", icon: "📖" },
  { id: 6, name: "Tarix", icon: "🏛️" },
  { id: 7, name: "Ingliz tili", icon: "🇬🇧" },
  { id: 8, name: "Informatika", icon: "💻" },
  { id: 9, name: "Huquq", icon: "⚖️" }
];

function initBlitzView() {
  renderBlitzSubjectChips();
  loadCurrentBlitzQuestion(activeBlitzSubjectId);
  startBlitzCountdownTicker();
}

function renderBlitzSubjectChips() {
  const container = document.getElementById('blitzSubjectChips');
  if (!container) return;

  container.innerHTML = BLITZ_SUBJECTS.map(s => `
    <div class="blitz-chip ${s.id === activeBlitzSubjectId ? 'active' : ''}" onclick="selectBlitzSubject(${s.id})">
      <span>${s.icon}</span>
      <span>${escapeHtml(s.name)}</span>
    </div>
  `).join('');
}

function selectBlitzSubject(subjectId) {
  if (typeof playSound === 'function') playSound('click');
  activeBlitzSubjectId = subjectId;
  renderBlitzSubjectChips();

  const sub = BLITZ_SUBJECTS.find(x => x.id === subjectId) || BLITZ_SUBJECTS[0];
  const iconEl = document.getElementById('blitzSubjectIcon');
  const nameEl = document.getElementById('blitzSubjectName');
  if (iconEl) iconEl.textContent = sub.icon;
  if (nameEl) nameEl.textContent = sub.name;

  loadCurrentBlitzQuestion(subjectId);
}

async function loadCurrentBlitzQuestion(subjectId) {
  const qTextEl = document.getElementById('blitzQuestionText');
  const gridEl = document.getElementById('blitzOptionsGrid');
  const feedbackEl = document.getElementById('blitzFeedbackBox');

  if (feedbackEl) feedbackEl.style.display = 'none';
  if (qTextEl) qTextEl.innerHTML = '<span style="color:var(--text-muted);">Sinxron savol yuklanmoqda...</span>';
  if (gridEl) gridEl.innerHTML = '';

  const userId = state.currentUser ? state.currentUser.id : 0;
  try {
    const res = await fetch(`/api/blitz/current?subject_id=${subjectId}&user_id=${userId}&_t=${Date.now()}`, {
      cache: 'no-store'
    });
    if (!res.ok) throw new Error("Yuklab bo'lmadi");
    const data = await res.json();
    currentBlitzQuestionData = data;
    currentBlitzSecondsLeft = data.seconds_left || 60;
    currentBlitzMinuteEpoch = data.minute_epoch;

    renderBlitzQuestionData(data);
  } catch (err) {
    if (qTextEl) qTextEl.textContent = "Hozircha ushbu fandan savollar mavjud emas.";
  }
}

function renderBlitzQuestionData(data) {
  const qTextEl = document.getElementById('blitzQuestionText');
  const gridEl = document.getElementById('blitzOptionsGrid');
  const chapterEl = document.getElementById('blitzChapterTitle');
  const feedbackEl = document.getElementById('blitzFeedbackBox');

  if (chapterEl) chapterEl.textContent = data.chapter_title || "Blitz Savol";
  if (qTextEl) qTextEl.textContent = data.question_text || "Savol";

  const letters = ['A', 'B', 'C', 'D'];
  const opts = data.options || [];

  if (gridEl) {
    gridEl.innerHTML = opts.map((optText, idx) => {
      let extraClass = '';
      let disabled = data.already_answered ? 'disabled' : '';

      if (data.already_answered) {
        if (data.user_answer === idx) {
          extraClass = data.is_correct ? 'correct' : 'wrong';
        }
      }

      return `
        <button class="blitz-option-btn ${extraClass}" ${disabled} onclick="submitBlitzChoice(${idx})">
          <div class="blitz-opt-letter">${letters[idx]}</div>
          <div style="flex:1;">${escapeHtml(optText)}</div>
        </button>
      `;
    }).join('');
  }

  if (data.already_answered && feedbackEl) {
    const msgEl = document.getElementById('blitzFeedbackMsg');
    const expEl = document.getElementById('blitzExplanationText');
    const cardEl = document.getElementById('blitzFeedbackCard');

    feedbackEl.style.display = 'block';
    if (data.is_correct) {
      if (cardEl) { cardEl.className = 'minimal-card highlight-green'; }
      if (msgEl) msgEl.innerHTML = `✅ TO'G'RI JAVOB! (Keyingi sinxron savolga qoldi: <span id="blitzWaitSec">${currentBlitzSecondsLeft}s</span>)`;
    } else {
      if (cardEl) { cardEl.className = 'minimal-card highlight-red'; }
      if (msgEl) msgEl.innerHTML = `❌ NOTO'G'RI. (Keyingi savolga qoldi: <span id="blitzWaitSec">${currentBlitzSecondsLeft}s</span>)`;
    }
    if (expEl) expEl.textContent = data.explanation || "Daqiqa tugagach, avtomatik yangi savol chiqadi.";
  }
}

async function submitBlitzChoice(selectedIndex) {
  if (!state.currentUser) {
    if (typeof openAuthModal === 'function') openAuthModal();
    return;
  }

  if (!currentBlitzQuestionData || currentBlitzQuestionData.already_answered) return;

  const buttons = document.querySelectorAll('.blitz-option-btn');
  buttons.forEach(b => b.disabled = true);

  try {
    const res = await fetch('/api/blitz/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: state.currentUser.id,
        subject_id: activeBlitzSubjectId,
        minute_epoch: currentBlitzMinuteEpoch,
        selected_index: selectedIndex
      })
    });

    const result = await res.json();
    if (res.ok && result.success) {
      currentBlitzQuestionData.already_answered = true;
      currentBlitzQuestionData.user_answer = selectedIndex;
      currentBlitzQuestionData.is_correct = result.is_correct;
      currentBlitzQuestionData.explanation = result.explanation;

      if (result.is_correct) {
        if (typeof playSound === 'function') playSound('correct');
        if (buttons[selectedIndex]) buttons[selectedIndex].classList.add('correct');
        showCoinRewardPopup(result.coins_earned);
      } else {
        if (typeof playSound === 'function') playSound('wrong');
        if (buttons[selectedIndex]) buttons[selectedIndex].classList.add('wrong');
        if (buttons[result.correct_index]) buttons[result.correct_index].classList.add('correct');
      }

      // Update user state coins
      if (state.currentUser) {
        state.currentUser.coins = result.new_coins;
        state.currentUser.xp = 0;
        localStorage.setItem('edubattle_user', JSON.stringify(state.currentUser));
        updateHomeDailyLimitBadge();
        updateHeaderAndProfileUI();
      }

      // Show explanation
      const feedbackEl = document.getElementById('blitzFeedbackBox');
      const msgEl = document.getElementById('blitzFeedbackMsg');
      const expEl = document.getElementById('blitzExplanationText');
      const cardEl = document.getElementById('blitzFeedbackCard');

      if (feedbackEl) feedbackEl.style.display = 'block';
      if (result.is_correct) {
        if (cardEl) cardEl.className = 'minimal-card highlight-green';
        if (msgEl) msgEl.innerHTML = `🎉 TO'G'RI JAVOB! +${result.coins_earned} 🪙 Tanga qo'shildi!`;
      } else {
        if (cardEl) cardEl.className = 'minimal-card highlight-red';
        if (msgEl) msgEl.innerHTML = `❌ Noto'g'ri javob.`;
      }
      if (expEl) expEl.textContent = result.explanation || "";
    } else {
      alert(result.message || "Xatolik yuz berdi!");
      buttons.forEach(b => b.disabled = false);
    }
  } catch (e) {
    alert("Serverga ulanishda xatolik!");
    buttons.forEach(b => b.disabled = false);
  }
}

function startBlitzCountdownTicker() {
  if (blitzTickerInterval) clearInterval(blitzTickerInterval);

  blitzTickerInterval = setInterval(() => {
    const now = Date.now();
    const currentEpochMin = Math.floor(now / 60000);
    const sec = 60 - (Math.floor(now / 1000) % 60);
    currentBlitzSecondsLeft = sec;

    const timerVal = document.getElementById('blitzTimerVal');
    if (timerVal) {
      const formatted = (sec < 10 ? '0' : '') + sec;
      timerVal.textContent = `00:${formatted}`;
      if (sec <= 10) {
        timerVal.style.color = '#ef4444';
      } else {
        timerVal.style.color = '#f59e0b';
      }
    }

    const waitEl = document.getElementById('blitzWaitSec');
    if (waitEl) waitEl.textContent = `${sec}s`;

    // Critical live sync: If current minute epoch has changed (e.g. app was paused in background),
    // OR if second rolls over to 0/60, immediately fetch the live current synchronized question!
    if (currentBlitzMinuteEpoch && currentEpochMin !== currentBlitzMinuteEpoch) {
      loadCurrentBlitzQuestion(activeBlitzSubjectId);
    } else if (sec === 60 || sec === 0) {
      loadCurrentBlitzQuestion(activeBlitzSubjectId);
    }
  }, 1000);
}

// Background resume listener: instantly syncs the question when user switches back to app
document.addEventListener('visibilitychange', () => {
  if (!document.hidden && state.currentView === 'blitz') {
    const nowMin = Math.floor(Date.now() / 60000);
    if (!currentBlitzMinuteEpoch || nowMin !== currentBlitzMinuteEpoch) {
      loadCurrentBlitzQuestion(activeBlitzSubjectId);
    }
    startBlitzCountdownTicker();
  }
});

window.addEventListener('focus', () => {
  if (state.currentView === 'blitz') {
    const nowMin = Math.floor(Date.now() / 60000);
    if (!currentBlitzMinuteEpoch || nowMin !== currentBlitzMinuteEpoch) {
      loadCurrentBlitzQuestion(activeBlitzSubjectId);
    }
  }
});

function showCoinRewardPopup(coins) {
  const toast = document.createElement('div');
  toast.style.cssText = `
    position: fixed;
    top: 24%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: linear-gradient(135deg, #f59e0b, #d97706);
    color: #000;
    padding: 12px 24px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: 900;
    box-shadow: 0 8px 32px rgba(245, 158, 11, 0.6);
    z-index: 99999;
    pointer-events: none;
    animation: coinPulseFloat 1.8s forwards;
  `;
  toast.innerHTML = `🪙 +${coins} TANGA!`;
  document.body.appendChild(toast);
  setTimeout(() => {
    if (toast.parentNode) toast.parentNode.removeChild(toast);
  }, 1800);
}

async function updateHomeDailyLimitBadge() {
  const user = state.currentUser;
  const coinsEl = document.getElementById('homeCoinsText');
  const limitEl = document.getElementById('homeDailyLimitText');

  if (user) {
    if (coinsEl) coinsEl.textContent = (user.coins || 0).toLocaleString();

    const isTeacher = user.role === 'teacher' || user.role === 'admin';
    const isPro = user.is_pro === 1 || user.is_pro === true;

    if (isTeacher || isPro) {
      if (limitEl) {
        limitEl.textContent = "👑 Cheksiz (PRO)";
        limitEl.style.color = "#f59e0b";
      }
      return;
    }

    try {
      const res = await fetch(`/api/user-test-limit/${user.id}`);
      if (res.ok) {
        const data = await res.json();
        if (limitEl) {
          limitEl.textContent = `${data.today_count}/2 test`;
          limitEl.style.color = (data.today_count >= 2) ? "#ef4444" : "#10b981";
        }
      }
    } catch (e) {}
  }
}

function checkDailyTestLimit() {
  const user = state.currentUser;
  if (!user) {
    if (typeof openAuthModal === 'function') openAuthModal();
    return;
  }
  const isTeacher = user.role === 'teacher' || user.role === 'admin';
  const isPro = user.is_pro === 1 || user.is_pro === true;
  if (!isTeacher && !isPro) {
    openModal('proLimitModal');
  } else {
    alert("👑 Sizda PRO obuna faol! Siz cheklovsiz testlar va barcha imkoniyatlardan foydalanishingiz mumkin.");
  }
}

function openProPurchaseFromLimitModal() {
  closeModal('proLimitModal');
  if (typeof playSound === 'function') playSound('click');
  const user = state.currentUser;
  const targetId = user ? user.id : 0;
  const buyUrl = `https://t.me/edubattleuz_bot?start=buy_pro_${targetId}`;
  if (window.Telegram && window.Telegram.WebApp && typeof window.Telegram.WebApp.openTelegramLink === 'function') {
    window.Telegram.WebApp.openTelegramLink(buyUrl);
  } else {
    window.open(buyUrl, '_blank');
  }
}
