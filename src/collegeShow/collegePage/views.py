#coding=utf-8 
from django.shortcuts import render, render_to_response, redirect

from models import *
from django.http.response import HttpResponse

def reportedCollege(request):
    if request.method == 'POST':
        try:
            loginUserID = request.session.get("loginUser", "none")
            loginUser = Users.objects.get(id = loginUserID)
            return render_to_response("reportedCollege.html", { 'loginUser':loginUser})
        except:
            tempUser = {}
            #学校名称
            tempUser['stuProvince'] = request.POST.get("stuProvince")
            tempUser['stuType'] = request.POST.get("stuType")
            tempUser['score'] = request.POST.get("score", '0')
            tempUser['rank'] = request.POST.get("rank", '0')
            
            if tempUser['score'] == "":
                tempUser['score'] = "0"
            if tempUser['rank'] == "":
                tempUser['rank'] = "0"
            #保存临时的用户成绩分数
            request.session["tempUser"] = tempUser
            return render_to_response("reportedCollege.html", {'tempUser':tempUser})
    else:
        #return render_to_response("reportedCollege.html")
        try:
            loginUserID = request.session.get("loginUser", "none")
            loginUser = Users.objects.get(id = loginUserID)
            return render_to_response("reportedCollege.html", {"loginUser":loginUser})
        except:
            tempUser = request.session.get("tempUser", "none")
            if tempUser == "none":
                return render_to_response("reportedCollege.html")
            else:
                return render_to_response("reportedCollege.html", {'tempUser':tempUser})

#带参数的装饰器 登录用户和临时用户的验证
def auth_user(webName = None):
    def decorator(func):
        def inner(request, *args, **kwargs):
            print '=============='
            print webName
            #判断是否是登录用户
            try:
                loginUserID = request.session.get("loginUser", "none")
                loginUser = Users.objects.get(id = loginUserID)
                return render_to_response(webName, {'loginUser':loginUser})
            except:
                #如果是用户中心 没有登录状态直接返回到主页面
                if webName == "user.html":
                    return render_to_response("index.html")
                else:
                    #临时用户
                    tempUser = request.session.get("tempUser", "none")
                    
                    if tempUser == "none":
                        return render_to_response(webName)
                    else:
                        return render_to_response(webName, {'tempUser':tempUser})
        return inner
    return decorator

@auth_user(webName = "collegescoreline.html")
def collegescoreline(request):
    pass
    
#跳转到主页面
@auth_user(webName = "index.html")
def index(request):
    pass
   
@auth_user(webName = "dataSearch.html")
def dataSearch(request):
    pass

@auth_user(webName = "user.html")
def user(request):
    pass

#地区批次线
@auth_user(webName = "areascoreline.html")
def areascoreline(request):
    pass

#一分一段
@auth_user(webName = "scoreparam.html")
def scoreparam(request):
    pass

#专业排名
@auth_user(webName = "professionrank.html")
def professionrank(request):
    pass

#专业信息
@auth_user(webName = "professiongroup.html")
def professiongroup(request):
    pass

#专业分数线
@auth_user(webName = "professionscore.html")
def professionscore(request):
    pass

#院校信息
def schoolinfo(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        SchoolData = getSchoolInfo(request)
        return render_to_response("school_info.html", {'schoolinfo':SchoolData, 'loginUser':loginUser})
    except:
        SchoolData = getSchoolInfo(request)
        return render_to_response("school_info.html", {'schoolinfo':SchoolData})
#获取学校信息
def getSchoolInfo(request):
    SchoolInfo = {}
    try:
        #学校名称
        schoolName = request.GET.get("schoolName")
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
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
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
        return render_to_response("school_major.html", {'schoolMajors':SchoolMajors, 'schoolinfo':SchoolInfo, 'loginUser':loginUser})
    except:
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
#历年分数线
def schoolenrol(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        SchoolData = getSchoolInfo(request)
        stuProvince = SchoolData["Province"]
        schoolName = SchoolData["SchoolName"]
        stuType = '理科'
        proidInfo = {}
        proidInfo['schoolName'] = schoolName
        proidInfo['stuProvince'] = stuProvince
        proidInfo['stuType'] = stuType
        return render_to_response("schoolenrol.html", {'schoolinfo':SchoolData, 'proidInfo':proidInfo, 'loginUser':loginUser})
    except:
        SchoolData = getSchoolInfo(request)
        stuProvince = SchoolData["Province"]
        schoolName = SchoolData["SchoolName"]
        stuType = '理科'
        proidInfo = {}
        proidInfo['schoolName'] = schoolName
        proidInfo['stuProvince'] = stuProvince
        proidInfo['stuType'] = stuType
        return render_to_response("schoolenrol.html", {'schoolinfo':SchoolData, 'proidInfo':proidInfo})
