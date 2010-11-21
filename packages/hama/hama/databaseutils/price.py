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
