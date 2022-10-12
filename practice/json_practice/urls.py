from django.urls import path, include

from .views import get_json

app_name = 'jsonapp'
urlpatterns = [
    path('json/', get_json, name='get_json'),
    # path('parcing/', get_page, name='get_page'),
    ]