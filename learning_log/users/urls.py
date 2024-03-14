from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


app_name = 'users'

"""为应用程序users定义URL模式"""


urlpatterns = [
    # 登录页面
    # re_path(r'^login/$',login.as_view,{'template_name':'users/login.html'},name='login'),
    
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
]