from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.views.generic import ListView
from.models import*

class CustomerListView(ListView):
   model=Customer
   template_name='customer/main.html'

def customer_render_pdf_view(request,*args,**kwars):
   template_path = 'customer/pdf2.html'

   customer=Customer.objects.get(pk=1)
   context = {'customer': customer}
    # Create a Django response object, and specify content_type as pdf
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
   template = get_template(template_path)
   html = template.render(context)
    # create a pdf
   pisa_status = pisa.CreatePDF(
      html, dest=response, )
    # if error then show some funy view
   if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
   return response

def render_pdf_view(request):
    template_path = 'customer/pdffile.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
   #  if downloaded
   #  response['Content-Disposition'] = 'attachment; filename="report.pdf"'
   # if browser shoe:
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, )
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response