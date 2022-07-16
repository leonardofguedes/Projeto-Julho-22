from django.contrib import admin
from .models import *


class ImageAdmin(admin.StackedInline):
    model = Image

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]





