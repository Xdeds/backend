from django.urls import path
from apps.user.views import CreateUserView, logout, signin, profile
    
urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]