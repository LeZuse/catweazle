from django.db import models

class Section(models.Model):    
    section_code = models.CharField(max_length=4, unique=True)
    section_name = models.CharField(max_length=32, unique=True)
    section_ordinal = models.IntegerField(null=True, blank=True, default=None)
                    
    class Meta:
        db_table = u'catweazle_sections'
        ordering = ['section_ordinal']
        verbose_name = '(OK) Section'

    def __unicode__(self):
        return u'%s-%s' % (self.section_code, self.section_name)


class PriceType(models.Model):
    price_type_name = models.CharField(max_length=64, unique=True, verbose_name='price type')

    def __unicode__(self):
        return self.price_type_name

    class Meta:
        db_table = u'catweazle_price_types'
        ordering = ['id']
        verbose_name = '(OK) Price type'


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=64, unique=True)
    
    class Meta:
        db_table = u'catweazle_suppliers'
        ordering = ['id']
        verbose_name = '(OK) Supplier'
    
    def __unicode__(self):
        return self.supplier_name
    

class Volume(models.Model):
    volume_name = models.CharField(max_length=64, blank=True)
    
    def __unicode__(self):
        return self.volume_name
    
    class Meta:
        db_table = u'catweazle_volumes'
        ordering = ['id']
        verbose_name = '(OK) Volume'


class ProductAttributeType(models.Model):
    product_attribute_type_name = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.product_attribute_type_name
    
    class Meta:
        db_table = u'catweazle_product_attribute_types'
        ordering = ['id']
        verbose_name = '(OK) Product attribute type'


class ProductAttribute(models.Model):
    product_attribute_name = models.CharField(max_length=64, unique=True)
    product_attribute_type = models.ForeignKey(ProductAttributeType)

    def __unicode__(self):
        return self.product_attribute_name
        
    class Meta:
        db_table = u'catweazle_product_attributes'
        ordering = ['id']
        verbose_name = '(OK) product attribute'


class PriceStyle(models.Model):
    price_style_name = models.CharField(max_length=16, blank=True)
    class Meta:
        db_table = u'catweazle_price_styles'
        ordering = ['id']
        verbose_name = '(OK) price style'
        
    def __unicode__(self):
        return self.price_style_name        


class PageStyle(models.Model):
    page_style_name = models.CharField(max_length=32, blank=True)
    class Meta:
        db_table = u'catweazle_page_styles'
        verbose_name = '(OK) page style'

    def __unicode__(self):
        return self.page_style_name


class ChangeCategory(models.Model):
    change_category_name = models.CharField(max_length=64, blank=True)
    
    class Meta:
        db_table = u'catweazle_change_categories'
        verbose_name_plural = u'(OK) Change categories'
    
    def __unicode__(self):
        return self.change_category_name
        
##################################################################################################

class Product(models.Model):
    product_id = models.CharField(primary_key=True, max_length=16)
    product_name = models.CharField(max_length=1024, default=u'', blank=True)
    presenter_section = models.ForeignKey(Section, default=13, blank=True)
    remark = models.CharField(max_length=3072, blank=True)
    volume = models.ForeignKey(Volume, blank=True, default=1)
    page_number = models.IntegerField(null=True, blank=True)
    page_style = models.ForeignKey(PageStyle, null=True, db_column='page_style', blank=True)
    is_new = models.IntegerField(null=True, blank=True)
    is_new_timestamp = models.DateTimeField(null=True, blank=True)
    srp = models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)
    qty = models.IntegerField(null=True, blank=True)
    price_style = models.ForeignKey(PriceStyle, null=True, db_column='price_style', blank=True)
    desc_original = models.TextField(blank=True)
    desc_presenter = models.TextField(blank=True)
    supplier_code = models.CharField(max_length=48)
    supplier = models.ForeignKey(Supplier, null=True, blank=True)
    

    
    def __unicode__(self):
        return self.product_id

    class Meta:
        db_table = u'catweazle_products'
   

class Price(models.Model):
    product = models.ForeignKey(Product)
    price_type = models.ForeignKey(PriceType)
    minimum_qty = models.PositiveIntegerField()
    price_value = models.DecimalField(max_digits=10, decimal_places=2)
    is_nlp = models.BooleanField()
    
    def __unicode__(self):
        return u'%s@%s: \u00a3%s' % (self.product, self.minimum_qty, self.price_value)
  
    class Meta:
        db_table = u'catweazle_prices'
        unique_together = ("product", "minimum_qty", "price_type")


class Attribute(models.Model):
    attribute = models.ForeignKey(ProductAttribute)
    product = models.ForeignKey(Product)
    attribute_timestamp = models.DateTimeField()
    attribute_value = models.CharField(max_length=128)
    
    class Meta:
        db_table = u'catweazle_attributes'

        
class Changelog(models.Model):
    product = models.ForeignKey(Product)
    field_changed = models.CharField(max_length=384)
    old_value = models.TextField()
    new_value = models.TextField()
    change_timestamp = models.DateTimeField()
    made_by_user = models.CharField(max_length=192, blank=True)
    change_category = models.ForeignKey(ChangeCategory)
    is_synchronised = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'catweazle_changelog'
