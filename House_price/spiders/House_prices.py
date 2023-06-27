import scrapy
from pathlib import Path
import json
import pandas as pd
# import string
from selenium import webdriver
from scrapy.http import HtmlResponse

from scrapy_selenium import SeleniumRequest
import time

# selenium.__file__

# List of features
amenity_list = set()

# List of Amenities in dictionary

amenity_dict = {'Bank & ATM': [],
                'Golf Course': [],
                'Early Learning Centre': [],
                'Kids Play Area': [],
                'Security': [],
                'Meditation Area': [],
                'Park': [],
                'Multipurpose Courts': [],
                'Intercom Facility': [],
                'Rain Water Harvesting': [],
                'AEROBICS ROOM': [],
                'DTH Television Facility': [],
                'Banquet Hall': [],
                'Piped Gas': [],
                'Earth quake resistant': [],
                'Private Garden': [],
                'Skydeck': [],
                'Internet/Wi-Fi Connectivity': [],
                'Cafeteria/Food Court': [],
                'Grand Entrance lobby': [],
                'Event Space & Amphitheatre': [],
                'Conference Room': [],
                'Recreational Pool': [],
                'Visitor Parking': [],
                'Guest Accommodation': [],
                'Kids Play Pool With Water Slides': [],
                'Concierge Services': [],
                'Mini Cinema Theatre': [],
                'Indoor Games Room': [],
                'Outdoor Tennis Courts': [],
                'Flower Gardens': [],
                'Vaastu Compliant': [],
                'Health club with Steam / Jaccuzi': [],
                'CCTV Camera': [],
                'Cricket net practice': [],
                'Bar/Lounge': [],
                'Club House': [],
                'Air Conditioned': [],
                'Canopy Walk': [],
                'Fire Fighting Equipment': [],
                'Private Terrace/Garden': [],
                'Cycling & Jogging Track': [],
                'RO Water System': [],
                'Activity Deck4': [],
                'Power Back Up': [],
                'Reserved Parking': [],
                'Barbeque Pit': [],
                'Dance Studio': [],
                'Kids Club': [],
                'Service/Goods Lift': [],
                'Retail Boulevard (Retail Shops)': [],
                'Waste Disposal': [],
                'Lift': [],
                'Library': [],
                'Laundry Service': [],
                'Rentable Community Space': [],
                'Indoor Squash & Badminton Courts': [],
                'Maintenance Staff': [],
                'Jogging and Strolling Track': [],
                'Library And Business Centre': [],
                'Water Storage': [],
                'Multipurpose Hall': [],
                'Coffee Lounge & Restaurants': [],
                'Gymnasium': [],
                'Swimming Pool': [],
                'Arts & Craft Studio': []}

##
city = []
bedrooms = []
bathrooms = []
balconies = []
postedOn = []
furnishing = []
facing = []
flrNum = []
totalFlrNum = []
RentOrSale = []

amenitites = []


locality = []
carpetArea = []
carpetAreaUnit = []
Lat = []
Long = []
noOfLifts = []

rentPrice = []
securityDeposit = []
maintenanceCharges = []
maintenanceChargesFrequency = []
firstMonthCharges = []

brokerage = []
exactPrice = []
sqftPrice = []

# maing dictionary of all the list

Df_dict = {"city": city,
           "bathrooms": bathrooms,
           "bedrooms": bedrooms,
           "balconies": balconies,
           "postedOn": postedOn,
           "furnishing": furnishing,
           "facing": facing,
           "flrNum": flrNum,
           "totalFlrNum": totalFlrNum,
           "RentOrSale": RentOrSale,
           "locality": locality,
           "carpetArea": carpetArea,
           "carpetAreaUnit": carpetAreaUnit,
           "Lat": Lat,
           "Long": Long,
           "noOfLifts": noOfLifts,
           "rentPrice": rentPrice,
           "securityDeposit": securityDeposit,
           "maintenanceCharges": maintenanceCharges,
           "maintenanceChargesFrequency": maintenanceChargesFrequency,
           "firstMonthCharges": firstMonthCharges,
           "brokerage": brokerage,
           "exactPrice": exactPrice,
           "sqftPrice": sqftPrice,
           }

Df_dict.update(amenity_dict)


