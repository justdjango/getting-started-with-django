from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='landing-page'),
    path('leads/',  include('leads.urls', namespace="leads"))
]
