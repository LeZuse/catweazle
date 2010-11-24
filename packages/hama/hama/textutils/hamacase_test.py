"""TODO docstring"""

import unittest

from hama.textutils.hamacase import hama_case

class UtilsTests(unittest.TestCase):
    """TODO docstring a"""
    def test_hama_case(self):
        """Capitalisation"""
        cases = {
            'ee': 'Ee',
            'seven or more': 'Seven or More'
            }
        
        for key in cases:
            self.assertEquals(hama_case(key), cases[key])