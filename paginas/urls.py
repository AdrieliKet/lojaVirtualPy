from django.urls import path
from .views import SobreView

urlpatterns = [
    path("sobre/", SobreView.as_view(), name="sobre"),
]
