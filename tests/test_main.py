import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
