from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, Feedback

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'order_date']
    list_filter = ['status', 'order_date']
    search_fields = ['customer__user__username', 'id']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feedback, FeedbackAdmin)
