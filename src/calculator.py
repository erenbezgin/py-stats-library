import math


class IstatistikHesaplayici:
    def ortalama(self, temiz_veri):
        if not temiz_veri:
            return 0
        return sum(temiz_veri) / len(temiz_veri)

    def maximum_deger(self, temiz_veri):
        if not temiz_veri:
            return None
        return max(temiz_veri)

    def minimum_deger(self, temiz_veri):
        if not temiz_veri:
            return None
        return min(temiz_veri)

    def standart_sapma(self, temiz_veri):
        if not temiz_veri:
            return 0
        ortalama = self.ortalama(temiz_veri)
        varyans = sum((x - ortalama) ** 2 for x in temiz_veri) / len(temiz_veri)
        return math.sqrt(varyans)
