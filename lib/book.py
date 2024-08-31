#!/usr/bin/env python3

class Book:
    def __init__(self,title="And Then There Were None",page_count="272"):
        self.title = title
        self.page_count = page_count
        Book.turn_page(self)
    @property
    def title(self):
        return self._title    
    @title.setter
    def title(self, value):
        self._title = value
    @property
    def page_count(self):
        return self._page_count
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int) and (page_count > 0):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    def turn_page(self):
        self.current_page = 69
        print("Flipping the page...wow, you read fast!")
            
        
    
        