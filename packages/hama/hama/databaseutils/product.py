""" 
Product
-------
    
This module contain classes that describe properties & behaviour of 
hama product. They should **never** be instantianted in top level code.
"""

from sqlalchemy import orm
from hama.databaseutils.price import Price

class Product(object):
    """ Product representation 
    
    Contains an attribute for each column in the database. 
    You can both read & write these. Also contains a collection
    of all it's prices.
    
    Few convenience methods allow to access other values than 
    numeric id for certain properties     
    """
     
    def __init__(self):
        
        #: Product's prices. See: hama.databaseutils.product.PricesContainer
        self.prices = None
        
        #: Product's parent See: hama.databaseutils.Database
        self.parent = None
        
        # TODO These few attributes are here only to please pylint
        # Once we establish the database schema whole class has to 
        # be defined excplicitely
        self.product_id = None
        self.product_name = None
        self.presenter_section = None
        self.supplier_id = None

    @orm.reconstructor
    def _init_on_load(self):
        """ "constructor" called by sqlalchemy """
        self.prices = self.PricesContainer(self)

    def __repr__(self):
        class_name = self.__class__.__name__
        product_id = self.product_id
        product_name = self.product_name
        repr_string = u'<%s: %s, %s>' % (class_name, product_id, product_name)
        return repr_string.encode('utf8')

    def __get_section (self):
        """ Point to the description of section 
        with product's `presenter_section` as id
        """
        return self.parent.sections[self.presenter_section]
        
    #: Shortcut to the row in sections database table corresponding
    #: to presenter_section. Read only.     
    section = property(fget=__get_section)
        
    def __get_supplier (self):
        """ Return product's supplier name """
        return self.parent.suppliers[self.supplier_id].name
    
    #: Shortcut to the row in suppliers database table corresponding
    #: to supplier_id. Read only.
    supplier = property(fget=__get_supplier)

    class PricesContainer(dict):
        """ Collection of all Price objects belonging to product
        
        It is available as `product.prices`. 
        """
        def __init__(self, parent):
            dict.__init__(self)
            
            # Create link to the containing Product object
            self.parent = parent


        def add(self, price_type_id, qty, price_value):
            """ Create new price and append it to the product.prices """
            product_id = self.parent.product_id            
            price = Price(product_id, price_type_id, qty, price_value)
            self._append(price)        
            self.parent.parent.session.add(price)
            return price


        def _append(self, price):
            """ Append price ojecs to product.prices 
            and make sqlalchemy aware 
            """

            key = (price.price_type_id, price.minimum_qty)
            assert key not in self, 'error!'
            
            self[key] = price
            self[key].parent = self.parent
