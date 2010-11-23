'''
testing all database utilities
'''

import unittest
from decimal import Decimal

from hama.databaseutils import Database
from sqlalchemy.orm import clear_mappers
class UtilsTests(unittest.TestCase):

    '''s'''
    def test_ddbb(self):
        '''s'''
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
