from django.urls import path
from . import views 


urlpatterns = [
    path('', views.Index, name = 'index'),    
    path('article/<int:id>/<slug:slug>/', views.Article_Details, name = 'article_details'), 
    path('registration/', views.User_Registration, name = 'registration'),
    path('login/', views.User_Login, name = 'login' ),
    path('logout/', views.getlogout, name="logout"),
    path('category/<name>', views.Category_Post, name="category"),
    path('about-me/', views.Myself, name = 'myself'), 
    path('create-article/', views.ArticlaeFrom, name = 'create-article'),
    path('show_category/', views.Show_Category, name = 'show_category'),
    path('create_author/', views.Create_Author, name = 'create_author')
]