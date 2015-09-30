$("#DateCountdown").TimeCircles({time: { Seconds: {color: "#F83333" }, Hours: {color: "#3070d1"}}});
var updateTime = function(){
    var date = $("#date").val();
    var time = $("#time").val();
    var datetime = date + ' ' + time + ':00';
    $("#DateCountdown").data('date', datetime).TimeCircles().start();
}
