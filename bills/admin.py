# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer, Product, Cust_bill, Inventory
# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cust_bill)
admin.site.register(Inventory)