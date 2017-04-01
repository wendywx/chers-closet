import scrapy
import csv

class NordstromSpider(scrapy.Spider):
    name = "nordstrom"

    def start_requests(self):
        # file with list of csv names and put the following in a for loop
        with open('csvlist.csv', 'r') as acsv:
            areader = csv.reader(acsv)
            for onecsv in areader:
                with open(onecsv, 'r') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        urls += row

        for url in urls:
            print("WE DONT WANT THIS SHIT---------------")
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        acceptedattrib =["averageRating", "brandName", "basePrice", "color", "productID", "productName", "gender", "productType", "productParentType"]
        #properties
        properties = response.css('script::text')[1].extract()
        #gets the image url in list form
        image = response.css('meta[property*="og:image"]::attr(content)').extract()
        imageurl = image[0]

        print('PRINTING PROPERTIES!!!-----------------------')
        count = 0
        countagain = 0

        datafile = open('data.txt','a') 
 
        for e in properties.split("{"):
            count += 1
            if(count is 5):
                attributes = e.split(",")
                for elem in attributes:
                    attr = elem.split(":")
                    countagain += 1
                    category = attr[0][1:-1]
                    data = attr[1]
                    #print(str(countagain) + category +" is " + data)
                    if category in acceptedattrib:
                        datafile.write(data +  ",")
        datafile.write(imageurl + "\n")


        print("PRINTING IMAGE-------------------------")
        print(image)


#spider = NordstromSpider()
#responses = spider.start_requests()
#for response in responses:
#    spider.parse(response)