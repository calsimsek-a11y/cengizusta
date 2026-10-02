# Cengiz Usta – Sivas Yapı

Cengiz Bostancı'nın (Sivas Yapı, İstanbul) tek sayfalık tanıtım sitesi. Bağımlılık yok: düz HTML + CSS + birkaç satır JS.

- `site/` — yayınlanan dosyalar (GitHub Pages bu klasörü yayınlar)
- `araclar/derle.py` — `index.html`, `404.html`, `robots.txt`, `sitemap.xml` üretir. **Alan adı değişirse** içindeki `SITE_URL`'i değiştirip `python3 araclar/derle.py` çalıştırın.
- `araclar/gorsel_hazirla.py` — `kaynak/` görsellerinden AVIF + WebP (480/900/1400) üretir.

## Tasarım sistemi (site/stil.css `:root`)
| Jeton | Değer | Kullanım |
|---|---|---|
| `--zemin` | #F7F7F5 | kırık beyaz sayfa zemini |
| `--yazi` | #1B2430 | antrasit metin |
| `--vurgu` | #1F3A5A | lacivert: ana buton, başlık vurgusu, iletişim bandı |
| `--vurgu-koyu` | #142940 | hover |
| `--vurgu-acik` | #E4EBF3 | ikon zemini, CTA kart |
| `--bakir` | #A8692F | küçük etiketler ve konum/tik ikonları (az kullan) |
| `--wa-ikon` | #1FA855 | yalnızca WhatsApp simgesi; buton beyaz + lacivert çerçeve |
| `--koyu` | #17212D | "Hakkında" ve alt bilgi zemini |

Yazı: sistem yazı tipi (hız için harici font yok). Butonlar en az 56 px yüksek; mobilde alttaki yapışkan bar 50 px.
