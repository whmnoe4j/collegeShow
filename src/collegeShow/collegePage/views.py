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
#院校信息
def PageSplit(page, length):
    "提供页数和数据总长度返回切片起点和终点"
    start = (int(page) - 1) * 10
    if length - start < 10:
        end = length
    else:
        end = start + 10
    return start, end
def schoolinfo(request):
    try:
        #学校名称
        schoolName = request.GET.get("schoolName")
        print '-----------' + schoolName
        SchoolList = CollegeDetailEwt.objects.filter(schoolname = schoolName)
        
        ListLength = len(SchoolList)
        if ListLength == 0:
            return HttpResponse('没有该学校信息!')
        SchoolData = {}
        for school in SchoolList:
            SchoolData["SchoolName"] = school.schoolname
            SchoolData["f985"] = school.f985
            SchoolData["f211"] = school.f211 
            SchoolData["fyan"] = school.fyan 
            SchoolData["Province"] = school.address if school.address else "暂无"
            SchoolData["Levels"] = school.levels if school.levels else "暂无"
            SchoolData["attach_to"] = school.attach_to if school.attach_to else "暂无"
            SchoolData["Rank"] = school.school_rank 
            SchoolData["schoolType"] = school.schooltype 
            SchoolData["character"] = school.character if school.character else "不详"
            SchoolData["Code"] = school.schoolid if school.schoolid else "00000"
            SchoolData["Address"] = school.postal_address.replace("\r", "") if school.postal_address else "暂无"
            SchoolData["Tel"] = school.tel.replace("\r", "") if school.tel else "暂无"
            SchoolData["KeyDiscipline"] = school.key_discipline if school.key_discipline else "不详"
            SchoolData["Facukty"] = school.faculty if school.faculty else "不详"
            SchoolData["OfficeWebsite"] = school.official_website if school.official_website else "不详"
            SchoolData["school_img"] = school.school_img
        print SchoolData['SchoolName']
        return render_to_response("school_base.html", {'schoolinfo':SchoolData})
    except:
        return render_to_response("school_base.html", {'schoolinfo':SchoolData})

