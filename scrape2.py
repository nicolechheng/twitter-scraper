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
driver.get('https://www.twitter.com/login')


def get_tweet_data(card):
    """Extract data from tweet card"""
    username = card.find_element_by_xpath('.//span').text
    try:
        handle = card.find_element_by_xpath('.//span[contains(text(), "@")]').text
    except NoSuchElementException:
        return

    try:
        postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
    except NoSuchElementException:
        return



    comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    responding = card.find_element_by_xpath('.//div[2]/div[2]/div[2]').text
    text = comment + responding
    reply_cnt = card.find_element_by_xpath('.//div[@data-testid="reply"]').text
    retweet_cnt = card.find_element_by_xpath('.//div[@data-testid="retweet"]').text
    like_cnt = card.find_element_by_xpath('.//div[@data-testid="like"]').text


    tweet = (username, handle, postdate, text, reply_cnt, retweet_cnt, like_cnt)
    return tweet

username = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//input[@name="session[username_or_email]"]')))
username.send_keys('mytwittest2021@gmail.com')
password = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//input[@name="session[password]"]')))
password.send_keys('nicole2021')
password.send_keys(Keys.RETURN)

search_input = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//input[@aria-label="Search query"]')))
search_input.send_keys('always near:CA since:2019-03-01 until:2019-03-31')
search_input.send_keys(Keys.RETURN)
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.LINK_TEXT,'Latest'))).click()
#clicks into user profile
#WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[2]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/div[1]/div[1]'))).send_keys(Keys.CONTROL + 't')
#WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[2]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/div[1]/div[1]'))).send_keys(Keys.CONTROL + Keys.TAB)
#clicks out of user profile
#so i need to try to open in a new window maybe?
#WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/div'))).click()

data = []
tweet_ids = set()
last_position = driver.execute_script("return window.pageYOffset;")
scrolling = True
location = {}

while scrolling:
    page_cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
    for card in page_cards[-15:]:
        tweet = get_tweet_data(card)
        if tweet:
            tweet_id = ''.join(tweet)
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)
                data.append(tweet)
                #here i'm trying to click into each account and then wanted to extract the location data and then i click the back arrow key... not working, telling me the elements are stale afterwards
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                        '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[2]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/div[1]/a/div/div[1]/div[1]'))).click()
                #WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                        #'/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div/div'))).click()
    scroll_attempt = 0
    while True:
        # check scroll position
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(2)
        curr_position = driver.execute_script("return window.pageYOffset;")
        if last_position == curr_position:
            scroll_attempt += 1

            # end of scroll region
            if scroll_attempt >= 3:
                scrolling = False
                break
            else:
                sleep(2)  # attempt another scroll
        else:
            last_position = curr_position
            break

# close the web driver
driver.close()

print(len(data))