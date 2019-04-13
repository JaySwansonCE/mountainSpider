import csv

def reverseCsv():
	results = []
	with open('data2.csv', 'w') as newNew:
		with open('data1.csv', 'r+') as f:
			newlist = reversed(list(csv.reader(f)))
			writer = csv.writer(newNew)
			for row in newlist:
				results.append(row)
			del results[-1]
			for row in results:
				writer.writerows([row])
reverseCsv()

#Reverses csv and deletes area name