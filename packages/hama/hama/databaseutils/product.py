""" TODO docstring """

from sqlalchemy import orm
from hama.databaseutils.price import Price

class PricesContainer(object):
    """ TODO docstring """
    def __init__(self, parent):
        self.parent = parent
        self.container = {}

    
    def __getitem__(self, key):
        return self.container[key]

    def __setitem__(self, key, value):
        self.container[key] = value
        
    def add(self, price_type_id, qty, price_value):
        """ TODO docstring """
        key = (int(price_type_id), int(qty))
        price = Price(self.parent.product_id, price_type_id, qty, price_value)
        assert key not in self.container, 'error!'
        self.container[key] = price
        self.parent.parent.session.add(price)

    def append(self, price):
        """ TODO docstring """
        key = (int(price.price_type_id), int(price.minimum_qty))
        assert key not in self.container, 'error!'
        self.container[key] = price

    def __len__(self):
        return len(self.container)

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, len(self.container))
        
    def __iter__(self):
        keys = sorted(self.container.keys())
        return iter([self.container[i] for i in keys])

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

