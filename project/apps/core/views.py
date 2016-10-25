from django.http import HttpResponse


def home(request):
	return HttpResponse("Tis but a backend.")