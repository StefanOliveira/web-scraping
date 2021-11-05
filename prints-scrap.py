from bs4 import BeautifulSoup
import urllib.request as urllib_request

import requests

html = requests.get("http://10.1.20.14/info_configuration.html?tab=Home&menu=DevConfig").content

soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

totaisImpressos = soup.find("td", attrs={'class': 'itemFont'})
 
totaisImpressos = totaisImpressos.text.strip()

print(totaisImpressos)