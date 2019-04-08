from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_view.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('', include('blog.urls')),
    path('', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
