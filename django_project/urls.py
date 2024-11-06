

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home_view 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('papers/', include('papers.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

