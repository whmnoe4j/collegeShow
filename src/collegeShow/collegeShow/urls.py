# coding=UTF-8
"""collegeShow URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from collegePage import views
from collegePage import API

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
   
    url(r'^dataSearch/', views.dataSearch, name = 'dataSearch'),
    url(r'^reportedCollege/', views.reportedCollege, name = 'reportedCollege'),
    url(r'^collegescoreline/', views.collegescoreline, name = 'collegescoreline'),
    url(r'^areascoreline/', views.areascoreline, name = 'areascoreline'),
    #登录注册
    url(r'^login/', API.login, name = "login"),
    url(r'^logout/', API.logout, name = "logout"),
    url(r'^register/', API.register, name = "register"),
    
    #API
    #院校信息
    url(r"^api_college/", API.showCollege, name = "college"),
    #大学分数线
    url(r'^api_collegescoreline/', API.showCollegeSchoolScoreLine, name = 'collegescoreList'),
    #地区批次线
    url(r'^api_areascoreline/', API.showAreaScoreLine, name = "areascoreList"),
    #一分一段表
    url(r'^api_scoreparam/', API.showScoreParm, name = "scoreparm"),
    #专业大类
    url(r'^api_subjectgroup/', API.showSubjectGroup, name = "subjectgroup"),
    #专业细分类
    url(r'^api_majorgroup/', API.showMajorGroupList, name = "majorgroup"),
    #专业小类
    url(r'^api_professionsmall/', API. showProfessionSmall, name = "majorgroup"),
    #专业信息
    url(r'^api_profession/', API.showProfession, name = "profession"),
    #专业排名
    url(r'^api_professionrank/', API.showProfessionRank, name = "professionrank"),
    #同分考生去向
    url(r'^api_samescore/', API.sameScore, name = "sameScore"),
    #专业分数线
    url(r'^api_professionscore/', API.professionscore, name = "professionscore"),
    #推荐学校
    url(r'^api_recommendSchool/',API.recommendSchool,name='recommendSchool'),
    
    #个人中心
    url(r'^user/', views.user, name = "user"),
    url(r"^edit_user/", API.editUser, name = "editUser"),
    
    
    
    
    url(r'^scoreparam/', views.scoreparam, name = 'scoreparam'),
    url(r'^professionrank/', views.professionrank, name = 'professionrank'),
    #专业大全
    url(r'^professiongroup/', views.professiongroup, name = 'professiongroup'),
    #专业分数线
    url(r'^professionscore/', views.professionscore, name = 'professionscore'),
    #院校信息
    url(r'^schoolinfo/$', views.schoolinfo, name = 'schoolinfo'),
    #院校专业
    url(r'^schoolmajor/$', views.schoolmajor, name = 'schoolmajor'),
    #历年分数线
    url(r'^schoolenrol/$', views.schoolenrol, name = 'schoolenrol'),

]
