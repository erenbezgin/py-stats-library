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
