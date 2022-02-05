from django.urls import path
from.views import *

app_name='customer'

urlpatterns = [
    path('test/',render_pdf_view,name='test_view' ),
    path('',CustomerListView.as_view(),name='CustomerListView' ),
    # path('pdf/<slug:id>',customer_render_pdf_view,name='customer-pdf-view' ),
    path('pdf/', customer_render_pdf_view, name='customer-pdf-view'),
   
]
