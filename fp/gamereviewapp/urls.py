
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getGame/', views.getGame, name='game'),
    path('gamedetail/<int:id>', views.gamedetail, name='gamedetail'),
    path('newGame/', views.newGame, name='newgame'),
    path('newReview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]