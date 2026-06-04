# ELEKTRONİK HARP YARIŞMASI 2026 - KRİTİK TASARIM RAPORU

**Takım Adı:** Dev-in-Scrubs
**Proje Adı:** Aegis-AI OMEGA v3.0

---

## İÇİNDEKİLER
1. TEMEL SİSTEM ÖZETİ (10 Puan)
    1.1 Sistem Tanımı
    1.2 Sistem Nihai Performans Özellikleri
2. ORGANİZASYON ÖZETİ (5 Puan)
    2.1 Takım Organizasyonu
    2.2 Zaman Akış Çizelgesi ve Bütçe
3. DETAYLI TASARIM ÖZETİ (25 Puan)
    3.1 Nihai Sistem Mimarisi ve Alt Sistemlerin Özeti
    3.2 Sistem ve Alt Sistemlerin Üç Boyutlu Tasarımı
    3.3 Sistem ve Alt Sistemlerin SWaP Bilgisi
4. ED GÖREVLERİ VE EKRAN GÖRSELLERİ (20 Puan)
    4.1 Sinyal Tespiti
    4.2 Parametre Çıkarımı
    4.3 Sinyal İzleme ve Dinleme
    4.4 Yön Bulma (DF)
    4.5 Konum Belirleme
5. ET GÖREVLERİ VE EKRAN GÖRSELLERİ (20 Puan)
    5.1 Sürekli Karıştırma
    5.2 Arabakışlı Karıştırma
    5.3 Analog Telsiz Aldatma
    5.4 GNSS Aldatma
6. SİMÜLASYON VE TEST (15 Puan)
    6.1 Etkinlik Simülasyonları
    6.2 Alt Sistem Geliştirme Testleri
    6.3 Görev Testleri
7. REFERANSLAR

---

## 1. TEMEL SİSTEM ÖZETİ (10 Puan)

