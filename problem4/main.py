# tulis solusi code disini
class OngkosKirim:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_harga(self):
        volume = self.hitung_volume()
        if volume < 50:
            return 5000
        else:
            harga = 5000 + ((volume - 50) / 50) * 1000
            return harga

def main():
    
    panjang = 5
    lebar = 2
    tinggi = 4
    berat = 1

    pengiriman = OngkosKirim(panjang, lebar, tinggi, berat)
    harga = pengiriman.hitung_harga()

    print(f"Harga : Rp {harga}")

if __name__ == "__main__":
    main()