$(document).ready(function(){
	$(".fav-form").submit(function(event){
	    	event.preventDefault();
	    	var form = $(this);
            var data =  new FormData(form.get(0));
	    	$.ajax({
	            url: $('.fav-form').attr('action'),
	            type: "POST",
	            data: data,
	            cache: false,
	            processData: false,
	            contentType: false,
	            success: function() {
	              var fav_value = $("input[type=submit]").val();
	              if(fav_value == "Favorite") {
	              	$("input[type=submit]").val("Unfavorite");
	              }
	              else {
	              	$("input[type=submit]").val("Favorite");
	              }

	            },
	            error: function(response) {
	            	alert("error")
	            }
	         }); 

	    }); 

	});