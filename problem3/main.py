# tulis solusi code disini
class Kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def penjumlahan(self):
        return self.angka1 + self.angka2

    def pengurangan(self):
        return self.angka1 - self.angka2

    def perkalian(self):
        return self.angka1 * self.angka2

    def pembagian(self):
        if self.angka2 != 0:
            return self.angka1 / self.angka2
        else:
            return "Error: Pembagian dengan nol tidak bisa dilakukan."

def main():
    operasi = [
        ("Penjumlahan", 3, 4),
        ("Pengurangan", 15, 4),
        ("Perkalian", 10, 10),
        ("Pembagian", 12, 3)
    ]

    for op in operasi:
        nama_operasi, angka1, angka2 = op
        calc = Kalkulator(angka1, angka2)
        if nama_operasi == "Penjumlahan":
            print(f"{nama_operasi} : {calc.penjumlahan()}")
        elif nama_operasi == "Pengurangan":
            print(f"{nama_operasi} : {calc.pengurangan()}")
        elif nama_operasi == "Perkalian":
            print(f"{nama_operasi} : {calc.perkalian()}")
        elif nama_operasi == "Pembagian":
            print(f"{nama_operasi} : {calc.pembagian()}")

if __name__ == "__main__":
    main()
