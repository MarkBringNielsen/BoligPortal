from  selenium import webdriver
from geopy.geocoders import Nominatim
import requests
import json

locator = Nominatim(user_agent='myGeocoder')
OB = locator.geocode('Odense, Odense Banegård')


# f = open('src\seenApartments.json')
# data = json.load(f)
# for p in data['people']:




portal = 'https://www.boligportal.dk/lejeboliger/odense/'
driver = webdriver.Chrome(executable_path='C:\\Users\\Mark\\Documents\\chromedriver')
driver.get(portal)
driver.find_element_by_xpath("//button[@class='coi-banner__accept']").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")

# 'temporaryFlexColumnClassName css-1lj5xbb-FlexColumn'
apartment_box = driver.find_element_by_xpath("//div[contains(@class, 'css-1lj5xbb-FlexColumn')]")
apartments = apartment_box.find_elements_by_xpath(".//div[contains(@class, 'css-1rd0wqj-FlexColumn')]")

acceptable = []

for apartment in apartments:


    street = apartment.find_element_by_xpath(".//div[contains(@class, 'css-1wrf1k9-Text-Text')]").text

    print(street)
    link = apartment.find_element_by_xpath(".//a").get_attribute('href')

    aprt_cord = locator.geocode(street)

    if aprt_cord is None:
        continue

    r = requests.get(f"http://router.project-osrm.org/route/v1/car/{aprt_cord.longitude},{aprt_cord.latitude};{OB.longitude},{OB.latitude}?overview=false")
    routes = json.loads(r.content)
    route_1 = routes.get("routes")[0]
    print (route_1['distance'])
    if (route_1['distance'] < 3500):
        acceptable.append({link : route_1['distance']})

print(acceptable)
