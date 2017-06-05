# coding=UTF-8
'''
Created on 2017年6月4日

@author: ZWT
'''
from django.db.models.query import QuerySet
from django.http.response import HttpResponse

from models import CollegeSchoolscoreline
from models import CollegeAreascoreline
from models import Profession
from models import ProfessionRank
from models import Gaokao

import json


BatchList = ["本科提前批","本科一批","本科二批","本科三批","专科提前批","专科批","专科一批","专科二批"]
StudentTypeList =["文科","理科","综合","其他"]
SubjectTypeList = ["本科","高职专科"]

def showCollegeSchoolScoreLine(request):
    """院校分数线API
    http://127.0.0.1:8000/collegescoreline/?stuProvince=江西&batch=3&stuType=1&year=2014&start=0
    Get：stuProvince(生源地)stuType(1为文科2为理科3为综合4为其他)batch(录取批次)year(录取年份)start(数据开始)length(数据长度)
    Response:{"Msg": "Success", "Start": 0, "Length": 359, "Result": "True",
        "Data": [["北京信息科技大学", "北京", "2014", 528, 523], ["北京联合大学", "北京", "2014", 523, 522]]}
    """
    SuccessResponse = {"Result":"True","Msg":"Success","Data":[]}
    ErrorResponse = {"Result":"False","Msg":"Error","Data":[]}
    try:
        #从get中提取参数
        studentProvine = request.GET.get("stuProvince")
        studentType = StudentTypeList[int(request.GET.get("stuType"))-1]
        studentBatch = BatchList[int(request.GET.get("batch"))-1]
        studentYear = request.GET.get("year")
        startPoint = int(request.GET.get("start"))
        
        #使用参数过滤数据
        collegeList = CollegeSchoolscoreline.objects.filter(area_student=studentProvine,batch=studentBatch,studentclass=studentType,dateyear=studentYear)
        collegeListLength = len(collegeList)
        if collegeListLength == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        #初始化数据列表
        resultList = []
        for college in collegeList:
            schoolName = college.name_school
            schoolProvince = college.area_school
            maxScore = college.maxscore
            meanScore = college.meanscore
            resultList.append([schoolName,schoolProvince,studentYear,maxScore,meanScore])
        try:
            resultList = resultList[startPoint:(startPoint+10)]
        except:
            if len(resultList) > 10:
                resultList = resultList[:10]
        SuccessResponse["Data"] = resultList
        SuccessResponse["Length"] = collegeListLength
        SuccessResponse["Start"] = startPoint
        return HttpResponse(json.dumps(SuccessResponse,encoding='utf8',ensure_ascii=False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))
