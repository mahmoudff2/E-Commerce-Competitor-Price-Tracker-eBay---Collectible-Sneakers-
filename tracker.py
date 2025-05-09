from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument("--disable-gpu") 
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)
data = []
number_of_pages = int(input('How many pages you want to scrape?'))
driver.get("https://www.ebay.com/b/Collectible-Sneakers/bn_7000259435")
for _ in range(number_of_pages):
    time.sleep(4)
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.brwrvr__item-card--list')))
    for _ in range(85):
        driver.execute_script("window.scrollBy(0, 180)")
        time.sleep(0.13)
    products = driver.find_elements(By.CSS_SELECTOR, '.brwrvr__item-card--list')
    for product in products:
        title = product.find_element(By.CSS_SELECTOR, '.bsig__title__text').text
        price = product.find_element(By.CSS_SELECTOR, '.bsig--primary:nth-child(1) span').text
        try:
            img_url = product.find_element(By.CSS_SELECTOR, 'li.carousel__snap-point:nth-child(1) a img').get_attribute('src')
            link = product.find_element(By.CSS_SELECTOR, 'li.carousel__snap-point:nth-child(1) a').get_attribute('href')
        except:
            img_url = None
            link = None
        data.append((title,price,img_url,link))


    clk = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Go to next page']")
    clk.click()
    time.sleep(2)

with open('eBay_Collectible_Sneakers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Image URL', 'Link'])
    for p in data:
        writer.writerow(p)

time.sleep(3)
driver.close()
print('Done !')


