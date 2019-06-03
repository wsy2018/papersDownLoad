import urllib.request
import requests
from bs4 import BeautifulSoup
import os
# https://dblp.uni-trier.de/db/journals/tnn/tnn30.html
def  getlist(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.content,'html.parser')
	soup2=soup.find_all('li', {"class": "entry article"})
	j = 1
	fp = open('list_tnn30.txt', 'w')
	for i in soup2:
	    s =i.find('a')['href']+'\n'
	    print(s)
	    fp.write(s)
	    j = j+1
	fp.close()
	return j

def createPath(path):
	if not os.path.exists(path):
		os.makedirs(path)
	return path

if __name__ == '__main__':
	url = "https://dblp.uni-trier.de/db/journals/tnn/tnn30.html"
	print('total:',getlist(url))
