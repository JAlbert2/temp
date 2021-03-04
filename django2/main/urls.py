from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sucess',views.sucess, name='sucess'),
    path('stats',views.stats, name='stats'),
    path('video', views.video, name='video'),
    path('scanner', views.scanner, name='scanner')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)