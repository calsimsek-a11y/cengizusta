"""Cengiz Usta – Sivas Yapı sitesini üretir: site/index.html, 404.html, robots.txt, sitemap.xml.

Alan adı değişince yalnızca SITE_URL'i değiştirip tekrar çalıştırın:
    python3 araclar/derle.py
"""
import json
from datetime import date
from pathlib import Path
from urllib.parse import quote

SITE_URL = "https://calsimsek-a11y.github.io/cengizusta/"  # sonunda / olmalı
GSC_DOGRULAMA = ""  # Search Console meta etiketi içeriği (gerekirse)

TEL_GORUNEN = "0542 800 32 63"
TEL_LINK = "tel:+905428003263"
EPOSTA = "cengizbostanciusta@gmail.com"
WA_MESAJ = "Merhaba Cengiz Usta, boya/tadilat işi için bilgi ve fiyat almak istiyorum."
WA_LINK = "https://wa.me/905428003263?text=" + quote(WA_MESAJ)

KOK = Path(__file__).resolve().parent.parent
SITE = KOK / "site"

BOLGELER = ["Beyoğlu", "Taksim", "Şişhane", "Tarlabaşı", "Dolapdere", "Piyalepaşa",
            "Okmeydanı", "Şişli", "Mecidiyeköy", "Beşiktaş", "Fatih", "Topkapı"]

HIZMETLER = [
    ("beyoglu-boya-badana-ustasi", "Boya & Badana",
     "Duvar ve tavanlarda yüzey hazırlığı, macun, astar ve boya. Eşyalarınızı örtüyor, işi bitirince ortalığı temiz bırakıyoruz.",
     "Beyoğlu'nda bir evde duvarı rulo ile boyayan Cengiz Usta"),
    ("ev-tadilati-olcu-alma", "Tadilat",
     "Ev ve işyerinde yenilenmesi gereken yerleri birlikte konuşuyor, ölçüsünü alıyor, işi ihtiyaca göre planlıyoruz.",
     "Taksim'de ev tadilatı öncesi duvar ölçüsü alan Cengiz Usta"),
    ("istanbul-kiremit-cati-tamiri", "Çatı Tamiri",
     "Kırık kiremit, akan ve su alan çatılar, çatı bakımı. Önce sorunun nereden geldiğine bakıyor, sonra onarıyoruz.",
     "İstanbul'da emniyet kemeriyle kiremit çatı tamiri yapan Cengiz Usta"),
    ("duvar-siva-onarimi", "Duvar & Tavan Onarımı",
     "Kabaran sıva, çatlak, rutubet izi ve dökülen tavanlar. Yüzeyi düzeltip boyaya hazır hale getiriyoruz.",
     "Şişli'de dökülen duvar sıvasını onaran Cengiz Usta"),
    ("ev-bakim-onarim", "Ev & İşyeri Bakım İşleri",
     "Dolap kapağı, menteşe, küçük tamiratlar, rötuş boya. Kimsenin gelmek istemediği küçük işleri de yapıyoruz.",
     "Beşiktaş'ta mutfak dolabı menteşesini ayarlayan Cengiz Usta"),
]

SAHNELER = [
    ("beyoglu-boya-badana-ustasi", "Evde duvar boyama", "Beyoğlu'nda bir dairede duvar boyayan Cengiz Usta"),
    ("istanbul-kiremit-cati-tamiri", "Kiremit çatı onarımı", "İstanbul'da kiremit çatı tamiri yapan Cengiz Usta"),
    ("duvar-siva-onarimi", "Sıva ve yüzey düzeltme", "Duvarda sıva onarımı yapan Cengiz Usta"),
    ("tavan-tamiri", "Tavan onarımı", "İskele üzerinde tavan tamiri yapan Cengiz Usta"),
    ("ev-tadilati-olcu-alma", "Tadilat öncesi ölçü", "Ev tadilatı için ölçü alan Cengiz Usta"),
    ("cati-su-yalitimi-onarimi", "Teras ve çatı yalıtımı kontrolü", "Su alan teras çatının yalıtımını inceleyen Cengiz Usta"),
    ("tadilat-on-gorusme", "Ev sahibiyle ön görüşme", "Ev sahibiyle tadilat planını konuşan Cengiz Usta"),
    ("ustalarla-is-plani", "Ekiple iş planı", "Yanında çalışan ustalara yapılacak işi anlatan Cengiz Usta"),
    ("pencere-cevresi-boya", "Pencere çevresi boya", "Pencere kenarında fırça ile rötuş boya yapan Cengiz Usta"),
    ("ev-bakim-onarim", "Küçük onarım işleri", "Mutfak dolabında menteşe ayarı yapan Cengiz Usta"),
]

