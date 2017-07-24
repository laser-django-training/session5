from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(null=True, blank=True)
	visible = models.BooleanField(default=True)
	creationdate = models.DateTimeField()
