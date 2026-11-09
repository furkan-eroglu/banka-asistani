import sqlite3

baglanti = sqlite3.connect("banka.db")
imlec = baglanti.cursor()

imlec.execute("""
    SELECT id, tur, bakiye,
           ROW_NUMBER() OVER (ORDER BY tur) AS sira
    FROM hesaplar
""")
for satir in imlec.fetchall():
    print(satir)

baglanti.close()
