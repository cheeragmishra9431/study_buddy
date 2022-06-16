from django.urls import path
from .import views

urlpatterns=[path('login/', views.loginPage, name="login"),
            path('register/', views.registerPage, name="register"),
            path('', views.home, name="home"), 
            path('logout/', views.logoutUser, name="logout"),
            path('room/<str:pk>/', views.room, name="room"),
            path('create-room', views.createRoom, name="create-room" ),  
            path('update-room/<str:pk>', views.updateRoom, name="update-room" ),  
            path('delete-room/<str:pk>', views.deleteRoom, name="delete-room" ),  
            path('delete-message/<str:pk>', views.deleteMessage, name="delete-message" ),  
            path('update-user/', views.updateUser, name="update-user" ),  
            path('profile/<str:pk>', views.userProfile, name="user-profile" ),  
            path('topics', views.topicsPage, name="topics" ),  
            path('activity', views.activityPage, name="activity" ),  
]
# unless untill the name of the room doesn't change we can change the path variable it will point to the same location