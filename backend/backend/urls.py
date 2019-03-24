
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from timelapsed import views

router = routers.DefaultRouter()    

router.register(r'user', views.UsersView, basename = 'user')

router.register(r'topic', views.TopicView, basename = 'topic')
router.register(r'card', views.CardView, basename = 'card')
router.register(r'event', views.EventView, basename = 'event')
router.register(r'date', views.DateRangeView, basename = 'date')

"""
Note, all of the routes that are mentioned here may or may not be used, they are just here for now so that I can test that the work. 

"""


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include(router.urls)), 
    path('auth/', include('rest_framework_social_oauth2.urls'))     
]