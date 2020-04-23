from django.db import models

# Create your models here.


"""创建user表"""
class User(models.Model):
	username = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	groups = models.CharField(max_length=100)

	def __str__(self):                      # def __str__ 美化字段的显示，方便查看
		return self.username


"""创建Group表"""
class Group(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name