erdemHesap = {
    'ad' : 'Erdem Yagsagan',
    'hesapno' : '1231324',
    'bakiye' : 3000,
    'ekHesap' : 2000
}
metinHesap = {
    'ad' : 'Metin Yagsagan',
    'hesapno' : '312132',
    'bakiye' : 2000,
    'ekHesap' : 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if (miktar > hesap['bakiye']):
        ekhesapsorusu = input('Yetersiz bakiye\nEk hesap kullanmak ister misiniz ?(e/h) ')
        if (ekhesapsorusu == 'e'):
            if((hesap['bakiye'] + hesap['ekHesap']) >= miktar):
                sonekhesapbakiyesi = (hesap['ekHesap'] + hesap['bakiye']) - miktar
                print(f'Ek hesap bakiyeniz {hesap["ekHesap"]}\nIslem basariyla gerceklesti\nKalan ek hesap bakiyesi {sonekhesapbakiyesi}')
        elif (ekhesapsorusu == 'h'):
            print('Bakiye yetersiz islemi gerceklestiremiyoruz.')

    else:
        kalanbakiye = hesap['bakiye'] - miktar
        print(f"Para basariyla cekilmistir.\nKalan bakiye {kalanbakiye}")



paraCek(erdemHesap,4500)
