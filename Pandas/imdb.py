import pandas as pd

df = pd.read_csv('imdb.csv')

# 1- Dosyada hakkındaki bilgiler.
result = df
result = df.columns
print(result)

# 2- ilk 5 kaydı gösterin
result = df.head(10)

# 3- ilk 10 kaydı gösterin
result = df.head(10)

# 4- Son 5 kaydı gösterin
result = df.tail()

# 5- Son 10 kaydı gösterin
result = df.tail(10)

# 6- Sadece Movie_Title kolonunu alın.
result = df['name']

# 7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın.
result = df['name'].head()

# 8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın.
result = df[['name', 'rating']].head()

# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın.
result = df[['name', 'rating']].tail(7)

# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci 5 kaydı alın.
result = df[5:10][['name', 'rating']]

# 11- Sadece Movie_Title ve Rating kolonunu içeren ve imdb puanı 8.0
#     ve üstünde olan kayıtlardan ilk 50 tanesini alınız.
result = df[df['rating'] >= 8.0][['name', 'rating']].head(50)

# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
result = df[(df['year'] >= 2014) & (df['year'] <= 2015)][['name']]

# 13- Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı
#     8 ile 9 arasında olan filmleri listeleyiniz.

print(result)
