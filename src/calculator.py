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

    def medyan(self, temiz_veri):
        """Verilen temiz veri listesinin medyanını hesaplar."""
        if not temiz_veri:
            return None
        sorted_veri = sorted(temiz_veri)
        n = len(sorted_veri)
        if n % 2 == 1:
            return sorted_veri[n // 2]
        else:
            return (sorted_veri[n // 2 - 1] + sorted_veri[n // 2]) / 2

    def mod(self, temiz_veri):
        """Verilen temiz veri listesinin modunu hesaplar."""
        if not temiz_veri:
            return None
        frekans = {}
        for num in temiz_veri:
            if num in frekans:
                frekans[num] += 1
            else:
                frekans[num] = 1
        max_frekans = max(frekans.values())
        mod_degerleri = [k for k, v in frekans.items() if v == max_frekans]
        return min(mod_degerleri) if mod_degerleri else None

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

    def aciklik(self, temiz_veri):
        """Verilen temiz veri listesinin açıklığını hesaplar."""
        if not temiz_veri:
            return 0
        return self.maximum_deger(temiz_veri) - self.minimum_deger(temiz_veri)

    def degisim_katsayisi(self, temiz_veri):
        ortalama = self.ortalama(temiz_veri)
        standart_sapma = self.standart_sapma(temiz_veri)
        if ortalama == 0:
            return 0
        return standart_sapma / ortalama

    def geometrik_ortalama(self, temiz_veri):
        if not temiz_veri:
            return 0
        carpim = 1
        for num in temiz_veri:
            if num <= 0:
                return None
            carpim *= num
        return carpim ** (1 / len(temiz_veri))

    def ceyrekler(self, temiz_veri):
        """Verilerin çeyreklerini hesaplar."""
        if not temiz_veri:
            return None
        sorted_veri = sorted(temiz_veri)
        n = len(sorted_veri)
        q1 = sorted_veri[n // 4]
        q2 = self.medyan(temiz_veri)
        q3 = sorted_veri[3 * n // 4]
        return {"Q1": q1, "Q2": q2, "Q3": q3}

    def z_scoru_hesapla(self, temiz_veri):
        """Verilen temiz veri listesinin z-skorlarını hesaplar."""
        if not temiz_veri:
            return []
        ortalama = self.ortalama(temiz_veri)
        standart_sapma = self.standart_sapma(temiz_veri)
        if standart_sapma == 0:
            return [0] * len(temiz_veri)
        z_skorlari = [(x - ortalama) / standart_sapma for x in temiz_veri]
        return z_skorlari

    def kovaryans_hesapla(self, veri_x, veri_y):
        """VErilen iki veri listesinin kovaryansını hesaplar"""
        if not veri_x or not veri_y or len(veri_x) != len(veri_y):
            return None
        ortalama_x = self.ortalama(veri_x)
        ortalama_y = self.ortalama(veri_y)
        kovaryans = sum(
            (x - ortalama_x) * (y - ortalama_y) for x, y in zip(veri_x, veri_y)
        ) / (len(veri_x) - 1)
        return kovaryans

    def korelasyon_hesapla(self, veri_x, veri_y):
        """VErilen iki veri listesinin ilişki gücünü hesaplar"""
        kovaryans = self.kovaryans_hesapla(veri_x, veri_y)
        standart_sapma_x = self.standart_sapma(veri_x)
        standart_sapma_y = self.standart_sapma(veri_y)
        if standart_sapma_x == 0 or standart_sapma_y == 0:
            return 0
        korelasyon = kovaryans / (standart_sapma_x * standart_sapma_y)
        return korelasyon
