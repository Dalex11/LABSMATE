from django.urls import path
from users.views import *


urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('refresh/', Refresh.as_view()),

]