# Karar Derlemeleri (Markdown)

**Derleyen: Av. Hakan Dimdik** ([@hakandimdik](https://x.com/hakandimdik))

Bu depodaki emsal karar derlemelerinin tamamını Av. Hakan Dimdik hazırlamış ve X hesabında herkesin yararlanması için paylaşmıştır. Kararların seçimi, konulara göre tasnifi ve başlıklandırılması onun emeğidir. Bu depo yalnızca biçim dönüştürür: PDF'leri, başlık hiyerarşisini koruyarak Markdown'a çevirir; arama, not alma (Obsidian) ve yapay zekâ araçlarına yükleme kolaylaşsın diye.

**35 derleme · 66.332 sayfa · yaklaşık 134 bin karar künyesi.** İndirme ve dönüştürme tarihi: 27.11.2026.

> **Atıf.** Bu derlemelerden yararlanırken kaynak olarak Av. Hakan Dimdik'i gösterin. Her derlemenin altında özgün PDF'in ve paylaşıldığı gönderinin bağlantısı vardır; güncel sürümler için özgün paylaşımlara bakın. Bu depoda yayımlanmak üzere derlemelerin Markdown ve yapılandırılmış veri biçimlerine dönüştürülmesi ve paylaşılması için Av. Hakan Dimdik'ten izin alınmıştır. Derlemeler üzerindeki haklar derleyene aittir; bu depo içerik üzerinde hak iddia etmez. Derleyenin talebi hâlinde içerik kaldırılır.

**Yapay zekâ araçları:** önce [AGENTS.md](AGENTS.md) dosyasını okuyun; konu dizini: [dizin/derlemeler.md](dizin/derlemeler.md).

## Nasıl kullanılır

| Ne | Nerede | Kime |
|---|---|---|
| Okuma ve arama | `md/<kod>/`: konu başlığına göre klasörler, en çok 48 KB'lık dosyalar; her derlemenin dizini `00-icindekiler.md`, hepsinin dizini [dizin/derlemeler.md](dizin/derlemeler.md) | GitHub'da ya da klonda okuyanlar, Obsidian, kod yardımcıları |
| Yükleme dosyaları | `python3 araclar/cilt.py <kod>` ile `yukle/<kod>/` altında üretilen, en çok 3 MB'lık ciltler; yanında [TALIMAT.txt](TALIMAT.txt) ve [dizin/konular.tsv](dizin/konular.tsv) | NotebookLM, ChatGPT, Claude Projects gibi dosya yüklenen ürünler |
| Veri | `veri/kararlar/<kod>.jsonl.gz`: karar başına bir kayıt; [veri/README.md](veri/README.md) | Geliştiriciler (RAG, analiz) |

Dosya yüklenen ürünlerde (NotebookLM, ChatGPT, Claude Projects) üç adım:

1. Depoyu indirin, `python3 araclar/cilt.py kira` çalıştırın (kod, aşağıdaki tabloların "dizin" sütunundadır). Ciltler `yukle/kira/` altına yazılır; depoda tutulmaz.
2. Ciltleri ve `dizin/konular.tsv` dosyasını ürüne kaynak olarak yükleyin. Ürünlerin dosya boyutu ve sayısı sınırları değişir; yüklemeden önce ürünün güncel sınırına bakın, cilt sığmıyorsa `md/<kod>/` altındaki küçük dosyaları kullanın.
3. `TALIMAT.txt` içeriğini ürünün talimat kutusuna (Claude Projects'te proje talimatı, ChatGPT'de özel GPT ya da proje talimatı) yapıştırın; talimat kutusu yoksa (NotebookLM) dosyayı kaynak olarak ekleyin ve ilk iletide ona uyulmasını isteyin.

Kabuk erişimi olan yardımcılar için: `python3 araclar/ara.py "icra inkar tazminati"` Türkçe harfe duyarsız arar ve tekrar eden alıntıları birleştirir.

Dosyalarda `#` konu başlığı, `##` karar künyesidir (ör. `Yargıtay HGK 2021/164 K.`); künyenin altındaki paragraflar o karardan alıntıdır.

## Borçlar ve sözleşmeler

| Derleme | Sayfa | Karar | MB | Dizin | Özgün PDF | Paylaşım |
|---|--:|--:|--:|---|---|---|
| Borçlar Genel Hukukuna İlişkin Emsal Kararlar | 1.112 | 3.752 | 3,6 | [borclar-genel](md/borclar-genel/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1Tds94HCnpZfAApwepPXlVd-jhQcg61t6/view) | [gönderi](https://x.com/hakandimdik/status/2124090681207472476) |
| Özel Hukukun Temel İlkelerine İlişkin Emsal Kararlar | 154 | 469 | 0,5 | [temel-ilkeler](md/temel-ilkeler/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1JfqwStlCxN7KCkayO96pGLF6THx_1aro/view) | [gönderi](https://x.com/hakandimdik/status/2121554873317814690) |
| Kira Hukuku Emsal Kararlar (V7) | 5.668 | 14.949 | 20,5 | [kira](md/kira/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1m2-_-6lDyG_3P3_cWJjBt7lU6FdOVm9W/view) | [gönderi](https://x.com/hakandimdik/status/2124454352404320562) |
| Adi Ortaklığa İlişkin Emsal Kararlar | 1.490 | 2.421 | 5,8 | [adi-ortaklik](md/adi-ortaklik/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1mxjfvWUORiih8Fi47levqi6phEZ4drVa/view) | [gönderi](https://x.com/hakandimdik/status/2125321992522150357) |
| Arsa Payı Karşılığı İnşaat Sözleşmesi ve Kentsel Dönüşüme İlişkin Emsal Kararlar | 6.051 | 7.955 | 21,4 | [arsa-payi](md/arsa-payi/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1LDO38F_FatbwhaymCt75ai9Oz0D_evMe/view) | [gönderi](https://x.com/hakandimdik/status/2125661687864774675) |
| Arsa Payı Karşılığı İnşaat Sözleşmesine İlişkin Emsal Kararlar — ESKİ SÜRÜM (güncel hâli: `arsa-payi`) | 29 | 72 | 0,1 | [arsa-payi-ilk](md/arsa-payi-ilk/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1Ct0Zefa-jizzCc-QLa21l5aoyipKtjKG/view) | [gönderi](https://x.com/hakandimdik/status/2120883737848320342) |
| Yükleniciden Bağımsız Bölüm Satın Alanlara İlişkin Emsal Kararlar | 75 | 191 | 0,2 | [yukleniciden-satin-alan](md/yukleniciden-satin-alan/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1P06qvp9O6bmQShcZKs7KftUBJ9oizTYu/view) | [gönderi](https://x.com/hakandimdik/status/2123838189089763573) |
| FIDIC Sözleşmelerine İlişkin Emsal Kararlar | 97 | 103 | 0,3 | [fidic](md/fidic/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/18QEEL-K2Je-kVvYl0EcKTBAzQxHJxer-/view) | [gönderi](https://x.com/hakandimdik/status/2122564591293022527) |
| CISG'e (Milletlerarası Mal Satımı) İlişkin Emsal Kararlar (V1) | 14 | 22 | <0,1 | [cisg](md/cisg/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/11qXFVBAeykRHDVaQV-m0imZOUaLJ08Es/view) | [gönderi](https://x.com/hakandimdik/status/2121496753039966621) |

## Taşınmaz ve eşya hukuku

| Derleme | Sayfa | Karar | MB | Dizin | Özgün PDF | Paylaşım |
|---|--:|--:|--:|---|---|---|
| Tapu Tescil Davalarına İlişkin Emsal Kararlar | 175 | 455 | 0,5 | [tapu-tescil](md/tapu-tescil/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1DO5gkMFqZIJOb7F7rhxzdfPfDuUaYiwy/view) | [gönderi](https://x.com/hakandimdik/status/2121733453393883152) |
| Muris Muvazaasına İlişkin Emsal Kararlar (V1) | 35 | 89 | 0,1 | [muris-muvazaasi](md/muris-muvazaasi/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1DfWIvBcGH35BqA-29AsyjwV6xPg_sv06/view) | [gönderi](https://x.com/hakandimdik/status/2120809451896926410) |
| Kadastro Hukukuna İlişkin Emsal Kararlar | 134 | 389 | 0,4 | [kadastro](md/kadastro/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1s8hjIRFYyTYKkJLCgKcLo742EsS_lOXi/view) | [gönderi](https://x.com/hakandimdik/status/2121733410905260202) |
| Kamulaştırma Hukukuna İlişkin Emsal Kararlar | 86 | 254 | 0,2 | [kamulastirma](md/kamulastirma/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1Uhk-ZNNk4Xskj3k2lSl8PlQEBF4RxzIE/view) | [gönderi](https://x.com/hakandimdik/status/2121856528135213458) |
| Kat Mülkiyeti Hukukuna İlişkin Emsal Kararlar | 1.813 | 5.711 | 6,3 | [kat-mulkiyeti](md/kat-mulkiyeti/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1O-Gz70yLzErSGhzH2SV-ESziW1Z6zR1l/view) | [gönderi](https://x.com/hakandimdik/status/2124760185310724537) |
| El Atmanın Önlenmesine İlişkin Emsal Kararlar | 4.140 | 6.290 | 13,5 | [el-atma](md/el-atma/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1GHPDJqIk8VpBFaT41bxJtvhVlCTxoY0O/view) | [gönderi](https://x.com/hakandimdik/status/2125974297445327239) |
| Ecrimisile İlişkin Emsal Kararlar | 1.433 | 3.396 | 4,8 | [ecrimisil](md/ecrimisil/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1tpOUlhpvXjDguHOAZHFxcLp4EWlZPaiM/view) | [gönderi](https://x.com/hakandimdik/status/2125205873844768942) |
| Ortaklığın Giderilmesi Davasına İlişkin Emsal Kararlar | 1.341 | 3.166 | 4,4 | [ortakligin-giderilmesi](md/ortakligin-giderilmesi/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/16zY2S9V_TShKKIStfKX0IM7g4xaXqyh7/view) | [gönderi](https://x.com/hakandimdik/status/2124838622704607329) |

## Aile ve miras hukuku

| Derleme | Sayfa | Karar | MB | Dizin | Özgün PDF | Paylaşım |
|---|--:|--:|--:|---|---|---|
| Boşanma Davalarına İlişkin Emsal Kararlar | 7.566 | 27.137 | 25,2 | [bosanma](md/bosanma/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1wUKTzu-MpNYCjnKlOPSOzoHY3euhqBg1/view) | [gönderi](https://x.com/hakandimdik/status/2124110639895355572) |
| Mal Rejiminin Tasfiyesine İlişkin Emsal Kararlar | 1.345 | 3.757 | 4,8 | [mal-rejimi](md/mal-rejimi/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1dH645N1EIDHusmCfsWvNWn2kyTim3a8q/view) | [gönderi](https://x.com/hakandimdik/status/2124148860784345519) |
| Miras Hukukuna İlişkin Emsal Kararlar (V2) | 3.253 | 7.713 | 11,2 | [miras](md/miras/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1s4Uxu30tKzleDbePq996nvHd_TTgqDlP/view) | [gönderi](https://x.com/hakandimdik/status/2124817867946266977) |

## İcra ve iflas hukuku

| Derleme | Sayfa | Karar | MB | Dizin | Özgün PDF | Paylaşım |
|---|--:|--:|--:|---|---|---|
| Takibe İtiraz, İtirazın Kaldırılması ve İtirazın İptaline İlişkin Emsal Kararlar | 8.475 | 11.158 | 31,0 | [itiraz](md/itiraz/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1ybv6rgW5rIIwyYYOJR9ctkwfLp1Ck2jJ/view) | [gönderi](https://x.com/hakandimdik/status/2126093665944649754) |
| İcra Hukukunda Şikâyete İlişkin Emsal Kararlar | 4.661 | 9.903 | 15,4 | [sikayet](md/sikayet/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/14tGrLA3RyIlJ8sOBsb74arght3QINNRR/view) | [gönderi](https://x.com/hakandimdik/status/2126061525886455833) |
| Menfi Tespit, İstirdat ve Borçtan Kurtulma Davalarına İlişkin Emsal Kararlar | 10.208 | 13.526 | 36,7 | [menfi-tespit](md/menfi-tespit/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1VoeNRqjbkW8i7Per2JmMZUWqU4Kc3PpY/view) | [gönderi](https://x.com/hakandimdik/status/2126192082326798830) |

## Tazminat ve sorumluluk

| Derleme | Sayfa | Karar | MB | Dizin | Özgün PDF | Paylaşım |
|---|--:|--:|--:|---|---|---|
| Malpraktis Davalarına İlişkin Emsal Kararlar | 5.230 | 6.750 | 18,1 | [malpraktis](md/malpraktis/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1wg_S8q2PblyejBOO-1W1ly27pJuBpCji/view) | [gönderi](https://x.com/hakandimdik/status/2126020087886856210) |
| Trafik Kazalarından Doğan Tazminat Davalarına İlişkin Emsal Kararlar | 84 | 263 | 0,2 | [trafik](md/trafik/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1toJugLsSwKfuN3dKEM1hJKEXWTFP03Ih/view) | [gönderi](https://x.com/hakandimdik/status/2121973692531917161) |

## İş hukuku

| Derleme | Sayfa | Karar | MB | Dizin | Özgün PDF | Paylaşım |
|---|--:|--:|--:|---|---|---|
| İş Hukukuna İlişkin Emsal Kararlar | 135 | 315 | 0,4 | [is-hukuku](md/is-hukuku/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1zd8Q7Y-ZKIfdszdMQeXwxLRiKSl09v63/view) | [gönderi](https://x.com/hakandimdik/status/2122020463559733396) |

## Arabuluculuk ve tahkim

| Derleme | Sayfa | Karar | MB | Dizin | Özgün PDF | Paylaşım |
|---|--:|--:|--:|---|---|---|
| Dava Şartı Arabuluculuğa İlişkin Emsal Kararlar — Cilt 1 | 58 | 120 | 0,2 | [arabuluculuk-c1](md/arabuluculuk-c1/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1gRVphTadY4OpLETUFCx3Ie7k3xlmAvrB/view) | [gönderi](https://x.com/hakandimdik/status/2122071734677389525) |
| Dava Şartı Arabuluculuğa İlişkin Emsal Kararlar — Cilt 2 | 674 | 2.382 | 2,3 | [arabuluculuk-c2](md/arabuluculuk-c2/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1k57zv8-SoVeLawqmHJt_XTUrS0wc9f1l/view) | [gönderi](https://x.com/hakandimdik/status/2122071734677389525) |
| Dava Şartı Arabuluculuğa İlişkin Emsal Kararlar — Cilt 3 | 600 | 978 | 2,2 | [arabuluculuk-c3](md/arabuluculuk-c3/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1CUWA7H8phBWtGHVFImENdwgV4Mfx-Z6j/view) | [gönderi](https://x.com/hakandimdik/status/2122071734677389525) |
| Dava Şartı Arabuluculuğa İlişkin Emsal Kararlar — Cilt 4 | 72 | 97 | 0,2 | [arabuluculuk-c4](md/arabuluculuk-c4/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1xxmnoF3LjFrqiKB25XJt12wTiqBXw5KI/view) | [gönderi](https://x.com/hakandimdik/status/2122071734677389525) |
| Dava Şartı Arabuluculuğa İlişkin Emsal Kararlar — Cilt 5 | 59 | 67 | 0,2 | [arabuluculuk-c5](md/arabuluculuk-c5/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1Yvyd4xp8pVVvrTx5L-fY4RQmHnhGv8d4/view) | [gönderi](https://x.com/hakandimdik/status/2122071734677389525) |
| Dava Şartı Arabuluculuğa İlişkin Emsal Kararlar — Cilt 6 | 12 | 8 | <0,1 | [arabuluculuk-c6](md/arabuluculuk-c6/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/11NGFVizha2aM60ZTO1xDJlzFdgmf-ESd/view) | [gönderi](https://x.com/hakandimdik/status/2122071734677389525) |
| Dava Şartı Arabuluculuğa İlişkin Emsal Kararlar — Cilt 7 | 6 | 4 | <0,1 | [arabuluculuk-c7](md/arabuluculuk-c7/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1DjSFdmeqPUbrb1VZcEyQcWKp2WuCeYGP/view) | [gönderi](https://x.com/hakandimdik/status/2122071734677389525) |
| Dava Şartı Arabuluculuğa İlişkin Emsal Kararlar — Cilt 8 | 6 | 7 | <0,1 | [arabuluculuk-c8](md/arabuluculuk-c8/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1UpTr7_4VWBng7n0-5oEeKECSuN0UZx0g/view) | [gönderi](https://x.com/hakandimdik/status/2122071734677389525) |
| Tahkime İlişkin Emsal Kararlar (V2) | 41 | 85 | 0,1 | [tahkim](md/tahkim/00-icindekiler.md) | [PDF](https://drive.google.com/file/d/1MVO1q7aTOlhueZz5_o1n5Erx-bFKril4/view) | [gönderi](https://x.com/hakandimdik/status/2121490970545983892) |

## Dönüştürme ve doğrulama

Dönüştürme [pdf-md](https://github.com/hasanimer/pdf-md-skill) betiğiyle yapıldı. Her çıktı, PDF'ten ikinci bir motorla (`pdftotext`) çıkarılan metinle boşluklar atılarak karakter karakter karşılaştırıldı: 34 derleme tam eşleşti.

- Kapak ve içindekiler sayfaları atlandı (ilk yer imine kadar), `Sayfa N / M` altbilgileri atıldı, karar künyelerinin sonundaki `:` silindi.
- *Arsa Payı Karşılığı İnşaat ve Kentsel Dönüşüm* derlemesindeki 3 fark kayıp değildir: başka yazı tipiyle basılmış `₺` ve `III` parçalarını başvuru metni satır sonuna atıyor, Markdown doğru yerde tutuyor.
- Yer imi sayısı ile başlık sayısı, Kira Hukuku V7 dışındaki tüm derlemelerde birebir tutuyor.
- `yapi.py` dönüştürücü çıktısını konu başlıklarına göre parçalara böler; `python3 yapi.py --dogrula` parça dosyalarından yeniden kurulan başlık dizisini ve boşluksuz metni dönüştürücü çıktısıyla karşılaştırır, dizinlerle veri kümesinin tutarlılığını ve üretimin yinelenebilirliğini denetler (`log/yapi.log`).

Her dosyanın yoklama, dönüştürme ve doğrulama çıktısı `log/<ad>.log` içindedir.

## Bilinen sınırlar

- Paragraf sınırları sezgiseldir; doğrulama yalnız metnin eksiksizliğini ölçer.
- *Kira Hukuku V7*'de s. 1061 ve s. 4301 çevresinde 12 punto kalın olmayan bir bölüm var. Gövde metni başlık sanılmasın diye bu stil başlık sayılmadı. Bu yüzden düz satır olarak çıkan 3 kaynak satırı elle düzeltildi (`ek/Kira_Hukuku_Emsal_Kararlar_V7.satirlar.tsv`): `- Yargıtay 8. HD 2017/15084 K.:` → `#### Yargıtay 8. HD 2017/15084 K.`; `A. ARABULUCULUK ŞARTI SAĞLANMIŞ OLMAZ` → `### A. ARABULUCULUK ŞARTI SAĞLANMIŞ OLMAZ`; `B. ARABULUCULUK ŞARTI SAĞLANMIŞ OLUR` → `### B. ARABULUCULUK ŞARTI SAĞLANMIŞ OLUR`. Başlığa çevrilen satırlar konu başlığı ya da karar künyesi olarak işlenir; künyede baştaki liste tiresi ve sondaki iki nokta atılmıştır. Düzeltmeler `log/<ad>.log` içinde `=== yapi satirlar` altında, `log/yapi.log` içinde de yazılıdır.
- Metin Unicode NFC biçimine getirilir (dönüştürücü çıktısındaki birkaç ayrık harf+işaret çifti birleşik harf olur); doğrulama da NFC'den sonra karşılaştırır. Kaynaktaki küçük kusurlar olduğu gibi kalır (ör. Boşanma derlemesinde `#` ile başlayan iki gövde satırı).
- Başlıklar biçimine göre sınıflanır (konu, karar künyesi, FIDIC'te özgün metin/çeviri ara başlığı). Künye biçiminde olmayan 39 başlık satırı (Kira Hukuku V7'de başlık stiliyle yazılmış gövde cümleleri) düz paragraf olarak yazıldı. Sınıflayıcının kararsız kaldığı başlıklar `log/<ad>.log` içinde `=== yapi basliklar` altındadır; düzeltme `ek/<ad>.basliklar.tsv` (başlığın sınıfı) ya da `ek/<ad>.satirlar.tsv` (kaynak satırının kendisi) ile yapılır.
- Künyelerin yalnız %2,5'inde esas numarası vardır; 1.265 künyenin altında metin yoktur (çoğu art arda sıralanmış seri kararlardır; hangi komşu alıntıyı paylaştıklarını kaynak söylemez, metin kopyalanmamıştır). Kayıtların yaklaşık %21'i başka bir kayıtla aynı alıntıyı taşır; künye sayısı bağımsız karar sayısı değildir.
- Alınmayanlar: eski sürümler (Kira V2–V6, Tahkim V1), karar derlemesi olmayan paylaşımlar (dilekçe örnekleri, sunumlar, bilgi notları) ve Tasarrufun İptali derlemesi.
- X araması eksiksiz olmayabilir; Google Drive dışında bir bağlantıyla paylaşılmış derleme varsa burada yoktur.

## Atıf ve teşekkür

Derlemeleri hazırlayan ve bu depoda yayımlanmasına izin veren Av. Hakan Dimdik'e teşekkür ederiz.

- **Derlemeler:** Av. Hakan Dimdik — [x.com/hakandimdik](https://x.com/hakandimdik). `kaynaklar.tsv` her derlemenin paylaşıldığı gönderiyi, `indir.tsv` özgün PDF'in Drive kimliğini tutar.
- **Kira Hukuku derlemesi:** derleyenin belirttiği üzere Av. Yankı Büyüksezer'in paylaştığı kararlara da yer verilmiştir.
- **Dönüştürme:** [pdf-md](https://github.com/hasanimer/pdf-md-skill).

Önerilen atıf biçimi: *Av. Hakan Dimdik, "<derlemenin adı>", X (@hakandimdik), 2026.*

## Yeniden üretme

Özgün PDF'ler depoda tutulmaz (`pdf/` yok sayılır); `indir.tsv` içindeki Drive kimliklerinden yeniden indirilir.

```bash
./indir.sh
ls pdf/*.pdf | xargs -P 4 -n 1 ./cevir.sh
python3 yapi.py && python3 yapi.py --dogrula
python3 araclar/cilt.py            # isteğe bağlı: yükleme ciltleri (yukle/)
```

`cevir.sh` betiği `~/.claude/skills/pdf-md/scripts/pdf2md.py` yolunda arar; başka yerdeyse `PDF2MD` değişkeniyle verin; çıktıyı `ara/<ad>/` altına yazar (depoda tutulmaz). Dosyaya özel seçenekler `ek/<ad>.args` içindedir. `derlemeler.tsv` derlemelerin kayıt defteridir (kod, ad, başlık, alan, sürüm, sıra); `yapi.py` (yalnız Python standart kitaplığı) `md/`, `dizin/`, `veri/` ile `AGENTS.md`, `llms.txt`, `TALIMAT.txt` ve bu dosyayı baştan üretir. `kaynaklar.tsv` her derlemenin paylaşım bağlantısını ve gönderi kimliğini tutar.
