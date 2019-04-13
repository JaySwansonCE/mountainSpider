import scrapy
import csv

class routeSpider(scrapy.Spider):

	links = []
	with open('data2.csv', 'r+') as f:
		newlist = list(csv.reader(f))
		for row in newlist:
			links.append(str(row))

	name = "areaScrape"
	allowed_domains = ['www.mountainproject.com']
	start_urls = ['https://www.mountainproject.com/area/107819791/beach-front-wall', 'https://www.mountainproject.com/area/106030487/the-betagraph', 'https://www.mountainproject.com/area/106210774/blacksmith-fork-canyon', 'https://www.mountainproject.com/area/107223329/cherry-creek-boulders', 'https://www.mountainproject.com/area/109202143/cherry-peak', 'https://www.mountainproject.com/area/105739662/china-wall', 'https://www.mountainproject.com/area/106455546/cliffs-of-insanity', 'https://www.mountainproject.com/area/108194413/crag-in-the-sky', 'https://www.mountainproject.com/area/106371925/date-wall', 'https://www.mountainproject.com/area/106018101/first-practice-wall', 'https://www.mountainproject.com/area/105739608/fucoidal-quartzite', 'https://www.mountainproject.com/area/108419946/green-canyon', 'https://www.mountainproject.com/area/113564484/green-canyon-bouldering', 'https://www.mountainproject.com/area/106789178/high-creek-canyon', 'https://www.mountainproject.com/area/107174245/hobbit-caves', 'https://www.mountainproject.com/area/105739440/kentucky-fried-penguin', 'https://www.mountainproject.com/area/107547979/margaritaville', 'https://www.mountainproject.com/area/106008969/mile-385-area', 'https://www.mountainproject.com/area/105739822/mini-pinacle', 'https://www.mountainproject.com/area/106018109/monkey-wrench-buttress', 'https://www.mountainproject.com/area/107159348/mullein-land', 'https://www.mountainproject.com/area/106835378/new-world', 'https://www.mountainproject.com/area/106821185/preston-valley-pinnacle', 'https://www.mountainproject.com/area/107515268/promised-land', 'https://www.mountainproject.com/area/109990799/providence-canyon', 'https://www.mountainproject.com/area/107747828/quality-cave', 'https://www.mountainproject.com/area/106657092/right-hand-fork', 'https://www.mountainproject.com/area/106593859/rodent-ranch', 'https://www.mountainproject.com/area/105739605/second-practice-wall', 'https://www.mountainproject.com/area/106736881/shocking-awe', 'https://www.mountainproject.com/area/106758070/skunk-caves', 'https://www.mountainproject.com/area/107743568/smith-rock', 'https://www.mountainproject.com/area/107594094/smithfield-dry-canyon', 'https://www.mountainproject.com/area/107465735/solar-cave', 'https://www.mountainproject.com/area/111849326/sound-show-wall', 'https://www.mountainproject.com/area/106192769/superbowl', 'https://www.mountainproject.com/area/110293231/tangent-wall', 'https://www.mountainproject.com/area/107793263/tidal-wave-cave', 'https://www.mountainproject.com/area/106835318/utopia', 'https://www.mountainproject.com/area/112333766/wall-of-colors', 'https://www.mountainproject.com/area/105739611/wall-of-illness', 'https://www.mountainproject.com/area/107194808/wall-of-jericho', 'https://www.mountainproject.com/area/107765467/the-waterfront']
	
	def parse(self, response):
		count_routes= len(response.xpath('//*[@id="left-nav-route-table"]/tr'))
		while count_routes > 0:
			yield {
					'area_name': response.xpath('//*[@id="single-area-picker-name"]/text()').extract_first(),
					'route_name': response.xpath('//*[@id="left-nav-route-table"]/tr[' + str(count_routes) + ']/td[2]/a/text()').extract(),
					'route_link': response.xpath('//*[@id="left-nav-route-table"]/tr[' + str(count_routes) + ']/td[2]/a/@href').extract_first()		
				}
			count_routes = count_routes - 1

#//*[@id="left-nav-route-table"]/tbody/tr[1]/td[2]/a
#//*[@id="climb-area-page"]/div/div[1]/h1/text()
#//*[@id="single-area-picker-name"]


# print('THIS IS Amount of routes: ' + str(count_routes))








