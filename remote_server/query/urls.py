from django.conf.urls import url
from query import views
urlpatterns = [
    url(r'^api/get/Cve/$', views.getCve),
    url(r'^api/get/Cnvd$',views.getCnvd),
    url(r'^api/get/Instance_info$',views.getinstance),
    url(r'^api/get/Attack$',views.getAttack),
]