# from bs4 import BeautifulSoup as bs 
# import requests
# import os


# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'} 


# def getTarget():
#     target = input("who do you want to instascrape?")
#     target_url = f'https://www.instagram.com/{target}/'
#     req = requests.get(target_url,stream = True, headers = headers)
#     req.raise_for_status
#     req.encoding = 'utf-8'
#     soup = bs(req.text,'html.parser')
#     suggested = soup.select('span')
#     print(suggested)

# def init():
#     getTarget()

# init()


#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json


class Insta_Info_Scraper:

    def getinfo(self, url):
        html = urllib.request.urlopen(url, context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'
                             })
        similar = soup.find('ul', class_ = 'YlNGR')
        text = data[0].get('content').split()
        user = '%s %s %s' % (text[-3], text[-2], text[-1])
        followers = text[0]
        following = text[2]
        posts = text[4]
        print ('User:', user)
        print ('Followers:', followers)
        print ('Following:', following)
        print ('Posts:', posts)
        print ('Similar:', similar)
        print ('---------------------------')

    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

        with open('users.txt') as f:
            self.content = f.readlines()
        self.content = [x.strip() for x in self.content]
        for url in self.content:
            self.getinfo(url)


if __name__ == '__main__':
    obj = Insta_Info_Scraper()
    obj.main()