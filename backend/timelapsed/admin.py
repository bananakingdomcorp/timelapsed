from django.contrib import admin

#Registers stuff that you can view from the admin page. 


from .models import Users, Topic, Event, Date_Range, Card

class CardAdmin(admin.ModelAdmin):
  fields = ['User', 'Topic', 'Name', 'Description', 'Position', 'Expected_Finish']

class UsersAdmin(admin.ModelAdmin):
  fields= ['Email']

class TopicAdmin(admin.ModelAdmin):
  fields = ['User', 'Name', 'Position'] 

class EventAdmin(admin.ModelAdmin):
  fields = ['User'] 

class DateRangeAdmin(admin.ModelAdmin):
  fields = ['User', 'Event_ID', 'Card_ID', 'Date', 'Begin_Time', 'End_Time']


admin.site.register(Users, UsersAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Date_Range, DateRangeAdmin)
admin.site.register(Card, CardAdmin)