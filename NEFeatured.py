from bs4 import BeautifulSoup
import requests
import csv
from NEFrontPage import NewEggItems

class FeaturedItems:

    def __init__(self):
        self.f_page = NewEggItems()
        self.choose = None
        self.f_page.categorySelect()


    def chooseCategory(self):
        self.choose = input('Type category name: ')

    def itemDetails(self):
        source = requests.get(self.f_page.categoryDict.get(self.choose)).text
        
        soup = BeautifulSoup(source, 'lxml')
        item = soup.find('div', class_='item-container')

        #csv_file = open('newegg_product.csv', 'w')
        #csv_writer = csv.writer(csv_file)
        #csv_writer.writerow(['Product Name', 'Product Link', 'Current Price', 'MSRP', 'Promotion'])
        for item in soup.find_all('div', class_='item-container'):
            item_link = item.a['href']
            item_name = item.find('a', class_='item-title').text

            try:
                item_price_was = item.find('span', class_='price-was-data').text
                item_promo = item.find('p', class_='item-promo').text
                price_current_main = item.find('li', class_='price-current').strong.text
                price_current_sub = item.find('li', class_='price-current').sup.text

            except AttributeError:
                item_price_was = 'N/A'
                item_promo = None
                price_current_main = item.find('li', class_='price-current').strong.text
                price_current_sub = item.find('li', class_='price-current').sup.text
                print("Product Name: {}".format(item_name))
                print("Product Link: {}".format(item_link))
                print("Current Price: ${}{}".format(price_current_main, price_current_sub))
                print("Before Saving: {}".format(item_price_was))
                print('\n')
                #csv_writer.writerow([item_name, item_link, '${}{}'.format(price_current_main, price_current_sub), item_price_was, item_promo])

            else:
                print("Product Name: {}".format(item_name))
                print("Product Link: {}".format(item_link))
                print("Current Price: ${}{}".format(price_current_main, price_current_sub))
                print("Before Saving: ${:,.2f}".format(float(item_price_was)))
                print(item_promo)
                print('\n')
                #csv_writer.writerow([item_name, item_link, '${}{}'.format(price_current_main, price_current_sub), item_price_was, item_promo])
        #csv_file.close()        
        

            
NE = FeaturedItems()
NE.chooseCategory()
NE.itemDetails()

        



