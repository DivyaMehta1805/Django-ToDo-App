from django.db import models
from django.utils import timezone

class Todo(models.Model):
	text = models.CharField(max_length=40)
	complete = models.BooleanField(default=False)
	at = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.text

# from django.db import models

# class Graph(models.Model):
#     title = models.CharField(max_length=200)
#     is_completed = models.BooleanField(default=False)
#     completed_at = models.DateTimeField(null=True, blank=True)
    
#     def __str__(self):
#         return self.title
