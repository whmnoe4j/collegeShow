#coding=utf-8 
from django.shortcuts import render, render_to_response, redirect
from collegePage import API
import json

# from collegePage.models import *
BatchList = ["本科提前批", "本科一批", "本科二批", "本科三批", "专科提前批", "专科批", "专科一批", "专科二批"]
StudentTypeList = ["文科", "理科", "综合", "其他"]
SubjectTypeList = ["本科", "高职专科"]
#跳转到主页面
def index(request):
    
    return render_to_response("index.html")

def dataSearch(request):
#     Search("江西")
    return render_to_response("dataSearch.html")

def reportedCollege(request):
    
    return render_to_response("reportedCollege.html")

#def collegescoreline(request):
#    #从get中提取参数
#    try:
#        studentProvine = request.GET.get("stuProvince")
#        studentType = StudentTypeList[int(request.GET.get("stuType")) - 1]
#        studentBatch = BatchList[int(request.GET.get("batch")) - 1]
#        studentYear = request.GET.get("year")
#        startPoint = int(request.GET.get("start"))
#    except:
#        #江西&batch=3&stuType=1&year=2014&start=0
#        studentProvine = '北京'
#        studentType = "文科"
#        studentBatch = "本科提前批"
#        studentYear = '2015'
#        startPoint = 0
#    if studentProvine:
#       
#        datas = API.showCollegeSchoolScoreLine(studentProvine, studentType, studentBatch, studentYear, startPoint)
#        print datas
#        return render_to_response("collegescoreline.html", datas)
#    else:
#        studentProvine = '北京'
#        studentType = "文科"
#        studentBatch = "本科提前批"
#        studentYear = '2015'
#        startPoint = 0
#        datas = API.showCollegeSchoolScoreLine(studentProvine, studentType, studentBatch, studentYear, startPoint)
#        return render_to_response("collegescoreline.html", datas)


def collegescoreline(request):
    #从get中提取参数
       
    #API.showCollegeSchoolScoreLine(request)
    
    return render_to_response("collegescoreline.html")
# def Search(studentProvince):
#     if studentProvince == "江西":
#         dataList = EwtNewJiangxi.objects.all()
#     print dataList[0].schoolname



