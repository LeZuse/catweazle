"""TODO docstring"""

from sqlalchemy.orm import clear_mappers
from hama.databaseutils import Database

def determine_supplier(codes):
    '''
    Finds supplier name & code for hama code
    This function wouldn't be neccessary if I could access IFS programmatically

    >>> from hama.jimbo import determine_supplier
    >>> 1 + 1
    2
    '''

    class SupplierInfo(object):
        """TODO docstring"""
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
        
        clear_mappers()
      
    return resolved_codes
