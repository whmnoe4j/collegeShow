#coding=UTF-8
from django.shortcuts import render, render_to_response, redirect
from django.contrib.messages.storage import session
import json
from django.http.response import HttpResponse
from models import *

def auth_admin(func):
    def inner(request, *args, **kwargs):
        #判断是否是登录用户
        loginUser = request.session.get("loginUser", "none")
        if loginUser == 'none':
            return redirect('/sign_in')
        else:
            if loginUser.status == 0:
                print u'该账号被冻结'
                return HttpResponse("该账号被冻结，请联系管理员！返回<a href='/sign_in'>登录</a>")
            #该用户权限不足够
            if loginUser.type != 2:
                print u'该用户权限不足'
                return HttpResponse("该用户权限不足！返回<a href='/sign_in'>登录</a>")
            else:
                print u'管理员!'
                #下面的返回是执行被装饰的函数
                return func(request, *args, **kwargs)
    return inner
#跳转至用户管理后台中心
@auth_admin
def adminIndex(request):
    
    loginUser = request.session.get("loginUser", "none")
    users = Users.objects.order_by('-id')[0:10]
    adminUserCount = Users.objects.filter(type = 2).count()
    vipUserCount = Users.objects.filter(type = 1).count()
    #冻结用户
    warnUserCount = Users.objects.filter(status = 0).count()
    
    userCount = Users.objects.all().count()
    professionCount = Profession.objects.all().count()
    collegeCount = CollegeDetailEwt.objects.all().count()
    jianxiCount = EwtNewJxMean.objects.all().count()
    counts = {}
    counts['adminUserCount'] = adminUserCount
    counts['vipUserCount'] = vipUserCount
    counts['warnUserCount'] = warnUserCount
    counts['userCount'] = userCount
    counts['professionCount'] = professionCount
    counts['collegeCount'] = collegeCount
    counts['jianxiCount'] = jianxiCount
    return render_to_response("admins/index.html", {"users":users, 'adminUser':loginUser, 'counts':counts})

#跳转至所有用户管理
@auth_admin
def adminUsers(request):
    loginUser = request.session.get("loginUser", "none")
    users = find(request, Users)
    return render_to_response("admins/users.html", {"users":users['datas'], 'allPage':users["allPage"], 'curPage':users["curPage"], 'adminUser':loginUser})

#跳转个体用户管理
@auth_admin
def adminUser(request):
    loginUser = request.session.get("loginUser", "none")
    if loginUser == 'none':
        
        return redirect("/sign_in")
    else:
        userId = int(request.GET.get('id', -1))
        print userId
        if userId == -1:
            #默认找到admin的资料
            user = Users.objects.get(id = loginUser.id)
            
            return render_to_response("admins/user.html", {'user':user, 'adminUser':loginUser})
        else:
            user = Users.objects.get(id = userId)
            print user.username
            return render_to_response("admins/user.html", {'user':user, 'adminUser':loginUser})


#跳转登入
def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print username, password
        try:
            loginUser = Users.objects.get(username = username)
        except:
            loginError = u"用户名不存在"
            print loginError
            return render_to_response("admins/sign-in.html", {'loginError':loginError, 'username':username, 'password':password})
        else: 
            if loginUser.password == password:
                request.session["loginUser"] = loginUser
                return redirect("/adminIndex")
            else:
                loginError = "密码错误"
                return render_to_response("admins/sign-in.html", {'loginError':loginError, 'username':username, 'password':password})
    return render_to_response("admins/sign-in.html")

#退出登入
def sign_out(request):
    del request.session["loginUser"]  #删除session
    return redirect("/sign_in")

#翻页的功能
def find(request, dbName):
    
    ONE_PAGE_OF_DATA = 15 
    result = {}
    try:  
        curPage = int(request.GET.get('curPage', '1'))  
        allPage = int(request.GET.get('allPage', '1'))  
        pageType = str(request.GET.get('pageType', ''))  
    except ValueError:  
        curPage = 1  
        allPage = 1  
        pageType = ''  
  
    #判断点击了【下一页】还是【上一页】  
    if pageType == 'pageDown':  
        curPage += 1  
    elif pageType == 'pageUp':  
        curPage -= 1  
    elif pageType == 'pageFirst':
        curPage = 1
    elif pageType == 'pagelast':
        curPage = allPage   
    startPos = (curPage - 1) * ONE_PAGE_OF_DATA  
    endPos = startPos + ONE_PAGE_OF_DATA  
    #datas = dbName.objects.all()[startPos:endPos]  
    datas = dbName.objects.order_by('-id')[startPos:endPos]
  
    if curPage == 1 and allPage == 1: #标记1  
        allPostCounts = dbName.objects.count()  
        allPage = allPostCounts / ONE_PAGE_OF_DATA  
        remainPost = allPostCounts % ONE_PAGE_OF_DATA  
        if remainPost > 0:  
            allPage += 1 
    
    result["datas"] = datas
    result["allPage"] = allPage
    result["curPage"] = curPage
    return result
@auth_admin
def deleteUser(request):
    if request.method == "POST":
        userId = int(request.POST.get('id', 0))
        if userId == 0:
            pass
        else:
            Users.objects.get(id = userId).delete()
            
            return redirect("/adminUsers")
    else:
        return redirect("/sign_in")
    
@auth_admin      
def updateUser(request):
    if request.method == "POST":
        userId = int(request.POST['userId'])
        username = request.POST['username']
        password = request.POST['password']
        sex = request.POST['sex']
        stutype = request.POST['stutype']
        schooladdress = request.POST['schooladdress']
        score = request.POST['score']
        rank = request.POST['rank']
        status = request.POST['status']
        types = request.POST['type']
        if username == "" or rank == '' or password == "":
            return redirect("/adminUsers")
        else:
            user = Users.objects.get(id = userId)
            user.userId = userId
            user.username = username
            user.password = password
            user.sex = sex
            user.stutype = stutype
            user.schooladdress = schooladdress
            user.score = score
            user.rank = rank
            user.status = status
            user.type = types
            user.save()
            return redirect("/adminUsers")
    else:
        return redirect("/sign_in")
@auth_admin 
def addUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        sex = request.POST['sex']
        stutype = request.POST['stutype']
        schooladdress = request.POST['schooladdress']
        score = int(request.POST['score'])
        rank = int(request.POST['rank'])
        status = int(request.POST['status'])
        types = int(request.POST['type'])
        print types
        if username == "" or username == '' or password == "":
            return redirect('/adminUsers')
        else:
            u = Users.objects.filter(username__exact = username)
            if len(u) > 0:
                print username
                print '用户名已经存在'
                errorMsg = "用户名已经存在"
                return HttpResponse(json.dumps(errorMsg), content_type = 'application/json')
            else:
                user = Users()
                user.username = username
                user.password = password
                user.sex = sex
                user.stutype = stutype
                user.schooladdress = schooladdress
                user.score = score
                user.rank = rank
                user.status = status
                user.type = types
                print user
                user.save()
            return redirect('/adminUsers')
    else:
        return redirect("/sign_in")
    
