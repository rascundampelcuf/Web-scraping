
class Book(object):
    
    def __init__(self):
        self._title = ''    
        self._authors = ''    
        self._rate = ''        
        self._bookType = '--'
        self._price = '--'
        self._availability = ''
    
    def __str__(self):
        return 'Book({}, {}, {}, {}, {}, {})'.format(self._title, self._authors, self._rate, self._availability, self._bookType, self._price)
    
    def __repr__(self):
        return str(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
        
    @property
    def authors(self):
        return self._author
    
    @authors.setter
    def authors(self, authors):
        self._authors = authors
        
    @property
    def rate(self):
        return self._rate
        
    @rate.setter
    def rate(self, rate):
        self._rate = rate
        
    @property
    def bookType(self):
        return self._bookType
        
    @bookType.setter
    def bookType(self, bookType):
        self._bookType = bookType
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price
        
    @property
    def availability(self):
        return self._availability
    
    @availability.setter
    def availability(self, availability):
        self._availability = availability
        
    def get_list(self):
        return [self._title, self._authors, self._rate, self._availability, self._bookType, self._price]
