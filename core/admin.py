# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User, Group

class UserAdmin(ImportExportModelAdmin):

    class Meta:
        model = User
