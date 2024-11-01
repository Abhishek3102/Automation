from selenium import webdriver
from selenium.webdriver.edge.service import Service
import pandas as pd
import time

path = 'D:\Edge Driver\msedgedriver.exe'  
service = Service(executable_path=path)
website = 'https://forms.gle/PLt6xeVt5jRodXcZ8'  
driver = webdriver.Edge(service=service)

df = pd.read_csv('fake_data.csv')

for i in range(0, len(df)):
    driver.get(website)
    time.sleep(3)
    for column in df.columns:
        text_input = driver.find_element(by='xpath', value=f'//div[contains(@data-params, "{column}")]//input | '
                                                           f'//div[contains(@data-params, "{column}")]//textarea')
        text_input.send_keys(df.loc[i, column])
    submit_button = driver.find_element(by='xpath', value='//div[@role="button"]//span[text()="Submit"]')  # "Submit" text may vary depending on language
    submit_button.click()

driver.quit()
