# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# x = int(input('Sayi giriniz: '))
# if (x > 0) and (x < 100 ):
#     print('Sayisiniz 0-100 arasindadir.')
# else:
#     print('Sayiniz 0-100 arasinda degil')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# x = int(input('Sayi giriniz: '))
# if (x > 0) and (x%2 == 0 ):
#     print('Sayisiniz pozitif cift sayidir..')
# else:
#     print('Sayiniz pozcitif cift sayi degildir.')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'erdemyagsagan@gmail.com'
# password = 'erdem12345'
#
# valueEmail = input('Email: ')
# valuePassword = input('Sifre: ')
#
# if (email == valueEmail) and (password == valuePassword):
#     print('Giris basarili.')
# elif not(email == valueEmail) and (password == valuePassword):
#     print('Email hatali.')
# elif (email == valueEmail) and not(password == valuePassword):
#     print('Parola hatali.')
# elif not not(email == valueEmail) and not(password == valuePassword):
#     print('Email ve parola hatali.')
# else:
#     print('Hatali giris')


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# x = int(input('x sayisini giriniz: '))
# y = int(input('y sayisini giriniz: '))
# z = int(input('z sayisini giriniz: '))
#
# if (x > y) and (x > z):
#     print('x en buyuk sayidir. ')
#
# elif (y > x) and (y > z):
#     print('y en buyuk sayidir. ')
#
# else:
#     print('z en buyuk sayidir.')


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = int(input('1. vize notunuzu giriniz: '))
# vize2 = int(input('2. vize notunuzu giriniz: '))
# final = int(input('Final notunuzu girniiz: '))
# ortalama = ((((vize1 + vize2) * 60) / 100) + ((final * 40) / 100)) / 2
#
# if (ortalama > 50) and (final > 50):
#     print(f'Ortalamaniz: {ortalama}\nBasarili !')
# elif (final > 70):
#     print(f'Basarili !')
# else:
#     print('Basarisiz !')


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

ad = input('Adinizi giriniz: ')
kilo = float(input('Kilonuzu giriniz: '))
boy = float(input('Boyunuzu giriniz: '))

formul = (kilo / boy**2)

if (formul > 0) and (formul <= 18.4):
    print('Zayif')
if (formul > 18.5) and (formul <= 24.9):
    print('Normal')
if (formul > 25.0) and (formul <= 29.9):
    print('Fazla Kilolu')
if (formul > 30.0) and (formul <= 34.9):
    print('Obez')

