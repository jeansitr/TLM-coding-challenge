$(document).ready(function(){

    $("#ninjifybtn").click(function() {

        let buzzwords = ($("#buzzwords").val()).toLowerCase().replaceAll(" ", ",")

        $.ajax({
            url: "/ninjify",
            type: 'GET',
            data: { x: buzzwords },
            dataType: 'json',
            success: function(data) {
                console.log(data.ninjaname)
            },
            error: function(data){
                console.log(data.responseText);
            }
        });
    });
});