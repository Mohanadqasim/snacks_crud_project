from django.contrib import admin
from django.urls import path
from .views import ListPageView,DetailPageView, SnackCreateView,SnackUpdateView,SnackDeleteView

urlpatterns = [
    path('', ListPageView.as_view(), name='snack_list'),
    path('<int:pk>/', DetailPageView.as_view(), name='snack_detail'),
    path('create', SnackCreateView.as_view(), name='create_snack'),
    path('update/<int:pk>', SnackUpdateView.as_view(), name='update_snack'),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name='delete_snack'),
]
