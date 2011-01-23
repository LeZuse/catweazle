from catweazle.models import Section, Product, PriceType, Price, Supplier, Volume, ProductAttributeType, ProductAttribute, PriceStyle, PageStyle, ChangeCategory, Attribute
from django.contrib import admin



class ProductAdmin(admin.ModelAdmin):
    
    class PriceInline(admin.TabularInline):
        model = Price
        extra = 0
    
    class AttributeInline(admin.TabularInline):
        model = Attribute
        extra = 0

    fieldsets = [
       ('Info', {'fields': ['product_id', 'product_name', 'remark', 'supplier_code', 'supplier']}),
       ('Detail', {'fields': ['qty', 'desc_original', 'desc_presenter'], 'classes': ['collapse']}),
       ('Pricing', {'fields': ['srp', 'price_style'], 'classes': ['collapse']}),
       ('Presenter', {'fields': ['volume', 'presenter_section', 'page_number', 'page_style', 'is_new', 'is_new_timestamp'], 'classes': ['collapse']})
    ]
#    
    inlines = [PriceInline, AttributeInline]
    list_display = ('product_id', 'product_name', 'remark', 'presenter_section')
    search_fields = ['product_id', 'product_name', 'remark']
    list_filter = ['supplier', 'is_new']
    readonly_fields = ('supplier_code', 'page_number', 'page_style', 'is_new', 'is_new_timestamp')

# , ', '', 'presenter_section'

admin.site.register(Section)
admin.site.register(Product, ProductAdmin)
admin.site.register(PriceType)
admin.site.register(Price)
admin.site.register(Supplier)
admin.site.register(Volume)
admin.site.register(ProductAttributeType)
admin.site.register(ProductAttribute)
admin.site.register(PriceStyle)
admin.site.register(PageStyle)
# admin.site.register(ChangeCategory)
admin.site.register(Attribute)
