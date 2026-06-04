# ELEKTRONİK HARP YARIŞMASI 2026 - KRİTİK TASARIM RAPORU METİNLERİ

**Takım Adı:** Arat
**Proje Adı:** Arat OMEGA v3.0

*(Aşağıdaki metinleri doğrudan KTR Word şablonunuzdaki ilgili başlıkların altına kopyalayıp yapıştırabilirsiniz.)*

---

## 1. TEMEL SİSTEM ÖZETİ (10 Puan)

### 1.1 Sistem Tanımı
Arat takımı olarak geliştirdiğimiz "Arat OMEGA v3.0", karmaşık elektromanyetik harp sahasında otonom karar verebilen, yapay zeka destekli ve Software Defined Radio (SDR) tabanlı entegre bir Bilişsel Elektronik Harp (Cognitive EW) sistemidir. 

Sistemimiz coğrafi olarak dağıtık **2 ana üniteden** (Ana ED/ET Ünitesi ve Yavru ED/ET Ünitesi) oluşmaktadır. 
- **Ana Elektronik Destek (ED) Sistemi:** 20x30 cm boyutlarında dairesel olarak sıralanmış 8 adet Vivaldi anten ve geniş bantlı SDR alıcısından oluşmaktadır. Temel görevi spektrumdaki sinyallerin tespit edilmesi ve yüksek doğrulukla yön bulma (DF) işleminin yapılmasıdır.
- **Yavru Elektronik Destek (ED) Sistemi:** 90 derece yerleşim açısına sahip Vivaldi antenlerden oluşur ve Ana ED sistemi ile TDOA/AOA tabanlı konum belirleme görevini yürütür.
- **Elektronik Taarruz (ET) Sistemi:** Hem Ana hem de Yavru ED ünitesi üzerinde birer adet bulunacak şekilde, 1 metre yüksekliğinde Log-Periyodik antenlerden oluşmaktadır. 4 farklı bantta yüksek RF çıkış gücü ile köreltme ve karıştırma görevlerini yerine getirir. Taarruz donanımı, ısınmaya karşı metal kafes ve aktif fan soğutmalı bir haznede muhafaza edilmektedir.

### 1.2 Sistem Nihai Performans Özellikleri
*(Bu kısmı Word şablonunuzdaki tabloya yerleştirin)*

