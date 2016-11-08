from django.apps import AppConfig



class UserConfig(AppConfig):
	name = "user"


	def ready(self):
		"""
		Import signals when app is ready.
		"""
		from . import signals