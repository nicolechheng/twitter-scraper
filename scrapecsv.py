import pandas as pd
import openpyxl
import csv
import re
from getpass import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

path = r"C:\Program Files (x86)\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)

data = pd.read_csv(r"C:\Users\nikki\Pictures\absolutewords.csv")
df = pd.DataFrame(data)
location_data = []
#print(df['Link leading to mention'].dropna())

for i in df['Author URL'].dropna():
    driver.get(i)

    try:
        location = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@data-testid="UserProfileHeader_Items"]/span/span')))
        #location = driver.find_element_by_xpath('//div[@data-testid="UserProfileHeader_Items"]/span/span')
    except Exception:
        continue
    location_data.append(location.text)

location_data = pd.DataFrame(location_data)
print(location_data)

location_data.to_excel(r'C:\Users\nikki\Pictures\words.xlsx', index = False)
