# This is an auto-generated Django model module.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CollegeAreascoreline(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    dateyear = models.IntegerField(db_column = 'DateYear')  # Field name made lowercase.
    provincearea = models.CharField(db_column = 'ProvinceArea', max_length = 20)  # Field name made lowercase.
    studentclass = models.CharField(db_column = 'StudentClass', max_length = 50)  # Field name made lowercase.
    batch = models.CharField(db_column = 'Batch', max_length = 50)  # Field name made lowercase.
    scoreline = models.IntegerField(db_column = 'ScoreLine')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'college_areascoreline'


class CollegeDetailEwt(models.Model):
    schoolname = models.CharField(max_length = 50, blank = True, null = True)
    f985 = models.CharField(max_length = 4, blank = True, null = True)
    f211 = models.CharField(max_length = 4, blank = True, null = True)
    fyan = models.CharField(max_length = 4, blank = True, null = True)
    address = models.CharField(max_length = 15, blank = True, null = True)
    levels = models.CharField(max_length = 15, blank = True, null = True)
    attach_to = models.CharField(max_length = 20, blank = True, null = True)
    school_rank = models.CharField(max_length = 4, blank = True, null = True)
    schooltype = models.CharField(max_length = 15, blank = True, null = True)
    character = models.CharField(max_length = 15, blank = True, null = True)
    schoolid = models.CharField(max_length = 10, blank = True, null = True)
    postal_address = models.TextField(blank = True, null = True)
    tel = models.TextField(blank = True, null = True)
    key_discipline = models.CharField(max_length = 15, blank = True, null = True)
    faculty = models.CharField(max_length = 50, blank = True, null = True)
    official_website = models.CharField(max_length = 100, blank = True, null = True)
    school_img = models.CharField(max_length = 100, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'college_detail_ewt'


class CollegeDetailTel(models.Model):
    schoolname = models.CharField(max_length = 50, blank = True, null = True)
    key_disciplines = models.IntegerField(blank = True, null = True)
    academician = models.IntegerField(blank = True, null = True)
    doctor_station = models.IntegerField(blank = True, null = True)
    master = models.IntegerField(blank = True, null = True)
    tel = models.TextField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'college_detail_tel'


class CollegeSchoolscoreline(models.Model):
    id = models.AutoField(db_column = 'ID', primary_key = True)  # Field name made lowercase.
    name_school = models.CharField(db_column = 'Name_School', max_length = 50)  # Field name made lowercase.
    area_school = models.CharField(db_column = 'Area_School', max_length = 20)  # Field name made lowercase.
    dateyear = models.IntegerField(db_column = 'DateYear')  # Field name made lowercase.
    area_student = models.CharField(db_column = 'Area_Student', max_length = 20)  # Field name made lowercase.
    studentclass = models.CharField(db_column = 'StudentClass', max_length = 50)  # Field name made lowercase.
    batch = models.CharField(db_column = 'Batch', max_length = 50)  # Field name made lowercase.
    maxscore = models.IntegerField(db_column = 'MaxScore')  # Field name made lowercase.
    meanscore = models.IntegerField(db_column = 'MeanScore')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'college_schoolscoreline'


class CollegeScoreparm(models.Model):
    province = models.CharField(max_length = 20, blank = True, null = True)
    category = models.CharField(max_length = 20, blank = True, null = True)
    years = models.CharField(max_length = 10, blank = True, null = True)
    score = models.CharField(max_length = 10, blank = True, null = True)
    num = models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'college_scoreparm'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EwtNewAnhui(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 100, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_anhui'


class EwtNewGansu(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 30, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_gansu'


class EwtNewHenan(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 30, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_henan'


class EwtNewHunan(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 100, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_hunan'


class EwtNewJiangsu(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 100, blank = True, null = True)
    subjects_level = models.CharField(max_length = 10, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_jiangsu'


class EwtNewJiangxi(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 30, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_jiangxi'


class EwtNewJxMean(models.Model):
    province = models.CharField(max_length = 10, blank = True, null = True)
    schoolprovince = models.CharField(max_length = 10, blank = True, null = True)
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 30, blank = True, null = True)
    studenttype = models.CharField(db_column = 'studentType', max_length = 4, blank = True, null = True)  # Field name made lowercase.
    batch = models.CharField(max_length = 10, blank = True, null = True)
    getnum = models.IntegerField(blank = True, null = True)
    meanscore = models.IntegerField(blank = True, null = True)
    meanrank = models.IntegerField(blank = True, null = True)
    diffscore = models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_jx_mean'        


class EwtNewJilin(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 100, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_jilin'


class EwtNewJxzk(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 30, blank = True, null = True)
    min_score = models.IntegerField(blank = True, null = True)
    beyond_score = models.IntegerField(blank = True, null = True)
    min_rank = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    mean_score = models.IntegerField(blank = True, null = True)
    mean_rank = models.IntegerField(blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_jxzk'


class EwtNewShandong(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 100, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_shandong'


class EwtNewShanxi(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 30, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_shanxi'


class EwtNewSichuan(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 30, blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    score = models.IntegerField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_sichuan'


class EwtNewZhejiang(models.Model):
    schoolname = models.CharField(max_length = 30, blank = True, null = True)
    profession = models.CharField(max_length = 100, blank = True, null = True)
    mean_score_rank = models.IntegerField(blank = True, null = True)
    mean_score = models.FloatField(blank = True, null = True)
    admission_number = models.IntegerField(blank = True, null = True)
    studenttype = models.CharField(max_length = 10, blank = True, null = True)
    levels = models.CharField(max_length = 10, blank = True, null = True)
    batch = models.CharField(max_length = 10, blank = True, null = True)
    year = models.IntegerField(blank = True, null = True)
    school_province = models.CharField(max_length = 10, blank = True, null = True)
    province = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'ewt_new_zhejiang'


class Gaokao(models.Model):
    studentprovince = models.CharField(max_length = 5)
    years = models.IntegerField()
    studenttype = models.CharField(max_length = 2)
    levels = models.CharField(max_length = 2)
    batch = models.CharField(max_length = 10)
    rank = models.IntegerField()
    score = models.IntegerField()
    admission_number = models.IntegerField()
    schoolprovince = models.CharField(max_length = 5)
    schoolname = models.CharField(max_length = 20)
    profession = models.CharField(max_length = 20)

    class Meta:
        managed = False
        db_table = 'gaokao'


class JiangxiWlZk1415(models.Model):
    years = models.IntegerField()
    name_province = models.CharField(max_length = 10)
    name_school = models.CharField(max_length = 50)
    min_score = models.IntegerField()
    out_score = models.IntegerField()
    min_score_weici = models.IntegerField()
    wl = models.CharField(max_length = 5)
    pici = models.CharField(max_length = 10)
    mean_score = models.IntegerField()
    mean_score_weici = models.IntegerField()
    diff = models.CharField(max_length = 10)

    class Meta:
        managed = False
        db_table = 'jiangxi_wl_zk_14_15'


class Profession(models.Model):
    subject_type = models.CharField(max_length = 10)
    subject_name = models.CharField(max_length = 30)
    major_class = models.CharField(max_length = 50)
    major_name = models.CharField(max_length = 50)
    major_code = models.CharField(max_length = 10)
    major_degree = models.CharField(max_length = 30, blank = True, null = True)
    major_time = models.CharField(max_length = 30)
    major_course = models.CharField(max_length = 400)

    class Meta:
        managed = False
        db_table = 'profession'


class ProfessionRank(models.Model):
    major_code = models.CharField(max_length = 10)
    major_name = models.CharField(max_length = 50)
    rank_num = models.IntegerField()
    rank_school = models.CharField(max_length = 50)

    class Meta:
        managed = False
        db_table = 'profession_rank'


class Users(models.Model):
    username = models.CharField(max_length = 10)
    password = models.CharField(max_length = 10)
    sex = models.CharField(max_length = 2, blank = True, null = True)
    stuprovince = models.CharField(max_length = 10)
    stutype = models.CharField(max_length = 2)
    schooladdress = models.CharField(db_column = 'schoolAddress', max_length = 30, blank = True, null = True)  # Field name made lowercase.
    score = models.IntegerField(blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'users'

class CollegeMajor(models.Model):
    schoolname = models.CharField(max_length = 100, blank = True, null = True)
    edudirectly = models.CharField(max_length = 15, blank = True, null = True)
    f985 = models.CharField(max_length = 4, blank = True, null = True)
    f211 = models.CharField(max_length = 4, blank = True, null = True)
    schoolprovince = models.CharField(max_length = 30, blank = True, null = True)
    specialtype = models.CharField(max_length = 30, blank = True, null = True)
    specialtyname = models.CharField(max_length = 30, blank = True, null = True)
    level = models.CharField(max_length = 10, blank = True, null = True)

    class Meta:
        managed = False
        db_table = 'college_major'
