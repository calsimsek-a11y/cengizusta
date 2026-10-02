"""Hizmet ve semt sayfalarının içeriği. derle.py bu listeden /<yol>/index.html üretir.

Kural: doğrulanmamış iddia yok (yıl, müşteri sayısı, garanti, sertifika yazma).
Her sayfanın metni kendine özgü olmalı; semt adını değiştirip aynı metni çoğaltma.
"""

HIZMET_SAYFALARI = [
    {
        "yol": "boya-badana",
        "tur": "hizmet",
        "menu": "Boya & Badana",
        "hizmet": "Boya ve badana",
        "baslik": "İstanbul Boya Badana Ustası | Ev ve İşyeri Boyama – Cengiz Usta",
        "aciklama": "Beyoğlu, Taksim, Şişli, Beşiktaş ve Fatih'te ev ve işyeri boya badana. Yüzey hazırlığı, macun, astar ve temiz teslim. Cengiz Usta: 0542 800 32 63.",
        "etiket": "Boya & Badana",
        "h1": "İstanbul’da Boya Badana Ustası",
        "giris": "Odanızı, dairenizi ya da dükkânınızı boyatmak mı istiyorsunuz? Cengiz Usta yüzeyi hazırlamadan boyaya geçmez; eşyalarınızı örter, işi bitirince ortalığı temiz bırakır.",
        "gorsel": ("beyoglu-boya-badana-ustasi", "İstanbul'da bir dairede duvarı rulo ile boyayan boya badana ustası Cengiz Usta"),
        "bolumler": [
            ("Boya işi nasıl yapılıyor?", [
                "İyi bir boyanın yarısı hazırlıktır. Önce mobilyalar ortaya toplanır, zemin ve eşyalar naylonla örtülür, priz ve kapı kasaları bantlanır.",
                "Ardından duvardaki çatlak, delik ve kabarmalar kazınır, macunla doldurulur ve zımparalanır. Gerekiyorsa astar atılır; son olarak iki kat boya uygulanır. Böylece boya hem düzgün görünür hem de daha uzun dayanır.",
            ]),
            ("Hangi boya işlerini yapıyoruz?", [
                "Tek oda boyasından komple daire boyasına, tavan badanasından kapı ve pencere kasası boyasına kadar iç mekân boya işlerinin hepsi için arayabilirsiniz. Kiracı çıkışı ya da taşınma öncesi daire yenileme, ofis ve dükkân boyası da yaptığımız işler arasında.",
                "Rutubet lekesi ya da sararma olan tavanlarda önce lekenin sebebine bakarız; leke tutucu astar kullanmadan üstüne boya atmak lekenin kısa sürede geri gelmesine yol açar.",
            ]),
            ("Boya rengi ve malzeme", [
                "Kullanılacak boyanın markasını ve rengini birlikte seçeriz. Kendi seçtiğiniz bir boya varsa onunla da çalışırız. Fiyatı belirleyen başlıca şeyler duvar metrekaresi, yüzeyin durumu ve kullanılacak boyadır; bu yüzden fiyatı işi gördükten ya da fotoğrafını aldıktan sonra konuşuyoruz.",
            ]),
        ],
        "maddeler": ["Oda ve daire boyası", "Tavan badanası", "Kapı, pencere ve kasa boyası", "Rutubet ve lekeli duvar hazırlığı", "Ofis ve dükkân boyası", "Kiracı çıkışı daire yenileme"],
        "sss": [
            ("Eşyalı evde boya yapılabilir mi?", "Evet. Eşyalar odanın ortasına toplanıp örtülür, zemin korunur. Oda oda ilerleyerek evde yaşamaya devam etmenizi zorlaştırmamaya çalışırız."),
            ("Boya kaç günde biter?", "Bu, oda sayısına ve duvarların durumuna bağlı. İşi gördükten sonra size yaklaşık süreyi baştan söyleriz."),
            ("Boya kokusu ne kadar sürer?", "Kullanılan boyaya göre değişir. İş bittikten sonra odaları bir süre havalandırmanız yeterli olur; kokusu az boya tercih etmek isterseniz bunu baştan konuşabiliriz."),
        ],
    },
    {
        "yol": "tadilat",
        "tur": "hizmet",
        "menu": "Tadilat",
        "hizmet": "Ev ve işyeri tadilatı",
        "baslik": "Ev ve İşyeri Tadilatı İstanbul | Taksim, Beyoğlu – Cengiz Usta",
        "aciklama": "Taksim, Beyoğlu, Şişli ve çevresinde ev, daire ve dükkân tadilatı. Ölçü, planlama ve uygulama doğrudan ustayla. Cengiz Usta: 0542 800 32 63.",
        "etiket": "Tadilat",
        "h1": "Ev ve İşyeri Tadilatı",
        "giris": "Dairenizi kiraya vermeden önce yenilemek, dükkânınızı yeni sezona hazırlamak ya da yıpranmış bir odayı toparlamak… Tadilatı aracı olmadan, işi yapacak ustayla konuşarak planlayın.",
        "gorsel": ("ev-tadilati-olcu-alma", "Taksim'de ev tadilatı öncesi duvar ölçüsü alan tadilat ustası Cengiz Usta"),
        "bolumler": [
            ("Tadilata nereden başlıyoruz?", [
                "Önce yerinde bakıp ölçü alırız. Ne yapılmak istendiğini, bütçeyi ve süreyi birlikte konuşuruz. Hangi işin önce yapılması gerektiğini (örneğin önce sıva, sonra boya) baştan sıraya koyarız ki iş yarıda tıkanmasın.",
                "Tadilat sırasında evde oturmaya devam edecekseniz çalışılacak alanları buna göre planlarız.",
            ]),
            ("Ne tür tadilat işleri?", [
                "Duvar ve tavan düzeltme, sıva yenileme, alçı ve boya işleri, kiralık daire ya da dükkânların teslim öncesi yenilenmesi, küçük onarımlar ve yıpranmış alanların toparlanması yaptığımız işlerin başında gelir.",
                "İşin bir kısmı farklı bir uzmanlık gerektiriyorsa bunu açıkça söyler, ona göre plan yaparız.",
            ]),
            ("Apartmanda tadilat yaparken", [
                "Eski apartmanlarda malzemenin merdivenden taşınması, gürültülü işlerin saatleri ve molozun toplanması komşularla sorun çıkmaması için önceden planlanır. Gerekirse apartman yönetimine bilgi verilmesini de baştan konuşuruz.",
            ]),
        ],
        "maddeler": ["Daire yenileme", "Dükkân ve ofis yenileme", "Kiracı çıkışı tadilat", "Sıva, alçı ve boya", "Duvar ve tavan düzeltme", "Küçük onarım işleri"],
        "sss": [
            ("Tadilat için keşif ücretli mi?", "Ön görüşme ücretsizdir. İşi telefonda ya da WhatsApp'tan gönderdiğiniz fotoğraflarla konuşur, gerekirse yerinde bakarız."),
            ("Malzemeyi kim alıyor?", "İki türlü de çalışılabilir: malzemeyi biz temin edebiliriz ya da sizin seçtiğiniz malzemeyle çalışırız. Bunu fiyat konuşurken netleştiririz."),
            ("İşyerinde mesai dışında çalışılabilir mi?", "Dükkân ve ofislerde işin müşterilerinizi etkilememesi için çalışma saatlerini birlikte planlayabiliriz."),
        ],
    },
    {
        "yol": "cati-tamiri",
        "tur": "hizmet",
        "menu": "Çatı Tamiri",
        "hizmet": "Çatı tamiri",
        "baslik": "İstanbul Çatı Tamiri | Akan ve Su Alan Çatı Onarımı – Cengiz Usta",
        "aciklama": "Beyoğlu ve İstanbul merkezde çatı tamiri: kırık kiremit, akan ve su alan çatı, teras ve çatı bakımı. Cengiz Usta ile doğrudan görüşün: 0542 800 32 63.",
        "etiket": "Çatı Tamiri",
        "h1": "İstanbul’da Çatı Tamiri ve Akan Çatı Onarımı",
        "giris": "Tavanda su izi mi var, yağmurda damlıyor mu? Çatı tamirinde önce suyun nereden girdiğini bulmak gerekir. Cengiz Usta sorunun kaynağına bakar, sonra onarır.",
        "gorsel": ("istanbul-kiremit-cati-tamiri", "İstanbul'da emniyet kemeriyle kiremit çatı tamiri yapan Cengiz Usta"),
        "bolumler": [
            ("Çatı neden su alır?", [
                "En sık görülen sebepler kırık ya da kaymış kiremitler, baca dibi ve duvar birleşimlerindeki açılmalar, tıkanmış oluklar ve teraslarda yıpranmış su yalıtımıdır. Su çoğu zaman tavandaki lekenin tam üstünden değil, biraz uzaktan girer; bu yüzden tahminle değil, bakarak çalışmak gerekir.",
            ]),
            ("Çatı tamirinde neler yapıyoruz?", [
                "Kırık ve kaymış kiremitlerin değiştirilmesi, mahya ve kenar onarımı, baca ve duvar dibi birleşimlerinin elden geçirilmesi, oluk temizliği ve teras çatılarda yalıtım kontrolü yaptığımız işler arasında.",
                "Çatıda emniyet ekipmanıyla çalışılır. Yağmurlu ve rüzgârlı havada çatıya çıkılmaz; acil durumlarda geçici önlemi konuşuruz.",
            ]),
            ("Kışa girmeden çatı bakımı", [
                "Sonbaharda yapılan kısa bir kontrol, kışın akan bir çatıyla uğraşmaktan çok daha kolaydır. Özellikle Beyoğlu, Cihangir ve Fatih'teki eski kiremit çatılı binalarda yağmur mevsiminden önce bakım yaptırmanızı öneririz.",
            ]),
        ],
        "maddeler": ["Kırık kiremit değişimi", "Akan çatı onarımı", "Su alan teras kontrolü", "Baca dibi ve duvar birleşimi", "Oluk temizliği", "Kış öncesi çatı bakımı"],
        "sss": [
            ("Çatım akıyor, ne göndermeliyim?", "Tavandaki lekenin, varsa çatının ve binanın dışarıdan görünen fotoğraflarını WhatsApp'tan gönderin. Böylece sorunun ne olabileceğini önceden konuşabiliriz."),
            ("Yağmur yağarken çatı tamiri yapılır mı?", "Güvenlik için yağmurlu havada çatıda çalışılmaz. Acil bir durumda suyun içeri girmesini azaltacak geçici önlemleri konuşur, kalıcı onarımı hava açınca yaparız."),
            ("Apartman çatısı için kiminle görüşmeliyim?", "Ortak alan olduğu için genelde apartman yöneticisiyle birlikte karar verilir. Yöneticinize bilgi vermemiz gerekirse yardımcı oluruz."),
        ],
    },
    {
        "yol": "duvar-tavan-tamiri",
        "tur": "hizmet",
        "menu": "Duvar & Tavan",
        "hizmet": "Duvar ve tavan tamiratı",
        "baslik": "Duvar ve Tavan Tamiri, Sıva Onarımı İstanbul – Cengiz Usta",
        "aciklama": "Dökülen sıva, çatlak duvar, rutubetli ve su lekeli tavan onarımı. Beyoğlu, Şişli, Beşiktaş ve Fatih'te Cengiz Usta: 0542 800 32 63.",
        "etiket": "Duvar & Tavan Onarımı",
        "h1": "Duvar ve Tavan Tamiri, Sıva Onarımı",
        "giris": "Kabaran, dökülen sıva; çatlayan duvar; su almış tavan… Bu sorunlarda üstüne boya atmak çözüm değildir. Önce yüzey sağlamlaştırılır, sonra boyaya hazırlanır.",
        "gorsel": ("duvar-siva-onarimi", "Dökülen duvar sıvasını mala ile onaran Cengiz Usta"),
        "bolumler": [
            ("Sıva neden dökülür?", [
                "Eski binalarda sıvanın dökülmesinin başlıca sebepleri nem, çatıdan ya da tesisattan gelen su ve zamanla zayıflayan eski sıvadır. Nemin kaynağı giderilmeden yapılan onarım kısa sürede tekrar kabarabilir; bu yüzden önce sebebe bakarız.",
            ]),
            ("Onarım nasıl yapılıyor?", [
                "Gevşemiş ve kabarmış sıva kazınarak temizlenir, gerekiyorsa yüzey sağlamlaştırılır. Ardından sıva ve alçı ile düzeltilir, macunlanır ve zımparalanarak boyaya hazır hale getirilir.",
                "Tavandaki su lekelerinde önce leke tutucu astar uygulanır; aksi halde leke boyanın üstünden yeniden çıkar.",
            ]),
        ],
        "maddeler": ["Dökülen sıva onarımı", "Çatlak duvar tamiri", "Su lekeli tavan onarımı", "Rutubetli duvar hazırlığı", "Alçı ve macun işleri", "Boya öncesi yüzey düzeltme"],
        "sss": [
            ("Duvardaki rutubeti tamamen çözüyor musunuz?", "Rutubetin kaynağına göre değişir. Kaynak çatı ya da duvar dibiyse onu da konuşuruz; tesisat kaçağı gibi farklı bir uzmanlık gerekiyorsa bunu açıkça söyleriz."),
            ("Sadece tek bir duvar için de geliyor musunuz?", "Evet, küçük onarımlar için de arayabilirsiniz."),
        ],
    },
]

