import requests
from bs4 import BeautifulSoup
import re

url = 'http://www.cbe.org.eg/en/EconomicResearch/Statistics/Pages/OfficialRatesListing.aspx'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
body = soup.find('div', {'class':'inner-content-inner'})

# date of data
date = body.find('div', {'id':'WebPartWPQ2'}).find('h2').contents
date = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', str(date))
date = {"date": date[0]}

# data content
table = body.find('table', {'class':'table'})
results = []
results.append(date)
for n, i in enumerate(table.findAll('tr')):
    j = i.find_all('td')
    if len(j) == 0:
        continue
    else:
        data = {
            "num" : n,
            "curr" : j[0].text,
            "buy" : j[1].text,
            "sell" : j[2].text
            }
        results.append(data)
print(results)

