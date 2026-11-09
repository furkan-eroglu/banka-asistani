import sqlite3

baglanti = sqlite3.connect("banka.db")
imlec = baglanti.cursor()

imlec.execute("DROP TABLE IF EXISTS hesaplar")
imlec.execute("DROP TABLE IF EXISTS musteriler")

imlec.execute("""
    CREATE TABLE musteriler (
        id INTEGER PRIMARY KEY,
        ad TEXT,
        sehir TEXT
    )
""")
imlec.execute("""
    CREATE TABLE hesaplar (
        id INTEGER PRIMARY KEY,
        musteri_id INTEGER,
        tur TEXT,
        bakiye REAL
    )
""")

imlec.executemany(
    "INSERT INTO musteriler VALUES (?, ?, ?)",
    [
        (1, "Ayşe Yılmaz", "İstanbul"),
        (2, "Mehmet Demir", "Ankara"),
        (3, "Zeynep Kaya", "İzmir"),
        (4, "Ali Çelik", "İstanbul"),
    ],
)

imlec.executemany(
    "INSERT INTO hesaplar VALUES (?, ?, ?, ?)",
    [
        (1, 1, "vadesiz", 15000),
        (2, 1, "vadeli", 50000),
        (3, 2, "vadesiz", 800),
        (4, 3, "vadesiz", 4200),
        (5, 3, "vadeli", 12000),
    ],
)

baglanti.commit()
baglanti.close()
print("Veritabani hazir")
