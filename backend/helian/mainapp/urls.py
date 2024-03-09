from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.users, name="users"),
    path('newuser/', views.new_user, name='new_user'),
    path('add_esg_report/', views.add_esg_report, name='add_esg_report'),
    #path('gencomps/', views.generate_companies, name='gen_comps'),
    #path('genetfs/', views.generate_etfs, name='gen_etfs'),
    path('update_esg_score/', views.update_esg_score, name='update_esg_score'),
    path('get_all_company_symbols/', views.get_all_company_symbols, name='get_all_company_symbols'),
    path('post_portfolio/', views.post_portfolio, name="post_portfolio")
]