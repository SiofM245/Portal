from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
	body = models.TextField()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',args=(str(self.id)))

	