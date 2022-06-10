$(document).ready(function(){

    $(".ninjifybtn").click(function() {

        let buzzwords = ($("#buzzwords").val()).toLowerCase().replaceAll(" ", ",")

        $.ajax({
            url: "/ninjify",
            type: 'GET',
            data: { x: buzzwords },
            dataType: 'json',
            success: function(data) {
                if (data.ninjaname){
                    if ($("#ninjanamebox").hasClass("hidden"))
                        toggleNinjifyBox();

                    $("#ninjaname").text(data.ninjaname);
                    $(".errorbox").removeClass("error");
                }
            },
            error: function(data){
                $(".errorbox").addClass("error");
                $(".errorlbl").text("An error has occured: " + data.responseJSON.error);
            }
        });
    });

    $("#resetbtn").click(function(){
        toggleNinjifyBox();
        $("#ninjaname").text("");
        $("#buzzwords").val("");
    });

    $('#buzzwords').keyup(function (e) {
        if (e.keyCode === 13) {
            $(".ninjifybtn").trigger("click");
        }
    });

    function toggleNinjifyBox(){
        $(".ninjify-box").each(function(i, box){ 
            let $box = $(box);
            $box.hasClass("hidden") ? $box.removeClass("hidden") : $box.addClass("hidden");
        });
    }

});

