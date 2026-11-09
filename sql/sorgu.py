import sqlite3

baglanti = sqlite3.connect("banka.db")
imlec = baglanti.cursor()

imlec.execute("CREATE INDEX IF NOT EXISTS idx_hesaplar_musteri ON hesaplar(musteri_id)")
imlec.execute("EXPLAIN QUERY PLAN SELECT * FROM hesaplar WHERE musteri_id = 3")
for satir in imlec.fetchall():
    print(satir)

baglanti.close()
