import pytest


from banka_hesabi import BankaHesabi


def test_para_yatir_bakiyeyi_arttirir():
    hesap = BankaHesabi("Ayşe", 1000)
    hesap.para_yatir(500)
    assert hesap.bakiye == 1500


def test_para_cek_yetersiz_bakiyede_hata_verir():
    hesap = BankaHesabi("Ayşe", 1000)
    with pytest.raises(ValueError):
        hesap.para_cek(1500)


def test_para_cek_negatif_tutarda_hata_verir():
    hesap = BankaHesabi("Ayşe", 1000)
    with pytest.raises(ValueError):
        hesap.para_cek(-100)
