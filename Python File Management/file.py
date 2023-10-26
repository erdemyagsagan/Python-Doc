import requests

# file = open('newfile','w')
# print(file)
# file.write('Hello World My name is metin')
# file.close()

result = requests.get("https://api.exchangeratesapi.io/v1/latest")
print(result)