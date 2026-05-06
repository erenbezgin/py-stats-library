class VeriTemizleyici:
    def __init__(self):
        pass

    def temizle(self, ham_veri):
        temiz_liste = []
        for i in ham_veri:
            try:
                sayi = float(i)
                temiz_liste.append(sayi)
            except (ValueError, TypeError):
                continue
        return temiz_liste
