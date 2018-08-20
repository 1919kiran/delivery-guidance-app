from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dummyapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('donor', views.index_donor, name='index_donor'),
    path('robin', views.robin_dashboard, name='robin_dashboard'),
    path('create_food_record', views.create_food_record, name='create_food_record'),
    path('test', views.get_donors, name='get_donors'),
    path('register_robin', views.register_robin, name='register_robin'),
    path('login_robin', views.login_robin, name='login_robin'),
    path('register_donor/', views.register_donor, name='register_donor'),
    path('robin_delivering/', views.robin_delivering, name='robin_delivering'),
    path('login_donor/', views.login_donor, name='login_donor'),
    path('robin_dashboard/', views.robin_dashboard, name='robin_dashboard'),
    path('calculate_points/', views.calculate_points, name='calculate_points'),
    path('robin_delivering/', views.robin_delivering, name='robin_delivering'),
    path('faq/', views.faq, name='faq'),
    path('askq/', views.askq, name='askq'),
    path('authenticate/', views.authenticate, name='authenticate'),
    #path('anon_donate/', views.anon_donate, name='anon_donate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
