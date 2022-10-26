import requests , os
from bs4 import BeautifulSoup
import shutil

nam = input("Enter the name of image you want to download.... == ")

path = os.path.join("wallpaper")
shutil.rmtree(path)

urlin = 'https://wall.alphacoders.com/search.php?search=' + nam.replace(' ' , '+')

page = requests.get(urlin)

soup = BeautifulSoup(page.content , 'html.parser')

content = soup.find_all('a')

d = []
for i in content:
    x = i.get('href')
    try:
        if x.startswith('/big.php'):
            a = ('https://wall.alphacoders.com/'+ x )
            d.append(a)
    except:
        print('-----')



os.mkdir(path)
