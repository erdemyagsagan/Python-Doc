import requests

url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4M2IwNWE0MGE2ZTcwNzE2YzdkZjZjMjE2Mzg4Nzc4YyIsInN1YiI6IjY1MzE2Y2M3OGQyMmZjMDEyYzg3MTNhNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ZJPr2tUi8FaUNpuffyqhSyY5hr0N2uKkRxdTobcK9pU"
}

response = requests.get(url, headers=headers)

print(response.text)