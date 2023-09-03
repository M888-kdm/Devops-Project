from django.urls import path
from . import views

app_name="formulaire"

urlpatterns=[
    path('',views.index, name="index"),
    path('users/', views.user_list, name='user_list'),
    path('visit_count/', views.visit_count, name='visit_count'),
]
