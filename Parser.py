import requests
from bs4 import BeautifulSoup

f = open("personal.txt", "w")
f.close()
def parse():
 url = 'https://omgtu.ru/ecab/persons/index.php?b=14'
 response = requests.get(url)
 soup = BeautifulSoup(response.text, 'lxml')
 prepods = soup.find_all('div', class_='main__content')

 for prepod in prepods:
     print(prepod.text)

 with open('personal.txt', 'a') as f:
      print(prepod.text, file=f)

parse()