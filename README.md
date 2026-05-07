#Py-Stats-Library (Mini-Numpy)

Bu kütüphane, ham verileri temizleyen, derinlemesine istatistiksel analizler yapan, regresyon modelleriyle gelecek tahminleri yürüten ve olasılık hesaplamaları sunan modüler bir Python aracıdır. Modern veri bilimi kütüphanelerinin (Numpy, Pandas) temelindeki matematiksel mantığı anlamak amacıyla geliştirilmiştir.

 #Neden Bu Proje?

Bu proje, sadece kod yazmak için değil, modern veri bilimi araçlarının arkasındaki yazılım mimarisini kavramak için geliştirilmiştir:
Veri Boru Hattı (Data Pipeline): Verinin temizlenmesinden işlenmesine ve analizine kadar olan süreci yönetmek.
Matematiksel Algoritmalar: İstatistiksel formülleri manuel koda dökerek algoritma kurma yeteneğini artırmak.
Tahminleme Yeteneği: Geçmiş verilerden yola çıkarak geleceğe dair öngörüler oluşturmak (Lineer Regresyon).

#Kütüphane Özellikleri


1. Veri Temizleme (VeriTemizleyici)Hatalı veri tiplerini ve sayı formatındaki metinleri ("10") otomatik olarak dönüştürür/ayıklayır.None, inf ve nan gibi analizi bozan değerleri temizler.

2. İstatistiksel Hesaplamalar (IstatistikHesaplayici)Merkezi Eğilim: Ortalama, Varyans, Standart Sapma, Medyan, Mod, Çeyreklikler (Q1, Q3).Analiz: Z-Skoru hesaplama ve Aykırı Değer (Outlier) tespiti.İlişkisel İstatistik: Kovaryans ve Korelasyon (Pearson R) hesaplamaları.Veri Ölçeklendirme: Verileri 0-1 arasına çeken Min-Max Normalizasyonu.

3. Tahminleme ve OlasılıkDoğrusal Regresyon: $y = mx + b$ denklemiyle veri odaklı gelecek tahminleri.Kombinatorik: Faktöriyel, Permütasyon ($P(n, r)$) ve Kombinasyon ($C(n, r)$) hesaplamaları.

4. Görselleştirme (GrafikCizici)Serpilme Diyagramı (Scatter Plot): Veri noktalarının dağılımını görme.Regresyon Çizgisi: Hesaplanan tahmin çizgisini verilerin üzerine bindirme.


#Proje Yapısı

Plaintextpy-stats-library/
├── src/
│   ├── __init__.py
│   ├── cleaner.py     # Veri ön işleme ve güvenlik
│   ├── calculator.py  # İstatistiksel beyin, olasılık ve tahmin motoru
│   └── plotter.py     # Görselleştirme modülü (Matplotlib)
├── tests/
│   └── test_main.py   # Kullanım senaryoları ve testler
└── README.md

#Yol Haritası (Roadmap)

[x] Temel İstatistiksel Fonksiyonlar.
[x] Veri Temizleme ve Güvenlik Katmanı.
[x] Korelasyon ve İlişkisel Analizler.
[x] Basit Doğrusal Regresyon ve Tahminleme.
[x] Görselleştirme (Matplotlib Entegrasyonu).
[x] Aykırı Değer Tespiti (IQR Yöntemi).[x] Veri Normalizasyonu (Min-Max Scaling).
[x] Olasılık Temelleri (Faktöriyel, Permütasyon, Kombinasyon).
[ ] Sıradaki: Torba/Olay Analizcisi (Event Probability).
[ ] Sıradaki: Olasılık Dağılımları (Binom, Poisson, Normal).
[ ] Sıradaki: Kutu Grafiği (Box Plot) ile Aykırı Değer Görselleştirme.