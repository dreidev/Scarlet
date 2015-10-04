$(document).ready(function(){
	/* ajax function responsible for altering value of submit button and 
	altering favorite count */
	var fav_count = parseInt($("input[name=fav_count]").val(),10);
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
		            	$(".fav_count_div").empty();
		            	if(fav_value == "Favorite") {
		            		fav_count = fav_count+1;
		                    $("input[type=submit]").val("Unfavorite");
		                  }
		                  else{
		                  	fav_count = fav_count-1;
                            $("input[type=submit]").val("Favorite");
		                  }
		                $("input[name=csrfmiddlewaretoken]").val(json['csrf'])
		                $("input[name=fav_count]").val(fav_count);
		                $(".fav_count_div").append(fav_count);		            	
						}
		            },
		            error: function(response) {
		            	alert("error")
		            }
	         }); 

	    }); 

	});
