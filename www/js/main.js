/*
*/

function run(){
	$("#submit_btn").click(function(){
		var val = $("#target_num").val();
		$.ajax({
			type: "POST",
			url: "./py/setTarget.py",
			data: { "target": val }, 
			success: function(){
				alert("Goal is now : " + val + " m");
			},
			error: function(er){
				alert("something wrong.");
				console.log(er);
			}
		});
	});
}

$(function(){
	run();
})