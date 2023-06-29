from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('MANIMath_Account.urls')),
    path('', include('MANIMath_WebUI.urls')),
    path('', include('MANIMath_Api.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
