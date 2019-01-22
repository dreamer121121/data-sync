from django.conf.urls import url
from query import views
urlpatterns = [

    #'''CVE相关表'''
    url(r'^api/get/Cve/$', views.getCve),

    #"""CNVD相关表"""
    url(r'^api/get/Dev2vul$',views.getDev2vul),
    url(r'^api/get/Vulnerability$',views.getCnvd),

    #"""设备信息相关表"""
    url(r'^api/get/Instance$',views.getInstance),
    url(r'^api/get/Instanceport$', views.getInstanceport),

    #"""攻击信息相关表"""
    url(r'^api/get/Conpot_log$',views.getAttack),

]