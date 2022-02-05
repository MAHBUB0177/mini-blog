

from argparse import Namespace
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from website.models import */
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('',include('blogapi.urls')),
    # path('', include('website.urls')),
    path('home1', home_view, name='home1'),
    path('barcode', barcode_view, name='barcode'),
    path('customer',include('customer.urls',namespace='customer'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)