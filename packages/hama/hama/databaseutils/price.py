'''
Price
-----

This module contain class describing properties & behaviour of price. 
It should never be instantianted in top level code.
'''

class Price(object):
    '''
    Price representation
    '''
    def __init__(self, product_id, price_type_id, minimum_qty, price_value):

        #: Price's parent. See hama.databaseutils.Product
        self.parent = None
        
        # TODO These few attributes are here only to please pylint
        # Once we establish the database schema whole class has to 
        # be defined excplicitely        
        
        self.product_id = product_id
        
        #: Database id of the price_type. 
        #:
        #: .. warning:: Treat as read only!
        self.price_type_id = price_type_id

        #: Database id of the minimum_qty. 
        #:
        #: .. warning:: Treat as read only!   
        self.minimum_qty = minimum_qty
        
        self.price_value = price_value

    def delete(self):
        '''Remove the price from the product.'''
        self.parent.parent.session.delete(self)


    def __get_type (self):
        """ Return price's type name. """
        return self.parent.parent.price_types[self.price_type_id].name.upper()

    #: String representation of the `price_type`. Read only.    
    type_ = property(fget=__get_type)


    def set_minimum_qty(self, value):
        """ Change the minimum_quantity of the price """
        # FIXME This is not the final solution. If this is bypassed
        # and minimum_qty is changed directly, keys in prices
        # container will go out of sync
        
        old_key = (self.price_type_id, self.minimum_qty)
        self.minimum_qty = value
        new_key = (self.price_type_id, self.minimum_qty)
        del self.parent.prices[old_key]
        self.parent.prices[new_key] = self


    def set_price_type_id(self, value):
        """ Change the price_type of the price. """
        # FIXME This is not the final solution. If this is bypassed
        # nd price_type_id is changed directly, keys in prices
        # container will go out of sync
        
        
        old_key = (self.price_type_id, self.minimum_qty)
        self.price_type_id = value
        new_key = (self.price_type_id, self.minimum_qty)
        del self.parent.prices[old_key]
        self.parent.prices[new_key] = self


    def __repr__(self):
        repr_template = '<%s: %s@%s %s>'
        repr_data = (
            self.__class__.__name__,
            self.type_,
            self.minimum_qty,
            self.price_value
            )
        
        return repr_template % repr_data
