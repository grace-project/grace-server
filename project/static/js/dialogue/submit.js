var createChatBubble = function(text, align, color) {
	// create elemnt in DOM
	var el = document.createElement("div");
	el.className = "ui " + color + " " + align + " aligned segment";
	el.innerHTML = text;

	// append element in .results element
	$(".results").append(el);
}


$(".submit.button").api({
	url: "/mock-response",
	method: "POST",

	beforeSend: function(settings) {
		var query = $("#query");
		var value = query.val().trim();

		// disallow empty query
		if (value.length < 1) {
			return false;
		}

		// set query in POST data
		settings.data.query = value;

		// create user's chat bubble
		createChatBubble(settings.data.query, "left", "blue");

		// reset
		query.val("");
		query.trigger("update");
		$(".submit.button").html("Say");
		
		return settings;
	},

	onSuccess: function(response) {
		// create chat bubble for Grace's response
		createChatBubble(response.message, "right", "red");
	}
});