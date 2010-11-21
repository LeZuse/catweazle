#!/usr/bin/env python
from hama.databaseutils import Database

def main(codes):
    '''
    Finds supplier name & code for hama code
    This function wouldn't be neccessary if I could access IFS programmatically

    '''

    class SupplierInfo(object):
        def __init__(self, supplier_code, supplier):
            self.supplier_code = supplier_code
            self.supplier = supplier

        def __repr__(self):
            return '(<SupplierInfo> %s, %s)' % (self.supplier, self.supplier_code)

    database = Database()
    resolved_codes = {}

    for code in codes:
        try:
            product = database[code]
            supplier_code = product.supplier_code
            supplier_name = product.supplier
        except KeyError:
            supplier_code = None
            supplier_name = None
        
        resolved_codes[code] = SupplierInfo(supplier_code, supplier_name)
      
    return resolved_codes
