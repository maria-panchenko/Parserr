import requests
from bs4 import BeautifulSoup

f = open("personal.txt", "w")
f.close()
def parse():

 url = 'https://omgtu.ru/ecab/persons/index.php?b=14'
 response = requests.get(url)
 soup = BeautifulSoup(response.text, "lxml")
 block = soup.findAll('div', style="padding: 5px; font-size: 120%;")

 #page = requests.get(url)
 #print(page.status_code)

 doc = ''
 with open("personal.txt", "w", encoding="utf-8") as f:
     # Записываем каждый элемент списка block в файл построчно
     for personal in block:
         if personal.find('a'):  # находим тег
            doc = personal.text.strip().replace('\xa0', '')
            f.write(doc + "\n")
            print(doc)

