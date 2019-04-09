from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_view.LoginView.as_view(template_name='accounts/login.html'), name="login"),

    path('logout/', auth_view.LogoutView.as_view(
        template_name='accounts/logout.html'), name="logout"),

    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name="password-reset"),

    path('password-reset/done', auth_view.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name="password-reset-done"),

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name="password-reset-confirm"),

    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name="password-reset-complete"),

    path('', include('blog.urls')),
    path('', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
