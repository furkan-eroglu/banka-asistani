import sqlite3

baglanti = sqlite3.connect("banka.db")
imlec = baglanti.cursor()

imlec.execute("""
    SELECT id, bakiye,
           LAG(bakiye) OVER (ORDER BY id) AS onceki_bakiye
    FROM hesaplar
""")
for satir in imlec.fetchall():
    print(satir)

baglanti.close()
