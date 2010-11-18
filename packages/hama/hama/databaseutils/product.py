from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, join
from sqlalchemy.orm import mapper, sessionmaker, joinedload
 
engine = create_engine('mysql://python:211573@localhost:3306/catweazle2011?charset=utf8', echo=False)
metadata = MetaData(engine)
Session = sessionmaker(bind=engine)
session = Session()

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
    def __repr__(self):
        return (u'<%s: %s, %s>' % (self.__class__.__name__, self.product_id, self.product_name)).encode('utf8')

        
class Price(object):
    def __init__(self, product_id, price_type_id, minimum_qty, price_value):
        self.product_id = product_id
        self.price_type_id = price_type_id
        self.minimum_qty = minimum_qty
        self.price_value = price_value

    def delete(self):
        session.delete(self)

    def __repr__(self):
        return '<%s: %s@%s %s>' % (self.__class__.__name__, self.price_type_id, self.minimum_qty, self.price_value)

        
class Items(object):  
    def __init__(self):     
        products_table = Table('products', metadata, autoload=True)
        prices_table = Table('prices', metadata, autoload=True)
        mapper(Product, products_table) 
        mapper(Price, prices_table)
        
        products = session.query(Product).all()
        price_query = session.query(Price)
 
        for product in products:
            prices = price_query.filter(Price.product_id == product.product_id).all()
            product.prices = PricesContainer(product)
            for price in prices:              
                product.prices.append(price)
    
            self.__dict__[product.product_id] = product    
    
    def __getitem__(self, key):
        return self.__dict__[key]
        
    def keys(self):
        return self.__dict__.keys()


i = Items()
a = i['00004371']