NEDEN = [
    ("Doğrudan ustayla iletişim", "Telefonu Cengiz Usta açar. Aracı yok, çağrı merkezi yok; işi yapacak kişiyle konuşursunuz."),
    ("Ücretsiz ön görüşme", "İşi telefonda ya da yerinde birlikte konuşalım, ne gerektiğini net olarak söyleyelim."),
    ("Temiz ve özenli çalışma", "Eşyalar ve zemin örtülür, iş bitince ortam toparlanır. Evinize kendi evimiz gibi bakarız."),
    ("İstanbul merkez ilçelere hizmet", "Beyoğlu, Şişli, Beşiktaş ve Fatih başta olmak üzere merkez semtlere geliyoruz."),
]

SSS = [
    ("Fiyat nasıl belirleniyor?",
     "Her işin ölçüsü ve durumu farklı olduğu için fiyatı işi gördükten ya da fotoğrafını aldıktan sonra konuşuyoruz. WhatsApp'tan birkaç fotoğraf göndermeniz çoğu zaman yeterli olur."),
    ("Hangi semtlere geliyorsunuz?",
     "Beyoğlu, Taksim, Şişhane, Tarlabaşı, Dolapdere, Piyalepaşa, Okmeydanı, Şişli, Mecidiyeköy, Beşiktaş, Fatih ve Topkapı başta olmak üzere İstanbul'un merkez semtlerine geliyoruz."),
    ("Küçük işlere de geliyor musunuz?",
     "Evet. Tek odanın boyası, bir tavan onarımı ya da birkaç kiremidin değişmesi gibi küçük işler için de arayabilirsiniz."),
    ("Çatım su alıyor, ne yapmalıyım?",
     "Suyun geldiği yeri ve tavandaki izi fotoğraflayıp WhatsApp'tan gönderin. Sorunun kaynağına bakıp çatı tamirinin nasıl yapılacağını birlikte konuşalım."),
]


def picture(ad, alt, sizes, genislik, yukseklik, lazy=True, oncelik=False, cls=""):
    """AVIF + WebP kaynaklı, duyarlı <picture> üretir."""
    ws = [480, 900, 1400] if genislik >= 1400 else [480, 900]
    def srcset(ext):
        return ", ".join(f"img/{ad}-{w}.{ext} {w}w" for w in ws)
    nitelik = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"' if oncelik else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<picture><source type="image/avif" srcset="{srcset("avif")}" sizes="{sizes}">'
            f'<source type="image/webp" srcset="{srcset("webp")}" sizes="{sizes}">'
            f'<img src="img/{ad}-900.webp" alt="{alt}" width="{genislik}" height="{yukseklik}"{c}{nitelik}></picture>')


IKON = {
    "tel": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.15l-.3-.18-3 .78.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.25-.12-1.47-.72-1.7-.8s-.39-.12-.56.12-.64.8-.78.97-.29.18-.54.06a6.7 6.7 0 0 1-3.34-2.92c-.25-.43.25-.4.72-1.34a.45.45 0 0 0-.02-.43c-.06-.12-.56-1.34-.76-1.84s-.4-.42-.56-.43h-.48a.92.92 0 0 0-.66.31 2.8 2.8 0 0 0-.87 2.07 4.85 4.85 0 0 0 1.02 2.58 11.1 11.1 0 0 0 4.25 3.75c1.58.68 2.2.74 2.99.62a2.55 2.55 0 0 0 1.68-1.18 2.08 2.08 0 0 0 .14-1.18c-.06-.1-.23-.16-.48-.28z"/></svg>',
    "konum": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>',
    "tik": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>',
}


def butonlar(ek=""):
    return (f'<div class="cta-row{ek}">'
            f'<a class="btn btn-ana" href="{TEL_LINK}">{IKON["tel"]}<span>HEMEN ARA</span></a>'
            f'<a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener">{IKON["wa"]}<span>WHATSAPP’TAN YAZ</span></a>'
            f'</div>')


