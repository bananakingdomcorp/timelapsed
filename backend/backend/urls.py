
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from timelapsed import views
from searchapp import views as searchViews

router = routers.DefaultRouter()    

router.register(r'user', views.UsersView, basename = 'user')

router.register(r'topic', views.TopicView, basename = 'add topic')

router.register(r'card', views.CardView, basename = 'card')

router.register(r'subclass', views.SubclassesView, basename = 'subclass')

router.register(r'topic_relationship', views.TopicRelationshipsView, basename = 'topic_relationship')

router.register(r'card_relationship', views.CardRelationshipsView, basename = 'card_relationship')


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include(router.urls)), 
    path('auth/', include('rest_framework_social_oauth2.urls'))     
]