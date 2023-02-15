from django.urls import path
from .views import *

urlpatterns = [
    path('register/',regclass.as_view(),name='register'),
    path('login/',logclass.as_view(),name='login'),
    path('display/',listview.as_view(),name='display'),
    path('delete/<pk>',deleteview.as_view(),name='delete'),
    path('detail/<pk>',detail.as_view(),name='detail'),
    path('update/<pk>',update.as_view(),name='update'),
    path('filedis/',fileClass.as_view(),name='filedis'),
    path('displayfile/',filedis.as_view(),name='displayfile'),
    path('deletefile/<pk>',filedelete.as_view(),name='deletefile'),
    path('filedetail/<pk>',filedetail.as_view(),name='filedetail'),
    path('fileupdate/<pk>',fileUpdate.as_view(),name='fileupdate')
    
]
