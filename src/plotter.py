import matplotlib.pyplot as plt

from .calculator import IstatistikHesaplayici


class GrafikCizici:
    def regresyon_grafigi_ciz(self, x, y, egim, kesisim, hesaplayici):

        aykirilar = hesaplayici.aykiri_deger_bul(y)

        x_saglam, y_saglam = [], []
        x_bozuk, y_bozuk = [], []

        for i in range(len(y)):
            if y[i] in aykirilar:

                x_bozuk.append(x[i])
                y_bozuk.append(y[i])
            else:

                x_saglam.append(x[i])
                y_saglam.append(y[i])

        #  MAVİ nokta
        plt.scatter(x_saglam, y_saglam, color="blue", label="Normal Veriler")

        #  KIRMIZI ÇARPI (x)
        plt.scatter(
            x_bozuk, y_bozuk, color="red", marker="x", s=100, label="Aykırı Değerler"
        )

        y_tahmin = [(egim * i) + kesisim for i in x]
        plt.plot(x, y_tahmin, color="green", label="Tahmin Hattı")

        plt.legend()
        plt.show()
