import scrapy
from pathlib import Path
import json
# import string


# List of features
amenity_list = list()


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


class HousePricesSpider(scrapy.Spider):
    name = 'House_prices'

    def start_requests(self):
        urls = [
            "https://www.magicbricks.com/propertyDetails/3-BHK-2390-Sq-ft-Multistorey-Apartment-FOR-Rent-Rajaji-Nagar-in-Bangalore&id=4d423636393636313331",
            "https://www.magicbricks.com/propertyDetails/3-BHK-1950-Sq-ft-Multistorey-Apartment-FOR-Rent-Devanahalli-in-Bangalore-r1&id=4d423633373634303333",
            "https://www.magicbricks.com/propertyDetails/1-BHK-350-Sq-ft-Multistorey-Apartment-FOR-Rent-whitefield-in-Bangalore&id=4d423634363538363139",
            "https://www.magicbricks.com/propertyDetails/1-BHK-600-Sq-ft-Multistorey-Apartment-FOR-Rent-HSR-Layout-Sector-5-in-Bangalore&id=4d423636313130363131",

            # "https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment&cityName=Kolkata",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # Pointing out the location of desired data using xpath

        contents = response.xpath(
            '//body/div/div/script/text()').getall()

        print("\n\n\n hey \n\n\n ")
        print(type(contents))

        # Converting list output to string for further processing

        contents = " ".join(contents)

        # Striping the text in the script tag to get the desired json (string format)

        start_index = contents.find('{')
        end_index = contents.rfind('}') + 1
        dictionary_string = contents[start_index:end_index]

        # Converting string json to dictionary for processing

        dict = json.loads(dictionary_string)

        # fn = f"newjsonbro.json"
        # Path(fn).write_text(dictionary_string, encoding='utf-8')

        print("\n\n\n bye \n\n\n ")

        print(dict["propertyDetailInfoBeanData"])

        try:
            city.append(dict["propertyDetailInfoBeanData"]
                        ["cityName"])
        except KeyError:
            city.append(0)

        try:
            bedrooms.append(dict["propertyDetailInfoBeanData"]
                            ["propertyDetail"]["detailBean"]["bedrooms"])
        except KeyError:
            bedrooms.append(0)

        try:
            bathrooms.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["bathrooms"])
        except KeyError:
            bathrooms.append(0)

        try:
            balconies.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["numberOfBalconied"])
        except KeyError:
            balconies.append(0)

        try:
            postedOn.append(dict["propertyDetailInfoBeanData"]
                            ["propertyDetail"]["detailBean"]["postedOn"])
        except KeyError:
            postedOn.append(0)

        try:
            furnishing.append(dict["propertyDetailInfoBeanData"]
                              ["propertyDetail"]["detailBean"]["furnished"])
        except KeyError:
            furnishing.append(0)

        try:
            facing.append(dict["propertyDetailInfoBeanData"]
                          ["propertyDetail"]["detailBean"]["facing"])
        except KeyError:
            facing.append(0)

        try:
            flrNum.append(dict["propertyDetailInfoBeanData"]
                          ["propertyDetail"]["detailBean"]["floorNumber"])
        except KeyError:
            flrNum.append(0)

        try:
            totalFlrNum.append(dict["propertyDetailInfoBeanData"]
                               ["propertyDetail"]["detailBean"]["totalFloorNumber"])
        except KeyError:
            totalFlrNum.append(0)

        try:
            RentOrSale.append(dict["propertyDetailInfoBeanData"]
                              ["propertyDetail"]["detailBean"]["saleRent"])

        except KeyError:
            RentOrSale.append(0)

        try:
            amenitites.append(dict["propertyDetailInfoBeanData"]
                              ["propertyDetail"]["detailBean"]["amenityMap"])
        except KeyError:
            amenitites.append(0)

        try:
            locality.append(dict["propertyDetailInfoBeanData"]
                            ["propertyDetail"]["detailBean"]["locality"])
        except KeyError:
            locality.append(0)

        try:
            carpetArea.append(dict["propertyDetailInfoBeanData"]
                              ["propertyDetail"]["detailBean"]["carpetArea"])
        except KeyError:
            carpetArea.append(0)
        try:
            carpetAreaUnit.append(dict["propertyDetailInfoBeanData"]
                                  ["propertyDetail"]["detailBean"]["carpetAreaUnit"])
        except KeyError:
            carpetAreaUnit.append(0)
        try:
            Lat.append(dict["propertyDetailInfoBeanData"]
                       ["propertyDetail"]["detailBean"]["latitude"])
        except KeyError:
            Lat.append(0)
        try:
            Long.append(dict["propertyDetailInfoBeanData"]
                        ["propertyDetail"]["detailBean"]["longitude"])
        except KeyError:
            Long.append(0)
        try:
            noOfLifts.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["noOfLifts"])
        except KeyError:
            noOfLifts.append(0)

        try:
            rentPrice.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["priceBreakUp"]["rentPrice"])
        except KeyError:
            rentPrice.append(0)
        try:
            securityDeposit.append(dict["propertyDetailInfoBeanData"]
                                   ["propertyDetail"]["detailBean"]["priceBreakUp"]["securityDeposit"])
        except KeyError:
            securityDeposit.append(0)
        try:
            maintenanceCharges.append(dict["propertyDetailInfoBeanData"]
                                      ["propertyDetail"]["detailBean"]["priceBreakUp"]["monthlyMaintenance"])
        except KeyError:
            maintenanceCharges.append(0)
        try:
            maintenanceChargesFrequency.append(dict["propertyDetailInfoBeanData"]
                                               ["propertyDetail"]["detailBean"]["maintenanceChargesFrequency"])
        except KeyError:
            maintenanceChargesFrequency.append(0)
        try:
            firstMonthCharges.append(dict["propertyDetailInfoBeanData"]
                                     ["propertyDetail"]["detailBean"]["priceBreakUp"]["firstMonthCharges"])
        except KeyError:
            firstMonthCharges.append(0)
        try:
            brokerage.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["brokerage"])
        except KeyError:
            brokerage.append(0)
        try:
            exactPrice.append(dict["propertyDetailInfoBeanData"]
                              ["propertyDetail"]["detailBean"]["exactSaleRentPrice"])
        except KeyError:
            exactPrice.append(0)
        try:
            sqftPrice.append(dict["propertyDetailInfoBeanData"]
                             ["propertyDetail"]["detailBean"]["sqftPrice"])
        except KeyError:
            sqftPrice.append(0)

        # url.append(dict["propertyDetailInfoBeanData"])
        # url.append(dict["propertyDetailInfoBeanData"])

        print("\n\n\n finish \n\n\n")
        print(len(Lat), len(Long), amenitites)

    def parse_list(self, response):

        # page = response.url.split("=")[-1]
        # filename = f"houses-{page}.html"

        # cards = response.css(".mb-srp__card")

        # print("\n\n\n {no} \n\n\n".format(no=len(cards)))

        contents = response.xpath(
            '(//div[@class="mb-srp__card"]/script[@type="application/ld+json"][1])/text()').getall()

        # fn = f"json.json"
        # Path(fn).write_text(",".join(contents))

        url = []
        NoRooms = []
        Lat = []
        Long = []
        Locality = []
        Capital = []

        for content in contents:
            # print(type(contents))
            # print("\n\n\n hey \n\n\n ")
            # print(type(json.loads(content)))
            # print("\n\n\n bye \n\n\n")

            cont = json.loads(content)
            print(cont["geo"])

            url.append(cont["url"])
            NoRooms.append(cont["numberOfRooms"])
            Lat.append(cont["geo"]["latitude"])
            Long.append(cont["geo"]["longitude"])
            Locality.append(cont["address"]["addressLocality"])
            Capital.append(cont["address"]["addressRegion"])

            print("\n\n\n finish \n\n\n")
        print(len(Lat), len(Long), url)


# ## Very important thing for amenity maps


# for element in new_amenity_map:
#     for key, value in element.items():
#         if value not in amenity_list:
#             amenity_map[key] = value
#             amenity_list.append(value)
#             print(f"New amenity added: {value}")

# print(amenity_list)
