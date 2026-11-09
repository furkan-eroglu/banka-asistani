musteri_adi = "Ayşe Yılmaz"
bakiye = 15250.75
aktif_mi = True

print(f"{musteri_adi} adlı müşterinin bakiyesi: {bakiye} TL")

islemler = [500, -200, 1500, -750]
islemler.append(300)  # Yeni bir işlem ekliyoruz
print(f"İşlem sayısı: {len(islemler)}")

musteri = {
    "ad": "Ayşe Yılmaz",
    "bakiye": 15250.75,
    "urunler": ["kredi kartı", "vadeli hesap"],
}

print(musteri["urunler"][0])


def toplam_hesapla(tutarlar: list[float]) -> float:
    toplam = 0
    for tutar in tutarlar:
        toplam += tutar
    return toplam

net = toplam_hesapla(islemler)


if net > 1000:
    print(f"Net giriş yüksek: {net} TL")
elif net > 0:
    print(f"Net giriş pozitif: {net} TL")
else:
    print("Net çıkış var")


def buyuk_islemleri_bul(tutarlar: list[float], esik_degeri: float) -> list[float]:
    buyuk_islemler = []
    for tutar in tutarlar:
        if abs(tutar) > esik_degeri:
            buyuk_islemler.append(tutar)
    return buyuk_islemler


print(buyuk_islemleri_bul(islemler, 600))