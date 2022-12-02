import requests
import urllib.request
import os
import sys
from bs4 import BeautifulSoup

siteURL = sys.argv[1]
siteHTML = requests.get(siteURL)
siteSoup = BeautifulSoup(siteHTML.content, 'html.parser')
photos = siteSoup.find_all('a', 'fileThumb')
try:
    title = siteSoup.find('span', 'subject').text

    for photo in photos:
        photoURL = 'https:' + photo.attrs['href']
        photoName = photoURL.split('/')[-1]
        try: urllib.request.urlretrieve(photoURL, os.getcwd() + f'/{title}/{photoName}')
        except (NotADirectoryError, FileNotFoundError):
            if not os.path.exists(os.getcwd() + f'/{title}'): os.mkdir(os.getcwd() + f'/{title}')
        except: print('An Error Occurred'); break
except AttributeError: print('Invalid URL')
