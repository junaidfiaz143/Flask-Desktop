$(document).ready(function() { 

	$('#btnPredict').click(function() {
		event.preventDefault();
		var form_data = new FormData($('#formUploadImage')[0]);
		$.ajax({
			type: 'POST',
			url: '/predict',
			data: form_data,
			contentType: false,
			processData: false,
			dataType: 'json'
			}).done(function(data, textStatus, jqXHR){
				$('#lblPrediction').text(data["prediction"])
				console.log(data["prediction"])
				// alert(data["prediction"])
			}).fail(function(data){
				$("#errorModal").modal({show:true});
			// alert("ERROR");
		});
	});

}); 