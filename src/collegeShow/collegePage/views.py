#coding=utf-8 
from django.shortcuts import render, render_to_response, redirect

from models import *
from django.http.response import HttpResponse
import json

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
        tempUser = request.session.get("tempUser", "none")
        
        if tempUser == 'none':
            tempUser = {}
            tempUser['stuProvince'] = loginUser.stuprovince
            tempUser['stuType'] = loginUser.stutype
            tempUser['score'] = loginUser.score
            tempUser['year'] = request.GET.get("year")
            tempUser['page'] = request.GET.get("page")
            request.session["tempUser"] = tempUser
        return render_to_response("dataSearch.html", {"loginUser":loginUser, 'tempUser':tempUser})
    except:
        print '获取登录用户失败'
        tempUser = request.session.get("tempUser", "none")
        print tempUser
        if tempUser == "none":
            
            return render_to_response("dataSearch.html")
        else:
            return render_to_response("dataSearch.html", {'tempUser':tempUser})
def reportedCollege(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        tempUser = request.session.get("tempUser", "none")
        if loginUser:
            return render_to_response("reportedCollege.html", {"loginUser":loginUser, 'tempUser':tempUser})
    except:
        tempUser = request.session.get("tempUser", "none")
        if tempUser == "none":
            return render_to_response("reportedCollege.html")
        else:
            recoSchool = recommendSchoolName(tempUser['stuProvince'], tempUser['stuType'], tempUser['year'], tempUser['score'], tempUser['page'])
            return render_to_response("reportedCollege.html", {'tempUser':tempUser, 'recoSchool':recoSchool})

def collegescoreline(request):
    try:
        #从get中提取参数
        #API.showCollegeSchoolScoreLine(request)
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        tempUser = request.session.get("tempUser", "none")
        if tempUser == "none":
            return render_to_response("collegescoreline.html")
        else:
            return render_to_response("collegescoreline.html", {'tempUser':tempUser, 'loginUser':loginUser})
    except:
        tempUser = request.session.get("tempUser", "none")
        if tempUser == "none":
            return render_to_response("collegescoreline.html")
        else:
            return render_to_response("collegescoreline.html", {'tempUser':tempUser})
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
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        tempUser = request.session.get("tempUser", "none")
        if tempUser == 'none':
            return render_to_response("areascoreline.html")
        else:
            return render_to_response("areascoreline.html", {'tempUser':tempUser, 'loginUser':loginUser})
    except:
        tempUser = request.session.get("tempUser", "none")
        if tempUser == 'none':
            return render_to_response("areascoreline.html")
        else:
            return render_to_response("areascoreline.html", {'tempUser':tempUser})
#一分一段
def scoreparam(request):
    try:
        tempUser = request.session.get("tempUser", "none")
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        if tempUser != 'none':
            return render_to_response("scoreparam.html", {'tempUser':tempUser, 'loginUser':loginUser})
        else:
            return render_to_response("scoreparam.html")
    except:
        tempUser = request.session.get("tempUser", "none")
        if tempUser != 'none':
            return render_to_response("scoreparam.html", {'tempUser':tempUser})
        else:
            return render_to_response("scoreparam.html")
#专业排名
def professionrank(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        tempUser = request.session.get("tempUser", "none")
        if tempUser != 'none':
            return render_to_response("professionrank.html", {'tempUser':tempUser, 'loginUser':loginUser})
        else:
            return render_to_response("professionrank.html")
    except:
        tempUser = request.session.get("tempUser", "none")
        if tempUser != 'none':
            return render_to_response("professionrank.html", {'tempUser':tempUser})
        else:
            return render_to_response("professionrank.html")
#专业信息
def professiongroup(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        tempUser = request.session.get("tempUser", "none")
        if tempUser != 'none':
            return render_to_response("professiongroup.html", {'tempUser':tempUser, 'loginUser':loginUser})
        else:
            return render_to_response("professiongroup.html")
    except:
        tempUser = request.session.get("tempUser", "none")
        if tempUser != 'none':
            return render_to_response("professiongroup.html", {'tempUser':tempUser})
        else:
            return render_to_response("professiongroup.html")
#专业分数线
def professionscore(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        tempUser = request.session.get("tempUser", "none")
        if tempUser != 'none' :
            return render_to_response("professionscore.html", {'tempUser':tempUser, 'loginUser':loginUser})
        else:
            return render_to_response("professionscore.html")
    except:
        tempUser = request.session.get("tempUser", "none")
        if tempUser != 'none' :
            return render_to_response("professionscore.html", {'tempUser':tempUser})
        else:
            return render_to_response("professionscore.html")
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
        tempUser = request.session.get("tempUser", "none")
        stuProvince = tempUser["stuProvince"]
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
    else:
        SchoolData = getSchoolInfo(request)
        schoolName = SchoolData["SchoolName"]
        stuType = '理科'
        proidInfo = {}
        proidInfo['schoolName'] = schoolName
        proidInfo['stuProvince'] = stuProvince
        proidInfo['stuType'] = stuType
        return render_to_response("schoolenrol.html", {'schoolinfo':SchoolData, 'proidInfo':proidInfo, 'loginUser':loginUser})
def PageSplit(page, length):
    "提供页数和数据总长度返回切片起点和终点"
    start = (int(page) - 1) * 10
    if length - start < 10:
        end = length
    else:
        end = start + 10
    return start, end
def recommendSchoolName(stuProvince, stuType, Year, score, page):
    """推荐学校
    http://127.0.0.1:8000/api_recommendSchool/?stuProvince=江西&stuType=文科&year=2014&score=468&page=1
    Get：studentProvince(生源地)studentType(1为文科,2为理科)year(当年年限)score(分数)page(数据切页数，每页10条数据)
    Response:{"PageNum": 11, , "Result": "True", "Msg": "Success", "Page": 1,
        "Data": [["江西服装学院", "服装与服饰设计", 2015, "本科三批", 18, 447, 25327, -9]], 
        "Batch": {"Province": "江西", "Bacth": "本科三批", "StuType": "文科", "BatchLine": 450, "Year": "2014"}}
    """
#    stuProvince = request.GET.get("stuProvince")
#    stuType = request.GET.get("stuType")
#    Year = request.GET.get("year")
#    score = request.GET.get("score")
##     rank = request.GET.get("rank")
#    page = int(request.GET.get("page"))
    try:
    #     计算分数对应批次线
        Batch = CollegeAreascoreline.objects.filter(provincearea = stuProvince, studentclass = stuType, dateyear = Year)
        if Batch:
            Batch = [[x.batch, x.scoreline] for x in Batch]#查询所有批次线
            BatchNum = len(Batch) #计算存在多少个批次线
            batchDiff = [int(score) - int(batch[1])  for batch in Batch]#计算当前分数到所有分数线的分差
            batchDiff_abs = [abs(n) for n in batchDiff]
            minDiff = min(batchDiff_abs)#存入最小的分差绝对值
            minDiff_index = batchDiff_abs.index(minDiff)#获取最小分差对应的索引
            scoreDiff = batchDiff[minDiff_index] #应投报的档次线的分差值
            if minDiff > 10 and scoreDiff < 0:  #若最小分值差绝对值大于10而且实际值为负数，说明无法进行补录跳批次录取，需降级
                if batch.index(min(batch)) - 1 <= BatchNum - 1: 
                    stuBatch = Batch[minDiff_index + 1]
                else:
                    return HttpResponse(json.dumps({"Result":"True", "Msg":"请确认是否达到批次线"}))
            else:
                stuBatch = Batch[minDiff_index]
        #查询在分差上下3分区间的学校
        if score:
            schoolList = EwtNewJxMean.objects.filter(province = stuProvince, studenttype = stuType, batch = stuBatch[0], diffscore__lt = (scoreDiff + 3), diffscore__gt = (scoreDiff - 3)).order_by("-year", "-meanscore", "diffscore", "-getnum")
        ListLength = len(schoolList)
        schoolData = []
        for schoollist in schoolList:
            SchoolInfo = {}
            profession = schoollist.profession
            year = schoollist.year
            batch = schoollist.batch
            getnum = schoollist.getnum
            meanscore = schoollist.meanscore
            meanrank = schoollist.meanrank
            diffscore = schoollist.diffscore
            #获取学校名
            SchoolsDetail = ''
            try:
                schoolNames = schoollist.schoolname
                SchoolsDetail = CollegeDetailEwt.objects.get(schoolname = schoolNames)
    #            if "(" in schoolNames:
    #                schoolNames = schoolNames[:schoolNames.index('(')]
    #                SchoolsDetail = CollegeDetailEwt.objects.get(schoolname = schoolNames)
    #            else:
    #                SchoolsDetail = CollegeDetailEwt.objects.get(schoolname = schoolNames)
            except:
                SchoolsDetail = CollegeDetailEwt.objects.get(schoolname = schoollist.schoolname)
                print schoollist.schoolname
                print '匹配学校出错'
            else:   
                SchoolInfo["SchoolName"] = schoollist.schoolname
                SchoolInfo["f985"] = SchoolsDetail.f985
                SchoolInfo["f211"] = SchoolsDetail.f211 
                SchoolInfo["fyan"] = SchoolsDetail.fyan 
                SchoolInfo["Province"] = SchoolsDetail.address if SchoolsDetail.address else "暂无"
                SchoolInfo["Levels"] = SchoolsDetail.levels if SchoolsDetail.levels else "暂无"
                SchoolInfo["attach_to"] = SchoolsDetail.attach_to if SchoolsDetail.attach_to else "暂无"
                SchoolInfo["Rank"] = SchoolsDetail.school_rank 
                SchoolInfo["schoolType"] = SchoolsDetail.schooltype 
                SchoolInfo["character"] = SchoolsDetail.character if SchoolsDetail.character else "不详"
                SchoolInfo["Code"] = SchoolsDetail.schoolid if SchoolsDetail.schoolid else "00000"
                SchoolInfo["Address"] = SchoolsDetail.postal_address.replace("\r", "") if SchoolsDetail.postal_address else "暂无"
                SchoolInfo["Tel"] = SchoolsDetail.tel.replace("\r", "") if SchoolsDetail.tel else "暂无"
                SchoolInfo["KeyDiscipline"] = SchoolsDetail.key_discipline if SchoolsDetail.key_discipline else "不详"
                SchoolInfo["Facukty"] = SchoolsDetail.faculty if SchoolsDetail.faculty else "不详"
                SchoolInfo["OfficeWebsite"] = SchoolsDetail.official_website if SchoolsDetail.official_website else "不详"
                SchoolInfo["school_img"] = SchoolsDetail.school_img
                SchoolInfo["profession"] = profession
                SchoolInfo["year"] = year
                SchoolInfo["batch"] = batch
                SchoolInfo["getnum"] = getnum
                SchoolInfo["meanscore"] = meanscore
                SchoolInfo["meanrank"] = meanrank
                SchoolInfo["diffscore"] = diffscore
           
            schoolData.append(SchoolInfo)
        if page:
            start, end = PageSplit(page, ListLength)
            schoolData = schoolData[start:end]
        
        return schoolData
    except:
        return []
#按分推荐学校
def recommendschool(request):
    try:
        loginUserID = request.session.get("loginUser", "none")
        loginUser = Users.objects.get(id = loginUserID)
        tempUser = {}
        #学校名称
        tempUser['stuProvince'] = request.GET.get("stuProvince")
        tempUser['stuType'] = request.GET.get("stuType")
        tempUser['year'] = request.GET.get("year")
        tempUser['score'] = request.GET.get("score")
        tempUser['page'] = request.GET.get("page")
        recoSchool = recommendSchoolName(tempUser['stuProvince'], tempUser['stuType'], tempUser['year'], tempUser['score'], tempUser['page'])
        print tempUser
        #保存临时的用户成绩分数
        request.session["tempUser"] = tempUser
        return render_to_response("reportedCollege.html", {'tempUser':tempUser, 'recoSchool':recoSchool, 'loginUser':loginUser})
    except:
        tempUser = {}
        #学校名称
        tempUser['stuProvince'] = request.GET.get("stuProvince")
        tempUser['stuType'] = request.GET.get("stuType")
        tempUser['year'] = request.GET.get("year")
        tempUser['score'] = request.GET.get("score")
        tempUser['page'] = request.GET.get("page")
        recoSchool = recommendSchoolName(tempUser['stuProvince'], tempUser['stuType'], tempUser['year'], tempUser['score'], tempUser['page'])
        print tempUser
        #保存临时的用户成绩分数
        request.session["tempUser"] = tempUser
        return render_to_response("reportedCollege.html", {'tempUser':tempUser, 'recoSchool':recoSchool})
    
def auth(func):
    def inner(reqeust, *args, **kwargs):
        v = reqeust.COOKIES.get('user')
        if not v:
            return redirect('/index')
        return func(reqeust, *args, **kwargs)
    return inner

