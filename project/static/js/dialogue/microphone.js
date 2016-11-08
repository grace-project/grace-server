$(".microphone.button").click(function() {
	var rec = new webkitSpeechRecognition();
	var _this = $(this);

	rec.onresult = function(e) { 
		// get transcript from results
		var query = $("#query");
		query.val(e.results[0][0].transcript);
		query.trigger("change");
		_this.removeClass("red");
	};

	// listen
	rec.start();

	// update button
	_this.addClass("red");
});