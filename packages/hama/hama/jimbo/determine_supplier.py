#!/usr/bin/env python
from hama.databaseutils import session, report_table

def main(codes):
    '''
    Finds supplier name & code for hama code
    This function wouldn't be neccessary if I could access IFS programmatically

    ..todo: replace placeholder with real code in hama.jimbo.determine_supplier
    '''

    class SupplierInfo(object):
        def __init__(self, supplier_code, supplier):
            self.supplier_code = supplier_code
            self.supplier = supplier

        def __repr__(self):
            return '(<SupplierInfo> %s, %s)' % (self.supplier, self.supplier_code)


    not_resolved_codes = list(codes)
    resolved_codes = {}

    query = report_table.select().where(report_table.c.Code.in_(codes))
    result = session.execute(query)

    for i in result:
        resolved_codes[i.Code] = SupplierInfo(i['Supplier Code'], i['Supplier'])
        not_resolved_codes.remove(i.Code)
    
    for i in not_resolved_codes:
        resolved_codes[i] = SupplierInfo(None, None)
      
    return resolved_codes