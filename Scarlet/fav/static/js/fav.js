$(document).ready(function(){
	var positive_part = $("input[name=positive_part]").val();
	var negative_part = $("input[name=negative_part]").val();
	$(".fav-button").click(function(){
        var object_id = $(this).attr("object");
        var form = ".fav-form"+ object_id ;
        var button = '#fav-button'+object_id;
        var button_value = $(this).val();
        var data =  new FormData($(form).get(0));
        var fav_count_div = ".fav_count_div" + object_id;
        var fav_count_field = "#fav_count"+object_id;
        var fav_count_val = parseInt($("#fav_count"+object_id).val());
       	if(button_value == positive_part ) {
       		data.append('fav_value',positive_part);
       	}
       	else{

       		data.append('fav_value',negative_part);
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
	            	if(button_value == json["positive_part"]) {
	            		fav_count_val = fav_count_val+1;
	                    $(button).val(json["negative_part"]);
	                  }
	                  else{
	                  	fav_count_val = fav_count_val-1;
                        $(button).val(json["positive_part"]);
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
