""" TODO docstring """

from sqlalchemy import orm
from hama.databaseutils.price import Price

class PricesContainer(dict):
    """ TODO docstring """
    def __init__(self, parent):
        self.parent = parent

    def add(self, price_type_id, qty, price_value):
        """ TODO docstring """
        key = (price_type_id, qty)
        price = Price(self.parent.product_id, price_type_id, qty, price_value)
        assert key not in self, 'error!'
        self[key] = price
        self.parent.parent.session.add(price)


    def append(self, price):
        """ TODO docstring """
        key = (price.price_type_id, price.minimum_qty)
        assert key not in self, 'error!'
        self[key] = price

        

class Product(object):
    """ TODO docstring """
    def __init__(self):
        self.prices = None
        
        # FIXME These few attributes are here only to please pylint
        # Once we establish the database schema whole class has to 
        # be defined excplicitely
        self.parent = None
        self.product_id = None
        self.product_name = None
        self.presenter_section = None
        self.supplier_id = None

    @orm.reconstructor
    def init_on_load(self):
        """ TODO docstring """
        self.prices = PricesContainer(self)

    def __repr__(self):
        class_name = self.__class__.__name__
        product_id = self.product_id
        product_name = self.product_name
        repr_string = u'<%s: %s, %s>' % (class_name, product_id, product_name)
        return repr_string.encode('utf8')

    def __get_section (self):
        """ TODO section docstring """
        return self.parent.sections[self.presenter_section]
        
    section = property(fget=__get_section)
        
    def __get_supplier (self):
        """ TODO docstring """
        return self.parent.suppliers[self.supplier_id].name
        
    supplier = property(fget=__get_supplier)

