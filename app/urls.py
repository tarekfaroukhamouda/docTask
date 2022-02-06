from unicodedata import name
from django.urls import path
from app import views

app_name='app'
urlpatterns = [
    path(r'',views.index,name='login'),
    path(r'register/',views.register,name='register'),
    path(r'uploadInvestication/',views.uploadInvestication,name='uploadInv'),
    path(r'getDashboard/<user_id>',views.getDashboard,name='geDashboard')
    
]
