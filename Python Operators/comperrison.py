# 1- Girilen 2 sayıdan hangisi büyüktür ?

# a = int(input('a sayisini giriniz'))
# b = int(input('b sayisini giriniz'))
#
# result = (a > b)
# print(f'a: {a} b: {b} den büyüktür: {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# vize1 = int(input('1. vize notunuzu giriniz: '))
# vize2 = int(input('2. vize notunuzu giriniz: '))
# final = int(input('Final notunuzu girniiz: '))
# ortalama = ((((vize1 + vize2) * 60) / 100) + ((final * 40) / 100)) / 2
# print(f'Ortalamaniz: {ortalama}')

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# sayi = int(input('Sayi giriniz = '))
# ciftSayi = ((sayi % 2) == 0)
# print(f'Sayiniz {sayi} cift sayidir {ciftSayi}')

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.

userMail = 'erdemyagsagan'
userPassword = '123456'

inputUserMail = input('Email giriniz: ')
inputUserPassword = input('Sifre giriniz: ')

mailMatch = (userMail == inputUserMail)
passwordMatch = (userPassword == inputUserPassword)
result = (mailMatch & passwordMatch)

# print(f'Giris {result}')
