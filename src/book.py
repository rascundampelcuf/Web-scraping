
class Book(object):
    
    def __init__(self):
        self.title = ''    
        self.author = ''    
        self.rate = ''        
        self.bookType = ''
        self.price = ''
        # self.category = ''
        # self.link = ''
    
    def __str__(self):
        return 'Book({}, {})'.format(self.title, self.author)
    
    def get_title(self):
        return self.title
    
    def set_title(self, value):
        self.title = value
        
    def get_author(self):
        return self.author
    
    def set_author(self, value):
        self.author = value
        
    def get_rate(self):
        return self.rate
        
    def set_rate(self, value):
        self.rate = value
        
    def get_bookType(self):
        return self.bookType
        
    def set_bookType(self, value):
        self.bookType = value
        
    def get_price(self):
        return self.price
    
    def set_price(self, value):
        self.price = value
        
    # def get_category(self):
    #     return self.category
    
    # def set_category(self, value):
    #     self.category = value    
    
    # def get_link(self):
    #     return self.link
    
    # def set_link(self, value):
    #     self.link = value
        