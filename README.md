# 📊 py-stats-library

Bu kütüphane, Python temellerini güçlendirmek, Nesne Yönelimli Programlama (OOP) mantığını kavramak ve temiz kod (Clean Code) prensiplerini uygulamak amacıyla geliştirilmektedir.

## 🚀 Neden Bu Projeyi Yapıyoruz?
Yazılım dünyasına adım atarken sadece teorik bilgiyle yetinmeyip, gerçek bir ihtiyaca (veri analizi) yönelik araçlar geliştirerek şu becerileri pekiştirmeyi hedefliyoruz:
- **Modüler Yapı:** Kodları farklı sorumluluklara sahip sınıflara bölmek (`cleaner`, `calculator`).
- **Hata Yönetimi:** Kullanıcı hatalarına (yanlış veri girişi, boş liste vb.) karşı dayanıklı sistemler kurmak.
- **Git/GitHub İş Akışı:** Profesyonel commit mesajları ve repo yönetimi ile sürüm kontrolü yapmak.
- **İstatistiksel Algoritmalar:** Matematiksel formülleri manuel olarak koda dökerek algoritma kurma yeteneğini artırmak.

## 🛠️ Kütüphane Özellikleri

### 1. Veri Temizleme (`VeriTemizleyici`)
- Liste dışındaki girdileri otomatik engeller.
- Sayı formatındaki metinleri (`"10"`) sayıya çevirir.
- `None`, `inf` (sonsuz) ve `nan` (belirsiz) değerleri ayıklar.

### 2. İstatistiksel Hesaplamalar (`IstatistikHesaplayici`)
- **Seviye 1 (Temel):** Ortalama, Maksimum/Minimum, Açıklık, Varyans, Standart Sapma.
- **Seviye 2 (Dağılım):** Medyan, Mod, Çeyreklikler (Q1, Q2, Q3).

## 📂 Dosya Yapısı
```text
py-stats-library/
├── src/
│   ├── __init__.py
│   ├── cleaner.py     # Veri ön işleme
│   └── calculator.py  # İstatistiksel beyin
├── tests/
│   └── test_main.py   # Kullanım örnekleri
└── README.md

Gelecek Planları
[ ] Z-Skoru hesaplama (Seviye 2 tamamlanacak). [x]

[ ] Korelasyon ve Kovaryans (İki değişkenli analiz).[x]

[ ] Veri Görselleştirme (Matplotlib entegrasyonu).