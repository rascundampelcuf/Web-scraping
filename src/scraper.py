
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
            
    def __get_title_from_book(self, book, text):
        title = text.findAll('a', 'title')[0].string
        book.set_title(title)
        
    def __get_rating_from_book(self, book, text):
        rating = text.findAll('div', 'rating')
        [s.extract() for s in rating[0]('svg')]
        try:
            rating = rating[0].string.strip()
        except Exception:
            rating = 'None'
        book.set_rate(rating)
        return books
    
    def scrape(self):
        page = self.__download_html(self.url)
        titles = self.__get_titles(page)
        
        for book in titles:
            print(book)
        # print(page.prettify())
            

Scraper().scrape()