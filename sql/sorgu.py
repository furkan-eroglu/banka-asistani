import sqlite3

baglanti = sqlite3.connect("banka.db")
imlec = baglanti.cursor()

imlec.execute("""
    SELECT musteriler.ad, SUM(hesaplar.bakiye)
    FROM musteriler
    INNER JOIN hesaplar ON hesaplar.musteri_id = musteriler.id
    WHERE hesaplar.tur = 'vadesiz'
    GROUP BY musteriler.ad
""")
for satir in imlec.fetchall():
    print(satir)

baglanti.close()
