class VeriTemizleyici:
    def __init__(self):
        pass

    def temizle(self, ham_veri):
        """Verilen ham veri listesini temizler ve sadece sayısal değerleri içeren bir liste döndürür."""
        temiz_liste = []
        for i in ham_veri:
            try:
                sayi = float(i)
                temiz_liste.append(sayi)
            except (ValueError, TypeError):
                continue
        return temiz_liste
