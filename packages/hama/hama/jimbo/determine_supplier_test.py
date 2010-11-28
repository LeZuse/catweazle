"""TODO docstring"""

import unittest

from hama.jimbo.determine_supplier import determine_supplier

class UtilsTests5(unittest.TestCase):

    def test_determine_supplier(self):
        """Jimbo: determine_supplier"""
        cases = [
            (['00101330'], 'hama'),
            (['00004069'], 'hama')
            ]
        
        for case in cases:
            code = case[0]
            supplier = case[1]
            
            s = determine_supplier(code)[code[0]].supplier
            
            self.assertEquals(s, supplier)
