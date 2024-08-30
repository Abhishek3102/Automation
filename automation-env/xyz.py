from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up your Selenium WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.thesun.co.uk/sport/football/")

# Define the XPath expressions
titles = driver.find_elements(By.XPATH, "//a/span[contains(@class, 'title-class')]")  # Replace 'title-class' with the actual class
subtitles = driver.find_elements(By.XPATH, "//a/span[contains(@class, 'subtitle-class')]")  # Replace 'subtitle-class' with the actual class
links = driver.find_elements(By.XPATH, "//a[contains(@class, 'link-class')]")  # Replace 'link-class' with the actual class

# Iterate over the elements and print them
for title, subtitle, link in zip(titles, subtitles, links):
    print(f"Title: {title.text}")
    print(f"Subtitle: {subtitle.text}")
    print(f"Link: {link.get_attribute('href')}")
    print()

# Close the WebDriver
driver.quit()




















from selenium import webdriver
from selenium.webdriver.edge.service import Service
import pandas as pd
from datetime import datetime
from selenium.webdriver.common.by import By
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

web = 'https://www.thesun.co.uk/sport/football/'
path = 'D:\Edge Driver\msedgedriver.exe' 

options = webdriver.EdgeOptions()
options.add_argument('headless')
service = Service(executable_path=path)
driver = webdriver.Edge(service=service,options=options)
driver.get(web)

containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = container.find_element(by='xpath', value='//a/span').text
    subtitle = container.find_element(by='xpath', value='//a/h3').text
    link = container.find_element(by='xpath', value='//a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'football_headlines_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)


driver.quit()
# <span class="teaser__headline teaser__kicker t-p-color" data-original-text="LEW HORIZONS">LEW HORIZONS</span>
# <h3 class="teaser__subdeck" data-original-text=" Hilarious moment Arteta offers reporter new job if he's 'agile &amp; mobile enough'"> Hilarious moment Arteta offers reporter new job if he's 'agile &amp; mobile enough'</h3>
# /html/body/div[6]/main/div/div[2]/div/div[3]/div/div[2]/a










from selenium import webdriver
from selenium.webdriver.edge.service import Service
import pandas as pd
from datetime import datetime
from selenium.webdriver.common.by import By
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

web = 'https://www.thesun.co.uk/sport/football/'
path = 'D:\Edge Driver\msedgedriver.exe' 

options = webdriver.EdgeOptions()
options.add_argument('headless')
service = Service(executable_path=path)
driver = webdriver.Edge(service=service,options=options)
driver.get(web)

containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []
for container in containers:
    title = driver.find_elements(By.XPATH, "//a/span[contains(@class, 'teaser__headline teaser__kicker t-p-color')]")
    subtitle = driver.find_elements(By.XPATH, "//h3[contains(@class, 'teaser__subdeck')]")
    link = driver.find_elements(By.XPATH, "//a[contains(@class, 'text-anchor-wrap')]")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'football_headlines_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)


driver.quit()