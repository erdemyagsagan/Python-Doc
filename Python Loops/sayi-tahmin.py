'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
      üzerinden hesaplansın.
'''

import random
sayi = random.randint(1,100)
print(sayi)

can = int(input('kaç hak kullanmak istersiniz: '))
hak = can
sayac = 0

while 0 < hak:
    hak -= 1
    sayac += 1
    tahmin = int(input('Sayiyi tahmin ediniz: '))
    if (sayi == tahmin):
        puan = (100 - (20 * (sayac-1)))
        print(f"Tebrikler sayiyi dogru bildiniz ! \nPuaniniz {puan}")
        break
    elif (sayi < tahmin):
        print('Daha kucuk sayi giriniz')
        print(f'Kalan hak {hak}')
    elif (sayi > tahmin):
        print('Daha buyuk sayi giriniz')
        print(f'Kalan hak {hak}')
if (hak ==0) :
    print('\nSayiyi bulamadiniz')