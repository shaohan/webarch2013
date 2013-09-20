function validator() {

	//validate name input
	if ($("#your_name").val().length > 0) {
		$("#output_name").text($("#your_name").val());
		$("#output_name_1").text($("#your_name").val());
		$("#output_name_2").text($("#your_name").val());
		$("#output_name_3").text($("#your_name").val());
	} else {
		alert("Please enter your name.");
		return false;
	}

	
	//validate title input
	if ($("#title input[type='radio']:checked").val().length > 0) {
		$("#output_title").text($("#title input[type='radio']:checked").val());
	}


	//validate year
	if ($("#year").val().match('^[12][0-9]{3}$')) {
		$("#output_year").text($("#year").val());
	} else {
		alert("Please enter a valid year!");
		return false;
	}


	//validate occupation
	if ($("#occupation").val().length > 0) {
		$("#output_occupation").text($("#occupation").val());
	} else {
		alert("Please enter your occupation.");
		return false;
	}


	//validate reaction
	if ($("#reaction option:selected").val().length > 0) {
		$("#output_reaction").text($("#reaction option:selected").val());
	} else {
		alert("Please choose the reaction when you see a cockroach.");
		return false;
	}


	// validate monster
	if ($("#monster input[type='checkbox']:checked").val().length = 0) {
		alert("Please select at least one monster.");
		return false;
	}


	// fill-in monster
	if ($("#godzilla").is(":checked")) {
		$("#output_godzilla").text($("#godzilla").val());
	} 
	
	if ($("#kingkong").is(":checked")) {
		$("#output_kingkong").text($("#kingkong").val());
	}
	
	if ($("#mothra").is(":checked")) {
		$("#output_mothra").text($("#mothra").val());
	}
	
	if ($("#gamera").is(":checked")) {
		$("#output_gamera").text($("#gamera").val());
	}
	

	// show madlib-output
	$("#madlib-output").show();	
	return false;
}

$(document).ready(function() {
	$("#madlib-input").submit(validator);
});