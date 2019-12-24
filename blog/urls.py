from django.urls import path
from blog import views

urlpatterns = [
    path('post_list', views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]