class HousePricesSpider(scrapy.Spider):

    name = 'House_prices'

    def start_requests(self):

        # driver_path = "E:/projects/chromedriver"
        # driver = Chrome(executable_path=driver_path)
        # driver.get("https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment&cityName=Bangalore")
        urls = [
            "https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment&cityName=Bangalore",
        ]

        for url in urls:
            yield SeleniumRequest(url=url, callback=self.parse_list)

        # print("\n\n\n city\n\n", city)

    def parse(self, response):

        # Pointing out the location of desired data using xpath

        contents = response.xpath(
            '//body/div/div/script/text()').getall()

        # Converting list output to string for further processing

        contents = " ".join(contents)

        # Striping the text in the script tag to get the desired json (string format)

        start_index = contents.find('{')
        end_index = contents.rfind('}') + 1
        dictionary_string = contents[start_index:end_index]

        # Converting string json to dictionary for processing

        dict = json.loads(dictionary_string)

        try:
            city.append(dict["propertyDetailInfoBeanData"]
                        ["cityName"])
        except KeyError:
            city.append(9)

        try:
            bedrooms.append(dict["propertyDetailInfoBeanData"]
                            ["propertyDetail"]["detailBean"]["bedrooms"])
        except KeyError:
            bedrooms.append(9)

        try:
            bathrooms.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["bathrooms"])
        except KeyError:
            bathrooms.append(9)

        try:
            balconies.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["numberOfBalconied"])
        except KeyError:
            balconies.append(9)

        try:
            postedOn.append(dict["propertyDetailInfoBeanData"]
                            ["propertyDetail"]["detailBean"]["postedOn"])
        except KeyError:
            postedOn.append(9)

        try:
            furnishing.append(dict["propertyDetailInfoBeanData"]
                              ["propertyDetail"]["detailBean"]["furnished"])
        except KeyError:
            furnishing.append(9)

        try:
            facing.append(dict["propertyDetailInfoBeanData"]
                          ["propertyDetail"]["detailBean"]["facing"])
        except KeyError:
            facing.append(9)

        try:
            flrNum.append(dict["propertyDetailInfoBeanData"]
                          ["propertyDetail"]["detailBean"]["floorNumber"])
        except KeyError:
            flrNum.append(9)

        try:
            totalFlrNum.append(dict["propertyDetailInfoBeanData"]
                               ["propertyDetail"]["detailBean"]["totalFloorNumber"])
        except KeyError:
            totalFlrNum.append(9)

        try:
            RentOrSale.append(dict["propertyDetailInfoBeanData"]
                              ["propertyDetail"]["detailBean"]["saleRent"])

        except KeyError:
            RentOrSale.append(9)

        try:
            amenity_features = dict["propertyDetailInfoBeanData"]["propertyDetail"]["detailBean"]["amenityMap"]
            amenitites.append(amenity_features)
            for dict_value in amenity_dict.keys():

                try:

                    if dict_value in amenity_features.values():
                        amenity_dict[dict_value].append(1)

                    else:
                        amenity_dict[dict_value].append(0)
                except:
                    pass

        except KeyError:
            for i in amenity_dict.keys():
                amenity_dict[i].append(9)

        try:
            locality.append(dict["propertyDetailInfoBeanData"]
                            ["propertyDetail"]["detailBean"]["locality"])
        except KeyError:
            locality.append(9)

        try:
            carpetArea.append(dict["propertyDetailInfoBeanData"]
                              ["propertyDetail"]["detailBean"]["carpetArea"])
        except KeyError:
            carpetArea.append(9)
        try:
            carpetAreaUnit.append(dict["propertyDetailInfoBeanData"]
                                  ["propertyDetail"]["detailBean"]["carpetAreaUnit"])
        except KeyError:
            carpetAreaUnit.append(9)
        try:
            Lat.append(dict["propertyDetailInfoBeanData"]
                       ["propertyDetail"]["detailBean"]["latitude"])
        except KeyError:
            Lat.append(9)
        try:
            Long.append(dict["propertyDetailInfoBeanData"]
                        ["propertyDetail"]["detailBean"]["longitude"])
        except KeyError:
            Long.append(9)
        try:
            noOfLifts.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["noOfLifts"])
        except KeyError:
            noOfLifts.append(9)

        try:
            rentPrice.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["priceBreakUp"]["rentPrice"])
        except KeyError:
            rentPrice.append(9)
        try:
            securityDeposit.append(dict["propertyDetailInfoBeanData"]
                                   ["propertyDetail"]["detailBean"]["priceBreakUp"]["securityDeposit"])
        except KeyError:
            securityDeposit.append(9)
        try:
            maintenanceCharges.append(dict["propertyDetailInfoBeanData"]
                                      ["propertyDetail"]["detailBean"]["priceBreakUp"]["monthlyMaintenance"])
        except KeyError:
            maintenanceCharges.append(9)
        try:
            maintenanceChargesFrequency.append(dict["propertyDetailInfoBeanData"]
                                               ["propertyDetail"]["detailBean"]["maintenanceChargesFrequency"])
        except KeyError:
            maintenanceChargesFrequency.append(9)
        try:
            firstMonthCharges.append(dict["propertyDetailInfoBeanData"]
                                     ["propertyDetail"]["detailBean"]["priceBreakUp"]["firstMonthCharges"])
        except KeyError:
            firstMonthCharges.append(9)
        try:
            brokerage.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["brokerage"])
        except KeyError:
            brokerage.append(9)
        try:
            exactPrice.append(dict["propertyDetailInfoBeanData"]
                              ["propertyDetail"]["detailBean"]["exactSaleRentPrice"])
        except KeyError:
            exactPrice.append(9)
        try:
            sqftPrice.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["sqftPrice"])
        except KeyError:
            sqftPrice.append(9)

        new = pd.DataFrame.from_dict(Df_dict)

        new.to_csv('file1.csv')

        # return Df_dict

    def parse_list(self, response):

        driver = webdriver.Edge()
        driver.get(response.url)

        # Pointing out the location of desired data using xpath

        # Extract and process data from the initial page

        # Simulate scrolling behavior using Selenium

        Xpath = '(//div[@class="mb-srp__card"]/script[@type="application/ld+json"][1])/text()'

        last_height = driver.execute_script(
            "return document.body.scrollHeight")

        while True:
            # Scroll to the bottom of the page
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Wait for the page to load new content
            time.sleep(3)  # Adjust the wait time if needed

            # Check if the page height has changed after scrolling
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

            # Extract and process data from the scrolled page

            contents = response.xpath(
                '(//div[@class="mb-srp__card"]/script[@type="application/ld+json"][1])/text()').getall()

            for content in contents:

                # Changing string to json file

                cont = json.loads(content)

                # Appending new data
                yield scrapy.Request(url=cont["url"], callback=self.parse)

            # Convert the current page source to a Scrapy Response
            response = HtmlResponse(
                driver.current_url,
                body=driver.page_source,
                encoding='utf-8'
            )

        # driver.quit()

        # # making new lists

        # url = []

        # Df_dict.update(amenity_dict)
        # new = pd.DataFrame.from_dict(Df_dict)

        # # new.to_csv('file1.csv')

        # print("hey\n\n\n\n")

        # print(amenity_dict)
