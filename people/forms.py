#usr/bin/env python
#_*_coding:utf-8_*_
"""
@author:lifei4
@file_name:forms.py
@time:2018-08-13 19:51
"""

from django import forms

class UserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)