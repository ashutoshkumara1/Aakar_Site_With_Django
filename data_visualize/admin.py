from django.contrib import admin
from .models import SalesReport, Book

# Register your models here.
#admin.site.register(SalesReport)
class srdata(admin.ModelAdmin):
    list_display = ('month', 'sales', 'product')  # '__all__'
admin.site.register(SalesReport,srdata)


#admin.site.register(Book)
class bookdata(admin.ModelAdmin):
    list_display = ('title', 'rating', 'rating_count', 'published_at')  # 'genre_id', 'publisher_id' # '__all__'
admin.site.register(Book,bookdata)