def yapisal_veri():
    isletme = {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": SITE_URL + "#isletme",
        "name": "Cengiz Bostancı – Sivas Yapı",
        "alternateName": ["Cengiz Usta", "Sivas Yapı"],
        "description": "İstanbul'da boya badana, ev ve işyeri tadilatı, çatı tamiri, duvar ve tavan onarımı.",
        "url": SITE_URL,
        "telephone": "+90 542 800 32 63",
        "email": EPOSTA,
        "image": SITE_URL + "img/og-cengiz-usta.jpg",
        "logo": SITE_URL + "favicon.svg",
        "founder": {"@type": "Person", "name": "Cengiz Bostancı"},
        "address": {"@type": "PostalAddress", "addressLocality": "İstanbul", "addressCountry": "TR"},
        "areaServed": [{"@type": "Place", "name": f"{b}, İstanbul"} for b in BOLGELER],
        "knowsLanguage": "tr",
        "contactPoint": {"@type": "ContactPoint", "telephone": "+90 542 800 32 63",
                         "contactType": "customer service", "availableLanguage": "Turkish"},
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Hizmetler",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}}
                                for n in ["Boya ve badana", "Ev ve işyeri tadilatı", "Çatı tamiri",
                                          "Çatı bakım ve onarımı", "Su alan çatı onarımı",
                                          "Duvar ve tavan tamiratı", "Sıva ve boya yenileme",
                                          "Küçük ev ve işyeri onarım işleri"]],
        },
    }
    sss = {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": s,
                        "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in SSS],
    }
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Cengiz Usta – Sivas Yapı",
            "url": SITE_URL, "inLanguage": "tr-TR"}
    return "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>'
                     for x in (isletme, sss, site))


def sayfa():
    baslik = "Cengiz Usta | Boya Badana, Tadilat ve Çatı Tamiri İstanbul"
    aciklama = ("Beyoğlu, Taksim, Şişli, Beşiktaş, Fatih ve çevresinde boya badana, tadilat ve çatı tamiri. "
                "Cengiz Usta ile doğrudan iletişim: 0542 800 32 63.")
    gsc = f'<meta name="google-site-verification" content="{GSC_DOGRULAMA}">' if GSC_DOGRULAMA else ""

    hizmet_kartlari = "\n".join(
        f'<article class="kart">{picture(ad, alt, "(min-width: 960px) 30vw, (min-width: 640px) 45vw, 100vw", 1400, 933)}'
        f'<div class="kart-ic"><h3>{b}</h3><p>{t}</p></div></article>'
        for ad, b, t, alt in HIZMETLER)
    hizmet_kartlari += (f'<article class="kart kart-cta"><div class="kart-ic"><h3>Aklınızdaki iş burada yok mu?</h3>'
                        f'<p>Sıva, boya yenileme, su alan çatı, küçük tamirat… Ne olduğunu anlatın, yapılabilir mi hemen söyleyelim.</p>'
                        f'<a class="link-ok" href="{WA_LINK}" target="_blank" rel="noopener">WhatsApp’tan fotoğraf gönderin →</a></div></article>')

    galeri = "\n".join(
        f'<li><button type="button" class="galeri-oge" data-ad="{ad}" data-baslik="{b}" aria-label="{b} – büyüt">'
        f'{picture(ad, alt, "(min-width: 960px) 20vw, (min-width: 640px) 33vw, 50vw", 1400, 933)}'
        f'<span>{b}</span></button></li>'
        for ad, b, alt in SAHNELER)

    neden = "\n".join(f'<li><span class="neden-ikon">{IKON["tik"]}</span><h3>{b}</h3><p>{t}</p></li>' for b, t in NEDEN)
    bolgeler = "\n".join(f'<li>{IKON["konum"]}{b}</li>' for b in BOLGELER)
    sss = "\n".join(f'<details><summary>{s}</summary><p>{c}</p></details>' for s, c in SSS)

    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{baslik}</title>
<meta name="description" content="{aciklama}">
<link rel="canonical" href="{SITE_URL}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#B5532C">
<meta name="geo.region" content="TR-34">
<meta name="geo.placename" content="İstanbul">
{gsc}
<meta property="og:type" content="website">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Cengiz Usta – Sivas Yapı">
<meta property="og:title" content="{baslik}">
<meta property="og:description" content="{aciklama}">
<meta property="og:url" content="{SITE_URL}">
<meta property="og:image" content="{SITE_URL}img/og-cengiz-usta.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Cengiz Usta İstanbul'da bir evde duvar boyarken">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preload" as="image" type="image/avif" imagesrcset="img/beyoglu-boya-badana-ustasi-480.avif 480w, img/beyoglu-boya-badana-ustasi-900.avif 900w, img/beyoglu-boya-badana-ustasi-1400.avif 1400w" imagesizes="(min-width: 960px) 46vw, 100vw">
<link rel="stylesheet" href="stil.css?v={date.today():%Y%m%d}">
{yapisal_veri()}
</head>
<body>
<a class="atla" href="#icerik">İçeriğe geç</a>
<header class="ust">
  <div class="kap ust-ic">
    <a class="marka" href="./" aria-label="Cengiz Usta – Sivas Yapı ana sayfa">
      <span class="marka-isaret" aria-hidden="true">SY</span>
      <span><strong>Sivas Yapı</strong><small>Cengiz Bostancı</small></span>
    </a>
    <nav aria-label="Ana menü" class="menu">
      <a href="#hizmetler">Hizmetler</a><a href="#hakkinda">Cengiz Usta</a><a href="#isler">İşlerden</a><a href="#bolgeler">Bölgeler</a><a href="#iletisim">İletişim</a>
    </nav>
    <a class="ust-tel" href="{TEL_LINK}">{IKON["tel"]}<span>{TEL_GORUNEN}</span></a>
  </div>
