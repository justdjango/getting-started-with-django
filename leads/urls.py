
from django.urls import path
from .views import home_page

app_name = "leads"

urlpatterns = [
    path('all/', home_page)
]