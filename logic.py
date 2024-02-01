"""
Note from Author:
    Hey there! For that one person that might be seeing this, thanks for checking
    my work out. I had a blast making this game, or whatever you might call this.
    This is mainly for my own use. I play a game called Geoguessr where you need 
    to guess the location of a place. Knowing what languages look like in written
    form is a huge bonus. Feel free to use it and let me know. 
                                                                    - theSupreme
"""

"""
Context:
    This file contains all the request and parsing logic for the app. I am using
    BeautifulSoup to scrape data off wikipedia, which is then shown to the user 
    to guess the language.
"""
# all the necessary imports
import requests
import random
from data import languages
from bs4 import BeautifulSoup

# function to retrieve data from wikipedia
def get_info():

    # try block because it throws exceptions all the time
    try:
        # choosing a random langauge from the list in the other file
        lang = languages[random.randint(0, len(languages) - 1)]

        # url that requests a random article with our language
        url = "https://" + lang + ".wikipedia.org/wiki/Special:Random"

        # parsing the response
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # storing all the paragraphs into a list
        paragraphs = soup.find_all('p')
        
        # choosing the first paragraph to display
        '''
        Sometimes it only contains a new line character which breaks the game.
        To counter that, I had a loop that ran through each index of the list
        until it finds a paragraph which is not empty. It still wasn't working
        so I reverted back to the first paragraph.
        '''
        the_question = paragraphs[0].text

        # returns the question and the current language 
        return [the_question, lang]

    # catching the exception when it happens
    except Exception as e:
        print('Exception has occured')

# a method that verifies if the response if empty, in which case
# calls the request fucntion again
def get_page():
    info = get_info()

    while info is None:
        info = get_info()
    
    return info