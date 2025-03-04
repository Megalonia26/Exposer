from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from accountManager import views as account_viewes

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", account_viewes.userLogin, name="user-login"),
    path("register/", account_viewes.userRegister, name="user-registration"),
    path("lougout/", account_viewes.userLogout, name="user-logout"),
    path("", include("organiqueFood.urls")),
    path("user-profiles/<str:pk>", include("userprofiles.urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)