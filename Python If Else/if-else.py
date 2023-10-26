# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#    lise ya da üniversite olmalıdır.

# isim = input('Isminizi giriniz: ')
# yas = int(input('Yasinizi giriniz: '))
# egitim = input('Egitim durumunuzu giriniz\nUniversite = a\nLise = b\na veya b yi tuslayiniz:')
#
# ehliyet = (yas > 18) and (egitim == "a")
# if ehliyet:
#     print('Ehliyetinizi alabilirsiniz')
# else:
#     print('Ehliyet alamazsiniz')

    # 2- Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre
    #    not aralığına karşılık gelen not bilgisini yazdırınız.
    #    0 -24  => 0
    #    25-44  => 1
    #    45-54  => 2
    #    55-69  => 3
    #    70-84  => 4
    #    85-100 => 5

# sinav1 = int(input('Birinci sinav: '))
# sinav2 = int(input('Ikinci sinav: '))
# sozlu = int(input('Sozlu: '))
#
# ortalama = (sinav1 +sinav2 + sozlu) / 3
#
# if ortalama < 24:
#     print('Not bilginiz: 0')
# elif (25 <= ortalama < 45):
#     print('Not ortalamaniz: 1')
# elif (45 <= ortalama < 54):
#     print('Not ortalamaniz: 2')
# elif (55 <= ortalama < 69):
#     print('Not ortalamaniz: 3')
# elif (70 <= ortalama < 84):
#     print('Not ortalamaniz: 4')
# elif (85 <= ortalama < 100):
#     print('Not ortalamaniz: 5')

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.
#    (simdi) - (2018/8/1) => gün

import datetime
