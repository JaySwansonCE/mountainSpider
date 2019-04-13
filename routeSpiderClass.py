import scrapy
import csv

class routeSpider(scrapy.Spider):

	links = []
	with open('data2.csv', 'r+') as f:
		newlist = reversed(list(csv.reader(f)))
		for row in newlist:
			links.append(row)
			print(row)


	name = "route"
	allowed_domains = ['www.mountainproject.com']
	start_urls = ['https://www.mountainproject.com/area/106030487/the-betagraph']

	def parse(self, response):
		count_areas= len(response.xpath('//*[@id="climb-area-page"]/div/div[2]/div/div[3]/div'))
		print('THIS IS Amount of areas: ' + str(count_areas))
		while count_areas > 0:
	
			yield {
					'route_link': response.xpath('//*[@id="climb-area-page"]/div/div[2]/div/div[3]/div[' + str(count_areas) + ']/a/@href').extract_first()
				}
			count_areas = count_areas - 1














