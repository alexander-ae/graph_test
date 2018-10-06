from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
