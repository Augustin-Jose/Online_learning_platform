from django.conf.urls import url
from login import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('login/', views.login),

    url('reset_password/', auth_views.PasswordResetView.as_view(),name='password_reset_form'),
    url('reset_password_done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    url('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    url('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

   ]
