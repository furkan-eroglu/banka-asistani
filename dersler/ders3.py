with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Ayşe Yılmaz: 1500 TL\n")
    dosya.write("Mehmet Demir: 800 TL\n")


with open("notlar.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()


print(icerik)
