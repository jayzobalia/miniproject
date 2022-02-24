from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header = "Jay's Authenticator"
admin.site.site_title = "UMSRA Jay Zobalia's Portal"
admin.site.index_title = "Welcome to UMSRA Portal"

urlpatterns = [
path  ("",views.index, name = 'home'),
path  ("home",views.index, name = 'home'),
path  ("about",views.about, name = 'about'),
path  ("services",views.services, name = 'services'),
path  ("contact",views.contact, name = 'contact'),
path  ("video_feed",views.video_feed, name = 'video_feed')
]