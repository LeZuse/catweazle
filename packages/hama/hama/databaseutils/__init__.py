"""
Database
--------


"""

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import mapper, sessionmaker

from decimal import Decimal

from hama.databaseutils.product import Product
from hama.databaseutils.price import Price


# TODO store connenction details somewhere else
CONNECTION_STRING = 'mysql://python:211573@localhost:3306/\
catweazle2011?charset=utf8'


class Database(dict):
    """ 
    Describes the top Database object
    
    Currently can be instantiated only once per script per database, otherwise
    we get the `sqlalchemy.orm.mapper` errors
    """         
    def __init__(self, connection_string=None, echo=False):
        dict.__init__(self)
        
        class Container(object):
            """ Helper to hold additional tables in easy-to-access format 
            
            This will hopefuly go as soon as I'll get my head 
            around the sqlalchemy relationships
            """
        
        connection_string = CONNECTION_STRING
        
        # Boilerplate
        engine = create_engine(connection_string, echo=echo)
        metadata = MetaData(engine)
        self.session = sessionmaker(bind=engine)()     
        
        
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
        sections = self.session.execute(query).fetchall()        
        self.sections = {}
        
        for section in sections:
            section_id = section[0]          
            self.sections[section_id] = Container()
            self.sections[section_id].code = section[1]
            self.sections[section_id].name = section[2]
            
        query = tables['suppliers'].select()
        suppliers = self.session.execute(query).fetchall()        
        self.suppliers = {}
        
        for supplier in suppliers:
            supplier_id = supplier[0]          
            self.suppliers[supplier_id] = Container()
            self.suppliers[supplier_id].name = supplier[1]

        query = tables['price_types'].select()
        price_types = self.session.execute(query).fetchall()        
        self.price_types = {}
        
        for price_type in price_types:
            price_types_id = price_type[0]          
            self.price_types[price_types_id] = Container()
            self.price_types[price_types_id].name = price_type[1]        

        # Build the object
        # This is achieved by iterating through all products, finding any 
        # relevant info related to them and putting it into right container.
        #
        # It would be probably more elegant to do this via sqlalchemy
        # relationships, but I couldn't find enough time to get my 
        # head around it
        #
        # NB: each ``product'' is an instance of hama.databaseutils.Product

        
        for product in products:
            condition = (Price.product_id == product.product_id)
            prices = price_query.filter(condition).all()
            
            for price in prices:        
                product.prices._append(price)
            
            product.parent = self
            self[product.product_id] = product    
    
###### End __init__ ###########################################################
################################################################################

    
        
    def commit(self):
        """ Commit changes to database """
        self.session.commit()
        
    def rollback(self):
        """ Rollback uncommited changes 
        
        .. warning:: 
           
           This will currently **not restore all attributes** to 
           their former glory. If you, for example, rollback changes
           price `minimum_qty` or `price_type_id`, these changes will be
           purged from session.dirty but the keys im `product.prices` 
           will still have the new values
           
           In a nutshell: Don't rely on database object after you call rollback()
        """
        self.session.rollback()

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, len(self))
