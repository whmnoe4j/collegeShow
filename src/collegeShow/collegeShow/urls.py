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
from collegePage import adminViews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^index/', views.index, name = 'index'),
    url(r'^dataSearch/', views.dataSearch, name = 'dataSearch'),
    url(r'^reportedCollege/', views.reportedCollege, name = 'reportedCollege'),
    url(r'^collegescoreline/', views.collegescoreline, name = 'collegescoreline'),
    url(r'^areascoreline/', views.areascoreline, name = 'areascoreline'),
#    #登录注册
#    url(r'^login/', API.login, name = "login"),
#    url(r'^logout/', API.logout, name = "logout"),
#    url(r'^register/', API.register, name = "register"),
    
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
    url(r'^api_recommendSchool/', API.recommendSchool, name = 'recommendSchool'),
    
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
    #推荐学校
    #url(r'^recommendschool/$', views.recommendschool, name = 'recommendschool'),
    #推荐学校
    url(r'^api_collegescoreLine/$', API.CollegeScoreLine, name = 'CollegeScoreLine'),
    #管理员
    
#    url(r'^adminIndex/$', views.adminIndex, name = 'adminIndex'),
    
    #后台用户管理页面
    url(r'adminIndex/', adminViews.adminIndex, name = 'adminIndex'),
    url(r'adminUser/', adminViews.adminUser, name = 'user'),
    url(r'adminUsers/', adminViews.adminUsers, name = 'adminUsers'),
    url(r'sign_in/', adminViews.sign_in, name = 'sign_in'),
    url(r'sign_out/', adminViews.sign_out, name = 'sign_out'),
    url(r'deleteUser/', adminViews.deleteUser, name = 'deleteUser'),
    url(r'updateUser/', adminViews.updateUser, name = 'updateUser'),
    url(r'addUser/', adminViews.addUser, name = 'addUser'),
    
    #收藏功能
    url(r'collect/', views.collect, name = 'collect'),
    url(r'showCollect/', views.showCollect, name = 'showCollect'),
    #用户个人中心
    url(r'userInfo/', views.userInfo, name = 'userInfo'),
    url(r'updateInfo/', views.updateInfo, name = 'updateInfo'),
    url(r'deleCollect/', views.deleCollect, name = 'deleCollect'),
    
    #登录注册
    url(r'^login/', views.login, name = "login"),
    url(r'^logout/$', views.logout, name = "logout"),
    url(r'^register/', views.register, name = "register"),
    #注册会员
    url(r'^bevip/', views.bevip, name = "bevip"),
    #提交订单
    url(r'^order/', views.order, name = "order"),
    #注册验证
    url(r'^validregister/', views.validregister, name = "validregister"),
    #模糊查询
    url(r'^likesearch/', views.likesearch, name = "likesearch"),
    
    #修改密码
    url(r'^editpasswd/', views.editpasswd, name = "editpasswd"),
    #修改订单
    url(r'^update_order/$', adminViews.update_order, name = "update_order"),
    url(r'^delete_order/$', adminViews.delete_order, name = "delete_order"),
    #删除订单
    
]
