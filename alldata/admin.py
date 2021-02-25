from django.contrib import admin
from .models import *

admin.site.site_header = 'Guide Service Almaty'
class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'first_name', 'last_name', 'email')
admin.site.register(User, UserAdmin)

class BankCardAdmin(admin.ModelAdmin):
    list_display = ('bankcardid', 'name', 'user_userid')
admin.site.register(BankCard, BankCardAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('locationid', 'name')
admin.site.register(Location, LocationAdmin)

class TripInstanceAdmin(admin.ModelAdmin):
    list_display = ('tripinstanceid', 'title')
admin.site.register(TripInstance, TripInstanceAdmin)

class TripAdmin(admin.ModelAdmin):
    list_display = ('tripid', 'tripinstance_tripinstanceid')
admin.site.register(Trip, TripAdmin)

class GuideAdmin(admin.ModelAdmin):
    list_display = ('guideid', 'first_name', 'last_name')
admin.site.register(Guide, GuideAdmin)

class UserBuysTripAdmin(admin.ModelAdmin):
    list_display = ('user_userid', 'trip_tripid')
admin.site.register(UserBuysTrip, UserBuysTripAdmin)

class LocationOfTripInstanceAdmin(admin.ModelAdmin):
    list_display = ('location_locationid', 'tripinstance_tripinstanceid')
admin.site.register(LocationOfTripInstance, LocationOfTripInstanceAdmin)

class GuideLeadsTripAdmin(admin.ModelAdmin):
    list_display = ('user_userid', 'trip_tripid')
admin.site.register(GuideLeadsTrip, GuideLeadsTripAdmin)