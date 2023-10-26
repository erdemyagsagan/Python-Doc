def ortalama_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')

    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 85 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 80 and ortalama <= 84:
        harf = "BB"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "CB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CC"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "DC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DD"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "FD"
    else:
        harf = "FF"

    return ogrenciAdi + ": " + harf + "\n"
def notlari_oku():
    with open("sinav_notlari.txt", "r") as file:
        for satir in file:
            ortalama_hesapla(satir)

def notlari_gir():
    ad = input('Adini giriniz: ')
    soyad = input('Soyadi giriniz: ')
    not1 = input('Not1 giriniz: ')
    not2 = input('Not2 giriniz: ')
    not3 = input('Not3 giriniz: ')
    liste = [not1,not2,not3]

    with open("sinav_notlari.txt", "a") as file:
        file.write(f'{ad} {soyad} :{not1},{not2},{not3} \n')

def notlari_kaydet():
    with open("sinav_notlari.txt", "r") as file:
        liste = []

        for i in file:
            liste.append(ortalama_hesapla(i))

        with open("sinav_notlari.txt", "w") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input('1- Notlari oku\n2- Not gir\n3- Notlari kaydet\n4- Cikis\nHangi islemi yapmak istiyorsaniz menudeki sayiyi giriniz:')
    if islem == "1":
        notlari_oku()
    elif islem == "2":
        notlari_gir()
    elif islem == "3":
        notlari_kaydet()
    elif islem == "4":
        break
    else:
        print("Gecerli bir sayi giirniz")
        continue
