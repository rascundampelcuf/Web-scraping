
import requests
import csv
from bs4 import BeautifulSoup
from book import Book


class Scraper():
      
    def __init__(self):
        self.url = 'https://www.casadellibro.com/libros/literatura/121000000'
        self.books = []
          
    def __download_html(self, url):
        # Get data from url
        html = requests.get(url)
        # Convert HTML content to BeautifulSoup object
        soup = BeautifulSoup(html.content, 'html.parser')
        return soup
    
    def __get_title_from_book(self, book, text):
        # Get title from 'title' tag
        title = text.find('a', 'title').string.strip()
        book.set_title(title)
    
    def __get_authors_from_book(self, book, text):
        authors = text.findAll('div', 'authors')
        
    def __get_rating_from_book(self, book, text):
        # Get rating from 'rating' tag
        rating = text.find('div', 'rating')
        # Remove nested 'svg' tag to get the value
        [s.extract() for s in rating('svg')]
        try:
            rating = rating.string.strip()
        except Exception:
            rating = 'None'
        book.set_rate(rating)
    
    def __get_books(self, page):
        # Get books code from 'product__info' tag
        divs = page.findAll('div', 'product__info')
        for div in divs:            
            book = Book()
            self.__get_title_from_book(book, div)
            self.__get_authors_from_book(book, div)
            self.__get_rating_from_book(book, div)
            self.books.append(book)
    
    def scrape(self):
        page = self.__download_html(self.url)
        # titles = self.__get_titles(page)
        self.__get_books(page)
        # for book in self.books:
        #     print(book)
        # print(page.prettify())
            
    def data2csv(self, filename):
        # # Overwrite to the specified file.
        # # Create it if it does not exist.
        csvwriter = csv.writer(open("../data/" + filename, "w", newline='\n'))
        
        # # Dump all the data with CSV format
        csvwriter.writerow(['Title;Author;Rate;BookType;Price;Availability;'])
        for book in self.books:
            csvwriter.writerow([book.get_csv()])
            
            
output_file = "data.csv"
scraper = Scraper()
scraper.scrape()
scraper.data2csv(output_file)