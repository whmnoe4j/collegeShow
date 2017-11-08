#coding=utf-8 
from django.shortcuts import render, render_to_response, redirect

from models import *
from django.http.response import HttpResponse
import json
import time
import datetime

#带参数的装饰器 登录用户和临时用户的验证
def auth_user(webName = None):
    def decorator(func):
        def inner(request, *args, **kwargs):
            #print '=============='
            #print webName
            if request.META.has_key('HTTP_X_FORWARDED_FOR'):  
                ip = request.META['HTTP_X_FORWARDED_FOR']  
            else:  
                ip = request.META['REMOTE_ADDR']
            #print ip 
            #判断是否是登录用户
            loginUser = request.session.get("loginUser", "none")
            if loginUser != 'none':
                if loginUser.status == 0:
                    #print u'该账号被冻结'
                    del request.session['loginUser']
                    return HttpResponse("该账号被冻结，请联系管理员！返回<a href='/'>首页</a>")
                else:
                    return render_to_response(webName, {'loginUser':loginUser})
            else:
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
                #return func(request, *args, **kwargs)
        return inner
    return decorator

#判断用户是否被冻结
def auth_isStatus(func):
    def inner(request, *args, **kwargs):
        #判断是否是登录用户
        loginUser = request.session.get("loginUser", "none")
        if loginUser != 'none':
            if loginUser.status == 0:
                #print u'该账号被冻结'
                del request.session['loginUser']
                return HttpResponse("该账号被冻结，请联系管理员！返回<a href='/'>首页</a>")
            else:
                return func(request, *args, **kwargs)
        else:
            #临时用户
            return func(request, *args, **kwargs)
    return inner
#判断用户是否VIP
def auth_isVip(func):
    def inner(request, *args, **kwargs):
        #判断是否是登录用户
        loginUser = request.session.get("loginUser", "none")
        if loginUser != 'none':
            if loginUser.type < 1:
                #print u'该账号被冻结'
                #del request.session['loginUser']
                #return render_to_response("bevip.html", {'loginUser':loginUser})
                return redirect(bevip)
            else:
                return func(request, *args, **kwargs)
        else:
            #临时用户
            #return func(request, *args, **kwargs)
            return redirect(register)
    return inner