**Elektronik Destek (ED) Sistemi Özelinde:**
- **Kestirme (DF) Birimi Çalışma Frekans Aralığı:** 70 MHz - 6000 MHz
- **Kestirme (DF) Birimi Yanca Açı Kapsaması:** 360° (Ana Ünite) / 90° (Yavru Ünite)
- **Kestirme (DF) Birimi Kanal Sayısı:** 8 Kanal (Ana ünite dairesel dizilim)
- **Kestirme (DF) Birimi Anlık Bant Genişliği:** 160 MHz
- **Kestirme (DF) Birimi Yön Doğruluğu:** < 3 derece (RMS)
- **Kestirme (DF) Algoritması:** MUSIC ve Correlative Interferometry
- **Sinyal İzleme/Dinleme Birimi Kanal Sayısı:** 2 Kanal
- **AI Modülasyon Sınıflandırma Doğruluğu:** >%90 (-5dB SNR'a kadar, 1D CNN + Heuristic hibrit model ile)

**Elektronik Taarruz (ET) Sistemi Özelinde:**
- **Karıştırma Birimi Çalışma Frekans Aralığı:** 70 MHz - 6000 MHz
- **Karıştırma Birimi Kanal Sayısı:** 4 Farklı RF Kanalı
- **Karıştırma Tipleri ve Teknikleri:** Spot, Sweep, Baraj Karıştırma, Sürü Bastırma (Swarm Suppression)
- **Arabakışlı Karıştırma Özellikleri:** %90 Karıştırma (TX), %10 Dinleme (RX) (Mikro-saniye anahtarlama)
- **Telsiz Aldatma Özellikleri:** Analog Ses Aldatma (Voice Spoofing), Capture Effect
- **GNSS Aldatma Özellikleri:** GPS L1/L2 Spoofing (Zaman ve Konum Yanıltma)
- **DRFM Özellikleri:** RGPO, VGPO, Sentetik Sahte Hedef Üretimi

---

## 2. ORGANİZASYON ÖZETİ (5 Puan)

### 2.1 Takım Organizasyonu
**Arat** takımı, karmaşık mühendislik problemlerine "Solopreneur" (tek kişilik ekip) çevikliğiyle bütünsel çözümler üretmek amacıyla kurulmuştur. Ekibimiz, disiplinlerarası bir yaklaşımla teknolojinin farklı katmanlarında katma değer yaratmaya odaklanan tek bir teknoloji profesyonelinden oluşmaktadır. Organizasyonumuz aşağıdaki üç ana sütun üzerinde yürütülmektedir:
- **Yapay Zeka & Otonom Sistemler:** Karar destek ve otomasyon süreçlerinin geliştirilmesi.
- **Endüstriyel Optimizasyon:** Süreç ve kaynak verimliliği tasarımı ve iyileştirmeleri.
- **Sistem Mimarisi:** Donanım ve yazılımın uyum içinde çalıştığı, ölçeklenebilir entegre sistemlerin kurgulanması.

Takım üyemiz; Siber Vatan siber güvenlik eğitimi, TEİ Havacılık Motorları Okulu programı ve yapay zeka tabanlı patentli proje geliştirme tecrübelerine sahip olup, projelerin hem teknik (DSP, RF, Yazılım) hem de operasyonel (Donanım Entegrasyonu) süreçlerini tek merkezden yönetmektedir.

### 2.2 Zaman Akış Çizelgesi ve Bütçe
Çalışmalar, önceden belirlenen 2026 yarışma takvimine tam uyumlu ilerlemektedir. Çekirdek yazılım (Core Foundation), yapay zeka entegrasyonu (Autonomy) ve DRFM algoritmaları başarıyla tamamlanmıştır. Mevcut aşamada donanım üretim (HITL) testleri planlanmaktadır. 
Tahmini bütçemiz; Ettus USRP tabanlı SDR altyapıları, kompozit malzemeli hafif şasiler, Vivaldi ve Log-Periyodik RF anten dizileri ile aktif soğutmalı güç yükselteçleri (PA) üzerinden maliyet-etkin olacak şekilde optimize edilmiştir. Bugüne kadar yapılan prototipleme harcamaları planlanan bütçe sınırları dâhilinde gerçekleşmiştir.

---

## 3. DETAYLI TASARIM ÖZETİ (25 Puan)

### 3.1 Nihai Sistem Mimarisi ve Alt Sistemlerin Özeti
Sistem mimarisi, kapalı çevrim bir otonomi döngüsü üzerine inşa edilmiştir. Donanım hiyerarşisi aşağıdaki birimlerden (DKB) oluşmaktadır:
- **DKB-01 (SDR Alıcı/Verici Ünitesi):** Ettus USRP tabanlı geniş bantlı RF altyapısı.
- **DKB-02 (İşleme Birimi - SBC):** Otonom algoritmaların, AI modüllerinin (CNN Modülasyon Sınıflandırma) ve DRFM kernellerinin koştuğu yüksek performanslı işlemci birimi (Raspberry Pi 5 / NVIDIA Jetson).
- **DKB-03 (Anten Dizisi):** Yön bulma için dairesel yerleşimli Vivaldi antenler ve ET için dikey Log-Periyodik anten.
- **DKB-04 (Güç ve Enerji Yönetimi):** Sistemin LiPo/Li-ion bataryalardan beslenmesini ve DC-DC regülasyonunu sağlayan katman.

Tüm haberleşme ve I/Q veri senkronizasyonu, Ana ve Yavru ünite arasında düşük gecikmeli veri bağları üzerinden gerçekleştirilir. Geleneksel sistemlerin aksine Arat OMEGA, donanım abstraksiyonu (SoapySDR/UHD) sayesinde SDR donanımından bağımsız, donanım-agnostik bir yazılım mimarisiyle çalışır.

### 3.2 Sistem ve Alt Sistemlerin Üç Boyutlu Tasarımı
Sistemimiz "Manga/Tim Seviyesi Taşınabilir" ve kullanım sırasında **sabit (fixed-site)** kalacak şekilde tasarlanmıştır. Sahaya tekerlekli kompozit taşıma çantaları ile intikal ettirilir.
Kurulum aşamasında, yerden yüksekliği 120 cm olan dayanıklı karbon fiber/kompozit tripod (üçayak) mekanizmaları kullanılır. 
- Tripodun üst kısmına 20x30 cm çapında dairesel dizilmiş 8'li Vivaldi anten tablası (Ana ED ünitesi) yerleştirilir. 
- Bu tablanın hemen üzerine, elektronik taarruz görevlerini icra edecek olan 1 metre yüksekliğindeki Log-Periyodik anten entegre edilir. Böylece sistemin toplam yüksekliği 220 cm'yi kesinlikle aşmamaktadır (120 cm tripod + 100 cm anten).
- Taarruz (ET) donanımı olan güç yükselteçleri (PA), aşırı ısınmaya karşı metal bir kafes içerisine alınmış ve aktif fan ile soğutulan bir hazneye entegre edilmiştir. Bu hazne tripod gövdesine sabitlenmiştir.

### 3.3 Sistem ve Alt Sistemlerin SWaP Bilgisi
Arat sistemi, yüksek mobilite gereksinimleri gözetilerek kritik **SWaP-C (Size, Weight, Power and Cost)** optimizasyonlarına tabi tutulmuştur:
- **Boyutlar:** Tripod yüksekliği 120 cm, ET anteni 100 cm olmak üzere maksimum sistem yüksekliği 220 cm'dir.
- **Ağırlık:** Ana ED/ET ünitesi ve Yavru ED/ET ünitesinin her biri 10 kg'ın altında kalacak şekilde tasarlanmıştır. Tüm sistem (iki istasyon toplamı) **20 kg'ın altındadır**. Bu ağırlık tasarrufu, anten taşıyıcılarda 3D baskı kompozit materyaller ve karbon fiber donanımlar kullanılarak sağlanmıştır.
- **Güç (Power):** Sistem bünyesinde yer alan 4 farklı bant güç yükselteci (PA), SDR işlemci kartı, anten servo mekanizmaları ve soğutma fanları dâhil edildiğinde toplam donanım güç tüketimi (laptop hariç) **150 Watt'ın altındadır**. Enerji beslemesi, yüksek akım çekişine dayanıklı Lityum-Polimer (LiPo) bataryalar ile sağlanmaktadır.

---

## 4. ED GÖREVLERİ VE EKRAN GÖRSELLERİ (20 Puan)

### 4.1 Sinyal Tespiti
Geniş bantlı spektrum tarama yöntemiyle SDR üzerinden alınan I/Q verilerine gerçek zamanlı FFT işlemleri uygulanır. Elde edilen Güç Spektral Yoğunluk (PSD) verisi, **Adaptive CFAR (Constant False Alarm Rate)** ve Enerji Tespiti algoritmaları ile işlenir. Spektrumdaki gürültü zemini dinamik olarak hesaplanır; eşiği aşan pikler otonom motor tarafından işaretlenir. 
Ayrıca LPI radarlar (Düşük Tespit Edilme Olasılıklı Radarlar) gibi zorlu hedefler için **Wigner-Ville Distribution (WVD)** ve **Spectral Entropy** motorları koşturularak zaman-frekans uzayında düşük güçlü tehditlerin imzaları ayrıştırılır.

### 4.2 Parametre Çıkarımı
Sinyal tespitinden sonra hedefin I/Q verileri Digital Down Conversion (DDC) ile ana banda indirilir. Hilbert analitik sinyal yaklaşımıyla Merkez Frekans, Bant Genişliği ve SNR elde edilir. 
Modülasyon sınıflandırmasında **Hibrit (1D CNN + 2D CNN + Kural Tabanlı)** mimari kullanılmaktadır. Hızlı eşleşmeler için kural tabanlı motor (PRI, PW) devreye girerken, karmaşık dokular için **1D-ResNet (Ham I/Q verisi üzerinden)** ve **2D-EfficientNet-v2 (STFT Spektrogram görüntüleri üzerinden)** tabanlı hibrit Evrişimli Sinir Ağları (CNN) çalıştırılır. Sinyal spektrumundan ve I/Q dağılımından özellik çıkarımı yapılarak -5dB SNR'a kadar modülasyon tipleri (AM, FM, PSK, QAM varyantları) ve sembol hızları yüksek doğrulukla saptanır.

### 4.3 Sinyal İzleme ve Dinleme
Tespit edilen hedefin şifresiz bir analog muhabere (NBFM, AM) olduğu anlaşıldığında, sistemdeki Costas Loop ve PLL temelli demodülatör bloklar aktif edilir. İşlenen analog ses doğrudan Arat Taktik Arayüzü (Dashboard) üzerinden operatöre dinletilir ve aynı zamanda WAV formatında olay kaydı olarak tutulur. Sayısal sinyallerde ise pulse yapıları çıkarılarak PDW (Pulse Descriptor Word) şeklinde veritabanına yazılır.

### 4.4 Yön Bulma (DF)
Ana ED ünitesinde yer alan 20x30 cm dairesel yerleşimli 8 adet Vivaldi anten ile **Faz Karşılaştırmalı Yön Bulma** prensibi uygulanır. Antenlere ulaşan RF sinyallerinin uzamsal faz farkları yüksek çözünürlüklü **MUSIC (Multiple Signal Classification)** algoritması ile işlenerek kaynağın yanca açısı hesaplanır. Sistem bu donanım yapısıyla < 3 derece RMS yön doğruluğu hedefine ulaşmaktadır.

### 4.5 Konum Belirleme
Konum belirleme görevi, **Varış Zamanı Farkı (TDOA)** ve Yön Kestirimi (AOA) verilerinin füzyonu ile sağlanır. Birbirinden coğrafi olarak ayrılmış Ana Ünite ve Yavru Ünite (90° Vivaldi yerleşimli) GPS/PPS hassas zaman damgaları aracılığıyla senkronize edilir. Hedef sinyalin her iki istasyona ulaşma zamanları arasındaki fark (TDOA) ve yön açıları hesaplanarak, hedef koordinatları 2D taktik harita üzerinde kestirilir.

---

## 5. ET GÖREVLERİ VE EKRAN GÖRSELLERİ (20 Puan)

### 5.1 Sürekli Karıştırma
Sistem, Log-Periyodik taarruz antenleri ve 4 farklı kanala sahip PA (Güç Yükseltici) modülleri üzerinden sürekli karıştırma yapar. Otonom yapay zeka kararıyla hedefin durumuna göre **Spot** (dar bant yüksek güç), **Sweep** (frekans süpürme) ve **Baraj Karıştırma** (geniş bant gürültü) teknikleri kullanılır. Karıştırma taktiğinin (güç, modülasyon ve zamanlama) anlık olarak seçilmesinde **Derin Q-Ağı (DQN) ve Q-Learning** tabanlı Bilişsel Elektronik Taarruz (CEW) mimarisi kullanılır. Ayrıca birden fazla emiterin bulunduğu durumlarda (İHA Sürüleri vb.) "Swarm Suppression" mantığıyla koordinasyon linklerine eş zamanlı ve adaptif enerji basılır.

### 5.2 Arabakışlı Karıştırma
Ara-bakış (Look-through) yeteneğinde SDR donanımının Full-Duplex hızlı anahtarlama kapasitesinden yararlanılır. Karıştırma periyodu %90 TX, %10 RX zaman dilimlerine bölünür. Mikro-saniye mertebesindeki RX (Dinleme) süresinde hedef sinyalin hala yayında olup olmadığı anlık FFT/Enerji ölçümü ile denetlenir. Eğer hedef yayınını sonlandırmışsa sistem enerjiyi boşa harcamamak adına karıştırmayı derhal keser.

### 5.3 Analog Telsiz Aldatma
Hedefin amatör analog ses telsizi (NBFM/AM) olması durumunda sahte ses sentezlenerek hedefe yönelik asimetrik sızma gerçekleştirilir. FM sinyallerindeki "Capture Effect" (Güç Yakalama) prensibinden yararlanılarak, hedefe orijinal yayından daha güçlü sentetik bir analog sinyal basılır. Böylelikle hedef alıcının gerçek bilgiyi alamayıp, manipüle edilmiş yanıltıcı sesi duyması sağlanır.

### 5.4 GNSS Aldatma
GPS L1 ve L2 frekans bantlarında SDR kullanılarak sentetik uydu efemeris (yörünge) verisi üretilir. Hedefteki alıcının kilitlendiği asıl GNSS uyduları üzerine, yönlü Log-Periyodik anten aracılığıyla daha yüksek güçlü ancak "yanlış zaman ve konum" bilgisi içeren sahte PRN kodları yayınlanır (Spoofing). Böylece hedefin navigasyon sistemleri yanıltılır.

---

## 6. SİMÜLASYON VE TEST (15 Puan)

### 6.1 Etkinlik Simülasyonları
Sistemin simülasyon altyapısında:
- **ED Analizleri:** LPI radarların tespiti için WVD (Wigner-Ville) analizleri koşturulmuş, farklı gürültü koşullarında (Rayleigh Fading, AWGN) 1D-CNN modülasyon tanıma modelinin doğruluk testleri yapılmıştır. AOA ve TDOA algoritmaları için ideal istasyon yerleşim (baz uzunluğu) analizleri simüle edilmiştir.
- **ET Analizleri:** Frekans atlamalı (Frequency Hopping) sinyallere karşı akıllı karıştırma stratejilerinin başarımı yazılım çevriminde (SITL) sentetik hedefler yaratılarak doğrulanmıştır.

### 6.2 Alt Sistem Geliştirme Testleri
Donanım altyapısı (USRP ve SBC birimleri) masaüstü laboratuvar ortamında RF loopback kabloları ve RF zayıflatıcılar (attenuator) kullanılarak test edilmiştir. 150 Watt güç sınırlamasını aşmamak adına PA (Güç Yükseltici) modüllerinin termal karakteristiği ve görev döngüleri (Duty Cycle) laboratuvar ortamında incelenmiş, fanlı metal kafes soğutmasının yeterliliği termal sensörlerle doğrulanmıştır.

### 6.3 Görev Testleri
Önümüzdeki yol haritasında (v4.0 saha testleri) anten dizilerinin (Vivaldi ve Log-Periyodik) üretiminin tamamlanmasıyla birlikte açık arazide iki istasyon kurularak TDOA zaman senkronizasyonu doğrulaması yapılacaktır. Testler, donanım entegreli (HITL) kapalı devre RF testleri ile başlatılıp, nihai aşamada açık arazi (Field Test) drone uçuşlarıyla desteklenerek sistem doğrulaması tamamlanacaktır.
