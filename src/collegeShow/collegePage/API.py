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
        studentProvine = request.GET.get("stuProvince")
        studentType = request.GET.get("stuType")
        studentBatch = request.GET.get("batch")
        studentYear = request.GET.get("year")
        page = int(request.GET.get("page"))
        
        #使用参数过滤数据
        collegeList = CollegeSchoolscoreline.objects.filter(area_student = studentProvine, batch = studentBatch, studentclass = studentType, dateyear = studentYear)
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
        studentProvine = request.GET.get("stuProvince")
        studentType = request.GET.get("stuType")
        studentYear = request.GET.get("year")
        areaList = CollegeAreascoreline.objects.filter(provincearea = studentProvine, studentclass = studentType, dateyear = studentYear)
        if len(areaList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for area in areaList:
            Batch = area.batch
            ScoreLine = area.scoreline
            resultList.append([studentProvine, studentType, studentYear, Batch, ScoreLine])
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
    studentProvine = request.GET.get("stuProvince")
    studentType = request.GET.get("stuType")
    studentYear = request.GET.get("year")
#     try:
    parmList = CollegeScoreparm.objects.filter(province = studentProvine, category = studentType, years = studentYear)
    print parmList
    if len(parmList) == 0:
        return HttpResponse(json.dumps(SuccessResponse))
    resultList = []
    for parm in parmList:
        score = parm.score
        num = parm.num
        resultList.append([studentProvine, studentType, studentYear, score, num])
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

def showProfession(request):
    """专业信息API
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
        if len(ProfessionList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for profession in ProfessionList:
            Code = profession.major_code
            Name = profession.major_name
            Degree = profession.major_degree
            needTime = profession.major_time
            Course = profession.major_course
            resultList.append([Code, Name, Degree, needTime, Course])
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse, encoding = 'utf8', ensure_ascii = False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))

def showProfessionRank(request):
    """专业信息API
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
        studentProvine = request.GET.get("stuProvince")
        studentType = request.GET.get("stuType")
        Score = int(request.GET.get("score"))
        page = int(request.GET.get("page"))
        if ProvinceDict[studentProvine.encode("utf8")]:
            tempObject = ProvinceDict[studentProvine.encode("utf8")]
        else:
            return HttpResponse(json.dumps(ErrorResponse))
        DataList = tempObject.objects.filter(province = studentProvine, studenttype = studentType, score = Score).order_by("-year", "-batch", "rank")
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
        return HttpResponse(json.dumps(ErrorResponse))


def login(request):
    if request.method == "POST":
        Name= request.POST.get("username")
        PassWd = request.POST.get("password")
        if Name and PassWd:
            try:
                loginUser = Users.objects.get(username = Name,password = PassWd)
                print loginUser.username
            except:
                return HttpResponse(json.dumps({"Result":"False","Msg":"用户不存在或密码错误"}))
            else:
                request.session["loginUser"] = loginUser.id
#                     request.session["loginUser"] = loginUser
                return HttpResponse(json.dumps({"Result":"True","Msg":"登录成功"}))
    else:
        return HttpResponse(json.dumps({"Result":"False","Msg":"请使用POST请求"}))

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
                    return HttpResponse(json.dumps({"Result":"False","Msg":"用户已存在"}))
            except:
                user = Users(username=Name,password=PassWd,stuprovince=stuProvince,stutype=stuType)
                user.save()
                request.session["loginUser"] = user.id
                return HttpResponse(json.dumps({"Result":"True","Msg":"注册成功"}))
        else:
            return HttpResponse(json.dumps({"Result":"False","Msg":"请完整填写信息"}))
    else:
        return HttpResponse(json.dumps({"Result":"False","Msg":"请使用POST请求"}))
