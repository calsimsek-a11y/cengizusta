"""kaynak/ klasöründeki görselleri site/img/ altına AVIF + WebP, 3 genişlikte hazırlar."""
from pathlib import Path
from PIL import Image, ImageEnhance

KOK = Path(__file__).resolve().parent.parent
KAYNAK, HEDEF = KOK / "kaynak", KOK / "site" / "img"

# kaynak dosya -> sitedeki SEO dostu ad
ADLAR = {
    "scene-01": "beyoglu-boya-badana-ustasi",
    "scene-02": "istanbul-kiremit-cati-tamiri",
    "scene-03": "duvar-siva-onarimi",
    "scene-04": "tavan-tamiri",
    "scene-05": "ev-tadilati-olcu-alma",
    "scene-06": "cati-su-yalitimi-onarimi",
    "scene-07": "tadilat-on-gorusme",
    "scene-08": "ustalarla-is-plani",
    "scene-09": "pencere-cevresi-boya",
    "scene-10": "ev-bakim-onarim",
    "duvar-tamiri-orijinal": "cengiz-usta-duvar-tamiri",
}
GENISLIKLER = (480, 900, 1400)

HEDEF.mkdir(parents=True, exist_ok=True)
for kaynak, ad in ADLAR.items():
    im = Image.open(KAYNAK / f"{kaynak}.webp").convert("RGB")
    im = ImageEnhance.Contrast(im).enhance(1.03)
    for w in GENISLIKLER:
        if w > im.width:
            continue
        k = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        k.save(HEDEF / f"{ad}-{w}.webp", quality=78, method=6)
        k.save(HEDEF / f"{ad}-{w}.avif", quality=55)
    print(ad, im.size)

# Open Graph görseli (1200x630, JPEG — sosyal ağlar için)
og = Image.open(KAYNAK / "scene-01.webp").convert("RGB")
h = round(1200 * 630 / 1200)
og = og.resize((1200, round(og.height * 1200 / og.width)), Image.LANCZOS)
ust = (og.height - 630) // 2
og.crop((0, ust, 1200, ust + 630)).save(HEDEF / "og-cengiz-usta.jpg", quality=82, optimize=True, progressive=True)
