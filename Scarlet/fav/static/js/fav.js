$(document).ready(function(){
	$(".fav-form").submit(function(event){
	    	event.preventDefault();
            var fav_value = $("input[type=submit]").val();
            
            if(fav_value == "Favorite") {
            	var form = $(this);
           	 	var data =  new FormData(form.get(0));
	    		$.ajax({
		            url: "/fav/create/fav/",
		            type: "POST",
		            data: data,
		            cache: false,
		            processData: false,
		            contentType: false,
		            success: function(json) {
		            	if (json['success'] == 0) {
	                  alert(json['error'])                     
	                }
		            	else {
		              
		              	$("input[type=submit]").val("Unfavorite");
		            	$("input[name=csrfmiddlewaretoken]").val(json['csrf'])
						}
		            },
		            error: function(response) {
		            	alert("error")
		            }
	         }); }
	         else {
	         	var form = $(this);
           	 	var data =  new FormData(form.get(0));
	         	$.ajax({
	         		url: "/fav/delete/fav/",
		            type: "POST",
		            data:data,
		            cache: false,
		            processData: false,
		            contentType: false,
		            success: function(data) {
		            	$("input[type=submit]").val("Favorite");
		            	$("input[name=csrfmiddlewaretoken]").val(data['csrf'])
		            },
		            error: function(response) {
	            	alert("error in unfavoriting")
	            }
	         	})
	         } 

	    }); 

	});
