#!/usr/bin/python

import unittest

from hamacase import hama_case

class UtilsTests(unittest.TestCase):
    def test_hama_case(self):
          self.assertEquals(hama_case('ee'), 'Ee')