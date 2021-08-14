# apps/rooms/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rooms.models import Room

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
	pass