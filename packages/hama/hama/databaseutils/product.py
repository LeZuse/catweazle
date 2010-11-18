from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, join
from sqlalchemy.orm import mapper, sessionmaker, joinedload
from decimal import Decimal
 
engine = create_engine('mysql://python:211573@localhost:3306/catweazle2011?charset=utf8', echo=False)
metadata = MetaData(engine)
Session = sessionmaker(bind=engine)
session = Session()

class Product(object):
    def __repr__(self):
        return '(<%s>: %s, %s)' % (self.__class__.__name__, self.product_id, self.product_name)
        
class Price(object):
    def __init__(self, product_id, price_type_id, minimum_qty, price_value):
        self.product_id = product_id
        self.price_type_id = price_type_id
        self.minimum_qty = minimum_qty
        self.price_value = price_value

    def delete(self):
        session.delete(self)




class PricesContainer(object):
    def __init__(self, parent):
        self.parent = parent
    
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value
        
    def add(self, price_type_id, minimum_qty, price_value):
        key = (price_type_id, minimum_qty)
        price = Price(self.parent.product_id, price_type_id, minimum_qty, price_value)
        assert key not in self.__dict__, 'error!'
        self.__dict__[key] = price
        session.add(price)

class Items(object):  

    def __init__(self):
      
        products_table = Table('products', metadata, autoload=True)
        prices_table = Table('prices', metadata, autoload=True)
        mapper(Product, products_table) 
        mapper(Price, prices_table)
        
        
        # a = session.query(Product).filter(Product.product_id == '00103703').all()
        product_query = session.query(Product).all()
        price_query = session.query(Price).all()
        
        prices = {}
        
        
        for i in price_query:
            key = (i.price_type_id, i.minimum_qty)
            
            try:
                
                prices[i.product_id][key] = i
            except KeyError:
                prices[i.product_id] = {}
                prices[i.product_id][key] = i
            
        for i in product_query:
            try:
                pp = PricesContainer(i)
                for jj in prices[i.product_id]:
                    pp[jj] = prices[i.product_id][jj]
                
                i.prices = pp
                
            except KeyError:
                pass     
            
            self.__dict__[i.product_id] = i
    
    
    
    
    def __getitem__(self, key):
        return self.__dict__[key]
        
    def keys(self):
        return self.__dict__.keys()


i = Items()
a = i['00103700']