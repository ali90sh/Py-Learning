# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

from bidi.algorithm import get_display
import arabic_reshaper

divar = requests.get("https://divar.ir/s/iran")
soup = BeautifulSoup(divar.text, 'html.parser')

main = soup.find('main')
for link in main.find_all('a'):
    spans = link.find_all('span')
    for span in spans:
        if 'نردبان' in span.text:
            topic = (link.find('h2')).text
            shaped_topic = arabic_reshaper.reshape(topic)
            print(get_display(shaped_topic))
            
