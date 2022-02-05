from django.shortcuts import render


from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from.forms import User,SignUpForm
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse

import ast
# from appauth.utils import fn_get_query_result
# from finance.utils import fn_get_account_ledger
# from appauth.globalparam import fn_is_user_permition_exist
# from finance.utils import fn_get_accountinfo_bytran, fn_get_cash_gl_code, fn_cash_tran_posting, fn_transfer_tran_posting, fn_cancel_tran_batch
# from finance.validations import fn_val_account_number
# from finance.utils import fn_open_account_transaction_screen, fn_get_transaction_account_type, fn_get_account_info_byactype, fn_create_account, fn_get_accountinfo_byacnumber, fn_get_transaction_gl
# from appauth.views import get_global_data, fn_get_employee_by_app_user_id
from .forms import *
from .models import *
# from .myException import *
# from .validations import *
# from .utils import *
import math
from django.utils import timezone
import time
from datetime import date, datetime, timedelta
from decimal import Decimal
# from finance.models import Accounts_Balance
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist
from django.core import serializers
from random import randint
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db import connection, transaction
from django.template.loader import render_to_string
from django.db.models import Count, Sum, Avg, Subquery, Q, F,OuterRef
from django.core.files import File
import logging
import sys
import os
from io import BytesIO 
import barcode
from barcode.writer import ImageWriter
import random
logger = logging.getLogger(__name__)

def home(request):
  return render(request,'blog/home.html')

def navbar(request):
  return render(request,'blog/navbar.html')

def about(request):
  return render(request,'blog/about.html')

def contact(request):
  return render(request,'blog/contact.html')

def dashboard(request):
  return render(request,'blog/dashboard.html')

def Login(request):
  return render(request,'blog/Login.html')

def Logout(request):
  return render(request,'blog/Log out.html')

def signup(request):
  data=dict()
  form=SignUpForm()
  # data['form']=form
  return render(request,'blog/sign-up.html',{'form':form})




class sales_supplier_view(TemplateView):
    template_name = 'blog/sales-supplier-createlist.html'

    def get(self, request):
        context={}
        form = Supplier_Model_Form()
        context['form'] = form
        return render(request, self.template_name, context)


@transaction.atomic
def sales_supplier_insert(request):
    data = dict()
    data['form_is_valid'] = False
    data['error_message'] = ''
    try:
        with transaction.atomic():
            if request.method == 'POST':
                form = Supplier_Model_Form(request.POST)
                if form.is_valid():
                    try:
                        with transaction.atomic():
                            app_user_id = request.session["app_user_id"]
                            branch_code = request.session["branch_code"]
                            supp_name = form.cleaned_data["supp_name"]
                            supp_mobile = form.cleaned_data["supp_mobile"]
                            supp_address = form.cleaned_data["supp_address"]
                            joining_date = form.cleaned_data["joining_date"]

                            post = form.save(commit=False)
                            post.app_user_id = app_user_id
                            post.save()
                            data['success_message'] = 'Supplier Added Successfully! Supplier ID '
                            data['form_is_valid'] = True
                            return JsonResponse(data)
                    except Exception as e:
                        data['form_is_valid'] = False
                        if len(str(data['error_message'])) > 0:
                            return JsonResponse(data)
                        data['error_message'] = str(e)
                        logger.error("Error on line {} \nType: {} \nError:{}".format(
                            sys.exc_info()[-1], type(e).__name__, str(e)))
                        return JsonResponse(data)
                else:
                    data['error_message'] = form.errors.as_json()
            return JsonResponse(data)
    except Exception as e:
        data['error_message'] = str(e)
        return JsonResponse(data)

@transaction.atomic
def sales_supplier_edit(request, id):
    data = dict()
    context = {}
    try:
        with transaction.atomic():
            instance_data = get_object_or_404(
                Supplier_Information, supp_id=id)
            account_number = instance_data.account_number
            supp_id = instance_data.supp_id
            branch_code = instance_data.branch_code
            template_name = 'blog/sales-supplier-edit.html'
            context = {}
            data = dict()

            if request.method == 'POST':
                form = Supplier_Model_Form(
                    request.POST, instance=instance_data)  # forms name
                if form.is_valid():
                    supp_name = form.cleaned_data["supp_name"]
                    supp_mobile = form.cleaned_data["supp_mobile"]
                    supp_address = form.cleaned_data["supp_address"]
                    joining_date = form.cleaned_data["joining_date"]
                    app_user_id = request.session["app_user_id"]
    

                    obj = form.save(commit=False)
                    obj.account_number = account_number
                    obj.supp_id = supp_id
                    obj.branch_code = branch_code
                    obj.save()
                    # context = get_global_data(request)
                    context['success_message'] = ''
                    context['error_message'] = ''
                    data['form_is_valid'] = True
                else:
                    data['form_is_valid'] = False
                    context['error_message'] = form.errors.as_json()
                    print(form.errors.as_json())
                    return JsonResponse(data)
            else:
                form = Supplier_Model_Form(
                    instance=instance_data)  # forms name
                # context = get_global_data(request)
                context['form'] = form
                context['id'] = id
                data['html_form'] = render_to_string(
                    template_name, context, request=request)
            return JsonResponse(data)
    except Exception as e:
        data['error_message'] = str(e)
        return JsonResponse(data)