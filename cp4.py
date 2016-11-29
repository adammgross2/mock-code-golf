import BeautifulSoup
import urllib
import re
soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(u))
print sorted([m.match(str(x)).groups() for x in soup.findAll('li')], key= lambda x: x[1])
