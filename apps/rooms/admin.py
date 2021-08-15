# apps/rooms/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rooms.models import Room, RoomType

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
	pass

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
	pass

