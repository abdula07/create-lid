from django.urls import path
from . import views

app_name = 'create_lid'

urlpatterns = [
    path('create/lid', views.create_lid),
]
