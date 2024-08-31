#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand="Adidas", size=9):
        self.brand = brand
        self.size = size
        Shoe.cobble(self)
        self.condition = "New"
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            print("brand must be a string") 
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if isinstance(size, int) and (size > 0):
            self._size = size
        else:
            print("size must be an integer")
              
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
   