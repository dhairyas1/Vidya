
from django.urls import path, include
from .views import login_view, signup_view 
from django.contrib.auth.views import LogoutView
from .views import send_message, inbox

def debug_view(request):
    print("Logout view accessed")
    return LogoutView.as_view()(request)
    
urlpatterns = [
    path('signup/', signup_view, name='signup'),  
    path('login/', login_view, name='login'),  
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('send/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),

]
