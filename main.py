from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

list1 = []

list2 = []

try:
    site = driver.get(url="https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb")
    for i in range(1, 9):
        names = driver.find_element(By.CSS_SELECTOR, f"#anonCarousel1 > ol > li:nth-child({i}) > div > a > span > span > span.a-truncate-cut")
        price = driver.find_element(By.CSS_SELECTOR, f"#anonCarousel1 > ol > li:nth-child({i}) > div > a > div._discount-asin-shoveler_style_priceContainer__3lkqa > div._discount-asin-shoveler_style_priceToPay__EfL5V > span > span:nth-child(2) > span.a-price-whole")
        add = driver.find_element(By.CSS_SELECTOR, f"#anonCarousel1 > ol > li:nth-child({i}) > div > a > div._discount-asin-shoveler_style_priceContainer__3lkqa > div._discount-asin-shoveler_style_priceToPay__EfL5V > span > span:nth-child(2) > span.a-price-fraction")
        last = driver.find_element(By.CSS_SELECTOR, f"#anonCarousel1 > ol > li:nth-child({i}) > div > a > div._discount-asin-shoveler_style_priceContainer__3lkqa > div._discount-asin-shoveler_style_strikethroughPrice__3POb3 > span.a-price.a-text-price > span:nth-child(2)")
        prices = "$" + price.text + "." + add.text + " <- " + last.text
        list1.append(names.text)
        list2.append(prices)
        print(list1)
        df = pd.DataFrame(data=list1, columns=["Name of goods"])
        df["Deals"] = list2
        print("a")
        df.to_csv("Example.csv")
    print(df) 
except Exception as error:
    print("Sorry, we dont have 8 products yet")
finally:
    driver.close()
    driver.quit()