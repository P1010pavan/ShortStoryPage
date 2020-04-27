from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index1,name='index'),
    path('index1.html/',views.index11,name='index1'),
    path('contactus.html/',views.index2,name='contact'),
    path('aboutus.html/',views.index3,name='aboutus'),
    path('uploadpage.html/',views.index4,name='upload'),
    path('signin.html/',views.index5,name='signin'),
    path('signup.html/', views.index6, name='signup'),
    path('signout.html/', views.index7, name='signout'),

    path('termsandconditions.html/',views.index9,name='tm'),
    path('privacyandpolicy.html/',views.index10,name='pp'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),



]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)