import scrapy

class areaSpider(scrapy.Spider):
	name = "areas"
	allowed_domains = ['www.mountainproject.com']
	start_urls = ['https://www.mountainproject.com/area/105739310/logan',]

	def parse(self, response):
		count_areas= len(response.xpath('//*[@id="climb-area-page"]/div/div[2]/div/div[3]/div'))
		print('THIS IS Amount of areas: ' + str(count_areas))
		while count_areas > 0:
			yield {
					'area_link': response.xpath('//*[@id="climb-area-page"]/div/div[2]/div/div[3]/div[' + str(count_areas) + ']/a/@href').extract_first()
				}
			count_areas = count_areas - 1