from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
from geopy.geocoders import Nominatim
from chromedriver_location import location as cd_location
import requests
import json
import  pandas as pd 

locator = Nominatim(user_agent='myGeocoder')
OB = locator.geocode('Odense, Odense Banegård')

portal = 'https://www.boligportal.dk/lejeboliger/odense/'
chrome_options = Options()  
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(executable_path=cd_location,chrome_options=chrome_options)
driver.get(portal)
driver.find_element_by_xpath("//button[@class='coi-banner__accept']").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")

# 'temporaryFlexColumnClassName css-1lj5xbb-FlexColumn'
apartment_box = driver.find_element_by_xpath("//div[contains(@class, 'css-1lj5xbb-FlexColumn')]")
apartments = apartment_box.find_elements_by_xpath(".//div[contains(@class, 'css-1rd0wqj-FlexColumn')]")

apartment_rows = []

for apartment in apartments:
    link = apartment.find_element_by_xpath(".//a").get_attribute('href')

    driver.get(link)

    street = driver.find_element_by_xpath('.//div[@class="css-76suba-Text-Text"]').text.split(' - ')[0]
    aprt_cord = locator.geocode(street)

    info_boxes = driver.find_element_by_xpath('.//div[@class="css-1t2kpzi-Flex-Flex"]')

    apartment_info = [aprt_cord]

    for info in info_boxes.find_elements_by_xpath('.//div[@class="css-1xppb8-Box-Box"]'):

        data = None
        if not info.text == '-' and not info.text == '' :
            data = info.text

        apartment_info.append(data)

    apartment_rows.append(apartment_info)

    break

print(apartment_rows)

# def geo_distance():
#     street = apartment.find_element_by_xpath(".//div[contains(@class, 'css-1wrf1k9-Text-Text')]").text

#     print(street)
#     link = apartment.find_element_by_xpath(".//a").get_attribute('href')

#     aprt_cord = locator.geocode(street)

#     if aprt_cord is None:
#         continue

#     r = requests.get(f"http://router.project-osrm.org/route/v1/car/{aprt_cord.longitude},{aprt_cord.latitude};{OB.longitude},{OB.latitude}?overview=false")
#     routes = json.loads(r.content)
#     route_1 = routes.get("routes")[0]
#     print (route_1['distance'])
#     if (route_1['distance'] < 3500):
#         acceptable.append({link : route_1['distance']})
