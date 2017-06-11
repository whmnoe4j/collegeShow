# coding=UTF-8
'''
Created on 2017年6月4日
@author: ZWT
'''
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response, redirect

from models import *

import json
import numpy as np

SchoolTypeList = ["综合", "工科", "农业", "林业", "医药", "政法", "师范", "财经", "民族", "语言", "艺术", "军事", "体育", "其他"]
# BatchList = ["本科提前批","本科一批","本科二批","本科三批","专科提前批","专科批","专科一批","专科二批"]
# StudentTypeList =["文科","理科","综合","其他"]
# SubjectTypeList = ["本科","高职专科"]
ProvinceDict = {"安徽":EwtNewAnhui, "甘肃":EwtNewGansu, "河南":EwtNewHenan, "湖南":EwtNewHunan, "江西":EwtNewJiangxi, "吉林":EwtNewJilin, "山东":EwtNewShandong, "山西":EwtNewShanxi, "四川":EwtNewSichuan}
spcProvinceDict = {"江苏":EwtNewJiangsu, "浙江":EwtNewZhejiang}

def PageSplit(page, length):
    "提供页数和数据总长度返回切片起点和终点"
    start = (int(page) - 1) * 10
    if length - start < 10:
        end = length
    else:
        end = start + 10
    return start, end
##################################################API调用函数##########################################################

def showCollege(request):
    """院校信息API
    http://127.0.0.1:8000/college/?schoolProvince=江西&schoolType=1&page=3
    Get：schoolProvince(院校所在地)schoolType(办学类型,参考全局列表SchoolTypeList)batch(录取批次)page(数据切页数，每页10条数据)
    Response:{"Msg": "Success", "Length": 29, "Result": "True", "Page": 3
        "Data": [{"Province": "江西", "Code": "40066", "隶属单位": "江西省教育厅", "211": "False", "研": "False", "KeyDiscipline": "0个", "SchoolName": "赣西科技职业学院", "Rank": "暂无", "985": "False", "Facukty": "院士：0人 博士点：0个 硕士点：0个", "Levels": "高职(专科)", "Address": "江西省新余市劳动北路919号", "OfficeWebsite": "http://www.ganxidx.com", "Tel": "0790-6736399，6490308", "Type": "综合", "Class": "民办"}]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        schoolProvince = request.GET.get("schoolProvince")
        schoolType = request.GET.get("schoolType")
        #levels = request.GET.get("levels")
        character = request.GET.get("character")
        page = int(request.GET.get("page"))
        
        SchoolList = CollegeDetailEwt.objects.filter(character = character, address = schoolProvince, schooltype = schoolType).order_by("school_rank")
        ListLength = len(SchoolList)
        if ListLength == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for school in SchoolList:
            SchoolData = {}
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
            resultList.append(SchoolData)
        if page:
            start, end = PageSplit(page, ListLength)
            resultList = resultList[start:end]
            SuccessResponse["PageNum"] = int(ListLength / 10) + 1
            SuccessResponse["Page"] = page
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))

def showCollegeSchoolScoreLine(request):
    """院校分数线API
    http://127.0.0.1:8000/collegescoreline/?stuProvince=江西&batch=3&stuType=1&year=2014&page=1
    Get：stuProvince(生源地)stuType(1为文科2为理科3为综合4为其他)batch(录取批次)year(录取年份)page(数据切页数，每页10条数据)
    Response:{"Msg": "Success", "Start": 0, "Length": 359, "Result": "True",
        "Data": [["北京信息科技大学", "北京", "2014", 528, 523], ["北京联合大学", "北京", "2014", 523, 522]]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        #从get中提取参数
        studentProvince = request.GET.get("stuProvince")
        studentType = request.GET.get("stuType")
        studentBatch = request.GET.get("batch")
        studentYear = request.GET.get("year")
        page = int(request.GET.get("page"))
        
        #使用参数过滤数据
        collegeList = CollegeSchoolscoreline.objects.filter(area_student = studentProvince, batch = studentBatch, studentclass = studentType, dateyear = studentYear)
        ListLength = len(collegeList)
        if ListLength == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        #初始化数据列表
        resultList = []
        for college in collegeList:
            schoolName = college.name_school
            schoolProvince = college.area_school
            maxScore = college.maxscore
            meanScore = college.meanscore
            resultList.append([schoolName, schoolProvince, studentYear, maxScore, meanScore])
        if page:
            start, end = PageSplit(page, ListLength)
            resultList = resultList[start:end]
            SuccessResponse["PageNum"] = int(ListLength / 10) + 1
            SuccessResponse["Page"] = page
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))
    
