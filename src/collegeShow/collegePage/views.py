#coding=utf-8 
from django.shortcuts import render, render_to_response, redirect

from models import *
from django.http.response import HttpResponse

#跳转到主页面
def index(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        if loginUser:
            return render_to_response("index.html", {"loginUser":loginUser})
    except:
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
#一分一段
def scoreparam(request):
    #API.showCollegeSchoolScoreLine(request)
    return render_to_response("scoreparam.html")
#专业排名
def professionrank(request):
    #API.showCollegeSchoolScoreLine(request)
    return render_to_response("professionrank.html")
