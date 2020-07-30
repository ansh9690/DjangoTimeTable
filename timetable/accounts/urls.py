from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # register / login / logout urls
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
