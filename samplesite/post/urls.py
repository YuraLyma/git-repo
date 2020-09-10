from django.urls import path
from django.contrib.auth import views

from .views import index, post_details

urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('<int:post_id>/', post_details, name='post_details'),
	path('', index, name='index'),
]
