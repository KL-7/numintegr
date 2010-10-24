$(document).ready(function() {
	$("#inputForm").submit(function() {
		var errors = new Array();

		var inputs = $("#inputForm :input");
		for (var i = 0; i < inputs.length; ++i) {
			if (inputs[i].value.length == 0) {
				errors.push('all fields should be filled');
				break;
			}
		}

		var lowerLimit = $("#lowerLimit");
		var upperLimit = $("#upperLimit");
		var subintervalsNumber = $("#subintervalsNumber");

		var lowerLimitValue = parseFloat(lowerLimit.val());
		var upperLimitValue = parseFloat(upperLimit.val());

		if (lowerLimitValue != lowerLimit.val() || upperLimitValue != upperLimit.val()) {
			errors.push('integration limits should be float numbers');
		}

		var subintervalsNumberValue = parseInt(subintervalsNumber.val());

		if (subintervalsNumberValue != subintervalsNumber.val() || subintervalsNumberValue <= 0) {
			errors.push('number of subintervals should be positive integer');
		}

		if (errors.length > 0) {
			var errorList = $(".errors-list ul");
			errorList.children().remove();
			for (var i = 0; i < errors.length; ++i) {
				if (errors[i]) {
					errorList.append("<li>" + errors[i] + "</li>");
				}
			}
			$(".errors-list").fadeIn();
			return false;
		}

		return true;
	});
});
