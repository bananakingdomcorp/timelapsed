"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from timelapsed import views

router = routers.DefaultRouter()    

router.register(r'user', views.UsersView)
router.register(r'topic', views.TopicView)
router.register(r'card', views.CardView)
router.register(r'event', views.EventView)
router.register(r'date', views.DateRangeView)

"""
Note, all of the routes that are mentioned here may or may not be used, they are just here for now so that I can test that the work. 

"""


urlpatterns = [
    path('admin/', admin.site.urls),  path('api/', include(router.urls))     
]
