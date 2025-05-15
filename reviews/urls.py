from django.urls import path
from reviews import views 

urlpatterns = [
    path('list', views.book_list.as_view() , name='ptsd list'),
    path('create', views.create_review, name='create ptsd'),
]