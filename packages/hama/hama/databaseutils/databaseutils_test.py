'''
testing all database utilities
'''

import unittest

from hama.databaseutils import Database
from sqlalchemy.orm import clear_mappers
class UtilsTests(unittest.TestCase):

    '''s'''
    def test_ddbb(self):
        '''s'''
        database = Database()
        products = [
            ('00101300', '''aha Netbook Messenger, vertical, display sizes up to 26 cm (10.2")''')
            ]
        
        for product in products:
            product_code = product[0]
            product_name = product[1]
            self.assertEquals(database[product_code].product_name, product_name)
            clear_mappers()
            
class UtilsTests2(unittest.TestCase):            
    def test_cccc(self):
        '''d'''
        database = Database() 
        products = [
            ('00101300', '''ah Netbook Messenger, vertical, display sizes up to 26 cm (10.2")''')
            ]
        
        for product in products:
            product_code = product[0]
            product_name = product[1]
            self.assertEquals(database[product_code].product_name, product_name)
            clear_mappers()