from django.urls import path
from . import views
urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('add-post/',views.AddView.as_view(),name='addpost')
]
