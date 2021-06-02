from bs4 import BeautifulSoup as bs 
import requests
import shutil
import os
import time


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'} 
url_endings = { '.com': 4, 
                '.org' : 4, 
                '.net' : 4, 
                '.kr' : 3 }
def urlCheck(url_endings):
    while True:
        url_raw = input("website address please?...")
        if url_raw.startswith('www'):
            url = 'https://'+url_raw
        else: url = url_raw 
        for ending in url_endings:
            if ending in url:
                base_url = url[:url.index(ending)+url_endings[ending]]
                print(base_url)
            else:
                pass
        if base_url:
            break
        else :
            pass
    return url, base_url            

def imgLinkGet(url, base_url):
    r = requests.get(url,stream = True, headers=headers)
    r.raise_for_status
    r.encoding = 'utf-8'
    soup = bs(r.text,'html.parser')
    img_links_raw = soup.select('img')
    print(img_links_raw)
    print(len(img_links_raw))
    img_links = []
    for img_link_raw in img_links_raw:
        if img_link_raw['src'].startswith('//'):
            img_link = 'https:'+ img_link_raw['src']
        elif img_link_raw['src'] == 'about:blank':
            pass
        elif img_link_raw['src'].startswith('/'):
            img_link = base_url + img_link_raw['src']
        else:
            img_link = img_link_raw['src']
        img_links.append(img_link)
    print(img_links)
    return img_links

def sourceChecker():
    source = input("who's image is this?")
    os.makedirs('scrpimg/{}'.format(source),exist_ok=True)
    return source


def imgDownloader(img_links, source):
    i = 1
    for link in img_links:
        img_response = requests.get(link,stream=True, headers=headers)
        print('saving from {}, as {}_{}'.format(link,source,str(i)))
        with open(f'scrpimg/{source}/{source}_{str(i)}{link[-4:]}','wb') as out_file:
            shutil.copyfileobj(img_response.raw,out_file)
        i += 1

def init():
    url, base_url = urlCheck(url_endings)
    img_links = imgLinkGet(url, base_url)
    source = sourceChecker()
    imgDownloader(img_links,source)

init()