
import csv
import time
from book import Book
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class Scraper():
      
    def __init__(self):
        # self.url = 'https://www.casadellibro.com/libros/literatura/121000000/p'
        self.url = 'https://www.casadellibro.com/libros/literatura/narrativa-en-bolsillo/ciencia-ficcion-en-bolsillo/121005001/p'
        self.books = []
        self.status_code = 200
        self.csvwriter = csv.writer(open("../data/data.csv", "w", newline='\n', encoding="utf-8"), delimiter=';')
        self.csvwriter.writerow(['TITLE', 'AUTHOR', 'RATE', 'AVAILABILITY', 'BOOKTYPE', 'PRICE'])
        self.driver = webdriver.Chrome()
          
    def __set_driver(self, url):
        # Get data from url
        self.driver.get(url)
        try:
            time.sleep(20)
            WebDriverWait(self.driver, 3)
        except TimeoutException:
            pass
        if "404" in self.driver.title:
            self.status_code = 404
    
    def __quit_driver(self):
        self.driver.quit()
    
    def __get_title_from_book(self, book, text):
        # Get title from tag with class 'title'
        title = text.find_element_by_class_name('title').text.strip()
        book.title = title
        
    def __get_authors_from_book(self, book, text):
        # Get author from tag with class 'author'
        authors = 'Not available'
        try:
            authors = text.find_elements_by_class_name('author')
            authors = [author.text.strip() for author in authors]
        except Exception:
            pass
        book.authors = authors
        
    def __get_rating_from_book(self, book, text):
        # Get rating from tag with 'rating' class
        rating = text.find_element_by_class_name('rating').text.strip()
        
        # If there is not rating -> rating = 'None'
        rating = rating if rating != '' else 'None'
        book.rate = rating
        
    def __get_book_availability(self, text):
        # Get availability from existance of tag with class 'type active'
        availability = False
        try:
            availability = bool(text.find_elements_by_class_name('type-name'))
        except Exception:
            pass
        return availability
        
    def __set_book_availability(self, book, availability):
        book.availability = availability
    
    def __set_type_for_book(self, book, _type):        
        book.bookType = _type
        
    def __set_price_for_book(self, book, _price):
        # First element in list is the original price, and we want to get the price with discount
        price = _price[:-1].strip().replace(',', '.')
        book.price = float(price)
    
    def __get_booktypes(self, text):
        types = text.find_elements_by_css_selector('div.types')
        # Get type from tag with class 'type-name'
        btypes = types[0].find_elements_by_class_name('type-name')
        btypes = [t.text.strip() for t in btypes if t.text]
        
        # Get price from tag with class 'type-price'
        bprices = types[0].find_elements_by_class_name('type-price')
        bprices = [p.text.strip() for p in bprices if p.text]
        
        types = list(zip(btypes, bprices))
        return types
    
    def __get_books(self):
        # Get books code from 'product__info' tag
        divs = self.driver.find_elements_by_class_name('product__info')
        for div in divs:
            availability = self.__get_book_availability(div)
            # If book is not available just save title, author and rating
            if not availability:
                book = Book()
                self.__get_title_from_book(book, div)
                self.__get_authors_from_book(book, div)
                self.__get_rating_from_book(book, div)
                self.__set_book_availability(book, availability)
                self.books.append(book)                
            else:
                # If book is available save a book with the info for each type
                types = self.__get_booktypes(div)
                for _type, _price in types:
                    book = Book()
                    self.__get_title_from_book(book, div)
                    self.__get_authors_from_book(book, div)
                    self.__get_rating_from_book(book, div)
                    self.__set_book_availability(book, availability)
                    self.__set_type_for_book(book, _type)
                    self.__set_price_for_book(book, _price)
                    self.books.append(book)
                    
    def __data2csv(self):        
        # Dump all the data with CSV format        
        for book in self.books:
            self.csvwriter.writerow(book.get_list())
        self.books.clear()
    
    def scrape(self):
        print('Web scraping of books by "Casa del Libro"...')
        page_num = 1
        while (self.status_code == 200):
            print('Scraping page ' + str(page_num))
            self.__set_driver(self.url + str(page_num))
            self.__get_books()
            # if page_num % 100 == 0:
                # self.data2csv()
            page_num += 1
        self.__quit_driver()
        self.data2csv()
        
        # for book in self.books:
        #     print(book)
        # print(page.prettify())
            
    def data2csv(self):        
        # Dump all the data with CSV format        
        for book in self.books:
            self.csvwriter.writerow(book.get_list())
        self.books.clear()
            
scraper = Scraper()
scraper.scrape()