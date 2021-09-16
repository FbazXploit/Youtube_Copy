from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.IndexView, name = "index"),
  
  url(r'^result/(?P<keyword>[\w-]+)/$', views.resultView, name = "result"),
  
  url(r'^singleVideo/(?P<chId>[\w-]+)/(?P<videoId>[\w-]+)/$', views.singleVideoView, name = "singleVideo"),
  
  url(r'^chanel/(?P<chId>[\w-]+)/$', views.chanel, name = "chanel"),
  
  url(r'^chanel/video/(?P<chId>[\w-]+)/$', views.chanelVideo, name = "chanelVideo"),
  
  url(r'^chanel/playlist/(?P<chId>[\w-]+)/$', views.chanelPlay, name = "chanelPlay"),
  
  url(r'^chanel/detail/(?P<chId>[\w-]+)/$', views.chanelDet, name = "chanelDetail"),
  
  url(r'^getListPlay/(?P<playId>[\w-]+)/(?P<chId>[\w-]+)/$', views.listPlay, name = "listPlay"),
  
  url(r'^toolsFbaz/$', views.myTools, name = "tools"),
]
