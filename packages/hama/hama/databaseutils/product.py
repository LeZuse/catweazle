from sqlalchemy import orm


class PricesContainer(object):
    def __init__(self, parent):
        self.parent = parent
        self.container = {}
    
    def __getitem__(self, key):
        return self.container[key]

    def __setitem__(self, key, value):
        self.container[key] = value
        
    def add(self, price_type_id, minimum_qty, price_value):
        key = (int(price_type_id), int(minimum_qty))
        price = Price(self.parent.product_id, price_type_id, minimum_qty, price_value)
        assert key not in self.container, 'error!'
        self.container[key] = price
        session.add(price)

    def append(self, price):
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
    @orm.reconstructor
    def init_on_load(self):
        self.prices = PricesContainer(self.product_id)

    def __repr__(self):
        return (u'<%s: %s, %s>' % (self.__class__.__name__, self.product_id, self.product_name)).encode('utf8')

    def __get_section (self):
        return self.parent.sections[self.presenter_section]
        
    section = property(fget=__get_section)
        
    def __get_supplier (self):
        return self.parent.suppliers[self.supplier_id].name
        
    supplier = property(fget=__get_supplier)

