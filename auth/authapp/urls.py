# urls.py

from django.urls import path
from .views import Create_User,login


urlpatterns = [
    # ... other patterns
    path('create_user/', Create_User, name='create_user'),
    path('login/', login, name='login')
   
]
