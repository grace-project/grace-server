from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User



class Profile(models.Model):
	"""
	One-to-one field for a User's profile.
	"""
	user = models.OneToOneField(User)
	variables = JSONField()