</header>

<main id="icerik">
<section class="hero">
  <div class="kap hero-ic">
    <div class="hero-metin">
      <p class="ust-etiket">İstanbul’un mahalle ustası</p>
      <h1>Boya, Badana, Tadilat ve <em>Çatı Tamiri</em></h1>
      <p class="hero-alt">İstanbul’da ev ve işyerleriniz için güvenilir, temiz ve özenli tadilat hizmeti.</p>
      <p class="hero-bolge">{IKON["konum"]}Beyoğlu • Taksim • Şişli • Beşiktaş • Fatih ve çevresi</p>
      {butonlar()}
      <p class="hero-tel"><a href="{TEL_LINK}">{TEL_GORUNEN}</a><span>Telefonu Cengiz Usta açar.</span></p>
    </div>
    <figure class="hero-gorsel">
      {picture("beyoglu-boya-badana-ustasi", "Cengiz Usta Beyoğlu'nda bir dairede duvarı rulo ile boyarken", "(min-width: 960px) 46vw, 100vw", 1400, 933, lazy=False, oncelik=True)}
      <figcaption><strong>Cengiz Bostancı</strong> Sivas Yapı · İstanbul</figcaption>
    </figure>
  </div>
  <ul class="kap seritler" aria-label="Öne çıkanlar">
    <li>{IKON["tik"]}Doğrudan ustayla iletişim</li>
    <li>{IKON["tik"]}Ücretsiz ön görüşme</li>
    <li>{IKON["tik"]}Temiz ve özenli çalışma</li>
    <li>{IKON["tik"]}İstanbul merkez ilçeler</li>
  </ul>
</section>

<section id="hizmetler" class="bolum">
  <div class="kap">
    <header class="bolum-bas">
      <p class="ust-etiket">Hizmetlerimiz</p>
      <h2>Evinize, işyerinize özenli bir dokunuş</h2>
      <p>Bir odanın boyasından akan çatının tamirine kadar; ihtiyacınız olan işi birlikte değerlendirelim.</p>
    </header>
    <div class="kartlar">
{hizmet_kartlari}
    </div>
  </div>
</section>

<section id="hakkinda" class="bolum bolum-koyu">
  <div class="kap hakkinda">
    <figure class="hakkinda-gorsel">
      {picture("cengiz-usta-duvar-tamiri", "Cengiz Bostancı İstanbul'da bir dairede dökülen duvarın sıva tamirini yaparken", "(min-width: 960px) 38vw, 100vw", 1122, 1402)}
    </figure>
    <div class="hakkinda-metin">
      <p class="ust-etiket">Cengiz Usta hakkında</p>
      <h2>İşinizi doğrudan ustasına emanet edin.</h2>
      <p>Ben Cengiz Bostancı. Sivas Yapı adıyla İstanbul’da boya, badana, tadilat ve çatı tamiri işleri yapıyorum.</p>
      <p>Aradığınızda telefonu ben açarım; işi birlikte konuşur, yerinde ya da fotoğraftan bakar, ne yapılması gerektiğini açıkça söylerim. İşe başladığımızda da başında ben olurum.</p>
      <p>Evinize girerken eşyalarınızı örter, iş bitince ortalığı temiz bırakırım. Küçük ya da büyük, her işe aynı özeni gösteririm.</p>
      {butonlar(" cta-acik")}
    </div>
  </div>
</section>

<section id="isler" class="bolum">
  <div class="kap">
    <header class="bolum-bas">
      <p class="ust-etiket">İşlerden kareler</p>
      <h2>Boyadan çatıya, işin başında</h2>
      <p>Ön görüşmeden son rötuşa kadar yaptığımız işlerden sahneler. Büyütmek için görsele dokunun.</p>
    </header>
    <ul class="galeri">
{galeri}
    </ul>
    <p class="not">Bu bölümdeki görseller, yapılan iş türlerini anlatmak için yapay zekâ yardımıyla hazırlanmış temsili görsellerdir.</p>
  </div>
