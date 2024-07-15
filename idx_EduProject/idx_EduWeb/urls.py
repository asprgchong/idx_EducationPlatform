from django.urls import path
from . import views
urlpatterns = [
        path("", views.allCourses, name='allCourses'), 
        path('login/', views.login_page, name='login_page'),    # Login page
        path('register/', views.register_page, name='register'),  # Registration page
        path('profile/', views.profile, name="profile"), #profile view
        path('logout/', views.logoutView, name="logout"), #logout
        path('<str:lesson_num>/', views.index, name='index'),  # index view at /
        # path("", views.index, name='index'),  # index view at /
]

