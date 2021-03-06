from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns =[
    path('', views.MainHome, name='Mainhome'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit/', views.edit_profile, name='edit'),
    path('video/', views.videos, name='videoplayer'),
    path('contactus/',views.contact_us, name='contact_Us'),
    path('login/', auth_view.LoginView.as_view(template_name='account/login.html'), name="login"),
    
    path('logout/', auth_view.LogoutView.as_view(template_name='account/logout.html'), name="logout"),

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
