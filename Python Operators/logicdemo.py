# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# x = float(input('Bir sayi giriniz: '))
# result = (x > 0 ) and (x <= 100)
# print(f'Girilen sayi 0 ile 100 arasinda: {result}')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# x = float(input('Bir sayi giriniz: '))
# result = (x > 0 ) and (x % 2 == 0 )
# print(f'Girilen sayi cift ve pozitif: {result}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'erdemyagsagan@gmail.com'
# password = 'erdem12345'
#
# valueEmail = input('Email: ')
# valuePassword = input('Sifre: ')
#
# result = (email == valueEmail) and (password == valuePassword)
#
#
# print(f'Giris: {result}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# x = int(input('x sayisini giriniz: '))
# y = int(input('y sayisini giriniz: '))
# z = int(input('z sayisini giriniz: '))
#
# result = (x > y) and (x > z)
# print(f'x en buyuk sayidir {result}')
#
# result = (y > x) and (y > z)
# print(f'y en buyuk sayidir {result}')
#
# result = (z > y) and (z > x)
# print(f'z en buyuk sayidir {result}')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = int(input('1. vize notunuzu giriniz: '))
# vize2 = int(input('2. vize notunuzu giriniz: '))
# final = int(input('Final notunuzu girniiz: '))
# ortalama = ((((vize1 + vize2) * 60) / 100) + ((final * 40) / 100)) / 2
# basari = (ortalama > 50) and (final > 50)
# finalBasari = (final >= 70)
# print(f'Ortalamaniz: {ortalama}')
# print(f'Dersi pass gecme: {finalBasari}')
# print(f'Dersi gecme durumunuz: {basari}')


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

kiloendeks = (formul > 0) and (formul > 18.4)
