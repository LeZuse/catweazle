'''
Price
-----

setrui
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


    def __get_type (self):
        """TODO docstring"""
        return self.parent.parent.price_types[self.price_type_id].name.upper()

        
    type = property(fget=__get_type)


    def set_minimum_qty(self, value):
        """ TODO Replace temporary method
        
        This is not the final solution. If this is bypassed
        and minimum_qty is changed directly, keys in prises
        container will go out of sync
        """
        old_key = (self.price_type_id, self.minimum_qty)
        self.minimum_qty = value
        new_key = (self.price_type_id, self.minimum_qty)
        del self.parent.prices[old_key]
        self.parent.prices[new_key] = self


    def set_price_type_id(self, value):
        """ TODO Replace temporary method
        
        This is not the final solution. If this is bypassed
        and minimum_qty is changed directly, keys in prises
        container will go out of sync
        """
        old_key = (self.price_type_id, self.minimum_qty)
        self.price_type_id = value
        new_key = (self.price_type_id, self.minimum_qty)
        del self.parent.prices[old_key]
        self.parent.prices[new_key] = self


    def __repr__(self):
        repr_template = '<%s: %s@%s %s>'
        repr_data = (
            self.__class__.__name__,
            self.type,
            self.minimum_qty,
            self.price_value
            )
        
        return repr_template % repr_data
