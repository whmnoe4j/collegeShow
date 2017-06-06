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
    
    
    #API
    #大学分数线
    url(r'^collegescoreline/', views.collegescoreline, name = 'collegescoreList'),
    url(r'^api_collegescoreline/', API.showCollegeSchoolScoreLine, name = 'collegescoreList'),
    #地区批次线
    url(r'^areascoreline/', API.showAreaScoreLine, name = "areascoreList"),
    #专业大类
    url(r'^subjectgroup/', API.showSubjectGroup, name = "subjectgroup"),
    #专业细分类
    url(r'^majorgroup/', API.showMajorGroupList, name = "majorgroup"),
    #专业信息
    url(r'^profession/', API.showProfession, name = "profession"),
    #专业排名
    url(r'^professionrank/', API.showProfessionRank, name = "professionrank"),
    #同分考生去向
    url(r'^samescore/', API.sameScore, name = "sameScore")
]
