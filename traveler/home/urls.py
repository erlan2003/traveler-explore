from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('tours/', views.tours, name='tours'),
    path('attractions/', views.attractions, name='attractions'),
    path('attractions/<int:pk>/', views.attraction_detail, name='attraction_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.RegisterView.as_view(), name="register"),
    path('add-attraction/', views.add_attraction, name='add_attraction'),
    path('search_attractions/', views.search_attractions, name='search_attractions'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)