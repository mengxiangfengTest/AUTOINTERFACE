from django.db import models
# from pymysql import cursors, connect
# Create your models here.
# 仓库表
class warehouse(models.Model):
    name = models.CharField(max_length=30)              #仓库名称
    description = models.CharField(max_length=100)      #仓库简介
    member = models.IntegerField()                      #成员
    dbl = models.CharField(max_length=30)               #协同仓库
    status = models.BooleanField()                      #状态
    create_time = models.DateTimeField(auto_now=True)   #创建时间（自动获取当前时间）

    def __str__(self):
        return self.name
