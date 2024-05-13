from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"), 
    path("create", create_form, name="create"),
    path("update/<int:pk>", update_form, name="update"),
    path("delete/<int:pk>", delete, name="delete"),

    path('register', register, name='create_user'),
    path('login', login, name='login'),
    ]
