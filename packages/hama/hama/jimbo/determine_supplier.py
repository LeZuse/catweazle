from hama.databaseutils import Product, session, products_table


def main(codes):
    '''
    Finds supplier name & code for hama code
    This function wouldn't be neccessary if I could access IFS programmatically
    
    ..todo: replace placeholder with real code in hama.jimbo.determine_supplier
    '''
    
    resolved_codes = [(i, 'hama', i)for i in codes]
    
    return resolved_codes