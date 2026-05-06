import math


class IstatistikHesaplayici:
    def ortalama(self, temiz_veri):
        """Verilen temiz veri listesinin ortalamasını hesaplar."""
        if not temiz_veri:
            return 0
        return sum(temiz_veri) / len(temiz_veri)

    def maximum_deger(self, temiz_veri):
        """Verilen temiz veri listesinin maksimum değerini döndürür."""
        if not temiz_veri:
            return None
        return max(temiz_veri)

    def minimum_deger(self, temiz_veri):
        """Verilen temiz veri listesinin minimum değerini döndürür."""
        if not temiz_veri:
            return None
        return min(temiz_veri)

    def varyans_hesapla(self, temiz_veri):
        """Verilen temiz veri listesinin varyansını hesaplar."""
        if not temiz_veri:
            return 0
        if len(temiz_veri) < 2:
            return 0
        ortalama = self.ortalama(temiz_veri)
        varyans = sum((x - ortalama) ** 2 for x in temiz_veri) / (len(temiz_veri) - 1)
        return varyans

    def standart_sapma(self, temiz_veri):
        """Verilen temiz veri listesinin standart sapmasını hesaplar."""
        varyans = self.varyans_hesapla(temiz_veri)
        return math.sqrt(varyans)
