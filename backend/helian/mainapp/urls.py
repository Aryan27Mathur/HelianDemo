from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.users, name="users"),
    path('newuser/', views.new_user, name='new_user'),
    path('gencomps/', views.generate_companies, name='gen_comps')
]