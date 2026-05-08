import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.plotter import GrafikCizici
from src.cleaner import VeriTemizleyici
from src.calculator import IstatistikHesaplayici

liste = [10, "20", "hatali", 30.5, None, "40"]
temizleyici = VeriTemizleyici()
hesaplayici = IstatistikHesaplayici()
temiz_veri = temizleyici.temizle(liste)
print(hesaplayici.ortalama(temiz_veri))
print(hesaplayici.maximum_deger(temiz_veri))
print(hesaplayici.minimum_deger(temiz_veri))
print(hesaplayici.standart_sapma(temiz_veri))
print(hesaplayici.mod(temiz_veri))
print(hesaplayici.medyan(temiz_veri))
print(temizleyici.temizle("Bu bir liste değil"))
print(temizleyici.temizle([10, float("inf"), 20]))
print(f"Açıklık: {hesaplayici.aciklik(temiz_veri)}")
print(f"Değişim Katsayısı: {hesaplayici.degisim_katsayisi(temiz_veri)}")
print(f"Geometrik Ortalama: {hesaplayici.geometrik_ortalama(temiz_veri)}")
z_sonuclari = hesaplayici.z_scoru_hesapla(temiz_veri)
print(f"Z-Skorları: {z_sonuclari}")
liste_x = [1, 2, 3, 4, 5]
liste_y = [2, 4, 6, 8, 10]  # Tam katı, yani korelasyon 1 çıkmalı!

print(f"Korelasyon: {hesaplayici.korelasyon_hesapla(liste_x, liste_y)}")
# Senaryo: Kitap okuma saati vs Kelime haznesi
saatler = [1, 2, 3, 4, 5]
kelimeler = [1000, 2000, 3000, 4000, 5000]

# 10 saat okuyan biri tahminen kaç kelime bilir?
tahmin = hesaplayici.tahmin_et(saatler, kelimeler, 10)
print(f"Tahmin Edilen Kelime Haznesi: {tahmin}")  # 10000 çıkmalı
# 1. Verileri hazırla
saatler = [1, 2, 3, 4, 5]
notlar = [20, 45, 55, 80, 95]

# 2. Önce hesaplayıcıyı kullanarak denklemi bul (BEYİN)
model = hesaplayici.regresyon_hesapla(saatler, notlar)
egim = model["egim"]
kesisim = model["kesisim"]

# 3. Şimdi çiziciye bu bilgileri ver (EL)
cizici = GrafikCizici()
cizici.regresyon_grafigi_ciz(saatler, notlar, egim, kesisim)
# Normal verilerin arasına bir tane "aykırı" sızdıralım
aykiri_test_verisi = [10, 12, 11, 13, 12, 100]  # 100 burada bariz sırıtıyor
aykirilar = hesaplayici.aykiri_deger_bul(aykiri_test_verisi)

print(f"Tespit Edilen Aykırı Değerler: {aykirilar}")
# Beklenen çıktı: [100]
yaslar = [20, 30, 40, 50]
normalize_yaslar = hesaplayici.normalize_et(yaslar)
print(f"Normalize Yaşlar: {normalize_yaslar}")
# Beklenen: [0.0, 0.33, 0.66, 1.0] gibi bir çıktı.
# Senaryo: Torbada 5 Mavi, 3 Kırmızı bilye var.
# 2 bilye çekiyoruz, 2'sinin de Kırmızı gelme olasılığı nedir?
torba = {"mavi": 5, "kirmizi": 3}
secim = 2
istenen = {"kirmizi": 2}

sonuc = hesaplayici.olasilik_hesapla(torba, secim, istenen)
print(f"2 Kırmızı çekme olasılığı: %{sonuc * 100:.2f}")
# Matematiksel beklenen: C(3,2) / C(8,2) = 3 / 28 ≈ 0.107 (yani %10.71)
# Senaryo: Bir parayı 10 kez atıyoruz (n=10)
# Tura gelme olasılığı (p=0.5)
# Tam olarak 5 kez tura gelme (k=5) olasılığı nedir?

n, p, k = 10, 0.5, 5
binom_sonuc = hesaplayici.binom_dağilimi(n, p, k)

print(f"10 atışta 5 tura gelme olasılığı: %{binom_sonuc * 100:.2f}")
# Beklenen çıktı: %24.61 civarı.
