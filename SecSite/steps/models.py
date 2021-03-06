from django.db import models
from django.contrib.auth.models import User
		
class Steps(models.Model):
	title = models.CharField(verbose_name = 'Название проекта', max_length = 100)
	content = models.TextField(verbose_name = 'Описание работы', null = True, blank = True)
	published = models.DateTimeField(verbose_name = 'Дата публикации', auto_now_add = True, db_index = True)
	theme = models.ForeignKey('Themes', on_delete = models.PROTECT, null = True, verbose_name = 'Тема')
	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'
		ordering = ['-published']

class Themes(models.Model):
	name = models.CharField(verbose_name = 'Тема проекта', max_length = 50, db_index = True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Тема'
		verbose_name_plural = 'Темы'
		ordering = ['name']


