
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home page' ),
    path('profile', views.profile, name='profile page' ),
    path('form', views.form, name='form page' ),
    path('expression', views.expression, name='output page' )
]
