$(document).ready(function(){

    $(".ninjifybtn").click(function() {

        let buzzwords = ($("#buzzwords").val()).toLowerCase().replaceAll(" ", ",")

        $.ajax({
            url: "/ninjify",
            type: 'GET',
            data: { x: buzzwords },
            dataType: 'json',
            success: function(data) {
                if ($("#ninjanamebox").hasClass("hidden"))
                    toggleNinjifyBox();
                $("#ninjaname").text(data.ninjaname);
            },
            error: function(data){
                console.log(data.responseText);
            }
        });
    });

    $("#resetbtn").click(function(){
        toggleNinjifyBox();
        $("#ninjaname").text("");
        $("#buzzwords").val("");
    });

    function toggleNinjifyBox(){
        $(".ninjify-box").each(function(i, box){ 
            let $box = $(box);
            $box.hasClass("hidden") ? $box.removeClass("hidden") : $box.addClass("hidden");
        });
    }

});