#@auth_isVip
def reportedCollege(request):
    loginUser = request.session.get("loginUser", "none")

    if request.method == 'POST':
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
        if loginUser != 'none':
            loginUser.score = tempUser['score']
            loginUser.stuType = tempUser['stuType']
            loginUser.rank = tempUser['rank']
            loginUser.stuProvince = tempUser['stuProvince']
            return render_to_response("reportedCollege.html", { 'loginUser':loginUser})
        else:
            #保存临时的用户成绩分数
            request.session["tempUser"] = tempUser
            return render_to_response("reportedCollege.html", {'tempUser':tempUser})
    else:
        if loginUser != 'none':
            return render_to_response("reportedCollege.html", { 'loginUser':loginUser})
        tempUser = request.session.get("tempUser", "none")
        if tempUser == "none":
            return render_to_response("reportedCollege.html")
        else:
            return render_to_response("reportedCollege.html", {'tempUser':tempUser})


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
@auth_isStatus
def schoolinfo(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser != "none":
        SchoolData = getSchoolInfo(request)
        return render_to_response("school_info.html", {'schoolinfo':SchoolData, 'loginUser':loginUser})
    else:
        SchoolData = getSchoolInfo(request)
        return render_to_response("school_info.html", {'schoolinfo':SchoolData})
#获取学校信息
@auth_isStatus
def getSchoolInfo(request):
    SchoolInfo = {}
    try:
        #学校名称
        schoolName = request.GET.get("schoolName", "江西师范大学")
        SchoolList = CollegeDetailEwt.objects.filter(schoolname = schoolName)
        ListLength = len(SchoolList)
        if ListLength == 0:
            return HttpResponse('没有该学校信息!')
        
        for school in SchoolList:
            SchoolInfo["id"] = school.id
            #print SchoolInfo["id"]
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
@auth_isStatus
def schoolmajor(request):
    SchoolInfo = getSchoolInfo(request)
    loginUser = request.session.get("loginUser", "none")
    #学校名称
    schoolName = request.GET.get("schoolName")
    #为什么会连续访问两次呢？
    SchoolMajor = CollegeMajor.objects.filter(schoolname = schoolName)
    ListLength = len(SchoolMajor)
    if ListLength == 0:
        return HttpResponse('没有该学校信息!')
    SchoolMajors = []
    #print ListLength
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
    if loginUser != "none":
        return render_to_response("school_major.html", {'schoolMajors':SchoolMajors, 'schoolinfo':SchoolInfo, 'loginUser':loginUser})
    else:
        
        return render_to_response("school_major.html", {'schoolMajors':SchoolMajors, 'schoolinfo':SchoolInfo})
#历年分数线
@auth_isStatus
def schoolenrol(request):
    loginUser = request.session.get("loginUser", "none")
    SchoolData = getSchoolInfo(request)
    stuProvince = SchoolData["Province"]
    schoolName = SchoolData["SchoolName"]
    stuType = '理科'
    proidInfo = {}
    proidInfo['schoolName'] = schoolName
    proidInfo['stuProvince'] = stuProvince
    proidInfo['stuType'] = stuType
    #print loginUser
    if loginUser != "none":
        return render_to_response("schoolenrol.html", {'schoolinfo':SchoolData, 'proidInfo':proidInfo, 'loginUser':loginUser})
    else:
        
        return render_to_response("schoolenrol.html", {'schoolinfo':SchoolData, 'proidInfo':proidInfo})
    
    
#添加收藏
@auth_isStatus
def collect(request):
    if request.method == 'POST':
        userId = int(request.POST['user_id'])
        #print userId
        collegeId = int(request.POST['college_id'])
        #print collegeId
        
        collection = Collection()
        collection.user = Users.objects.get(id = userId)
        if collegeId != -1:
            collection.college = CollegeDetailEwt.objects.get(id = collegeId)
        collection.save()
        return HttpResponse('collect success')

#收藏功能
@auth_isStatus
def showCollect(request):
    if request.method == 'GET':
        #判断是否是登录用户
        loginUser = request.session.get("loginUser", "none")
        if loginUser != 'none':
            collections = Collection.objects.filter(user = loginUser)
            collectSchools = []
            for collect in collections:
                SchoolData = {}
                #print collect.college.schoolname 
                SchoolData["SchoolName"] = collect.college.schoolname 
                collectSchools.append(SchoolData)
            return HttpResponse(json.dumps(collectSchools))
        else:
            return HttpResponse(json.dumps([]))
        
    #CollegeMajor.objects.filter(schoolname = schoolName)      
@auth_isStatus
def userInfo(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser != 'none':
        collections = Collection.objects.filter(user = loginUser)
    
        return render_to_response("user_info.html", {"loginUser":loginUser, "collections":collections})
    else:
        return redirect("/")
#修改信息
@auth_isStatus
def updateInfo(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser != "none":
        if request.method == "POST":
            #Name = request.POST.get("username")
            sex = request.POST.get("sex")
            stuProvince = request.POST.get("stuProvince")
            stuType = request.POST.get("stuType")
            schoolAddress = request.POST.get("schoolAddress")
            score = request.POST.get("score")
            rank = request.POST.get("rank")
            loginUser = Users.objects.get(id = loginUser.id)
            #loginUser.username = Name
            loginUser.sex = sex
            loginUser.stuprovince = stuProvince
            loginUser.stutype = stuType
            loginUser.schooladdress = schoolAddress
            loginUser.score = score
            loginUser.rank = rank
           
            loginUser.save()
            request.session["loginUser"] = loginUser
        return redirect("/userInfo")
    else:
        
        return redirect("/")

#删除收藏
@auth_isStatus
def deleCollect(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser != "none":
        collect_id = int(request.GET.get("collect_id"))
        Collection.objects.filter(user = loginUser, college_id = collect_id).delete()
        return redirect("/userInfo")
    else:
        return redirect("/")
    

#登录注册
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #print username, password
        try:
            if "@" in username:
                loginUser = Users.objects.get(email = username)
            else:
                loginUser = Users.objects.get(username = username)
        except:
            #print u'用户名不存在'
            return HttpResponse(json.dumps({"result":False, "errorMsg":"用户名不存在"}))
        else:
            if loginUser:
                if loginUser.password == password:
                    lastlogin_date = time.strftime("%Y-%m-%d %X", time.localtime(time.time()))
                    loginUser.lastlogin_date = lastlogin_date
                    loginUser.save()
                    request.session["loginUser"] = loginUser
                    return HttpResponse(json.dumps({"result":True, "errorMsg":"登录成功"}))
                else:
                    return HttpResponse(json.dumps({"result":False, "errorMsg":"密码错误"}))
def logout(request):
    try: 
        del request.session["loginUser"]  #删除session
        return redirect("index")
    except:
        return redirect("index")
@auth_isStatus
def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        realname = request.POST.get("realname")
        tel = request.POST.get("tel")
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        stuProvince = request.POST.get("stuProvince")
        stuType = request.POST.get("stuType")
        stuScore = request.POST.get("score")
        sex = request.POST.get("sex")
        
        #print email, realname, tel
        try:
            user = Users.objects.get(email = email)
            if user:
                return HttpResponse("注册失败,该邮箱已经注册,请重新注册！")
            user_name = Users.objects.get(username = username)
            if user_name:
                return HttpResponse("注册失败,该用户名已存在,请重新注册！<a href='/register'>返回</a>")
        except:
            regression_date = time.strftime("%Y-%m-%d %X", time.localtime(time.time()))
            user = Users(email = email, username = username, password = password, stuprovince = stuProvince, stutype = stuType, sex = sex, score = stuScore, tel = tel, real_name = realname, rank = 0, status = 1, type = 0, schooladdress = '', regression_date = regression_date)
            user.save()
            request.session["loginUser"] = user
            return redirect("reportedCollege")
        else:
            return HttpResponse("注册失败")
    else:
        loginUser = request.session.get("loginUser", "none")
        if loginUser != "none":
            return render_to_response("register.html", {"loginUser":loginUser})
        else:
            return render_to_response("register.html")
#成为Vip
@auth_user(webName = "bevip.html")
def bevip(request):
    pass
@auth_user(webName = "success.html")
def success(request):
    pass
#订单
def order(request):
    loginUser = request.session.get("loginUser", "none")
    
    if request.method == "POST":
        
        username = request.POST.get("username")
        zhifu_name = request.POST.get("zhifu_name")
        zhifu_order = request.POST.get("zhifu_order")
        date = datetime.datetime.now()
        order = Order()
        if loginUser != "none":
            order.user = loginUser
        else:
            loginUser = Users(email = "test@qq.com", username = username, password = "123123", stuprovince = "江西", stutype = "理科", sex = "男", score = 0, tel = "", real_name = "", rank = 0, status = 1, type = 0, schooladdress = '', regression_date = date)
            loginUser.save()
            order.user = loginUser
            request.session["loginUser"] = loginUser
        order.username = loginUser.username
        order.zhifu_name = zhifu_name
        order.zhifu_order = zhifu_order
        order.count = 9.9
        order.createtime = date
        order.save()
        return render_to_response("success.html", {"loginUser":loginUser})
    else:
        loginUser = request.session.get("loginUser", "none")
        request.session["loginUser"] = loginUser
        #return render_to_response("success.html", {"loginUser":loginUser})
        return redirect(success)

#注册验证
def validregister(request):
    if request.method == "POST":
        username = request.POST.get("username")
        message = {'status': "error", 'message': '注册失败,该邮箱已经注册,请重新注册！'}
        email = request.POST.get("email")
        try:  
            user_email = Users.objects.get(email = email)
            print user_email 
            message["message"] = '注册失败,该邮箱已经注册,请重新注册！'
            return HttpResponse('注册失败,该邮箱已经注册,请重新注册！')
        except: 
            return HttpResponse('注册失败,该邮箱已经注册,请重新注册！')
            pass
#        try:  
#            user_username = Users.objects.get(username = username)
#            print user_username 
#            message["message"] = "注册失败,该用户名已存在,请重新注册！<a href='/register'>返回</a>"
#            return HttpResponse("注册失败,该用户名已存在,请重新注册！<a href='/register'>返回</a>")
#        except: 
#            pass
#        return None
    else:
        return redirect(register)

#模糊查询
def likesearch(request):
    if request.method == 'POST':
        input_text = request.POST.get("input_text", "江西师范大学")
        SchoolList = CollegeDetailEwt.objects.filter(schoolname__contains = input_text)[1:10]
        data = []
        if SchoolList is [] or input_text is "" or input_text is None:
            return HttpResponse(json.dumps(data))
        for school in SchoolList:
            data.append(school.schoolname)
        return HttpResponse(json.dumps(data))
    else:
        data = ['error']
        return HttpResponse(data)

