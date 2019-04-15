#This is an attempt to do fix the problem that all the areas and routes aren't on the same level


import scrapy
import csv

class routeSpider(scrapy.Spider):
	name = "areaRecursion"
	allowed_domains = ['www.mountainproject.com']

	def __init__(self):
		self.area_links = ['https://www.mountainproject.com/area/105739310/logan',]
		self.route_links = []

	def start_requests(self):
		for link in self.area_links:
			#url = str(*link)
			yield scrapy.Request(link, self.parse)

	def parse(self, response):
		count_areas= len(response.xpath('//*[@id="climb-area-page"]/div/div[2]/div/div[3]/div'))
		print('THIS IS Amount of areas: ' + str(count_areas))
		while count_areas > 0:
			link2area = response.xpath('//*[@id="climb-area-page"]/div/div[2]/div/div[3]/div[' + str(count_areas) + ']/a/@href').extract_first()
			self.area_links.append([link2area])
			count_areas = count_areas - 1
		for i in self.area_links:
			print (i)

	def start_requests2(self):
		print ("even here?")
		for link in self.area_links:
			yield scrapy.Request(link, self.parse2)

	def parse2(self, response):
		count_areas= len(response.xpath('//*[@id="climb-area-page"]/div/div[2]/div/div[3]/div'))
		print('THIS IS Amount of areas: ' + str(count_areas))
		while count_areas > 0:
			link2area = response.xpath('//*[@id="climb-area-page"]/div/div[2]/div/div[3]/div[' + str(count_areas) + ']/a/@href').extract_first()
			if 'area' in link2area:
				self.area_links.append([link2area])
			elif 'route' in link2area:
				self.route_links.append([link2area])
			count_areas = count_areas - 1
		print ("AREA LINKS:")
		for i in self.area_links:
			print (i)
		print ("ROUTE LINKS:")
		for i in self.route_links:
			print (i)



#//*[@id="left-nav-route-table"]/tbody/tr/td[2]/a
#//*[@id="left-nav-route-table"]/tbody/tr[1]/td[2]/a
#//*[@id="climb-area-page"]/div/div[2]/div/div[3]



