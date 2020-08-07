from django.urls import path
from .views import FlowersList, FlowerDetailView


app_name = 'flowers'

urlpatterns = [
    path('', FlowersList.as_view(), name='home'),
    path('detail/<int:pk>/', FlowerDetailView.as_view(), name='detail'),
]
