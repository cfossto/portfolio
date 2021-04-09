from django.contrib import admin
from .models import Venue, MyClubUser,Event
# Register your models here.

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display =('name','address','phone')
    ordering=('address',)
    search_fields = ('name','address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    #fields = (('name','venue'),'event_date','description','manager')
    list_display = ('name',"event_date",'venue')
    list_filter = ('event_date','venue')
    ordering = ('-event_date',)
    fieldsets = (
        ('Required information', {
            'description': "These fields are required",
            'fields': (('name','venue'),'event_date')
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': ('description','manager')
        })
    )

# admin.site.register(Venue)
admin.site.register(MyClubUser)
# admin.site.register(Event)