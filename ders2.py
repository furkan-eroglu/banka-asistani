class BankaHesabi:
    def __init__(self, sahip: str, bakiye: float = 0.0):
        self.sahip = sahip
        self.bakiye = bakiye

    def para_yatir(self, tutar: float) -> None:
        if tutar <= 0:
            raise ValueError("Yatırılacak tutar pozitif olmalı!")
        self.bakiye += tutar

    def bilgi(self) -> str:
        return f"{self.sahip}: {self.bakiye} TL"

    def para_cek(self, tutar: float) -> None:
        if tutar <= 0:
            raise ValueError("Çekilecek tutar pozitif olmalı!")
        if tutar > self.bakiye:
            raise ValueError("Yetersiz bakiye!")
        self.bakiye -= tutar


hesap = BankaHesabi("Ayşe Yılmaz", 1000)
hesap.para_yatir(500)
print(hesap.bilgi())
try:
    hesap.para_cek(-100)
    print("Fişiniz yazdırılıyor")
except ValueError as hata:
    print(f"İşlem başarısız: {hata}")

try:
    hesap.para_cek(300)
    print("Fişiniz yazdırılıyor")
except ValueError as hata:
    print(f"İşlem başarısız: {hata}")

try:
    hesap.para_yatir(-200)
    print("Fişiniz yazdırılıyor")
except ValueError as hata:
    print(f"İşlem başarısız: {hata}")
