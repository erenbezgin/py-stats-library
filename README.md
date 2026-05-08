# Py-Stats-Library (Mini-Numpy)


Bu kütüphane; ham verileri temizleyen, derinlemesine istatistiksel analizler yapan, regresyon modelleriyle gelecek tahminleri yürüten ve olasılık hesaplamalarını "Pure Python" mantığıyla gerçekleştiren modüler bir araçtır.

# Neden Bu Proje?
Bu proje, sadece kod yazmak için değil, modern veri bilimi araçlarının (Numpy, Pandas vb.) arkasındaki matematiksel mantığı ve yazılım mimarisini kavramak için geliştirilmiştir:

Veri Boru Hattı (Data Pipeline): Verinin temizlenmesinden işlenmesine ve analizine kadar olan süreci yönetmek.

Matematiksel Algoritmalar: İstatistiksel formülleri manuel koda dökerek algoritma kurma yeteneğini artırmak.

Tahminleme Yeteneği: Geçmiş verilerden yola çıkarak geleceğe dair öngörüler oluşturmak (Lineer Regresyon).

# Özellikler

# Veri Temizleme (DataCleaner)
Sayısal olmayan verileri ayıklama ve sayı formatındaki metinleri ("10") güvenli bir şekilde sayıya çevirme.

None, inf ve nan gibi analizi bozan değerleri temizleyerek güvenli bir veri akışı sağlama.

# İstatistiksel Hesaplamalar (IstatistikHesaplayici)

Merkezi Eğilim: Ortalama, Medyan, Mod, Geometrik ve Harmonik Ortalama.

Dağılım: Standart Sapma, Varyans, Açıklık, Çeyrekler Açıklığı (IQR).

İlişki: Kovaryans ve Korelasyon Katsayısı (Pearson R).

Analiz: Aykırı değer (Outlier) tespiti ve Z-Skoru hesaplama.

Ölçeklendirme: Verileri 0-1 arasına sıkıştıran Min-Max Scaling.

# Tahmin ve Modelleme
Basit Lineer Regresyon: Veriler arasındaki ilişkiyi denkleme dökme ve gelecek değerleri tahmin etme.

# Olasılık ve Kombinatorik

Faktöriyel, Permütasyon P(n, r) ve Kombinasyon C(n, r) hesaplamaları.

# Görselleştirme (GrafikCizici)
Matplotlib entegrasyonu ile verileri serpilme diyagramı (Scatter Plot) üzerinde gösterme.

Hesaplanan regresyon çizgisini grafik üzerine bindirme.

# Proje Yapısı
Plaintext

py-stats-library
/

├── src/
│  
├── __init__.py
│   
├── cleaner.py     # Veri ön işleme ve güvenlik
│   
├── calculator.py  # İstatistiksel beyin ve tahmin motoru
│   
└── plotter.py     # Görselleştirme modülü
├── tests/
│   
└── test_main.py   # Kullanım senaryoları ve testler
└── README.md

# Yol Haritası (Roadmap)
1. [x] Temel İstatistiksel Fonksiyonlar.

2. [x] Veri Temizleme ve Güvenlik Katmanı.

3. [x] Korelasyon ve İlişkisel Analizler.

4. [x] Basit Doğrusal Regresyon ve Tahminleme.

5. [x] Görselleştirme: Matplotlib entegrasyonu.

6. [x] Aykırı Değer Tespiti.

7. [x] Veri Normalizasyonu.

8. [x] Olasılık Temelleri (Faktöriyel, Permütasyon, Kombinasyon).

8. [ ] Sıradaki: Torba/Olay Analizcisi (Event Probability).

10. [ ] Sıradaki: Olasılık Dağılımları (Binom, Poisson, Normal).