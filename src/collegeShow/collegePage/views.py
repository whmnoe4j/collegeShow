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

def collegescoreline(request):
    #从get中提取参数
       
    #API.showCollegeSchoolScoreLine(request)
    return render_to_response("collegescoreline.html")





















#地区批次线
def areascoreline(request):
    #API.showCollegeSchoolScoreLine(request)
    return render_to_response("areascoreline.html")
