from django.urls import path, re_path
from toys import views

urlpatterns = [
    path('toys/$', views.toy_list),
    path(r'^toys/(?P<pk>[0-9]+)$',views.toy_detail)
]