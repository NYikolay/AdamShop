from django.urls import path

from accounts.views import Login, CreateUserView, Logout

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
]
