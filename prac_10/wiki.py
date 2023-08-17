"""
CP1404
Prac 10
Wikipedia API
"""

import wikipedia

page_title = input("Page title or Search phrase: ")
while page_title != "":
    try:
        wikipedia_page = wikipedia.page(title=page_title, auto_suggest=False)
        print(wikipedia_page.title)
        print(wikipedia_page.summary)
        print(wikipedia_page.url)
    except wikipedia.exceptions.DisambiguationError as error:
        print(error.options)
    page_title = input("Page title or Search phrase: ")
