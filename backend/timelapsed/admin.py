from django.contrib import admin

#Registers stuff that you can view from the admin page. 


from .models import Users, Topic, Event, Date_Range, Card

class CardAdmin(admin.ModelAdmin):
  fields = ['Email', 'Topic', 'Name', 'Description', 'Position',]

class UsersAdmin(admin.ModelAdmin):
  fields= ['Email']

class TopicAdmin(admin.ModelAdmin):
  fields = ['Email', 'Name', 'Position'] 

class EventAdmin(admin.ModelAdmin):
  fields = ['Email'] 

class DateRangeAdmin(admin.ModelAdmin):
  fields = ['Email', 'Event_ID', 'Card_ID', 'Begin_Date', 'Num_Weeks', 'Weeks_Skipped' 'Begin_Time', 'End_Time' 'Day']


admin.site.register(Users, UsersAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Date_Range, DateRangeAdmin)
admin.site.register(Card, CardAdmin)