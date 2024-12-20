from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

path = 'D:\\Edge Driver\\msedgedriver.exe'
website = 'https://forms.gle/WT68aV5UnPajeoSc8'
driver = webdriver.Edge()

df = pd.read_csv('fake_data.csv')

for i in range(len(df)):
    driver.get(website)
    time.sleep(2)

    full_name = driver.find_element(By.XPATH, '//input[@aria-label="Full Name"]')
    full_name.send_keys("Abhishek Pandey")

    contact_number = driver.find_element(By.XPATH, '//input[@aria-label="Contact Number"]')
    contact_number.send_keys("9167595918")

    email = driver.find_element(By.XPATH, '//input[@aria-label="Email ID"]')
    email.send_keys("abhishekpandey7845@gmail.com")

    address = driver.find_element(By.XPATH, '//textarea[@aria-label="Full Address"]')
    address.send_keys("SWASTIK SOCIETY, GULMOHAR ROAD, VILE PARLE WEST")

    pin_code = driver.find_element(By.XPATH, '//input[@aria-label="Pin Code"]')
    pin_code.send_keys("123456")

    dob = driver.find_element(By.XPATH, '//input[@aria-label="Date of Birth"]')
    dob.send_keys("01-01-1990")

    gender = driver.find_element(By.XPATH, '//input[@aria-label="Gender"]')
    gender.send_keys("Male")

    verification_code = driver.find_element(By.XPATH, '//input[@aria-label="Type this code"]')
    verification_code.send_keys("GNFPYC")

    submit_button = driver.find_element(By.XPATH, '//div[@role="button"]//span[text()="Submit"]')
    submit_button.click()

    time.sleep(2)

driver.quit()
