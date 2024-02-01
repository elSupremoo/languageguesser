"""
Note from Author:
    Hey there! For that one person that might be seeing this, thanks for checking
    my work out. I had a blast making this game, or whatever you might call this.
    This is mainly for my own use. I play a game called Geoguessr where you need 
    to guess the location of a place. Knowing what languages look like in written
    form is a huge bonus. Feel free to use it and let me know 
"""

import requests
import random
from data import languages
from bs4 import BeautifulSoup

def get_info():

    try:

        lang = languages[random.randint(0, len(languages) - 1)]
        url = "https://" + lang + ".wikipedia.org/wiki/Special:Random"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        
        answer = paragraphs[0].text

        return [answer, lang]

    except Exception as e:
        print('Exception has occured')

def get_page():
    info = get_info()

    while info is None:
        info = get_info()
    
    return info