var _BUSY = false;
var _QUESTIONS = ["who", "what", "when", "where", "why", "is", "how"];


$("#query").change(function() {
	var value = $(this).val().toLowerCase().trim();
	var submit = $(".submit.button");

	// loop through each _QUESTION to check if our input value starts
	// with a word that starts a sentence
	for (var i = _QUESTIONS.length - 1; i >= 0; i--) {
		// when we're asking Grace a question, lets change the
		// submit button text
		if (value.startsWith(_QUESTIONS[i])) {
			submit.html("Ask");
			return;
		}
	}

	// questions end with a question mark
	if (value.endsWith("?")) {
		submit.html("Ask");
		return;
	}

	// we're not asking a question, so that means we're sending a command
	if (submit.text() != "Say") {
		submit.html("Say");
	}
});


$("#query").keyup(function() {
	// block too many keyups
	if (!_BUSY) {
		_BUSY = true;
		setTimeout(function() {
			_BUSY = false;
		}, 100);
	} else {
		return;
	}

	$(this).trigger("change");
});