from django.views.generic.base import TemplateView



class IndexPageView(TemplateView):
	"""
	View for the index page.
	"""
	template_name = "core/index.html"