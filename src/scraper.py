
import requests
from bs4 import BeautifulSoup
from book import Book


class Scraper():
      
    def __init__(self):
        self.url = 'https://www.casadellibro.com/libros/literatura/121000000'
          
    def __download_html(self, url):
        html = requests.get(url)
        soup = BeautifulSoup(html.content, 'html.parser')
        return soup
    
    def __get_titles(self, page):
        books = []
        divs = page.findAll('div')
        for div in divs:
            book = Book()
            try:
                if div['class'] == ['product__info']:
                    book.set_title(div.a.string.strip())
                    books.append(book)
            except Exception:
                pass
            
        return books
    
    def scrape(self):
        page = self.__download_html(self.url)
        titles = self.__get_titles(page)
        
        for book in titles:
            print(book)
        # print(page.prettify())
            

Scraper().scrape()