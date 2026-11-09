import sqlite3

baglanti = sqlite3.connect("banka.db")
imlec = baglanti.cursor()

imlec.execute("""
    WITH musteri_toplamlari AS (
        SELECT musteri_id, SUM(bakiye) AS toplam
        FROM hesaplar
        GROUP BY musteri_id
    )
    SELECT musteriler.ad, musteri_toplamlari.toplam
    FROM musteriler
    LEFT JOIN musteri_toplamlari ON musteriler.id = musteri_toplamlari.musteri_id
""")
for satir in imlec.fetchall():
    print(satir)

baglanti.close()
