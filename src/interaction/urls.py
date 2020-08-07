from django.urls import path
from . import views
app_name = 'interaction'
urlpatterns = [

    path('detail/<int:flower_id>/action/',
         views.LikeFlowerView.as_view(), name='like-flower')
]
