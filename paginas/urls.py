from django.urls import path
from .views import IndexView
from .views import SobreView

urlpatterns = [

    path("", IndexView.as_view(), name="index"),
    path("sobre/", SobreView.as_view(), name="sobre"),
]
