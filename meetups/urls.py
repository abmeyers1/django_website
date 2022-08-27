# URL patterns holds list of all URLs in the app and what functions are associated 
# Django looks for 'urlpatterns' specifically

from django.urls import path
from . import views

urlpatterns = [
    # each path has 2 args: url and view to display
    path('meetups/', views.index )     # our-domain.com/meetups is active here .   Don't call the views function! no ()'s.
]