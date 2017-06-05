#coding=utf-8 
from django.shortcuts import render, render_to_response, redirect

# from collegePage.models import *

#跳转到主页面
def index(request):
    
    return render_to_response("index.html")

def dataSearch(request):
#     Search("江西")
    return render_to_response("dataSearch.html")

def reportedCollege(request):
    return render_to_response("reportedCollege.html")


# def Search(studentProvince):
#     if studentProvince == "江西":
#         dataList = EwtNewJiangxi.objects.all()
#     print dataList[0].schoolname



