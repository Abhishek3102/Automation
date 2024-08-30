from selenium import webdriver
from selenium.webdriver.edge.service import Service
import pandas as pd
from datetime import datetime
from selenium.webdriver.common.by import By
import os
import sys

# Get the application path for saving the CSV file
application_path = os.path.dirname(sys.executable)

# Get the current date for the CSV filename
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

# URL of the website to scrape
web = 'https://www.thesun.co.uk/sport/football/'
# Path to the Edge WebDriver executable
path = 'D:\Edge Driver\msedgedriver.exe' 

# Set up Edge browser options
options = webdriver.EdgeOptions()
options.add_argument('headless')  # Run browser in headless mode

# Set up the WebDriver service
service = Service(executable_path=path)
driver = webdriver.Edge(service=service, options=options)

# Open the webpage
driver.get(web)

# Find all containers with the relevant news article information
containers = driver.find_elements(By.CSS_SELECTOR, 'div.teaser__copy-container')

# Initialize lists to store titles, subtitles, and links
titles = []
subtitles = []
links = []

# Loop through each container and extract the title, subtitle, and link
for container in containers:
    try:
        # Extract the title using CSS selector
        title_element = container.find_element(By.CSS_SELECTOR, 'a.text-anchor-wrap')
        # Extract the subtitle using CSS selector
        subtitle_element = container.find_element(By.CSS_SELECTOR, 'h3.teaser__subdeck')
        # Extract the link associated with the title
        link = title_element.get_attribute('href')
        
        # Append the text and link to the respective lists
        titles.append(title_element.text)
        subtitles.append(subtitle_element.text)
        links.append(link)
    except Exception as e:
        print(f"Error encountered: {e}")
        continue

# Create a DataFrame from the collected data
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)

# Generate the filename and save the DataFrame to a CSV file
file_name = f'football_headlines_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path, index=False)

# Close the browser
driver.quit()
