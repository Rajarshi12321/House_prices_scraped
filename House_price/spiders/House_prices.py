import scrapy
from pathlib import Path
import json
# import string


class HousePricesSpider(scrapy.Spider):
    name = 'House_prices'

    def start_requests(self):
        urls = [
            "https://www.magicbricks.com/propertyDetails/3-BHK-2390-Sq-ft-Multistorey-Apartment-FOR-Rent-Rajaji-Nagar-in-Bangalore&id=4d423636393636313331",
            # "https://www.magicbricks.com/property-for-rent/residential-real-estate?bedroom=&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Service-Apartment&cityName=Kolkata",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # page = response.url.split("=")[-1]
        # filename = f"houses-{page}.html"

        # cards = response.css(".mb-srp__card")

        # print("\n\n\n {no} \n\n\n".format(no=len(cards)))

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

        fn = f"hellobro.json"
        Path(fn).write_text(dictionary_string, encoding='utf-8')

        print("\n\n\n bye \n\n\n ")

        # url = []
        # NoRooms = []
        # Lat = []
        # Long = []
        # Locality = []
        # Capital = []

        # for content in contents:
        #     # print(type(contents))
        #     # print("\n\n\n hey \n\n\n ")
        #     # print(type(json.loads(content)))
        #     # print("\n\n\n bye \n\n\n")

        #     cont = json.loads(content)
        #     print(cont["geo"])

        #     url.append(cont["url"])
        #     NoRooms.append(cont["numberOfRooms"])
        #     Lat.append(cont["geo"]["latitude"])
        #     Long.append(cont["geo"]["longitude"])
        #     Locality.append(cont["address"]["addressLocality"])
        #     Capital.append(cont["address"]["addressRegion"])

        #     print("\n\n\n finish \n\n\n")
        # print(len(Lat), len(Long), url)

    def parse_list(self, response):
        page = response.url.split("=")[-1]
        filename = f"houses-{page}.html"

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
