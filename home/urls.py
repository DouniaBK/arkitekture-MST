from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('contact/', views.contact_view, name='contact'),
    path('contact_success/', contact_success_view, name='contact_success'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('footer/', views.footer_view, name='footer'),
    path('terms/', views.terms_view, name='terms'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('disclaimer/', views.disclaimer_view, name='disclaimer'),
    path('impressum/', views.impressum_view, name='impressum'),
    path('projectone/', views.projectone_view, name='projectone'),
    path('projecttwo/', views.projecttwo_view, name='projecttwo'),
    path('send-test-email/', views.send_test_email, name='send_test_email'),

]