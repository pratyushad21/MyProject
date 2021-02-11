from django.contrib import admin
from .models import CartItem

# Register your models here.
from .models import Brand, Category, Product
from .models import CartItem
admin.site.register(CartItem)

class BrandAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active",]
    search_fields = ["name", "is_active",]
    list_filter = ["name", "is_active",]
    #readonly_fields = ["is_active",]
    
    class Meta:
        model = Brand

admin.site.register(Brand,BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active",]
    search_fields = ["name", "is_active",]
    list_filter = ["name", "is_active",]
    #readonly_fields = ["is_active",]
    
    class Meta:
        model = Category

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ["image_tag" ,"name" ,"price" ,"brand_id" ,"category_id" ,]
    search_fields = ["name","price","brand_id__name","category_id__name",]
    list_filter = ["brand_id","category_id",]
    #readonly_fields = ["quantity",]
    
    class Meta:
        model = Product

admin.site.register(Product,ProductAdmin)


