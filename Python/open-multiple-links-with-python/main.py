import selenium
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# open file and read lines
file_Stored = input("Input the location of file:")
file_to_login = open(file_Stored, 'r')
Lines = file_to_login.readlines()

# define chrome driver path
driver = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")

# read string before and after : symbol
count = 0
for line in Lines:
    count += 1

    # open links for every line
    driver.get(line)

    print("link", count, "opened")
    print("link is", line)

    # open new tab
    driver.execute_script("window.open('');")
    time.sleep(1)
    # Switch to the new window
    driver.switch_to.window(driver.window_handles[count])

    # Switch tab to the new tab, which we will assume is the next one on the right
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

time.sleep(2)
driver.quit()
