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
