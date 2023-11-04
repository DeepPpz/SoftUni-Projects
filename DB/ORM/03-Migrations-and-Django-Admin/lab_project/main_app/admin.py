from django.contrib import admin
from main_app.models import Product


# admin.site.register(Product) --> When we want to use the default admin interface


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_on')
    search_fields = ('name', 'category', 'supplier')
    list_filter = ('category', 'supplier')
    fieldsets = (
        ('General Information', {
            'fields': ('name', 'description', 'price', 'barcode')
        }),
        ('Categorization', {
            'fields': ('category', 'supplier')
        }),
    )
    date_hierarchy = ('created_on')
