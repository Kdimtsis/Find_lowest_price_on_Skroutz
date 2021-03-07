from bs4 import BeautifulSoup as bs
import requests
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

class Skroutz_search():

    def __init__(self):
        self.name = 'skroutz'


    def user_input(self):
        choice = input("What do you want to buy? ")
        return choice

    def search_item(self):

        choice = self.user_input()

        path = r"D:\User-1\Anaconda\Lib\site-packages\soccerapi\api\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get("https://www.skroutz.gr/")

        search = driver.find_element_by_name("keyphrase")  # ΕΔΩ ΒΡΙΣΚΕΤΑΙ ΤΟ SEARCH BAR ΣΤΟ ΣΚΡΟΥΤΖ
        search.send_keys(choice)  # ΟΤΙ ΒΑΛΩ ΕΔΩ ΘΑ ΚΑΝΕΙ ΣΕΡΤΣ ΣΤΟ SEARCH BAR
        search.send_keys(Keys.RETURN) # ΠΑΤΑΕΙ ΕΝΤΕΡ

        select_product = driver.find_element_by_xpath("/html/body/div[1]/main/section/ol/li[1]/div/h2/a")
        driver.execute_script("arguments[0].click();", select_product)

        current_link = driver.current_url
        return current_link


    def notify(self, title, message):
            notification.notify(title=title, message=message, timeout=10)


    def get_price(self):

        url = self.search_item()

        # GET THE NAME OF PRODUCT FROM URL
        product_name = url.split(".html")[0].split("/")[-1].replace("-", " ")

        data = requests.get(url, "html.parser")
        soup = bs(data.text, "html.parser")

        # A LIST WITH EVERY STORE
        shops = soup.find_all(class_="cf card js-product-card")

        all_prices = []
        # BECAUSE IT IS A NONE OBJECT WE MUST TURN IT INTO A STRING

        for shop in shops:
            x = str(shop)
            # product = x.partition("title=")[2].split(">")[0].replace("\"", "")
            price = x.split(" €")[0].split(">")[-1].replace(".", "").replace(",", ".")
            all_prices.append(float(price))

        lowest_price = sorted(all_prices)[0]
        self.notify(title="UPDATE", message=f"Lowest price for {product_name} is now {lowest_price} Euros")


user = Skroutz_search()
user.get_price()






