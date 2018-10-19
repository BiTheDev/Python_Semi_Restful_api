from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['first_name']) < 1:
			errors['first_name'] = "First_name should not be blank"
		if len(postData['last_name']) < 1:
			errors['last_name'] = "Last_name should not be blank"
		if len(postData['email']) < 1:
			errors['email'] = "Email should not be blank"
		return errors



class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email= models.CharField(max_length = 255)
    create_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now= True)

    objects = UserManager()