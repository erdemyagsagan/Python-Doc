# themoviedb.org => film ve dizi arşivi
# themoviedb' nin sunduğu apiyi uygulamanızda kullanınız.
# Anahtar kelimeye göre arama
# En popüler film listesi
# Vizyondaki film listesi

import requests

class Movie:
    def __init__(self):
        self.api_url = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1'
        self.api_token = '83b05a40a6e70716c7df6c216388778c'


    def popularMovie(self):
        response = requests.get(f"{self.api_url}'movie/popular?api_key={self.api_token}&language=en-US&page=1'")
        return response.json()


    def searchMovie(self,name):
        pass

movie = Movie()

while True:
    secim = input("1-Popular Movies\n2-Search Movies\n3-Exit\nSeçim: ")

    if secim == '1':
        result = movie.popularMovie()
        print(result)

    elif secim == '2':
        pass
    elif secim == '3':
        pass
    else:
        break

        import requests

        url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer 83b05a40a6e70716c7df6c216388778c"
        }

        response = requests.get(url, headers=headers)

        print(response.text)





