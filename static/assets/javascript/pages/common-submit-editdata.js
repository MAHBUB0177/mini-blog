$(function () {
	$('#btnSubmit').click(function () {
		post_edit_form_data();
	});
});

function post_edit_form_data() {
	const data_string = $("#edit_form").serialize();
	const data_url = $("#edit_form").attr('data-url');
	console.log("Test");
	$('#page_loading').modal('show');
	$.ajax({
		url: data_url,
		data: data_string,
		type: 'POST',
		dataType: 'json',
		success: function (data) {
			if (data.form_is_valid) {
				$('#page_loading').modal('hide');
				$('#edit_model').modal('hide');
				Swal.fire({
					position: 'top-center',
					icon: 'success',
					title: data.success_message,
					showConfirmButton: false,
					timer: 1500
				  })
				table_data.ajax.reload();
			} else {
				$('#page_loading').modal('hide');
				Swal.fire({
					position: 'top-center',
					icon: 'error',
					title: data.error_message,
				  })
				table_data.ajax.reload();
			}
		}
	})
	return false;
}


function print_div_data(divName) {
	var promise = new Promise(function (resolve,reject) {
	var divContents = document.getElementById(divName).innerHTML;
	var title = document.getElementById('print_title').value;
	var host="http://"+window.location.host+"/static/assets/stylesheets/custom.css" 
	var a = window.open('', '', 'height=3508, width=2480');
	a.document.write('<html><head>');
	a.document.write('<title>'+title+'</title>');
	a.document.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">');
	a.document.write('<link rel="stylesheet" href='+host+'>');
	a.document.write('</head><body>');
	a.document.write(divContents);
	a.document.write('</body></html>');
	a.document.close();
	if(a.document){
		resolve(a)
	}else{
		reject(("It is a failure lode print window."));
	}
// setTimeout(() => {
	//   a.print();
	// }, 500);

	});
	return promise;
	
}
function print_div(div){
print_div_data(div).then(x=>{
setTimeout(() => {
x.print()
}, 500);
x.onafterprint = x.close;  
}).catch(err=> {
alert("Error: " + err);
})
}