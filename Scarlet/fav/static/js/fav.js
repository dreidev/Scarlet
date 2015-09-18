$(document).ready(function(){
	// ajax function responsible for altering value of submit button .
	$(".fav-form").submit(function(event){
	    	event.preventDefault();
            var fav_value = $("input[type=submit]").val();
            var form = $(this);
           	var data =  new FormData(form.get(0));
           	if(fav_value == "Favorite") {
           		data.append('fav_value','favorite')
           	}
           	else{

           		data.append('fav_value','')
         	}            
	    		$.ajax({
		            url: "/fav/alter/fav/",
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

		            	if(fav_value == "Favorite") {
		                    $("input[type=submit]").val("Unfavorite");
		                  }
		                  else{
                             $("input[type=submit]").val("Favorite");
		                  }
		            	$("input[name=csrfmiddlewaretoken]").val(json['csrf'])
						}
		            },
		            error: function(response) {
		            	alert("ajax error")
		            }
	         }); 

	    }); 

	});
