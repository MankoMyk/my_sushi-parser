from bs4 import BeautifulSoup
import requests
import csv

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

try:
  # pageNumber = str(1)
  url = "https://list.in.ua/Івано-Франківськ/Суші/page/1"
  req = requests.get(url, headers)
  print (req)
  url = "https://list.in.ua/%D0%86%D0%B2%D0%B0%D0%BD%D0%BE-%D0%A4%D1%80%D0%B0%D0%BD%D0%BA%D1%96%D0%B2%D1%81%D1%8C%D0%BA/%D0%A1%D1%83%D1%88%D1%96/page/1"
  req = requests.get(url, headers)
  print (req)
  url = "https://thewhiskylist.com.au/distilleries/australia/wa"
  req = requests.get(url, headers)
  print (req)
  # soup = BeautifulSoup(req.content, 'html.parser')
  # divs = soup.find_all('div', {'class': 'item-search row js-load-business-container'})
  # with open('out.csv', 'w', newline='') as csvfile:
  #   header = ['Name', 'Adress', 'Phone', 'Email', 'Website',]
  #   data = ["", "", "", "", ""]
  #   writer = csv.writer(csvfile, dialect='excel')
  #   writer.writerow(header)
  #   for div in divs:
  #     # if div.a:
  #       data[0] = div.a['href']
  #       writer.writerow(data)
  #       # writer.writerow([div.a['href'],div.img['src']])
except Exception as ex:
  print(ex)
