import requests
import json
import geocoder
from  selenium import webdriver


portal = 'https://www.boligportal.dk/lejeboliger/odense/'

driver = webdriver.Chrome(executable_path='//home/setero/chromedriver')

driver.get(portal)



driver.find_element_by_xpath('css-1lj5xbb-FlexColumn')

