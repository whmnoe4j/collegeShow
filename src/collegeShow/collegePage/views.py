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
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        if loginUser:
            return render_to_response("dataSearch.html", {"loginUser":loginUser})
    except:
        return render_to_response("dataSearch.html")

def reportedCollege(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        if loginUser:
            return render_to_response("reportedCollege.html", {"loginUser":loginUser})
    except:
        return render_to_response("reportedCollege.html")

def collegescoreline(request):
    #从get中提取参数
       
    #API.showCollegeSchoolScoreLine(request)
    return render_to_response("collegescoreline.html")
def user(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        if loginUser:
            return render_to_response("user.html", {"loginUser":loginUser})
        else:
            return render_to_response("index.html")
    except:
        return render_to_response("index.html")



















#地区批次线
def areascoreline(request):
    return render_to_response("areascoreline.html")
#一分一段
def scoreparam(request):
    return render_to_response("scoreparam.html")
#专业排名
def professionrank(request):
    return render_to_response("professionrank.html")
#专业排名
def professiongroup(request):
    return render_to_response("professiongroup.html")
#专业分数线
def professionscore(request):
    return render_to_response("professionscore.html")

