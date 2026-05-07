import matplotlib.pyplot as plt


class GrafikCizici:
    def regresyon_grafigi_ciz(self, x, y, egim, kesisim):
        # ham verileri noktalar kulknarak göster
        plt.scatter(x, y, color="blue", label="Gerçek Veriler")
        # tahmin çizgisi hesapla
        y_tahmin = [(egim * i) + kesisim for i in x]
        # tahmin çizgisi göster
        plt.plot(x, y_tahmin, color="red", label="Tahmin Çizgisi")

        plt.xlabel("X Ekseni")
        plt.ylabel("Y Ekseni")
        plt.title("Grafik")
        plt.legend()
        plt.show()
