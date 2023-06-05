from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path("site/<series>", views.series, name="series"),
    path("site/<series>/<doacao>", views.doacao, name="doacao")
]
