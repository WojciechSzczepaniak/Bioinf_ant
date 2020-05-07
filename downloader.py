from bs4 import BeautifulSoup as bs
import requests
import pathlib
from pathlib import Path

path = pathlib.Path().absolute()

path_instances = pathlib.PurePath(path,Path("instances"))


url = "http://www.cs.put.poznan.pl/mkasprzak/bio/testy.html"
base_url = "http://www.cs.put.poznan.pl/mkasprzak/bio/"
download_list = []
numerator = 0

page = requests.get(url)
data = page.text
soup = bs(data,features="html.parser")

for link in soup.find_all('a'):
    if("ins" in str(link.get('href'))):
        download_list.append(base_url+link.get('href'))
for i in download_list:
    new = requests.get(i)
    data = bs(new.text,features="html.parser")
    new_path = pathlib.PurePath(str(path_instances),Path(str(numerator)+".txt"))
    file = open(str(new_path), "w")
    file.write(str(data))
    numerator += 1
