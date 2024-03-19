# Program to send bulk customized message through WhatsApp web application
# Author @inforkgodara

from numpy import add
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pandas
import time

# Load the chrome driver
driver = webdriver.Chrome("/Users/username/Desktop/03-Project/01-工程开发/04-自动发送WhatsApp/发送图片/chromedriver")
count = 0

# Open WhatsApp URL in chrome browser
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 20)

# Read data from excel
contacts = pandas.read_excel('/Users/username/Desktop/03-Project/01-工程开发/04-自动发送WhatsApp/发送图片/contact.xlsx', sheet_name='sheet1')

address = contacts.values.tolist()
print(address)

file_path = "/Users/username/Desktop/03-Project/01-工程开发/04-自动发送WhatsApp/发送图片/1.png"#file path

# Iterate excel rows till to finish
for i, n in address:
    # Assign customized message
    # message = excel_data['/Users/username/Downloads/python-automated-bulk-whatsapp-messages-master/WechatIMG25.jpeg']
    # Locate search box through x_path
    search_box = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    person_title = wait.until(lambda driver:driver.find_element_by_xpath(search_box))

    # Clear search box if any contact number is written in it
    person_title.clear()

    # Send contact number in search box
    person_title.send_keys(str(n))
    # count = count + 1

    # Wait for 2 seconds to search contact number
    time.sleep(5)

    try:
        # Load error message in case unavailability of contact number
        element = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/span')
    except NoSuchElementException:
        # Format the message from excel sheet
        person_title.send_keys(Keys.ENTER)
        attachment_section = driver.find_element_by_xpath('//div[@title = "附件"]')  
        attachment_section.click()
        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(file_path)   
        time.sleep(2)
        send_botton = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_botton.click()
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.ENTER)
        # actions.perform()
        time.sleep(2)


# Close chrome browser
driver.quit()
