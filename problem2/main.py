# tulis solusi code disini
import math

class BangunDatar:
    def __init__(self, *args):
        self.args = args 

    def hitung_volume(self):
        pass

class Kubus(BangunDatar):
    def hitung_volume(self):
        sisi = self.args[0]
        volume = sisi ** 3
        return volume
    
class Balok(BangunDatar):
    def hitung_volume(self):
        panjang = self.args[0]
        lebar = self.args [1]
        tinggi = self.args[2]
        volume = panjang * lebar * tinggi 
        return volume
    
class Tabung(BangunDatar):
    def hitung_volume(self):
        jari_jari = self.args[0]
        tinggi = self.args[1]
        volume = math.pi * (jari_jari ** 2) * tinggi 
        return volume 

def main():
    bangun_datar = [
        Kubus(10),
        Balok(3, 6, 10),
        Tabung(7, 10)
    ]

    print("Volume:")
    for bangun in bangun_datar:
        if isinstance(bangun, Kubus):
            print(f"Kubus: {bangun.hitung_volume()}")
        elif isinstance(bangun, Balok):
            print(f"Balok: {bangun.hitung_volume()}")
        elif isinstance(bangun, Tabung):
            print(f"Tabung: {bangun.hitung_volume()}")
            
if __name__ == "__main__":
    main()