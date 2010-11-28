""" Testing all database utilities."""

import unittest
from decimal import Decimal

from hama.databaseutils import Database

DATABASE = Database()

class DatabaseTests(unittest.TestCase):
    """ Tests for the Database class """    

    def test_db_read(self):
        """ Database::Product: reading products """
        
        products = [
        ('00101300', 
        'aha Netbook Messenger, vertical, display sizes up to 26 cm (10.2")',
        Decimal('11.41'))           
        ]
        
        for product in products:
            product_code = product[0]
            product_name_test_case = product[1]
            product_name_in_database = DATABASE[product_code].product_name
            
            self.assertEquals(product_name_in_database, product_name_test_case)
 
 
            
class PriceContainerTests(unittest.TestCase):
    """ Tests for the PriceContainer class """    
    
    def test_add_price(self):
        """ Database::Price: adding prices """
        product = DATABASE['00101300']
        prices = product.prices
        price = product.prices.add(1, 55, 66)
        
        self.assertEquals((1, 55) in product.prices, True)      
        self.assertRaises(AssertionError, prices.add, 1, 55, 66)
        self.assertEquals(price in DATABASE.session.new, True)



class PriceTests(unittest.TestCase):
    """ Tests for the Price class """  
    
    def test_modify_price(self):
        """ Database::Price: modifying prices """
        product = DATABASE['00101300']
        price = product.prices[2, 24]        
        price.price_value = 7.99
        self.assertEquals(price in DATABASE.session.dirty, True)


    def test_delete_price(self):
        """ Database::Price: removing prices """
        product = DATABASE['00101300']
        price = product.prices[2, 24]        
        price.delete()
        
        self.assertEquals(price in DATABASE.session.deleted, True)
        
        DATABASE.session.rollback()
        
    def test_type(self):
        """ Database::Price: price type """
        prices = [
            ('00101300', (1, 1), 'INV'),
            ('00101300', (2, 24), 'MIX')
            ]
        
        for price_test_case in prices:  
            product = DATABASE[price_test_case[0]]
            price = product.prices[price_test_case[1]]
            price_type_test_case = price_test_case[2]
            price_type_database = price.type
            self.assertEquals(price_type_database, price_type_test_case)


    def test_set_minimum_qty(self):
        """ Database::Price: set minimum qty """
        product = DATABASE['00101300']
        price = product.prices[2, 24]
        price.set_minimum_qty(12)
        
        self.assertEquals((2, 12) in product.prices, True)
        self.assertEquals((2, 24) not in product.prices, True)
        
        price.set_minimum_qty(24)
        

    def test_set_price_type_id(self):
        """ Database::Price: set price type id """
        product = DATABASE['00101300']
        price = product.prices[2, 24]
        price.set_price_type_id(3)
        
        self.assertEquals((3, 24) in product.prices, True)
        self.assertEquals((2, 24) not in product.prices, True)
        
        price.set_price_type_id(2)
