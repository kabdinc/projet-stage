# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from apps.authentication.models import Type_user,Intervenant

# Register your models here.
admin.site.register(Type_user)

admin.site.register(Intervenant)