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

    def bakiye_sorgula(self) -> float:
        return self.bakiye
