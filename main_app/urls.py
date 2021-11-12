from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.WishList.as_view(), name='wish_list'),
    path('/create/', views.WishCreate.as_view(), name='wish_create'),
    path('/delete/<int:pk>/', views.WishDelete.as_view(), name='wish_delete'),
]
