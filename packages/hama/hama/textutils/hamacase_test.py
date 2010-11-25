"""Test module for nosetests"""

import unittest

from hama.textutils.hamacase import hama_case

class HamaCaseTest(unittest.TestCase):
    """Test hama_case"""
    def test_hama_case(self):
        """Capitalisation"""
        cases = (
            ('ee','Ee'),
            ('seven or more', 'Seven or mOre', ['mOre'])
            )
        
        for case in cases:
            function_input = case[0]
            expected_result = case[1]            
            
            try:
                custom_words = case[2]
                result = hama_case(function_input, custom_words)
            except IndexError:               
                result = hama_case(function_input)
            
            self.assertEquals(result, expected_result)
