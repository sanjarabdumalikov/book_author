from django.contrib import admin
from .models import (bookModel,bookcategoryModel,authorModel)


admin.site.register(bookModel)
admin.site.register(authorModel)
admin.site.register(bookcategoryModel)
# Register your models here.
