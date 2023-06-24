import requests 
from bs4 import BeautifulSoup
import webbrowser

html=input('Enter div')
soup=BeautifulSoup(html,'html.parser')
divs=soup.find_all('div',attrs={'class':'list-group-item list-group-item-action'})
links=[i.find('a',class_=lambda x: x is None)['href'] for i in divs]
for i in links:
    webbrowser.open(i)

input('Ok')