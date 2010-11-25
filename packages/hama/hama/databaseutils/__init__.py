"""
TODO docstring
"""

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper, sessionmaker

from decimal import Decimal

from hama.databaseutils.product import Product, PricesContainer
from hama.databaseutils.price import Price


# TODO store connenction details somewhere else

ENGINE = 'mysql'
USER = 'python'
PASSWORD = '211573'
HOST = 'localhost'
DATABASE = 'catweazle2011'



CONNECTION_STRING = '%(e)s://%(u)s:%(p)s@%(h)s:3306/%(d)s?charset=utf8'
CONNECTION_STRING = CONNECTION_STRING % {
    'e': ENGINE,
    'u': USER, 
    'p': PASSWORD,
    'h': HOST,
    'd': DATABASE
}

class Database(object):
    """ TODO docstring """         
    def __init__(self, connection_string=None, echo=False):
        class Container(object):
            """ TODO docstring """
            pass       
        
        # XXX temporary fix before I sort out the connection details
        connection_string = CONNECTION_STRING
        
        # Boilerplate
        engine = create_engine(connection_string, echo=echo)
        metadata = MetaData(engine)
        Session = sessionmaker(bind=engine)
        self.session = session = Session()     
        
        
       # Database tables we're interested in
        table_names = [
            'products',
            'prices',
            'changelog',
            'page_styles',
            'price_styles', 
            'price_types',
            'volumes',
            'sections',
            'suppliers',
            'change_categories',
            'product_attribute_types',
            'product_attributes',
            'attributes'
            ]
         
        # Create all table objects and store them in ``tables'' dict
        tables = {}
        for table_name in table_names:
            tables[table_name] = Table(table_name, metadata, autoload=True)
        
        # Mapping needs to stay manual if we want to avoid
        # creating dummy classes for each table even if they're not needed
        mapper(Product, tables['products']) 
        mapper(Price, tables['prices'])


        # Read all database entries. Probably not the most
        # efficient approach, but with the size of our database 
        # it still is reasonably fast       
        products = self.session.query(Product).all()
        price_query = self.session.query(Price)
        

                    
        
        query = tables['sections'].select()
        sections = session.execute(query).fetchall()        
        self.sections = {}
        
        for section in sections:
            section_id = section[0]          
            self.sections[section_id] = Container()
            self.sections[section_id].code = section[1]
            self.sections[section_id].name = section[2]
            
        query = tables['suppliers'].select()
        suppliers = session.execute(query).fetchall()        
        self.suppliers = {}
        
        for supplier in suppliers:
            supplier_id = supplier[0]          
            self.suppliers[supplier_id] = Container()
            self.suppliers[supplier_id].name = supplier[1]
        

        # Build the object
        # This is achieved by iterating through all products, finding any 
        # relevant info related to them and putting it into right container.
        #
        # It would be probably more elegant to do this via sqlalchemy
        # relationships, but I couldn't find enough time to get my 
        # head around it
        #
        # NB: each ``product'' is an instance of hama.databaseutils.Product
        self.container = {}
        
        for product in products:
            condition = Price.product_id == product.product_id
            prices = price_query.filter(condition).all()
            
            for price in prices:
                price.parent = product           
                product.prices.append(price)
            
            product.parent = self
            self.container[product.product_id] = product    
    
###### End __init__ ###########################################################
################################################################################

    
    def __getitem__(self, key):
        return self.container[key]
        
    def keys(self):
        """ TODO docstring """
        return self.container.keys()
        
    def commit(self):
        """ TODO docstring """
        self.session.commit()
        
    def __contains__(self, code):
        return code in self.container
        
    def __iter__(self):
        keys = sorted(self.container.keys())
        return iter([self.container[i] for i in keys])
        
    def __len__(self):
        return len(self.container)

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, len(self.container))
