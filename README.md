 # py-stats-library

Bu kütüphane, ham verileri temizleyen, derinlemesine istatistiksel analizler yapan ve regresyon modelleriyle gelecek tahminleri yürüten modüler bir Python aracıdır.

# Neden Bu Projeyi Yapıyoruz?

Bu proje, sadece kod yazmak için değil, modern veri bilimi araçlarının (Numpy, Scipy vb.) arkasındaki matematiksel mantığı ve yazılım mimarisini kavramak için geliştirilmiştir:

Veri Boru Hattı (Data Pipeline): Verinin temizlenmesinden işlenmesine ve analizine kadar olan süreci yönetmek.

Matematiksel Algoritmalar: İstatistiksel formülleri manuel olarak koda dökerek algoritma kurma yeteneğini artırmak.

Tahminleme Yeteneği: Geçmiş verilerden yola çıkarak geleceğe dair öngörüler oluşturmak (Lineer Regresyon).

# Kütüphane Özellikleri

1. Veri Temizleme (VeriTemizleyici)

Liste dışındaki girdileri ve hatalı veri tiplerini otomatik engeller.

Sayı formatındaki metinleri ("10") güvenli bir şekilde sayıya çevirir.

None, inf (sonsuz) ve nan (belirsiz) değerleri ayıklayarak analizi güvenli hale getirir.

2. İstatistiksel Hesaplamalar (IstatistikHesaplayici)

Tekil Veri Analizi: Ortalama, Varyans, Standart Sapma, Medyan, Mod, Çeyreklikler (Q1, Q2, Q3).

Z-Skoru Analizi: Bir verinin grubun ortalamasından ne kadar saptığını ölçme.

İlişkisel İstatistik: İki farklı veri seti arasındaki Kovaryans ve Korelasyon (Pearson R) hesaplamaları.

Tahminleme Motoru: Basit Doğrusal Regresyon ($y = mx + b$) ile veri odaklı tahminler yapma.


# Proje Yapısı
Plaintextpy-stats-library/
├── src/
│   ├── __init__.py
│   ├── cleaner.py     # Veri ön işleme ve güvenlik
│   └── calculator.py  # İstatistiksel beyin ve tahmin motoru
├── tests/
│   └── test_main.py   # Kullanım senaryoları ve testler
└── README.md


# Yol Haritası 

1. [x] Temel İstatistiksel Fonksiyonlar.

2. [x] Veri Temizleme ve Güvenlik Katmanı.

3. [x] Korelasyon ve İlişkisel Analizler.

4. [x] Basit Doğrusal Regresyon ve Tahminleme.

5.[ ] Görselleştirme: Matplotlib ile histogram ve scatter plot çizimleri.

6.[ ] Olasılık Teorisi: Faktöriyel, kombinasyon ve olasılık dağılımları.