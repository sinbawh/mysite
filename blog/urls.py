from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('home', home_view,name='blog-home'),
    path('<int:pid>', single_view , name='blog-single'),
    path('category/<str:cat_name>',home_view, name='category'),
    path('author/<str:author_username>',home_view, name='author'),
    path('search/' , blog_search, name='search'),
    

    
]