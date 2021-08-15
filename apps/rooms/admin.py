# apps/rooms/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.rooms.models import (
	Room, RoomType,
	Amenity, Facility,
	HouseRule)

# Register your models here.
admin.site.register(Amenity)
admin.site.register(Facility)
admin.site.register(HouseRule)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
	pass

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
	pass