</section>

<section id="neden" class="bolum bolum-acik">
  <div class="kap">
    <header class="bolum-bas">
      <p class="ust-etiket">Neden Cengiz Usta?</p>
      <h2>Aracısız, açık ve temiz iş</h2>
    </header>
    <ul class="neden">
{neden}
    </ul>
  </div>
</section>

<section id="bolgeler" class="bolum">
  <div class="kap bolgeler-ic">
    <div>
      <p class="ust-etiket">Hizmet bölgeleri</p>
      <h2>İstanbul’un merkez semtlerindeyiz</h2>
      <p>Beyoğlu ve Taksim başta olmak üzere aşağıdaki semtlerde boya badana, tadilat ve çatı tamiri için geliyoruz. Listede olmayan yakın bir semtteyseniz yine de arayın.</p>
    </div>
    <ul class="bolge-liste">
{bolgeler}
    </ul>
  </div>
</section>

<section id="sss" class="bolum bolum-acik">
  <div class="kap dar">
    <header class="bolum-bas">
      <p class="ust-etiket">Sık sorulanlar</p>
      <h2>Aklınıza takılanlar</h2>
    </header>
    <div class="sss">
{sss}
    </div>
  </div>
</section>

<section id="iletisim" class="iletisim">
  <div class="kap iletisim-ic">
    <h2>İşinizi Anlatın, Fiyat Konuşalım</h2>
    <p>Arayın ya da WhatsApp’tan yazın. İşin fotoğrafını gönderirseniz daha hızlı yardımcı olabiliriz.</p>
    <a class="iletisim-tel" href="{TEL_LINK}">{TEL_GORUNEN}</a>
    {butonlar(" cta-merkez")}
    <p class="iletisim-bolge">{IKON["konum"]}İstanbul · Beyoğlu, Şişli, Beşiktaş, Fatih ve çevresi</p>
  </div>
</section>
</main>

<footer class="alt">
  <div class="kap">
    <p><strong>Cengiz Bostancı – Sivas Yapı</strong> | İstanbul</p>
    <p><a href="{TEL_LINK}">{TEL_GORUNEN}</a> · <a href="mailto:{EPOSTA}">{EPOSTA}</a></p>
  </div>
</footer>

<nav class="yapiskan" aria-label="Hızlı iletişim">
  <a class="btn btn-ana" href="{TEL_LINK}">{IKON["tel"]}<span>Telefon Et</span></a>
  <a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener">{IKON["wa"]}<span>WhatsApp</span></a>
</nav>

<dialog class="lightbox" aria-label="Görsel">
  <button type="button" class="lightbox-kapat" aria-label="Kapat">×</button>
  <picture><source type="image/avif"><img alt="" width="1400" height="933"></picture>
  <p></p>
</dialog>
<script src="site.js?v={date.today():%Y%m%d}" defer></script>
</body>
</html>
"""


def sayfa_404():
    return f"""<!doctype html>
<html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sayfa bulunamadı | Cengiz Usta – Sivas Yapı</title><meta name="robots" content="noindex, follow">
<link rel="icon" href="{SITE_URL}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{SITE_URL}stil.css"></head>
<body><main class="bolum"><div class="kap dar" style="text-align:center">
<p class="ust-etiket">404</p><h1>Aradığınız sayfa bulunamadı</h1>
<p>Boya, badana, tadilat ve çatı tamiri için ana sayfaya dönebilir ya da hemen arayabilirsiniz.</p>
<div class="cta-row cta-merkez"><a class="btn btn-ana" href="{SITE_URL}">Ana sayfa</a><a class="btn btn-wa" href="{TEL_LINK}">{TEL_GORUNEN}</a></div>
</div></main></body></html>
"""


def main():
    (SITE / "index.html").write_text(sayfa(), encoding="utf-8")
    (SITE / "404.html").write_text(sayfa_404(), encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n", encoding="utf-8")
    gorseller = "".join(
        f"<image:image><image:loc>{SITE_URL}img/{ad}-1400.webp</image:loc></image:image>"
        for ad, *_ in SAHNELER)
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
        f"<url><loc>{SITE_URL}</loc><lastmod>{date.today().isoformat()}</lastmod>{gorseller}</url>\n"
        "</urlset>\n", encoding="utf-8")
    (SITE / ".nojekyll").write_text("")
    print("Derlendi:", SITE_URL)


if __name__ == "__main__":
    main()
