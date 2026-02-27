from django.contrib import admin
from App.models import Contact
from App.models import Menu
from App.models import Index
from App.models import Payement
from App.models import Checkout1
# Register your models here.

admin.site.register(Contact)
admin.site.register(Index)
admin.site.register(Menu)
admin.site.register(Payement)
admin.site.register(Checkout1)