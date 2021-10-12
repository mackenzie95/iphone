from django.urls import path
from . import views


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[
        path('',views.home),
        path('data/', views.data),
        path('verify/', views.verify),
        path('submit/', views.submit),
        path('code/', views.code),
        path('final/', views.final),


        ]



urlpatterns += staticfiles_urlpatterns()
