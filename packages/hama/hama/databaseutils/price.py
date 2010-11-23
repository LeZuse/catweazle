'''
.. todo:: hama.databaseutils.price docstring
'''

class Price(object):
    '''
    TODO docstring
    '''
    def __init__(self, product_id, price_type_id, minimum_qty, price_value):
        self.product_id = product_id
        self.price_type_id = price_type_id
        self.minimum_qty = minimum_qty
        self.price_value = price_value
        self.parent = None

    def delete(self):
        '''Remove the price from the product.'''
        self.parent.parent.session.delete(self)

    def __get_price_type (self):
        """TODO docstring
        """
        return self
        
    price_type = property(fget=__get_price_type)

    def __repr__(self):
        repr_template = '<%s: %s@%s %s>'
        repr_data = (
            self.__class__.__name__,
            self.price_type_id,
            self.minimum_qty,
            self.price_value
            )
        
        return repr_template % repr_data