SEMT_SAYFALARI = [
    {
        "yol": "beyoglu",
        "tur": "semt",
        "semt": "Beyoğlu",
        "menu": "Beyoğlu",
        "baslik": "Beyoğlu Boya Badana Ustası, Tadilat ve Çatı Tamiri – Cengiz Usta",
        "aciklama": "Beyoğlu, Cihangir, Galata, Şişhane, Tarlabaşı ve Dolapdere'de boya badana, tadilat ve çatı tamiri. Cengiz Usta'yı doğrudan arayın: 0542 800 32 63.",
        "etiket": "Beyoğlu",
        "h1": "Beyoğlu Boya Badana, Tadilat ve Çatı Tamiri",
        "giris": "Beyoğlu’nun eski apartmanlarında boya, sıva ve çatı işleri dikkat ister. Cengiz Usta Beyoğlu ve çevresinde ev, daire ve dükkânlar için boya badana, tadilat ve çatı tamiri yapıyor.",
        "gorsel": ("cengiz-usta-duvar-tamiri", "Beyoğlu'nda eski bir dairede dökülen duvar sıvasını onaran Cengiz Usta"),
        "bolumler": [
            ("Beyoğlu’nun eski binalarında çalışmak", [
                "Cihangir, Galata, Şişhane ve Tarlabaşı’ndaki binaların çoğu yüksek tavanlı, kalın duvarlı ve eskidir. Bu binalarda sıva kabarması, tavanda su izi ve kiremit çatı sorunları sık görülür. Boyadan önce yüzeyi sağlamlaştırmak burada her zamankinden daha önemlidir.",
                "Dar sokaklar ve asansörsüz merdivenler yüzünden malzemenin taşınmasını ve molozun çıkarılmasını önceden planlarız.",
            ]),
            ("Beyoğlu’nda yaptığımız işler", [
                "Daire ve oda boyası, yüksek tavan badanası, dökülen sıva onarımı, kiralık daire yenileme, dükkân boyası ve akan kiremit çatıların tamiri Beyoğlu’nda en çok istenen işler arasında.",
            ]),
        ],
        "mahalleler": ["Cihangir", "Galata", "Şişhane", "Tarlabaşı", "Dolapdere", "Piyalepaşa", "Okmeydanı", "Kasımpaşa"],
        "sss": [
            ("Beyoğlu’nda asansörsüz binaya geliyor musunuz?", "Evet. Malzeme ve moloz taşımasını işin planına baştan dahil ederiz."),
            ("Beyoğlu’nda çatı tamiri yapıyor musunuz?", "Evet. Beyoğlu’ndaki kiremit çatılarda kırık kiremit değişimi ve akan çatı onarımı yapıyoruz. Önce suyun nereden girdiğine bakarız."),
        ],
    },
    {
        "yol": "taksim",
        "tur": "semt",
        "semt": "Taksim",
        "menu": "Taksim",
        "baslik": "Taksim Boya Ustası ve Tadilat Ustası – Cengiz Usta",
        "aciklama": "Taksim, Talimhane, Gümüşsuyu ve çevresinde daire, ofis ve dükkân için boya ve tadilat. Cengiz Usta ile doğrudan görüşün: 0542 800 32 63.",
        "etiket": "Taksim",
        "h1": "Taksim Boya ve Tadilat Ustası",
        "giris": "Taksim’de dairenizi, ofisinizi ya da dükkânınızı yenilemek için ustayla doğrudan konuşun. Boya, sıva ve tadilat işlerinde işin başında Cengiz Usta olur.",
        "gorsel": ("tadilat-on-gorusme", "Taksim'de ev sahibiyle tadilat planını konuşan Cengiz Usta"),
        "bolumler": [
            ("Kiralık daireler ve işyerleri", [
                "Taksim ve çevresinde kiraya verilen daireler sık el değiştirir. Kiracı çıkışı ile yeni kiracı arasındaki kısa sürede boya, küçük onarım ve temizliğe hazır teslim için işi zamanlayarak planlarız.",
                "Talimhane ve çevresindeki dükkân, ofis ve işletmelerde çalışmanın işinizi aksatmaması için saatleri birlikte belirleriz.",
            ]),
            ("Taksim’de yaptığımız işler", [
                "Daire boyası, ofis ve dükkân boyası, duvar ve tavan onarımı, sıva yenileme ve genel tadilat işleri.",
            ]),
        ],
        "mahalleler": ["Talimhane", "Gümüşsuyu", "Cihangir", "Tarlabaşı", "Elmadağ", "Harbiye"],
        "sss": [
            ("Kiracı çıkışında kısa sürede boya yapılabilir mi?", "Evet, işi tarihlerinize göre planlarız. Dairenin büyüklüğünü ve durumunu görünce net süre veririz."),
            ("Taksim’de dükkân boyası yapıyor musunuz?", "Evet. Dükkân ve ofislerde müşteri saatlerini aksatmamak için çalışma zamanını birlikte belirleriz."),
        ],
    },
    {
        "yol": "sisli",
        "tur": "semt",
        "semt": "Şişli",
        "menu": "Şişli",
        "baslik": "Şişli Boya Badana Ustası ve Tadilat – Cengiz Usta",
        "aciklama": "Şişli, Mecidiyeköy, Kurtuluş, Feriköy ve Bomonti'de boya badana, tadilat, duvar ve tavan onarımı. Cengiz Usta: 0542 800 32 63.",
        "etiket": "Şişli",
        "h1": "Şişli Boya Badana ve Tadilat",
        "giris": "Şişli ve Mecidiyeköy’de ev ve ofisler için boya badana, duvar onarımı ve tadilat. Fiyatı ve işi, işi yapacak ustayla konuşursunuz.",
        "gorsel": ("pencere-cevresi-boya", "Şişli'de bir dairede pencere kenarına rötuş boya yapan Cengiz Usta"),
        "bolumler": [
            ("Apartman daireleri ve ofisler", [
                "Şişli’nin büyük kısmı çok katlı apartmanlardan ve ofis binalarından oluşur. Apartmanlarda ortak alanların korunması, asansör kullanımı ve çalışma saatleri yönetimle uyumlu planlanır.",
                "Kurtuluş ve Feriköy’deki eski binalarda boya öncesi sıva ve tavan onarımı çoğu zaman işin önemli bir parçasıdır.",
            ]),
            ("Şişli’de yaptığımız işler", [
                "Daire ve oda boyası, ofis boyası, tavan badanası, rutubetli duvar hazırlığı, sıva onarımı ve tadilat.",
            ]),
        ],
        "mahalleler": ["Mecidiyeköy", "Kurtuluş", "Feriköy", "Bomonti", "Okmeydanı", "Nişantaşı", "Esentepe"],
        "sss": [
            ("Mecidiyeköy’de ofis boyası yapıyor musunuz?", "Evet. Ofisin çalışma düzenini bozmamak için işi mesai saatlerine göre planlayabiliriz."),
            ("Şişli’de fiyat nasıl belirleniyor?", "Metrekare, duvarların durumu ve kullanılacak boyaya göre. Fotoğraf gönderirseniz önden fikir verebiliriz."),
        ],
    },
    {
        "yol": "besiktas",
        "tur": "semt",
        "semt": "Beşiktaş",
        "menu": "Beşiktaş",
        "baslik": "Beşiktaş Boya Ustası, Tadilat ve Çatı Tamiri – Cengiz Usta",
        "aciklama": "Beşiktaş, Abbasağa, Sinanpaşa ve Ortaköy'de boya ustası, tadilat, duvar onarımı ve çatı tamiri. Cengiz Usta'yı arayın: 0542 800 32 63.",
        "etiket": "Beşiktaş",
        "h1": "Beşiktaş Boya Ustası ve Tadilat",
        "giris": "Beşiktaş’ta eviniz ya da işyeriniz için boya, onarım ve tadilat işlerinde Cengiz Usta ile doğrudan görüşün. Temiz çalışma ve açık fiyat.",
        "gorsel": ("tavan-tamiri", "Beşiktaş'ta iskele üzerinde tavan tamiri yapan Cengiz Usta"),
        "bolumler": [
            ("Boğaz’a yakın evlerde nem", [
                "Sahile ve yokuşlara yakın evlerde nem ve rutubet, boyanın kabarmasına ve tavanda lekelere yol açabilir. Bu evlerde boya öncesi yüzey hazırlığı ve doğru astar seçimi boyanın ömrünü belirler.",
            ]),
            ("Beşiktaş’ta yaptığımız işler", [
                "Daire boyası, tavan onarımı, dökülen sıva tamiri, kiralık daire yenileme, dükkân boyası ve çatı onarımı.",
            ]),
        ],
        "mahalleler": ["Abbasağa", "Sinanpaşa", "Türkali", "Vişnezade", "Ortaköy", "Dikilitaş"],
        "sss": [
            ("Beşiktaş’ta rutubetli duvarı boyuyor musunuz?", "Önce rutubetin kaynağına ve duvarın durumuna bakarız. Yüzey hazırlanmadan boya atmak lekenin kısa sürede geri gelmesine yol açar."),
            ("Hafta sonu çalışıyor musunuz?", "Uygunluk durumuna göre konuşabiliriz; arayıp sorabilirsiniz."),
        ],
    },
    {
        "yol": "fatih",
        "tur": "semt",
        "semt": "Fatih",
        "menu": "Fatih",
        "baslik": "Fatih Boya Badana, Tadilat ve Çatı Tamiri – Cengiz Usta",
        "aciklama": "Fatih, Topkapı, Aksaray, Balat ve Fener'de boya badana, sıva onarımı, tadilat ve çatı tamiri. Cengiz Usta: 0542 800 32 63.",
        "etiket": "Fatih",
        "h1": "Fatih Boya Badana ve Tadilat",
        "giris": "Fatih’in eski evlerinde boya, sıva ve çatı onarımı için Cengiz Usta’yı arayın. İşi önce yerinde görür, ne yapılması gerektiğini açıkça söyler.",
        "gorsel": ("ustalarla-is-plani", "Fatih'te bir tadilat işinde ustalara yapılacak işi anlatan Cengiz Usta"),
        "bolumler": [
            ("Tarihi yarımadanın eski yapıları", [
                "Balat, Fener ve Topkapı çevresindeki eski binalarda kalın duvarlar, eski sıvalar ve kiremit çatılar yaygındır. Bu yapılarda sert müdahale yerine dikkatli onarım, boya öncesinde de iyi bir yüzey hazırlığı gerekir.",
            ]),
            ("Fatih’te yaptığımız işler", [
                "Boya badana, dökülen sıva onarımı, su alan çatı tamiri, tavan onarımı ve ev-işyeri tadilatı.",
            ]),
        ],
        "mahalleler": ["Topkapı", "Aksaray", "Balat", "Fener", "Karagümrük", "Vefa"],
        "sss": [
            ("Fatih’te eski binada sıva onarımı yapıyor musunuz?", "Evet. Gevşemiş sıvayı temizleyip yüzeyi sağlamlaştırır, sonra boyaya hazırlarız."),
            ("Topkapı tarafına geliyor musunuz?", "Evet, Topkapı ve çevresi hizmet verdiğimiz bölgeler arasında."),
        ],
    },
]

TUM_SAYFALAR = HIZMET_SAYFALARI + SEMT_SAYFALARI
