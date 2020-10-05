from django.urls import path
from . import views as v

app_name = "home"

urlpatterns = [
     path('', v.IndexView, name="index"),
]
