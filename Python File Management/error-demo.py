liste = ["1","2","5a","10b","abc","10","50"]
# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# for a in liste:
#     try:
#         result = int(a)
#         print(result)
#     except Exception:
#         continue


# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.

# while True:
#     sayi = input('Sayi: ')
#     if sayi == 'q':
#         break
#     try:
#         result = float(sayi)
#         print(f"Girdiginiz sayi {result}")
#         break
#     except ValueError:
#         print('Gecerli bir sayi giriniz.')
#         continue


# 3: Girilen parola içinde türkçe karakter hatası veriniz.

def checkPassword(parola):
    turkce_karakterler = 'çğöşüİ'
    for x in parola:
        if x in turkce_karakterler:
            raise TypeError('Parola Turkce karakter icermemelidir.')
        else:
            print('Parola basariyla olusturuldu')
            break

parola = input('Parola giriniz: ')
checkPassword(parola)
# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
