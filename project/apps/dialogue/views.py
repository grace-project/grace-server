import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

	
POSSIBLE_MESSAGES = [
	"I have received your message.",
	"Good message.",
	"Can I help you with anything else?",
	"I can't reply to your message now."
]


@csrf_exempt
def mock_response(request):
	"""
	Mock response for initial debugging purposes.
	"""
	return JsonResponse({
		"success": True,
		"message": random.choice(POSSIBLE_MESSAGES),
		"data": {
			# "type": "map",
			# "coordinates": "40.9445:-74.0754"
		}
	})