from django.contrib import admin
from .models import Category, Title, Comments

# Register your models here.
admin.site.register(Category)
admin.site.register(Title)
admin.site.register(Comments)