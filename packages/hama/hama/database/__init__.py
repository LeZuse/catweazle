#!/usr/bin/env python

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, join
from sqlalchemy.orm import mapper, sessionmaker, joinedload

from decimal import Decimal


engine = create_engine('mysql://python:211573@localhost:3306/catweazle2011?charset=utf8', echo=False)
metadata = MetaData(engine)
Session = sessionmaker(bind=engine)
session = Session()


products_table = Table('products', metadata, autoload=True)
sections_table = Table('sections', metadata, autoload=True)
prices_table = Table('prices', metadata, autoload=True)


r = report_table = Table('product_report', metadata, autoload=True)


# _table = Table('', metadata, autoload=True)



class Product(object):
    pass

class Section(object):
    pass

class Price(object):
    pass


class Report(object):
    pass

mapper(Product, products_table) 
mapper(Section, sections_table)
mapper(Price, prices_table)

# a = session.query(Product, Section).filter(Product.section==Section.sectionID).filter(Product.productID.in_(['00106376', '00005370']))
# 
# 
# for i, j in a:
#     print '%s: %s %s' % (
#         i.productID.encode('utf8'), 
#         i.name.encode('utf8'), 
#         j.sectionName.encode('utf8')
#         )


# a = session.query(Product).options(joinedload('addresses'))


# add product
'''
    p = Product()
    p.supplier_code = u'  999'
    p.product_id = u'  999'
    p.is_new = 1
    p.supplier = 2
    session.add(p)
    session.commit()


p = Price()
p.product_id = '00004107'
p.price_type_id = 1
p.minimum_qty = 44
p.price_value = Decimal('22.22')
session.add(p)
session.commit()
'''








## update object
'''
    session.query(Product).filter_by(product_id = '00004195').update({ 'volume': 1 })
    session.query(Prices).filter_by(product_id='00004370', price_type_id=1, minimum_qty=12).update({'price_value': 7.99})
    session.commit()
'''

## remove object
'''
    session.query(Prices).filter_by(product_id='00004370', price_type_id=1, minimum_qty=12).delete()
    session.commit()
'''

## select from view
'''
    # q = report_table.select().where(report_table.c.Code.in_(['00005135', '028669']))
    q = report_table.select().where(report_table.c.New == 1).where(report_table.c.Section == 'HT')
    
    result = session.execute(q)
    
    for i in result:
        code = i.Code
        original_code = i['Supplier Code']
        supplier = i['Supplier']
    
        print '%s %s %s' % (code, original_code, supplier)
'''