$(document).ready(function(){
	$(".fav-button").click(function(){
        var object_id = $(this).attr("object");
        var form = ".fav-form"+ object_id ;
        var button = '#fav-button'+object_id;
        var button_value = $(this).val();
        var data =  new FormData($(form).get(0));
        var fav_count_div = ".fav_count_div" + object_id;
        var fav_count_field = "#fav_count"+object_id;
        var fav_count_val = parseInt($("#fav_count"+object_id).val());
       	if(button_value == "Favorite") {
       		data.append('fav_value','favorite');
       	}
       	else{

       		data.append('fav_value','');
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
	            	$(fav_count_div).empty();
	            	if(button_value == "Favorite") {
	            		fav_count_val = fav_count_val+1;
	                    $(button).val("Unfavorite");
	                  }
	                  else{
	                  	fav_count_val = fav_count_val-1;
                        $(button).val("Favorite");
	                  }
	                $("input[name=csrfmiddlewaretoken]").val(json['csrf']);
	                $(fav_count_field).val(fav_count_val);
	                $(fav_count_div).append(fav_count_val);		            	
					}
	            },
	            error: function(response) {
	            	alert("error")
	            }
        }); 
	});
});
