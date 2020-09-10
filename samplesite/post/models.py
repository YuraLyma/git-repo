from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from datetime import datetime

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50, verbose_name='Заголовок')
	content = models.TextField(verbose_name='Описание')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	time_of_creation = models.DateTimeField(auto_now_add=True, 
											verbose_name='Время создания')
	publication_time = models.DateTimeField(db_index=True, default=datetime.now(),
										    verbose_name='Время публикации')
	last_update = models.DateTimeField(auto_now=True,
									   verbose_name='Время последнего обновления')
	image = models.ImageField(upload_to='media', null=True, blank=True,
		                      verbose_name='Картинка')
	tags = TaggableManager(blank=True)

	def __str__(self):
		time = f"{self.last_update.year}.{self.last_update.month}.{self.last_update.day} " + \
			   f"{self.last_update.hour}:{self.last_update.minute}:{self.last_update.second}"

		return f"{self.title}, {time}"

	class Meta:
		verbose_name_plural = 'Посты'
		verbose_name = 'Пост'
		ordering = ['-publication_time']
