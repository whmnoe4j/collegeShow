#coding=utf-8 
from django.shortcuts import render, render_to_response, redirect

from models import *
from django.http.response import HttpResponse

#跳转到主页面
def index(request):
    
    return render_to_response("index.html")

def dataSearch(request):
#     Search("江西")
    return render_to_response("dataSearch.html")

def reportedCollege(request):
    return render_to_response("reportedCollege.html")






