'''
testing all database utilities
'''

import unittest
from decimal import Decimal

from hama.databaseutils import Database
from sqlalchemy.orm import clear_mappers

class DatabaseUtilsTests(unittest.TestCase):
    def test_db_read(self):
        database = Database()
        products = [
            ('00101300', 
            '''aha Netbook Messenger, vertical, display sizes up to 26 cm (10.2")''',
            Decimal('11.41'))           
            ]
        
        for product in products:
            product_code = product[0]
            product_name = product[1]
            

            self.assertEquals(database[product_code].product_name, product_name)
            
            clear_mappers()

class DatabasePriceTests(unittest.TestCase):            
    def test_db_add_price(self):
        database = Database()
        product = database['00101300']
        prices = product.prices
        
        old_prices_lenght = len(prices)
        product.prices.add(1, 55, 66)
        new_prices_lenght = len(prices)
        

        self.assertEquals(new_prices_lenght, old_prices_lenght + 1)        
        self.assertRaises(AssertionError, prices.add, 1, 55, 66)

        
        clear_mappers()             
