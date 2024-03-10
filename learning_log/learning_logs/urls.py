"""定义learning_logs的URL模式""" 
# from django.conf.urls import url
# from .import views 
# urlpatterns = [ 
#     # 主页
#     url(r'^$',views.index,name='index'),
# ]



# learning_logs/urls.py
from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 主页
    path('', views.index, name='index'),
]