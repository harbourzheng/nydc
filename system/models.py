from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	nick_name = models.CharField(max_length=30)
	interest = models.CharField(max_length=1000)
	intro = models.CharField(max_length=3000)
	bithday = models.DateField()
	astrology = models.CharField(max_length=25)
	avatar = models.ImageField("Profile Pic", upload_to="images/pic/", blank=True, null=True)
	zipcode =models.CharField(max_length=5)
	area = models.CharField(max_length=50)
	member_start = models.DateField()
	member_end = models.DateField()
	complete = models.BooleanField(default=False)

class Event(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=1000)
	shownow = models.BooleanField(default=False)
	time = models.DateField('start time')
	image = models.FileField("Event pic",upload_to='images/documents/',blank=True,null=True)
	fee = models.DecimalField(max_digits=5, decimal_places=2)


class EmailTemplete(models.Model):
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=5000)
	allsend =  models.BooleanField(default=False)

class EventMember(models.Model):
	user = models.ForeignKey(User)
	event = models.ForeignKey(Event)



