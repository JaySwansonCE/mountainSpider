import scrapy
import csv

class routeSpider(scrapy.Spider):
	name = "areaScrape"
	allowed_domains = ['www.mountainproject.com']

	def start_requests(self):
		with open('data2.csv', 'rt') as allLinks:
			allLinks = csv.reader(allLinks)
			for link in allLinks:
				url = str(*link)
				yield scrapy.Request(url, self.parse)
	
	def parse(self, response):
		count_routes= len(response.xpath('//*[@id="left-nav-route-table"]/tr'))
		while count_routes > 0:
			yield {
					'area_name': response.xpath('//*[@id="single-area-picker-name"]/text()').extract_first(),
					'route_name': response.xpath('//*[@id="left-nav-route-table"]/tr[' + str(count_routes) + ']/td[2]/a/text()').extract(),
					'route_link': response.xpath('//*[@id="left-nav-route-table"]/tr[' + str(count_routes) + ']/td[2]/a/@href').extract_first()		
				}
			count_routes = count_routes - 1







