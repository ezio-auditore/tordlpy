#!/usr/bin/env python

import urllib
import sys
import requests
from BeautifulSoup import BeautifulSoup
from sys import argv
import os.path
movie,category=argv[1],argv[2]
def make_link(movie_name, category):
    return ('http://kickass.to/usearch/%22'+movie+'%22%20category:'+category)



def gettor(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    del response
    for movie in soup.findAll('div', attrs={'class' : 'iaconbox floatright'}): 
        for link in movie.findAll('a',attrs={'class' : 'idownload icon16'}):
            download_file(link.get('href'))

def download_file(url):
    urllib.urlretrieve(url, "%s.torrent" %movie)
    choice = raw_input('Was that appropriate? ')
    if 'y' in choice:
        sys.exit(0)

if __name__ == '__main__':
    link = make_link(movie, category)
    gettor(link)
