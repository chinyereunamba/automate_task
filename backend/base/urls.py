from django.urls import path
from .views import home, create_form, update_form

urlpatterns = [
    path("", home, name="home"), 
    path("create", create_form, name="create"),
    path("update/<int:pk>", update_form, name="update"),
    ]
