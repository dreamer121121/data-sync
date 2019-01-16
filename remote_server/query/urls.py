from django.conf.urls import url
from query import views
urlpatterns = [

    #'''CVE相关表'''
    url(r'^api/get/Cve/$', views.getCve),

    #"""CNVD相关表"""
    url(r'^api/get/Dev2vul$',views.getdev2vul),
    url(r'^api/get/Cnvd$',views.getCnvd),

    #"""设备信息相关表"""
    url(r'^api/get/Instance_info$',views.getinstance),

    #"""攻击信息相关表"""
    url(r'^api/get/Attack$',views.getAttack),
]