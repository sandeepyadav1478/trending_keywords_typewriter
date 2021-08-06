import os
import pandas as pd
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser

load_button_loop = 10
keywords_export = "assets/google_trend_keywords.csv"
country_iso2 = "assets/country.csv"

keywords = []
counter = 0

print("\nChecking driver in catch or Downloading it ...")
option = webdriver.ChromeOptions()
option.add_argument('head')
driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)

def lets_fire(q):
    search_url="https://trends.google.com/trends/trendingsearches/daily?geo={q}" 
    print("\nSending request for country iso2 code :",q)
    driver.get(search_url.format(q=q))
    for i in range(0,load_button_loop):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@class="feed-load-more-button"]').click()
        except NoSuchElementException as er:
            print("\nError : No such file available \n",er)
    Results = driver.find_elements_by_xpath('//*[@class="title"]/span/a')
    for a in Results:
        global counter
        counter = counter + 1
        keywords.append(a.text)
        print("\nFound keyword ",a.text)


country_iso2_data = pd.read_csv(country_iso2)
for i in country_iso2_data["iso2"]:
    lets_fire(i)

print("quiting driver ...")
driver.quit()

print("\n Total numbers of keywords found on google trend : ",counter)


print("\n Saving data in ...",keywords_export)
keywords_df = pd.DataFrame(keywords)
keywords_df.columns = ['title']
keywords_df.to_csv(keywords_export,index=False)

