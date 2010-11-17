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