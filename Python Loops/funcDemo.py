# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

# def yazdir(kelime,adet):
#     print(kelime * adet)
# yazdir('Merhaba\n', 10)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

#
# def parameter(*args):
#     liste = []
#
#     for arguman in args:
#         liste.append(arguman)
#     return liste
# result = parameter(10,20,60)
# print(result)



# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def asalsayibulma (sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1:
#             for i in range (2,sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                 print(sayi)
# sayi1 = int(input('Baslangic sayisini giriniz: '))
# sayi2 = int(input("Bitis sayisin giriniz: "))
# asalsayibulma(sayi1,sayi2)


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def tambolenbulma (sayi):
    for i in range(1,sayi):
        if (sayi % i == 0):
            print(i)

sayi = int(input('Sayi giriniz: '))

tambolenbulma(sayi)