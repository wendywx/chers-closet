from django.contrib import admin
from .models import Product
from .models import Closet
from .models import Outfit
from .models import Type
from .models import User

# Register your models here.

admin.site.register(Product)
admin.site.register(Closet)
admin.site.register(Outfit)
admin.site.register(Type)
admin.site.register(User)
