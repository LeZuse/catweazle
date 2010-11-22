#!/usr/bin/python

import unittest

from hama.databaseutils import Database

class UtilsTests(unittest.TestCase):
    def test_ddbb(self):
          d = Database()
          
          self.assertEquals(d['00101300'].product_name, '''aha Netbook Messenger, vertical, display sizes up to 26 cm (10.2")''')
          
