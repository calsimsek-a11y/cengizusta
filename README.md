# Cengiz Usta – Sivas Yapı

Cengiz Bostancı'nın (Sivas Yapı, İstanbul) tek sayfalık tanıtım sitesi. Bağımlılık yok: düz HTML + CSS + birkaç satır JS.

- `site/` — yayınlanan dosyalar (GitHub Pages bu klasörü yayınlar)
- `araclar/derle.py` — `index.html`, `404.html`, `robots.txt`, `sitemap.xml` üretir. **Alan adı değişirse** içindeki `SITE_URL`'i değiştirip `python3 araclar/derle.py` çalıştırın.
- `araclar/gorsel_hazirla.py` — `kaynak/` görsellerinden AVIF + WebP (480/900/1400) üretir.

## Tasarım sistemi (site/stil.css `:root`)
| Jeton | Değer | Kullanım |
|---|---|---|
| `--zemin` | #FAF7F2 | kırık beyaz sayfa zemini |
| `--yazi` | #23262B | antrasit metin |
| `--vurgu` | #B5532C | terracotta: ana buton, başlık vurgusu |
| `--vurgu-koyu` | #8F3F1F | hover |
| `--vurgu-acik` | #F5E3D8 | ikon zemini, CTA kart |
| `--wa` | #1E7F47 | WhatsApp butonu |
| `--koyu` | #24272C | "Hakkında" ve alt bilgi zemini |

Yazı: sistem yazı tipi (hız için harici font yok). Butonlar en az 56 px yüksek; mobilde alttaki yapışkan bar 50 px.