def showAreaScoreLine(request):
    """地区分数线API
    http://127.0.0.1:8000/areascoreline/?stuProvince=江西&stuType=1&year=2014
    Get：stuProvince(生源地)stuType(1为文科2为理科3为综合4为其他)year(录取年份)
    Response:{"Msg": "Success","Result": "True",
        "Data": [["江西", "文科", "2014", "本科一批", 524], ["江西", "文科", "2014", "本科二批", 479], ["江西", "文科", "2014", "本科三批", 450]]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        #从get中提取参数
        studentProvince = request.GET.get("stuProvince")
        studentType = request.GET.get("stuType")
        studentYear = request.GET.get("year")
        areaList = CollegeAreascoreline.objects.filter(provincearea = studentProvince, studentclass = studentType, dateyear = studentYear)
        if len(areaList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for area in areaList:
            Batch = area.batch
            ScoreLine = area.scoreline
            resultList.append([studentProvince, studentType, studentYear, Batch, ScoreLine])
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))

def showScoreParm(request):
    """一分一段表
    http://127.0.0.1:8000/scoreparm/?stuProvince=江西&stuType=1&year=2015
    Get：stuProvince(生源地)stuType(1为文科2为理科)year(录取年份)
    Response:{"Msg": "Success","Result": "True",
        "Data": [["江西", "文科", "2015", "637-750", 2], ["江西", "文科", "2015", "634", 1]]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    studentProvince = request.GET.get("stuProvince")
    studentType = request.GET.get("stuType")
    studentYear = request.GET.get("year")
#     try:
    parmList = CollegeScoreparm.objects.filter(province = studentProvince, category = studentType, years = studentYear)
    print parmList
    if len(parmList) == 0:
        return HttpResponse(json.dumps(SuccessResponse))
    resultList = []
    for parm in parmList:
        score = parm.score
        num = parm.num
        resultList.append([studentProvince, studentType, studentYear, score, num])
    SuccessResponse["Data"] = resultList
    return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
#     except:
#         return HttpResponse(json.dumps(ErrorResponse))

def showSubjectGroup(request):
    """专业大类类别API
    http://127.0.0.1:8000/subjectgroup/?subjectType=1
    Get：subjectType(1为本科,2为高职专科)
    Response:{"Msg": "Success", "Result": "True",
        "Data": ["历史学", "艺术学", "管理学", "工学", "经济学", "教育学", "农学", "文学", "哲学", "医学", "理学", "法学"]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        subjectType = request.GET.get("subjectType")
        subjectQuery = Profession.objects.filter(subject_type = subjectType).query
        subjectQuery.group_by = ['subject_name']
        SubjectGroupList = QuerySet(query = subjectQuery, model = Profession)
        if len(SubjectGroupList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for group in SubjectGroupList:
            resultList.append(group.subject_name)
        resultList = list(set(resultList))
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))

def showMajorGroupList(request):
    """专业类型细分API
    http://127.0.0.1:8000/majorgroup/?subjectType=1&subjectName=艺术学
    Get：subjectType(1为本科,2为高职专科)subjectName(专业大类名)
    Response:{"Msg": "Success", "Result": "True",
        "Data":  ["音乐与舞蹈学类", "设计学类", "美术学类", "艺术学理论类", "戏剧与影视学类"]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        subjectType = request.GET.get("subjectType")
        subjectName = request.GET.get("subjectName")
        MajorGroupQuery = Profession.objects.filter(subject_type = subjectType, subject_name = subjectName).query
        MajorGroupQuery.group_by = ['major_class']
        MajorGroupList = QuerySet(query = MajorGroupQuery, model = Profession)
        if len(MajorGroupList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for major in MajorGroupList:
            resultList.append(major.major_class)
        resultList = list(set(resultList))
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))

def showProfessionSmall(request):
    """专业小类别API
    http://127.0.0.1:8000/profession/?subjectType=1&subjectName=艺术学&majorClass=美术学类
    Get：subjectType(1为本科,2为高职专科)subjectName(专业大类名)majorClass(专业子类名)
    Response:{"Msg": "Success", "Result": "True",
        "Data":  [["130402","绘画", "艺术学学士", "四年", "主干课程：主干学科：艺术学素描、色彩、专业技法、创作、中外美术史主要实践性教学环节：社会实践、艺术考察，每年1--2次，一般安排4--6周。"]]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        subjectType = request.GET.get("subjectType")
        majorClass = request.GET.get("majorClass")
        ProfessionList = Profession.objects.filter(subject_type = subjectType, major_class = majorClass)
        if len(ProfessionList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for profession in ProfessionList:
            Name = profession.major_name
            resultList.append(Name)
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))
    
def showProfession(request):
    """专业详细信息API
    http://127.0.0.1:8000/profession/?subjectType=1&subjectName=艺术学&majorClass=美术学类
    Get：subjectType(1为本科,2为高职专科)subjectName(专业大类名)majorClass(专业子类名)
    Response:{"Msg": "Success", "Result": "True",
        "Data":  [["130402","绘画", "艺术学学士", "四年", "主干课程：主干学科：艺术学素描、色彩、专业技法、创作、中外美术史主要实践性教学环节：社会实践、艺术考察，每年1--2次，一般安排4--6周。"]]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        subjectType = request.GET.get("subjectType")
        subjectName = request.GET.get("subjectName")
        majorClass = request.GET.get("majorClass")
        ProfessionList = Profession.objects.filter(subject_type = subjectType, subject_name = subjectName, major_class = majorClass) 
#        ProfessionList = Profession.objects.filter(subject_type = subjectType, subject_name = subjectName)
        if len(ProfessionList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for profession in ProfessionList:
            Code = profession.major_code
            Name = profession.major_name
            Degree = profession.major_degree
            needTime = profession.major_time
            Course = profession.major_course
            resultList.append([ Name, Code, Degree, needTime, Course])
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))

def showProfessionRank(request):
    """专业排名API
    http://127.0.0.1:8000/professionrank/?professionCode=130402
    http://127.0.0.1:8000/professionrank/?professionName=绘画
    Get：professionCode(专业代码)professionName(专业名称)
    Response:{"Msg": "Success", "Result": "True",
        "Data":  ["绘画", "四川大学", 1], ["绘画", "吉林大学", 2], ["绘画", "南开大学", 3]]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        professionCode = request.GET.get("professionCode")
        professionName = request.GET.get("professionName")
        if professionCode:
            RankList = ProfessionRank.objects.filter(major_code = professionCode)
        if professionName:
            RankList = ProfessionRank.objects.filter(major_name = professionName)
        if len(RankList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for profession in RankList:
            Name = profession.major_name
            SchooName = profession.rank_school
            RankNum = profession.rank_num
            resultList.append([Name, SchooName, RankNum])
            
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))

def sameScore(request):
    """同分考生去向
    http://127.0.0.1:8000/samescore/?stuProvince=江西&stuType=1&score=600&page=1
    Get：studentProvince(生源地)studentType(1为文科,2为理科)page(数据切页数，每页10条数据)
    Response:{"Msg": "Success", "Length": 81, "Result": "True", "Page": 1,
    "Data": [[2015, "本科", "本科提前批", 133, "港澳台", "香港中文大学(深圳)", "经济管理试验班"]]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        studentProvince = request.GET.get("stuProvince")
        studentType = request.GET.get("stuType")
        Score = int(request.GET.get("score"))
        page = int(request.GET.get("page"))
        print studentProvince, studentType, Score, page
        if ProvinceDict[studentProvince.encode("utf8")]:
            tempObject = ProvinceDict[studentProvince.encode("utf8")]
            
        else:
            return HttpResponse(json.dumps(ErrorResponse))
        DataList = tempObject.objects.filter(province = studentProvince, studenttype = studentType, score = Score).order_by("-year", "-batch", "rank")
        ListLength = len(DataList)
        
        if ListLength == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for data in DataList:
            d_year = data.year
            d_levels = data.levels
            d_batch = data.batch
            d_rank = data.rank
            d_schoolProvince = data.school_province
            d_schoolName = data.schoolname
            d_profession = data.profession
            resultList.append([d_year, d_levels, d_batch, d_rank, d_schoolProvince, d_schoolName, d_profession])
        if page:
            start, end = PageSplit(page, ListLength)
            resultList = resultList[start:end]
            SuccessResponse["PageNum"] = int(ListLength / 10) + 1
            SuccessResponse["Page"] = page
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        print u'数据库不存在该表:' 
        return HttpResponse(json.dumps(ErrorResponse))


def login(request):
    if request.method == "POST":
        Name = request.POST.get("username")
        PassWd = request.POST.get("password")
        if Name and PassWd:
            try:
                loginUser = Users.objects.get(username = Name, password = PassWd)
                print loginUser.username
            except:
                return HttpResponse(json.dumps({"Result":"False", "Msg":"用户不存在或密码错误"}))
            else:
                request.session["loginUser"] = loginUser.id
#                     request.session["loginUser"] = loginUser
                return HttpResponse(json.dumps({"Result":"True", "Msg":"登录成功"}))
    else:
        return HttpResponse(json.dumps({"Result":"False", "Msg":"请使用POST请求"}))

def logout(request):
    try: 
        del request.session["loginUser"]  #删除session
        return render_to_response("index.html")
    except:
        return render_to_response("index.html")

def register(request):
    if request.method == "POST":
        Name = request.POST.get("username")
        PassWd = request.POST.get("password")
        stuProvince = request.POST.get("stuProvince")
        stuType = request.POST.get("stuType")
        if Name and PassWd and stuProvince and stuType:
            try:
                user = Users.objects.get(username = Name)
                if user:
                    return HttpResponse(json.dumps({"Result":"False", "Msg":"用户已存在"}))
            except:
                user = Users(username = Name, password = PassWd, stuprovince = stuProvince, stutype = stuType)
                user.save()
                request.session["loginUser"] = user.id
                return HttpResponse(json.dumps({"Result":"True", "Msg":"注册成功"}))
        else:
            return HttpResponse(json.dumps({"Result":"False", "Msg":"请完整填写信息"}))
    else:
        return HttpResponse(json.dumps({"Result":"False", "Msg":"请使用POST请求"}))

def professionscore(request):
    """专业分数线
    http://127.0.0.1:8000/api_professionscore/?stuProvince=山东&batch=本科一批&stuType=文科&year=2015&page=1
    Get：studentProvince(生源地)studentType(1为文科,2为理科)page(数据切页数，每页10条数据)
    Response:{"Msg": "Success", "Length": 81, "Result": "True", "Page": 1,
    "Data": [[2015, "本科", "本科提前批", 133, "港澳台", "香港中文大学(深圳)", "经济管理试验班"]]}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        #考生位置
        studentProvince = request.GET.get("stuProvince")
        #院校位置
        schProvince = request.GET.get("schProvince")
        #录取批次
        batch = request.GET.get("batch")
        #考生文理科
        studentType = request.GET.get("stuType")
        #高考年份
        year = int(request.GET.get("year"))
        
        page = int(request.GET.get("page"))
        print studentProvince, batch, studentType, year, page
        if ProvinceDict[studentProvince.encode("utf8")]:
            tempObject = ProvinceDict[studentProvince.encode("utf8")]
            
        else:
            return HttpResponse(json.dumps(ErrorResponse))
        DataList = tempObject.objects.filter(province = studentProvince, school_province = schProvince, batch = batch, studenttype = studentType, year = year).order_by("-year", "-batch", "rank")
        ListLength = len(DataList)
        
        if ListLength == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for data in DataList:
            
            d_schoolName = data.schoolname
            d_profession = data.profession
            d_score = data.score
            d_rank = data.rank
            d_levels = data.levels
            d_admission_number = data.admission_number
            d_batch = data.batch
            d_studenttype = data.studenttype
            d_year = data.year
            d_schoolProvince = data.school_province
            resultList.append([d_schoolName, d_profession, d_score, d_rank, d_batch, d_levels, d_admission_number, d_studenttype, d_year , d_schoolProvince])
        if page:
            start, end = PageSplit(page, ListLength)
            resultList = resultList[start:end]
            SuccessResponse["PageNum"] = int(ListLength / 10) + 1
            SuccessResponse["Page"] = page
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        print u'数据库不存在该表:' 
        return HttpResponse(json.dumps(ErrorResponse))

def editUser(request):
    """个人中心信息修改api"""
    if request.method == "POST":
        Name = request.POST.get("username")
        sex = request.POST.get("sex")
        stuProvince = request.POST.get("stuProvince")
        stuType = request.POST.get("stuType")
        schoolAddress = request.POST.get("schoolAddress")
        score = request.POST.get("score")
        
        loginUserID = request.session.get("loginUser", "none")
        if loginUserID:
            loginUser = Users.objects.get(id = loginUserID)
            loginUser.username = Name
            loginUser.sex = sex
            loginUser.stuprovince = stuProvince
            loginUser.schooladdress = schoolAddress
            loginUser.score = score
            loginUser.save()
            return HttpResponse(json.dumps({"Result":"True", "Msg":"Success"}))
        else:
            return render_to_response("index.html")

def recommendSchool(request):
    """推荐学校
    http://127.0.0.1:8000/api_recommendSchool/?stuProvince=江西&stuType=文科&year=2014&score=468&page=1
    Get：studentProvince(生源地)studentType(1为文科,2为理科)year(当年年限)score(分数)page(数据切页数，每页10条数据)
    Response:{"PageNum": 11, , "Result": "True", "Msg": "Success", "Page": 1,
        "Data": [["江西服装学院", "服装与服饰设计", 2015, "本科三批", 18, 447, 25327, -9]], 
        "Batch": {"Province": "江西", "Bacth": "本科三批", "StuType": "文科", "BatchLine": 450, "Year": "2014"}}
    """
    SuccessResponse = {"Result":"True", "Msg":"Success", "Data":[]}
    ErrorResponse = {"Result":"False", "Msg":"Error", "Data":[]}
    try:
        stuProvince = request.GET.get("stuProvince")
        stuType = request.GET.get("stuType")
        Year = request.GET.get("year")
        score = request.GET.get("score")
    #     rank = request.GET.get("rank")
        page = int(request.GET.get("page"))
    
    #     计算分数对应批次线
        Batch = CollegeAreascoreline.objects.filter(provincearea=stuProvince,studentclass=stuType,dateyear=Year)
        if Batch:
            Batch = [[x.batch,x.scoreline] for x in Batch]#查询所有批次线
            BatchNum = len(Batch) #计算存在多少个批次线
            batchDiff = [int(score) - int(batch[1])  for batch in Batch]#计算当前分数到所有分数线的分差
            batchDiff_abs = [abs(n) for n in batchDiff]
            minDiff = min(batchDiff_abs)#存入最小的分差绝对值
            minDiff_index = batchDiff_abs.index(minDiff)#获取最小分差对应的索引
            scoreDiff = batchDiff[minDiff_index] #应投报的档次线的分差值
            if minDiff > 10 and scoreDiff < 0:  #若最小分值差绝对值大于10而且实际值为负数，说明无法进行补录跳批次录取，需降级
                if batch.index(min(batch))-1 <= BatchNum -1: 
                    stuBatch = Batch[batch.index(min(batch))+1]
                else:
                    return HttpResponse(json.dumps({"Result":"True", "Msg":"请确认是否达到批次线"}))
            else:
                stuBatch = Batch[batch.index(min(batch))]
        #查询在分差上下3分区间的学校
        if score:
            schoolList = EwtNewJxMean.objects.filter(province=stuProvince,studenttype=stuType,batch=stuBatch[0],diffscore__lt=(scoreDiff+3),diffscore__gt=(scoreDiff-3)).order_by("-year","-meanscore","diffscore","-getnum")
        ListLength = len(schoolList)
        if ListLength == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for school in schoolList:
            name = school.schoolname
            profession = school.profession
            year = school.year
            batch = school.batch
            getnum = school.getnum
            meanscore = school.meanscore
            meanrank = school.meanrank
            diffscore = school.diffscore
            resultList.append([name,profession,year,batch,getnum,meanscore,meanrank,diffscore])
        if page:
            start, end = PageSplit(page, ListLength)
            resultList = resultList[start:end]
            SuccessResponse["PageNum"] = int(ListLength / 10) + 1
            SuccessResponse["Page"] = page
        SuccessResponse["Data"] = resultList
        SuccessResponse["Batch"] = {"Province":stuProvince,"StuType":stuType,"Year":Year,"Bacth":stuBatch[0],"BatchLine":stuBatch[1]}
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
        
        return HttpResponse(json.dumps({"Result":"True", "Msg":"Success"}))
    except:
        return HttpResponse(json.dumps(ErrorResponse))
