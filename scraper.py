

import requests
from bs4 import BeautifulSoup
import csv

def load_page(url):
	with requests.get(url) as f:
		page = f.text
	return page

list_ids = ['LDC96S57','LDC96S58','LDC98S70','LDC98S74','LDC98T27','LDC98T29','LDC99T41','LDC2000T51','LDC2001S91','LDC2001T60','LDC2001T61','LDC2002S25','LDC2003T04','LDC2005S26','LDC2006S31','LDC2006S35','LDC2006S37','LDC2006T12','LDC2008L03','LDC2008S05','LDC2009S04','LDC2009S05','LDC2009T21','LDC2009T25','LDC2010S01','LDC2010T04','LDC2011S01','LDC2011S04','LDC2011S05','LDC2011S07','LDC2011S10','LDC2011T12','LDC2012S01','LDC2012T01','LDC2012T03','LDC2012T10','LDC2012T12','LDC2013T06','LDC2014S05','LDC2014S06','LDC2014S08','LDC2014T18','LDC2014T23','LDC2015L01','LDC2015S07','LDC2015T02','LDC2015T11','LDC2015T17','LDC2015T20','LDC2016S04','LDC2016T03','LDC2016T26','LDC2017S23','LDC2017T09','LDC2018S06','LDC2018S11','LDC2018S12','LDC2018T01','LDC2018T06','LDC2019S07','LDC2019T02','LDC2019T09','LDC2019T12','LDC2019T17','LDC2019T19','LDC2020S01','LDC2020T07','LDC2020T18','LDC2021S06','LDC2021S07','LDC2021T04','LDC2021T09']

#list_ids = ['LDC96S57', 'LDC96S58']

data = []

for id in list_ids:
	title = ''
	license = ''
	year = ''
	type = ''
	description = ''
	language=''
	url = 'https://catalog.ldc.upenn.edu/' + id
	raw_page = BeautifulSoup(load_page(url), 'lxml')

	even = raw_page.find_all(class_='even')#.find('em')#.text.strip()  # Link text
	odd = raw_page.find_all(class_='odd')
	elements = even + odd

	for e in elements:
		if e.find('em'):
			feature = e.find('em').text.strip()
			#print(feature)
			if feature == 'Item Name:':
				title = e.find_all('td')[1].text.strip()
				print(title)
			if feature == 'License(s):':
				license = e.find('a').text.strip()
				print(license)
			if feature == 'Member Year(s):':
				year = e.find_all('td')[1].text.strip()
				print(year)
			if feature == 'DCMI Type(s):':
				type = e.find_all('td')[1].text.strip()
				print(type)
			if feature == 'Language(s):':
				language = e.find_all('td')[1].text.strip()
				print(language)
			#if feature == 'Citation:':
			#	break

	ps = raw_page.find_all('p')
	for p in ps:
		paragraph = p.text.strip()
		description += ' ' + paragraph
	print(description)

	data.append({
		'url':url,
		'name': title,
		'license': license,
		'year':year,
		'type':type,
		'language':language,
		'description':description,
	})

print(data)

with open('output.csv', 'w', encoding='utf-8') as f:  # Open a csv file for writing
	fieldnames = ['url', 'name', 'license', 'year', 'type', 'language', 'description']  # These are the values we want to store
	writer = csv.DictWriter(f, delimiter=',', quotechar='"',  # Common quote character
							quoting=csv.QUOTE_NONNUMERIC,  # Make sure that all strings are quoted
							fieldnames=fieldnames
							)
	writer.writeheader()  # Create headers in our csv file

	for row in data:
		writer.writerow({k: v for k, v in row.items() if k in fieldnames})