def showAreaScoreLine(request):
    """地区分数线API
    http://127.0.0.1:8000/areascoreline/?stuProvince=江西&stuType=1&year=2014
    Get：stuProvince(生源地)stuType(1为文科2为理科3为综合4为其他)year(录取年份)
    Response:{"Msg": "Success","Result": "True",
        "Data": [["江西", "文科", "2014", "本科一批", 524], ["江西", "文科", "2014", "本科二批", 479], ["江西", "文科", "2014", "本科三批", 450]]}
    """
    SuccessResponse = {"Result":"True","Msg":"Success","Data":[]}
    ErrorResponse = {"Result":"False","Msg":"Error","Data":[]}
    try:
        #从get中提取参数
        studentProvine = request.GET.get("stuProvince")
        studentType = StudentTypeList[int(request.GET.get("stuType"))-1]
        studentYear = request.GET.get("year")
        areaList = CollegeAreascoreline.objects.filter(provincearea=studentProvine,studentclass=studentType,dateyear=studentYear)
        if len(areaList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for area in areaList:
            Batch = area.batch
            ScoreLine = area.scoreline
            resultList.append([studentProvine,studentType,studentYear,Batch,ScoreLine])
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse,encoding='utf8',ensure_ascii=False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))
def showSubjectGroup(request):
    """专业大类类别API
    http://127.0.0.1:8000/subjectgroup/?subjectType=1
    Get：subjectType(1为本科,2为高职专科)
    Response:{"Msg": "Success", "Result": "True",
        "Data": ["历史学", "艺术学", "管理学", "工学", "经济学", "教育学", "农学", "文学", "哲学", "医学", "理学", "法学"]}
    """
    SuccessResponse = {"Result":"True","Msg":"Success","Data":[]}
    ErrorResponse = {"Result":"False","Msg":"Error","Data":[]}
    try:
        subjectType = SubjectTypeList[int(request.GET.get("subjectType"))-1]
        subjectQuery = Profession.objects.filter(subject_type=subjectType).query
        subjectQuery.group_by = ['subject_name']
        SubjectGroupList = QuerySet(query=subjectQuery,model=Profession)
        if len(SubjectGroupList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for group in SubjectGroupList:
            resultList.append(group.subject_name)
        resultList = list(set(resultList))
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse,encoding='utf8',ensure_ascii=False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))
def showMajorGroupList(request):
    """专业类型细分API
    http://127.0.0.1:8000/majorgroup/?subjectType=1&subjectName=艺术学
    Get：subjectType(1为本科,2为高职专科)subjectName(专业大类名)
    Response:{"Msg": "Success", "Result": "True",
        "Data":  ["音乐与舞蹈学类", "设计学类", "美术学类", "艺术学理论类", "戏剧与影视学类"]}
    """
    SuccessResponse = {"Result":"True","Msg":"Success","Data":[]}
    ErrorResponse = {"Result":"False","Msg":"Error","Data":[]}
    try:
        subjectType = SubjectTypeList[int(request.GET.get("subjectType"))-1]
        subjectName = request.GET.get("subjectName")
        MajorGroupQuery = Profession.objects.filter(subject_type=subjectType,subject_name=subjectName).query
        MajorGroupQuery.group_by = ['major_class']
        MajorGroupList = QuerySet(query=MajorGroupQuery,model=Profession)
        if len(MajorGroupList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for major in MajorGroupList:
            resultList.append(major.major_class)
        resultList = list(set(resultList))
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse,encoding='utf8',ensure_ascii=False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))
def showProfession(request):
    """专业信息API
    http://127.0.0.1:8000/profession/?subjectType=1&subjectName=艺术学&majorClass=美术学类
    Get：subjectType(1为本科,2为高职专科)subjectName(专业大类名)majorClass(专业子类名)
    Response:{"Msg": "Success", "Result": "True",
        "Data":  [["130402","绘画", "艺术学学士", "四年", "主干课程：主干学科：艺术学素描、色彩、专业技法、创作、中外美术史主要实践性教学环节：社会实践、艺术考察，每年1--2次，一般安排4--6周。"]]}
    """
    SuccessResponse = {"Result":"True","Msg":"Success","Data":[]}
    ErrorResponse = {"Result":"False","Msg":"Error","Data":[]}
    try:
        subjectType = SubjectTypeList[int(request.GET.get("subjectType"))-1]
        subjectName = request.GET.get("subjectName")
        majorClass = request.GET.get("majorClass")
        ProfessionList = Profession.objects.filter(subject_type=subjectType,subject_name=subjectName,major_class=majorClass) 
        if len(ProfessionList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for profession in ProfessionList:
            Code = profession.major_code
            Name = profession.major_name
            Degree = profession.major_degree
            needTime =  profession.major_time
            Course = profession.major_course
            resultList.append([Code,Name,Degree,needTime,Course])
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse,encoding='utf8',ensure_ascii=False))
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
    SuccessResponse = {"Result":"True","Msg":"Success","Data":[]}
    ErrorResponse = {"Result":"False","Msg":"Error","Data":[]}
    try:
        professionCode = request.GET.get("professionCode")
        professionName = request.GET.get("professionName")
        if professionCode:
            RankList = ProfessionRank.objects.filter(major_code=professionCode)
        if professionName:
            RankList = ProfessionRank.objects.filter(major_name=professionName)
        if len(RankList) == 0:
            return HttpResponse(json.dumps(SuccessResponse))
        resultList = []
        for profession in RankList:
            Name = profession.major_name
            SchooName = profession.rank_school
            RankNum = profession.rank_num
            resultList.append([Name,SchooName,RankNum])
            
        SuccessResponse["Data"] = resultList
        return HttpResponse(json.dumps(SuccessResponse,encoding='utf8',ensure_ascii=False))
    except:
        return HttpResponse(json.dumps(ErrorResponse))
def sameScore(request):
    """同分考生去向"""
    SuccessResponse = {"Result":"True","Msg":"Success","Data":[]}
    ErrorResponse = {"Result":"False","Msg":"Error","Data":[]}
 
    studentProvine = request.GET.get("stuProvince")
    studentType = StudentTypeList[int(request.GET.get("stuType"))-1]
    Score = int(request.GET.get("score"))
    startPoint = request.GET.get("start")
    DataList = Gaokao.objects.filter(studentprovince=studentProvine,studenttype=studentType,score=Score).order_by("-years","-batch","rank")
    if len(DataList) == 0:
        return HttpResponse(json.dumps(SuccessResponse))
    resultList = []
    for data in DataList:
        d_year = data.years
        d_levels = data.levels
        d_batch = data.batch
        d_rank = data.rank
        d_schoolProvince = data.schoolprovince
        d_schoolName = data.schoolname
        d_profession = data.profession
        resultList.append([d_year,d_levels,d_batch,d_rank,d_schoolProvince,d_schoolName,d_profession])
    if startPoint:
        resultList = resultList[int(startPoint):(int(startPoint)+10)]
        SuccessResponse["Length"] = len(DataList)
        SuccessResponse["Start"] = startPoint
    SuccessResponse["Data"] = resultList
    return HttpResponse(json.dumps(SuccessResponse,encoding='utf8',ensure_ascii=False))
    
    