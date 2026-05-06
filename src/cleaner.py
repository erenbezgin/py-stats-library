import math


class VeriTemizleyici:
    def __init__(self):
        pass

    def temizle(self, ham_veri):
        """Verilen ham veri listesini temizler ve sadece sayısal değerleri içeren bir liste döndürür."""
        if not isinstance(ham_veri, list):
            print("Girdi bir liste olmalıdır.")
            return []

        temiz_liste = []
        for i in ham_veri:
            try:
                sayi = float(i)
                if not math.isnan(sayi) and not math.isinf(sayi):
                    temiz_liste.append(sayi)
            except (ValueError, TypeError):
                continue
        return temiz_liste
