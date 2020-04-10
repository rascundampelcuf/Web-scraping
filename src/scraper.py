
import csv
from book import Book
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

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
        WebDriverWait(self.driver, 15)        
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
        author = ''
        try:
            author = text.find_element_by_class_name('author').text.strip()
        except Exception:
            author = 'Not available'
        book.author = author
        
    def __get_rating_from_book(self, book, text):
        # Get rating from tag with 'rating' class
        rating = text.find_element_by_class_name('rating').text.strip()
        
        # If there is not rating -> rating = 'None'
        rating = rating if rating != '' else 'None'
        book.rate = rating
        
    def __get_book_availability(self, book, text):
        # Get availability from existance of tag with class 'type active'
        try:
            availability = bool(text.find_element_by_css_selector('div.type.active'))
        except Exception:
            availability = False        
        book._availability = availability
        
    def __get_type_from_book(self, book, text):
        # Get type from tag with class 'type-name'
        bookType = text.find_element_by_css_selector('div.type.active .type-name').text.strip()
        book.bookType = bookType
        
    def __get_price_from_book(self, book, text):
        # Get price from tag with class 'final-price'
        price = text.findAll('div', 'final-price')
        # book.price = price      
        # print(price)
    
    def __get_books(self):
        # Get books code from 'product__info' tag            
        divs = self.driver.find_elements_by_class_name('product__info')        
        
        for div in divs:            
            book = Book()
            self.__get_title_from_book(book, div)
            self.__get_authors_from_book(book, div)
            self.__get_rating_from_book(book, div)
            self.__get_book_availability(book, div)
            self.__get_price_from_book(book, div)
            self.books.append(book)
            print(book)
    
    def scrape(self):
        print('Web scraping of books by "Casa del Libro"...')
        page_num = 1
        # while (self.status_code == 200):
        print('Scraping page ' + str(page_num))
        self.__set_driver(self.url + self.path + str(page_num))
        self.__get_books()
            # if page_num % 100 == 0:
                # self.data2csv()
            # page_num += 1
        self.__quit_driver()
        # self.data2csv()
        
        # for book in self.books:
        #     print(book)
        # print(page.prettify())
            
    def data2csv(self):        
        # Dump all the data with CSV format        
        for book in self.books:
            self.csvwriter.writerow(book.get_list())
        self.books.clear()
        
    def test(self):      
        driver = webdriver.Chrome()
        driver.get(self.url + self.path)
        WebDriverWait(driver, 0)
        books = driver.find_elements_by_class_name('type-price')
        for book in books:
            print("-{}-".format(book.text.strip()))

        driver.quit()
        # try:
        #     element = WebDriverWait(driver, 60)#.until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
        #     driver.find_element_by_class_name('product__info')
        # finally:
        #     driver.quit()
            
scraper = Scraper()
scraper.scrape()
# scraper.test()