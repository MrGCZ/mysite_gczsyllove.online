from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


class CalendarEvent(models.Model):
	IMPORTANCE_LEVEL=(
	('1','Important'),
	('2','Fairly Important'),
	('3','Very Important'),
	('4','Specially Important'),
	('5','Extremly Important'),
	)
	name=models.CharField(max_length=100)
	remarkdate=models.DateTimeField()
	descriptions=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	importance=models.CharField(max_length=1,choices=IMPORTANCE_LEVEL,default=1)
	eventdone=models.NullBooleanField()
	ispast=models.NullBooleanField()
	tdelta=""
	mark=""
	def __str__(self):
		return self.name
	class Meta:
		ordering=("-importance","-created")
