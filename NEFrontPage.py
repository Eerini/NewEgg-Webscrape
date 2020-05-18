from bs4 import BeautifulSoup
import requests
import csv

'''
source = requests.get('https://www.newegg.com').text
soup = BeautifulSoup(source, 'lxml')

for category in soup.find_all('li', class_='main-nav-item'):

    category_name = category.a.text
    category_link = category.a['href']
    print(category_name)
'''

class NewEggItems:

    def __init__(self):
        self.source = requests.get('https://www.newegg.com').text
        self.soup = BeautifulSoup(self.source, 'lxml')
        self.categoryDict = {}
        self.categoryList = []

    def categorySelect(self):
        for category in self.soup.find_all('li', class_='main-nav-item'):
            category_name = category.a.text
            category_link = category.a['href']
            self.categoryDict[category_name] = category_link
            self.categoryList.append(category_name)
        print(self.categoryList)

        return self.categoryList

    
        

