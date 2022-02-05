from typing import AbstractSet
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

from logging import exception
from django import forms
from django.http import request
from crispy_forms.layout import Field
from django.forms import ModelForm, TextInput, Select, Textarea, IntegerField, ChoiceField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.widgets import DateTimeBaseInput, HiddenInput, Widget
from django.utils.translation import ugettext_lazy as _

from .models import *
# from.models import*

class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpForm(UserCreationForm):

  password1=forms.CharField(label=' Password',widget=forms.PasswordInput())
  def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)
  class Meta:
        model =User
        fields = ("username",'first_name','last_name','email')
        labels={
          'first_name':('First_name'),
          'last_name':('Last Name'),
          'email':('Email'),

        }
        widgets={
          'username':forms.TextInput(attrs={'class':'form-control'}),
          'forst_name':forms.TextInput(attrs={'class':'form-control'}),
          # 'forst_name':forms.TextInput(attrs={'class':'form-control'}),
          'last_name':forms.TextInput(attrs={'class':'form-control'}),
          'email':forms.TextInput(attrs={'class':'form-control'}),
        }

    
class Supplier_Model_Form(forms.ModelForm):
    # branch_code = ChoiceFieldNoValidation(label="Branch Name", required=False)

    def __init__(self, *args, **kwargs):
        super(Supplier_Model_Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        init_data = getattr(self, 'initial', None)

    class Meta:
        model = Supplier_Information
        fields = ['supp_name', 'proprietor_name', 'supp_address', 'supp_mobile', 'supp_email', 'supp_web', 'supp_key_person', 'supp_fax',
                  'branch_code','joining_date']

        widgets = {
            'supp_address': Textarea(attrs={'rows': 2, 'cols': 60, }),
            'joining_date': DateInput(),
        }

        labels = {
            "supp_id": _("Supplier ID"),
            "supp_name": _("Supplier Name"),
            "proprietor_name": _("Proprietor Name"),
            "supp_address": _("Supplier Address"),
            "supp_mobile": _("Mobile Number"),
            "supp_email": _("Email Address"),
            "supp_web": _("Web Address"),
            "supp_key_person": _("Contact Person Name"),
            "supp_fax": _("FAX Number"),
            "supp_grade": _("Supplier Grade"),
            "branch_code": _("Branch Name"),
            "joining_date": _("Opening Date")
        }