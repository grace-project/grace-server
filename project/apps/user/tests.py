from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class UserTestCase(TestCase):
	"""
	Test case for User model.
	"""

	def setUp(self):
		"""
		Set up testing environment for User model tests.
		"""
		from .signals import create_auth_token
		self.user = User.objects.create_user(username="test", password="test")


	def test_token_created(self):
		"""
		Assure that authentication token is created for user.
		"""
		# Find user's token
		token = Token.objects.get(user_id=self.user.id)

		# Assertions
		self.assertIsNotNone(token)
		self.assertIsNotNone(token.key)
		self.assertEqual(self.user.id, token.user_id)