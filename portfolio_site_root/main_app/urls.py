from django.urls import path,re_path
from . import views
from . import models


urlpatterns = [

    path('',views.index, name="index"),
    path('about/',views.about,name="about"),
    path('tickets/',views.tickets,name="tickets"),
    path('ml/',views.ml,name="ml")
]