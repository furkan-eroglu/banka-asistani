class BankaHesabi:
    def __init__(self, sahip: str, bakiye: float = 0.0):
        self.sahip = sahip
        self.bakiye = bakiye

    def para_yatir(self, tutar: float) -> None:
        self.bakiye += tutar

    def bilgi(self) -> str:
        return f"{self.sahip}: {self.bakiye} TL"

    def para_cek(self, tutar: float) -> bool:
        if tutar > self.bakiye:
            print("Yetersiz bakiye!")
            return False
        else:
            self.bakiye -= tutar
            return True


hesap = BankaHesabi("Ayşe Yılmaz", 1000)
hesap.para_yatir(500)
print(hesap.bilgi())
if hesap.para_cek(2000):
    print("Fişiniz yazdırılıyor")
else:
    print("Lütfen başka bir tutar girin")

if hesap.para_cek(300):
    print("Fişiniz yazdırılıyor")
else:
    print("Lütfen başka bir tutar girin")
