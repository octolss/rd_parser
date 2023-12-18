import requests
from bs4 import BeautifulSoup as BS

s = requests.Session()
response = s.get(url="https://www.rdveikals.lv/categories/lv/150/sort/5/filter/0_0_0_0/page/1/Portat%C4%ABvie-datori.html")

with open("index.html", "w") as file:
    file.write(response.text)

with open("index.html", "r") as file:   
    soup = BS(file, 'html.parser')

d = [i for i in soup.find_all('p') if i[] == "€"]
c = 0

for link in soup.find_all('h3'):

    a = link.get_text('a')
    with open("index.txt", "a") as file:
        file.write(a[2:len(a)-3])
        file.write(d[c].get_text())
    c+=1
