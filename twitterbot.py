from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

# Initialize the web driver
driver_service = Service(executable_path = "D:/New folder/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

username = "write your username"
password = "write your password"
delay = 1

# Set the time of the day when the tweets should be posted
post_time = "17:30"

# Read the list of sentences from a file
with open("C:/Users/Dell 5400/Desktop/coding/jupyter/quotes/sentences.txt", "r") as f:
    sentences = f.readlines()
    last_quote = sentences[-1]



# Log in to Twitter
driver.get("https://twitter.com/i/flow/login")
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
    print("Page is ready!")
except TimeoutException:
    pass
enter_username = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
enter_username.click()
enter_username.send_keys(username)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()

try:
    myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
    print("Page is ready!")
except TimeoutException:
    pass
enter_pass = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
enter_pass.send_keys(password)
driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span').click()

# Wait for the specified time
while True:
    current_time = time.strftime("%H:%M")
    if current_time == post_time:
        break
    time.sleep(60)
    
post_tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span')
post_tweet.click()
post_tweet.send_keys(last_quote)
    
    
# Close the web driver
driver.close()
