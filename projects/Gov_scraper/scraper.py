import requests
from bs4 import BeautifulSoup as bs

fundings_dict = {}



r_raw = requests.get("https://www.bizinfo.go.kr/see/seea/selectSEEA100.do").text

if r_raw:
    soup = bs(r_raw, 'html.parser')
    table_raw = soup.find('tbody').find_all("td", {'class' : 'txtAgL'})

for funding in table_raw:
    funding_name = funding.find('a')['title']
    url_code_raw = funding.find('a')['onclick']
    url_code = url_code_raw.split("'")[1]
    inner_url = f"https://www.bizinfo.go.kr/see/seea/selectSEEA140Detail.do?pblancId={url_code}"
    funding_attr = [funding_name, inner_url]
    fundings_dict[funding_name]  = funding_attr

print(fundings_dict)



