import scrapy
import csv

class routeSpider(scrapy.Spider):
	name = "areaScrape"
	allowed_domains = ['www.mountainproject.com']

	#def __init__(self):
	#	self.uniqueRouteIds = []

	def start_requests(self):
		with open('data3.csv', 'rt') as allLinks:
			allLinks = csv.reader(allLinks)
			for link in allLinks:
				url = str(*link)
				#self.uniqueRouteIds.append(url[38:46])
				yield scrapy.Request(url, self.parse)

	def parse(self, response):
		uniqueId = response.request.url[38:47]
		count_stars= len(response.xpath('//*[@id="starsWithAvgText-' + str(uniqueId) + '"]/span/img'))
		#I COULD PROBABLY DO A HEADING SEARCH FOR DESCRIPTION, PROTECTION AND LOCATION ALL IN ONE?
		descriptionString = ""
		descriptionArray = [3, 2]
		for i in descriptionArray:
			if response.xpath('//*[@id="route-page"]/div/div[3]/div[1]/div[' + str(i) + ']/div[1]/h2/text()').extract_first() == ("\n            Description\n            "):
				descriptionString = response.xpath('//*[@id="route-page"]/div/div[3]/div[1]/div[' + str(i) + ']/div[1]/div/text()').extract_first()
		protectionString = ""
		protectionArray = [3, 2]
		protectionArray2 = [3, 2]
		for i in protectionArray:
			for j in protectionArray2:
				if response.xpath('//*[@id="route-page"]/div/div[3]/div[1]/div[' + str(i) + ']/div[' + str(j) + ']/h2/text()').extract_first() == ("\n            Protection\n            "):
					protectionString = response.xpath('//*[@id="route-page"]/div/div[3]/div[1]/div[' + str(i) + ']/div[' + str(j) + ']/div/text()').extract_first()

		routeString = response.xpath('//*[@id="route-page"]/div/div[1]/h1/text()').extract_first()
		climbTypeNHeightString = response.xpath('//*[@id="route-page"]/div/div[3]/div[1]/div[1]/div[1]/table//tr[1]/td[2]/text()').extract_first()
		
		#pulls then converts the First Ascent list into a string
		faList = response.xpath('//*[@id="route-page"]/div/div[3]/div[1]/div[1]/div[1]/table//tr[2]/td[2]/text()').extract()
		faString = ''.join(str(e) for e in faList)

		yield {
				'area_name': response.xpath('//*[@id="route-page"]/div/div[1]/div[2]/a[5]/text()').extract_first(),
				'route_name': routeString.replace('\n', '')[8:],
				'yds_rating': response.xpath('//*[@id="route-page"]/div/div[1]/h2/span[1]/text()').extract_first(),
				'user_rating': count_stars,
				'climb_type_and_height': climbTypeNHeightString.replace('\n', '')[40:],
				'first_ascent': faString.replace('\n', '')[40:],
				'description': descriptionString,
				'protection': protectionString,
			}