### 1.1 Sistem Tanımı
Aegis-AI OMEGA, modüler, yapay zeka destekli ve Software Defined Radio (SDR) tabanlı entegre bir Bilişsel Elektronik Harp (Cognitive EW) platformudur. Sistem, coğrafi olarak dağıtık 2 ana üniteden oluşmaktadır: Bir adet **Ana ED/ET Ünitesi** ve bir adet **Yavru ED/ET Ünitesi**. Sistem, spektrumu akıllı otonom algoritmalarla analiz edip hedefe dinamik reaksiyon (karıştırma/aldatma) verebilen kapalı çevrim (closed-loop) bir otonomiye sahiptir. 
Sistemi oluşturan temel alt sistemler (DKB'ler):
- **DKB-01 SDR Alıcı/Verici Ünitesi:** Geniş bantlı RF sinyallerini I/Q verisine dönüştüren ve karıştırma sinyallerini yayan ana RF katmanı (Ettus USRP).
- **DKB-02 İşleme Birimi (SBC):** Algoritmaların koştuğu, yüksek performanslı işlemci ünitesi (Raspberry Pi 5 / Jetson).
- **DKB-03 Anten Dizisi:** Yön Bulma (DF) ve Karıştırma (Jamming) için kullanılan 12x Vivaldi dairesel dize ve 1x Log-Periyodik anten seti.
- **DKB-04 Güç ve Enerji Yönetimi:** Sistemin saha operasyonları için ihtiyaç duyduğu DC/AC dönüşümü ve batarya bloğu.

### 1.2 Sistem Nihai Performans Özellikleri

**Elektronik Destek (ED) Sistemi Özelinde:**
| Özellik | Performans Değeri |
| :--- | :--- |
| Kestirme (DF) Birimi Çalışma Frekans Aralığı | 70 MHz - 6000 MHz |
| Kestirme (DF) Birimi Yanca Açı Kapsaması | 360° |
| Kestirme (DF) Birimi Kanal Sayısı | 12 Kanal (Ana ünite dairesel dizilim) |
| Kestirme (DF) Birimi Anlık Bant Genişliği | 160 MHz |
| Kestirme (DF) Birimi Yön Doğruluğu | < 3 derece (RMS) |
| Kestirme (DF) Algoritması | MUSIC (Multiple Signal Classification) ve Correlative Interferometry |
| Sinyal İzleme/Dinleme Birimi Çalışma Frekans Aralığı | 70 MHz - 6000 MHz |
| Sinyal İzleme/Dinleme Birimi Kanal Sayısı | 2 Kanal |
| Sinyal İzleme/Dinleme Birimi Anlık Bant Genişliği | 160 MHz |
| Sinyal İzleme/Dinleme Birimi Demodülasyon Özellikleri | AM, FM, ASK, FSK, PSK, QAM varyantları otonom demodülasyon |
| AI Modülasyon Sınıflandırma Doğruluğu | Yüksek (>%90, -5dB SNR'a kadar) 1D CNN ile |

**Elektronik Taarruz (ET) Sistemi Özelinde:**
| Özellik | Performans Değeri |
| :--- | :--- |
| Karıştırma Birimi Çalışma Frekans Aralığı | 70 MHz - 6000 MHz |
| Karıştırma Birimi Kanal Sayısı | 4 Farklı RF Kanalı |
| Karıştırma Birimi Toplam Güç Tüketimi | < 150 Watt (PA ve soğutma dahil) |
| Karıştırma Tipleri ve Teknikleri | Spot, Sweep, Baraj Karıştırma (Sürü Bastırma) |
| Arabakışlı Karıştırma Özellikleri | %90 Karıştırma (TX), %10 Dinleme (RX) (Mikro-saniye anahtarlama) |
| Telsiz Aldatma Özellikleri | Analog Ses Aldatma, Capture Effect sızma |
| GNSS Aldatma Özellikleri | GPS L1/L2 Spoofing (Zaman ve Konum Yanıltma) |
| DRFM Özellikleri | RGPO, VGPO, Sentetik Sahte Hedef Üretimi |

## 2. ORGANİZASYON ÖZETİ (5 Puan)

### 2.1 Takım Organizasyonu
**Dev-in-Scrubs** takımı çok disiplinli mühendislik kadrosu ile aşağıdaki şekilde organize olmuştur:
- **Sinyal İşleme (DSP) Liderliği:** SDR arayüzleri, FPGA/C++ tabanlı DDC/DUC yapıları ve I/Q sinyal işleme geliştirimi.
- **Yapay Zeka Sorumlusu:** CNN tabanlı Modülasyon Sınıflandırma (AMC) ağları ve Reinforcement Learning tabanlı strateji ajanları.
- **Donanım ve RF Entegrasyon:** USRP, Vivaldi/Log-periyodik antenler, güç regülasyonu ve tripod üzeri elektromekanik yerleşim.
- **Yazılım Arayüzü ve Taktik Kontrol:** Aegis-UI Dashboard geliştirimi ve ağ haberleşmesi.

### 2.2 Zaman Akış Çizelgesi ve Bütçe
Çalışmalar, önceden belirlenen 2026 OMEGA yol haritasına tam uyumlu ilerlemektedir:
- **Tamamlananlar:** v1.0 (Core Foundation - Temel DSP), v2.0 (Autonomy - AI Entegrasyonu), v3.0 (OMEGA - DRFM, Sürü Bastırma).
- **Planlananlar:** v4.0 (Field Test - Gerçek saha/SDR testleri).
Tahmini bütçe; Raspberry Pi 5 / Jetson SBC'ler, Ettus USRP B210 altyapıları ve RF anten dizileri (Vivaldi + Log-Periyodik) üzerine optimize edilmiştir ve planlanan donanım alımları zamanında, bütçe sınırları (< 150W sarfiyatlı saha profili) dâhilinde gerçekleşmiştir.

## 3. DETAYLI TASARIM ÖZETİ (25 Puan)

### 3.1 Nihai Sistem Mimarisi ve Alt Sistemlerin Özeti
Sistem Mimarisi, **Ana Ünite** ve **Yavru Ünite** ayaklarından oluşan kapalı çevrim bir otonomi döngüsü kullanır. Birincil kontrol birimi olarak **Raspberry Pi 5 (8GB)** veya **NVIDIA Jetson Orin** seçilmiştir. RF Altyapısı olarak **Ettus USRP B210** (70MHz - 6GHz, 2x2 MIMO) kullanılarak SDR tabanlı esnek yapı hedeflenmiştir.

Sistem Mimarisi Blok Şeması:
`Saha Birimi -> 12x Vivaldi Anten -> LNA / Filtre -> SDR (USRP B210) -> USB 3.0 -> İşleme Birimi (SBC) -> Log-Periyodik ET Anteni (PA ile)`

I/Q verileri ağ üzerinden düşük gecikmeli link ile SBC üzerinde füzyonlanır. Donanım abstraksiyonu `SoapySDR/UHD` ile sağlanır. Yapay zeka modülasyon tanıma motoru, SDR'dan gelen veriyi anlık işler. Ettus USRP B210, Full-Duplex özelliği sayesinde hem ara-bakışlı karıştırma hem de faz koherent yön bulma yeteneklerini aynı donanımda birleştirir.

### 3.2 Sistem ve Alt Sistemlerin Üç Boyutlu Tasarımı
Sistem, "Manga/Tim Seviyesi Taşınabilir" ve kullanım sırasında **sabit (fixed-site)** bir platformdur. 
Operasyon alanına tekerlekli nakliye çantaları ile intikal edilir. Kurulum aşamasında 120 cm boyundaki askeri standartta tripodlar üzerine anten dizileri yerleştirilir. Alt bölümde, merkezde 12'li Vivaldi anten dairesel olarak yatay eksende dizilmiş, üst kısımda ise dikey polarizasyonlu Log-Periyodik ET anteni konumlandırılmıştır. DKB-01 ve DKB-02, tripod tabanında dış etkilerden korunan aktif fan soğutmalı bir kompozit çanta içinde yer alır. 

### 3.3 Sistem ve Alt Sistemlerin SWaP Bilgisi
| Alt Sistem | Boyut | Ağırlık | Güç (Watt) |
| :--- | :--- | :--- | :--- |
| Ana ED/ET Ünitesi (Tripod dahil) | Çap: 45cm, Yükseklik: 120cm | < 10 kg | Toplam Sistem < 150 W |
| Yavru ED/ET Ünitesi | Çap: 45cm, Yükseklik: 120cm | < 10 kg | Toplam Sistem < 150 W |

Enerjilendirme: 4S - 6S LiPo veya Lityum-İyon batarya blokları ile besleme planlanmıştır. Sahada 150W tepe yük durumunda sistem kendi bataryası ile minimum 4+ saat operasyonel kalabilmektedir. İhtiyaç halinde çantalar halinde hızlıca yer değişimi sağlanır.

## 4. ED GÖREVLERİ VE EKRAN GÖRSELLERİ (20 Puan)

### 4.1 Sinyal Tespiti
Geniş bantlı spektrum tarama yöntemiyle SDR üzerinden alınan I/Q verilerine gerçek zamanlı FFT işlemleri uygulanır. Elde edilen Güç Spektral Yoğunluk (PSD) verisi, **Adaptive CFAR (Constant False Alarm Rate)** ve Enerji Tespiti algoritmaları ile işlenir. Spektrumdaki gürültü zemini dinamik olarak hesaplanır; eşiği aşan pikler, otonom motor tarafından "Threat Candidates" olarak işaretlenir. 
Ayrıca LPI radarlar gibi zorlu hedefler için **Wigner-Ville Distribution (WVD)** ve **Spectral Entropy** motorları koşturularak düşük güçlü tehditlerin yapısal imzaları çıkartılır.

### 4.2 Parametre Çıkarımı
Sinyal tespitinden sonra Digital Down Conversion (DDC) ile hedef sinyal ana banda indirilir. Hilbert analitik sinyal yaklaşımıyla Merkez Frekansı, Bant Genişliği ve SNR elde edilir. 
Modülasyon sınıflandırmasında kural tabanlı algoritmalar ile **1D CNN derin öğrenme mimarisi (ResNet tabanlı)** hibrit olarak kullanılır. Sinyal spektrumundan ve I/Q dağılımından özellikleri çıkararak -5dB SNR'a kadar modülasyon (AM, FM, PSK, QAM vb.) ve sembol hızı %90 üzerinde başarı ile saptanır. 

### 4.3 Sinyal İzleme ve Dinleme
Analiz edilen sinyalin şifresiz bir analog (NBFM, AM) muhabere olduğu teyit edildiğinde, Costas loop ve PLL temelli demodülatör bloklar aktif edilir. Analog ses doğrudan Aegis-UI üzerinden operatörün kullanımına sunulur veya WAV olarak kaydedilir. Sayısal sinyallerde ise pulse yapıları çıkarılarak PDW (Pulse Descriptor Word) şeklinde veritabanına yazılır.

### 4.4 Yön Bulma (DF)
Yön bulma görevi, **Faz Karşılaştırmalı Yön Bulma** prensibiyle gerçekleştirilmektedir. 12 adet Vivaldi anten ile dairesel dizeye ulaşan sinyallerin uzamsal faz farkları hesaplanır. Algoritma olarak yüksek çözünürlüklü **MUSIC (Multiple Signal Classification)** ve Correlative Interferometry tercih edilmiştir. Bu sayede < 3 derece RMS doğruluğu hedeflenmiştir. 

### 4.5 Konum Belirleme
Konum belirleme görevi, **Varış Zamanı Farkı (TDOA)** ve Yön Kestirimi (AOA) verilerinin birleştirilmesi (Füzyon) ile yapılır. Bu işlem için asgari 2 adet dağıtık istasyon (Ana Ünite ve Yavru Ünite) konumlandırılır. GPS/PPS hassas zaman damgalarıyla eşitlenen istasyonlardan gelen zaman ve açı vektörleri kesiştirilerek harita (Aegis-UI) üzerinde kaynağın 2D lokasyonu kestirilir.

## 5. ET GÖREVLERİ VE EKRAN GÖRSELLERİ (20 Puan)

### 5.1 Sürekli Karıştırma
Sürekli karıştırmada hedefe DRFM ve DDS teknikleri ile statik karıştırma uygulanır. Operatör veya AI kararıyla hedefe yönelik Spot (dar bant enerji yoğunlaşması), Sweep (frekans aralığını dinamik süpürme) ve Baraj Karıştırma (AWGN) teknikleri kullanılır. Ayrıca birden fazla emiterin bulunduğu (İHA Sürüleri gibi) senaryolarda "Swarm Suppression" (Sürü Bastırma) ile koordinasyon linklerine eş zamanlı enerji basılır.

### 5.2 Arabakışlı Karıştırma
Ara-bakış (Look-through) yeteneğinde SDR'ın hızlı anahtarlama kapasitesi kullanılır. Sistem karıştırma görevini %90 TX (Karıştırma), %10 RX (Dinleme) zaman dilimlerine böler. Mikro saniye mertebesinde gerçekleşen dinleme anında hedefin hala yayın yapıp yapmadığı, tespit/eşikleme yaklaşımı ile (anlık FFT enerji ölçümü) kontrol edilir. Eğer hedefin yayını kesilmişse sistem enerjiyi boşa harcamamak adına karıştırmayı durdurur.

### 5.3 Analog Telsiz Aldatma
Hedefin amatör analog ses telsizi (NBFM/AM) olması durumunda sahte ses veya anons üretilerek sızma yapılır. FM sinyallerindeki "Capture Effect" (Güç Yakalama) prensibinden yararlanılarak, hedefe ana yayından daha güçlü sentetik bir analog sinyal basılır. Böylelikle hedef sistem alıcısının "yanlış duyması" hedeflenir.

### 5.4 GNSS Aldatma
GPS L1 ve L2 frekanslarında sentetik uydu efemeris verisi SDR kullanılarak dinamik şekilde oluşturulur. **Spoofing** (Aldatma) yöntemiyle, hedefteki alıcının kilitlendiği asıl GNSS uyduları üzerine daha yüksek güçlü ancak sahte zaman/konum bilgisi içeren PRN kodları yayınlanarak hedef manipüle edilir. Ek olarak radar sistemleri için RGPO ve VGPO gibi menzil ve hız kaydırma DRFM algoritmaları koşulabilir.

## 6. SİMÜLASYON VE TEST (15 Puan)

### 6.1 Etkinlik Simülasyonları
Yazılım mimarisi içerisinde `simulation/` modülü bulunmaktadır. 
- **ED Analizleri:** Spektral Entropi (Detection Metric) formülasyonu ($H(S)$) ile LPI radar tespit duyarlılığı simüle edilmiştir. AOA/TDOA için ideal yerleşim analizi (100+ metre uzaklık, clear-line-of-sight) yapılmıştır.
- **ET Analizleri:** Swarm bastırma ve otonom Reinforcement Learning ajanının frekans atlamalı hedeflere karşı karar verme başarımları SITL (Software-In-The-Loop) olarak test edilmiştir.

### 6.2 Alt Sistem Geliştirme Testleri
Donanım altyapısı USRP B210'lar ile masaüstü laboratuvar ortamında RF loopback ve attenuatör (zayıflatıcı) testleri ile doğrulanmaktadır. I/Q veri transfer hızı darboğazları tespit edilip Raspberry Pi 5 USB 3.0 I/O optimizasyonları tamamlanmıştır.

### 6.3 Görev Testleri
Test planlaması kapsamında, v4.0 Yol Haritasında gerçek saha (Field Test) doğrulama testleri yer almaktadır. Yazılım çevrim (SITL) sentetik EH ortamı testleri tamamlanmış olup, donanım entegreli (HITL) kapalı devre RF testleri sürmektedir. Anten dizileri üretildikten sonra açık arazide iki istasyon kurularak TDOA zaman senkronizasyonu doğrulaması yapılacaktır. Testler Aegis-UI Dashboard ve `verify_eh.py` (System Integrity Check) üzerinden takip edilmektedir.

## 7. REFERANSLAR
1. O'Shea, T. J., & West, N. (2016). "Radio Machine Learning Dataset Generation with GNU Radio".
2. DeepSig RadioML Veriseti.
3. ResNet-Based AMC Mimarisi Literatürü.
4. "Aegis-AI OMEGA v3.0 Geliştirici Dokümanları ve Manifesto", Dev-in-Scrubs Takımı, 2026.
5. TEKNOFEST 2026 Elektronik Harp Şartnamesi.
