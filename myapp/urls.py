from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.home, name='home'),
    path('favicon/', RedirectView.as_view(url='/static/images/favicon.ico')),
]
