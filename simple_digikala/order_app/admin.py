from django.contrib.admin import register, ModelAdmin

from order_app.models import Order, Order_item

@register(Order)
class Orderadmin(ModelAdmin):
    list_display = [
        'buyer',
        'seller',
        'code'
    ]
    search_fields = [
        'buyer',
        'seller',
        'code'
    ]

@register(Order_item)
class Order_itemadmin(ModelAdmin):
    list_display = [
        'order',
        'product',
        'num'
    ]
    search_fields = [
        'order',
        'product'
    ]