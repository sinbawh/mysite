from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('home', home_view,name='blog-home'),
    path('single', single_view , name='blog-single'),
    
    

    
]