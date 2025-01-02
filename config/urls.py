from django.contrib import admin
from django.urls import path
import app.views as views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sitter/', views.sitter, name='sitter'),
    path('ex_sitter/', views.ex_sitter, name='ex_sitter'),
    path('sitterapplication/', views.sitterapplication, name='sitterapplication'),
    path('community/', views.community, name='community'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('login/', views.login, name='login'), 
    path('login_end/', views.login_end, name='login_end'),
    path('sitter_login_end/', views.sitter_login_end, name='sitter_login_end'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('next_step/', views.next_step, name='next_step'),
    path('next_step1/', views.next_step1, name='next_step1'),
    path('signup_end/', views.signup_end, name='signup_end'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('sitter_profile/', views.sitter_profile, name='sitter_profile'),
    path('calculate_top_sitters/', views.calculate_top_sitters, name='calculate_top_sitters'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)