"""TODO docstring"""
#!/usr/bin/python

import unittest

from hama.textutils.hamacase import hama_case

class UtilsTests(unittest.TestCase):
    """TODO docstring"""
    def test_hama_case(self):
        """TODO docstring"""
        self.assertEquals(hama_case('ee'), 'Ee')
