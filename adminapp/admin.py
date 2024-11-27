from django.contrib import admin
from adminapp.models import CategoryDb,ProductDb

# Register your models here.
admin.site.register(CategoryDb)
admin.site.register(ProductDb)