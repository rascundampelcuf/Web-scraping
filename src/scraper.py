
import requests
from bs4 import BeautifulSoup


class Scraper():
      
      def __init__(self):
            self.url = 'https://www.casadellibro.com/libros/literatura/121000000'
          
      def __download_html(self, url):
            html = requests.get(url)
            soup = BeautifulSoup(html.content, 'html.parser')
            return soup
    
      def scrape(self):
            page = self.__download_html(self.url)
            
            print(page.prettify())
            

Scraper().scrape()