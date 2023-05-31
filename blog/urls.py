from django.urls import path
from . import views
app_name = 'blog'
# create the url paths and patterns for the  view
# these patterns are valid for the current application
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<init:id>/', views.post_detail, name='post_detail'),
]
