from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.Home, name='home'),
    path('update/', views.UpdateTB, name='update_tb'),
    path('update/<int:pk>/', views.Update, name='update'),
    path('add/', views.Add, name='add'),
]
