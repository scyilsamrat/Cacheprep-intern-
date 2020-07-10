from django.contrib import admin
from django.conf.urls.static import  static
from django.conf import settings
from django.urls import path
from django.conf.urls import url
from main import views
from main.api import Q_list,Q
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    url(r'^api/Question_list(?P<Q_tag>\w+)/$',Q_list.as_view(),name='Q_list'),
    url(r'^api/Question_list/$',Q_list.as_view(),name='Q_list'),
    url(r'^api/Question_list/(?P<Q_id>\d+)/$',Q.as_view(),name='Q_list')
    	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




'''
from django.urls import include,path
from django.contrib import admin
from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('addproduct/',views.Product),
    path('addcustomer/',views.customer),
    path('showcustomer/',views.showcustomer),
    path('print/',views.checker),
    path('showproduct/',views.showproduct),
    path('manageC/',views.manageC),
    path('manageP/',views.manageP),
    path('viewfile/',views.viewfile),

]
'''