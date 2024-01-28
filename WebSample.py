from selenium import webdriver
import pandas as pd
import os

website = 'https://www.thesun.co.uk/tech/'

driver = webdriver.Chrome()
driver.get(website)
contents = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for content in contents:
    title = content.find_element(by='xpath', value='//div[@class="teaser__copy-container"]/a/h3').text
    subtitle = content.find_element(by='xpath', value='//div[@class="teaser__copy-container"]/a/p').text
    link = content.find_element(by='xpath', value='//div[@class="teaser__copy-container"]/a').get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

my_disk = {'titles':titles,'subtitles':subtitles,'links':links,}

allData = pd.DataFrame(my_disk)
allData.to_markdown('allData(1).md')

driver.quit()
