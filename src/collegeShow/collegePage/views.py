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
def schoolinfo(request):
    SchoolData = getSchoolInfo(request)
    return render_to_response("school_info.html", {'schoolinfo':SchoolData})

#获取学校信息
def getSchoolInfo(request):
    SchoolInfo = {}
    try:
        #学校名称
        schoolName = request.GET.get("schoolName")
        #为什么会连续访问两次呢？
        print '-----------' + schoolName
        SchoolList = CollegeDetailEwt.objects.filter(schoolname = schoolName)
        
        ListLength = len(SchoolList)
        if ListLength == 0:
            return HttpResponse('没有该学校信息!')
        
        for school in SchoolList:
            SchoolInfo["SchoolName"] = school.schoolname
            SchoolInfo["f985"] = school.f985
            SchoolInfo["f211"] = school.f211 
            SchoolInfo["fyan"] = school.fyan 
            SchoolInfo["Province"] = school.address if school.address else "暂无"
            SchoolInfo["Levels"] = school.levels if school.levels else "暂无"
            SchoolInfo["attach_to"] = school.attach_to if school.attach_to else "暂无"
            SchoolInfo["Rank"] = school.school_rank 
            SchoolInfo["schoolType"] = school.schooltype 
            SchoolInfo["character"] = school.character if school.character else "不详"
            SchoolInfo["Code"] = school.schoolid if school.schoolid else "00000"
            SchoolInfo["Address"] = school.postal_address.replace("\r", "") if school.postal_address else "暂无"
            SchoolInfo["Tel"] = school.tel.replace("\r", "") if school.tel else "暂无"
            SchoolInfo["KeyDiscipline"] = school.key_discipline if school.key_discipline else "不详"
            SchoolInfo["Facukty"] = school.faculty if school.faculty else "不详"
            SchoolInfo["OfficeWebsite"] = school.official_website if school.official_website else "不详"
            SchoolInfo["school_img"] = school.school_img
        return SchoolInfo
    except:
        return []
#招生专业
def schoolmajor(request):
    SchoolInfo = getSchoolInfo(request)
    
    try:
        #学校名称
        schoolName = request.GET.get("schoolName")
        #为什么会连续访问两次呢？
        print '-----------' + schoolName
        SchoolMajor = CollegeMajor.objects.filter(schoolname = schoolName)
        
        ListLength = len(SchoolMajor)
        if ListLength == 0:
            return HttpResponse('没有该学校信息!')
        SchoolMajors = []
        print ListLength
        for school in SchoolMajor:
            SchoolData = {}
            SchoolData["SchoolName"] = school.schoolname 
            SchoolData["edudirectly"] = school.edudirectly 
            SchoolData["f985"] = school.f985 
            SchoolData["f211"] = school.f211 
            SchoolData["schoolprovince"] = school.schoolprovince 
            SchoolData["specialtype"] = school.specialtype 
            SchoolData["specialtyname"] = school.specialtyname 
            SchoolData["level"] = school.level 
            SchoolMajors.append(SchoolData)
        return render_to_response("school_major.html", {'schoolMajors':SchoolMajors, 'schoolinfo':SchoolInfo})
    except:
        return render_to_response("school_major.html", {'schoolMajors':SchoolMajors, 'schoolinfo':SchoolInfo})

#历年分数线
def schoolenrol(request):
    SchoolData = getSchoolInfo(request)
    return render_to_response("schoolenrol.html", {'schoolinfo':SchoolData})
