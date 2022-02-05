
function numberWithCommas(number) {
	var parts = number.toString().split(".");
	parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	return parts.join(".");
}

function StringToNumber(values) {
	var number_value = Number(values);
	return number_value;
}

function roundNumber(values) {
	var output_data = (Math.round(values * 100) / 100);
	return output_data;
}

function refresh_branch_list(branch_code) {
    var url = '/appauth-choice-branchlist';
    $.ajax({
        url: url,
        data: {
            'branch_code': branch_code
        },
        success: function (data) {
            $("#id_branch_code").html(data);
        }
    });
    return false;
}

function refresh_employee_list(branch_code) {
    var url = '/sales-choice-employeelist';
    $.ajax({
        url: url,
        data: {
            'branch_code': branch_code
        },
        success: function (data) {
            $("#id_employee_id").html(data);
        }
    });
    return false;
}

function refresh_appuser_list(branch_code) {
    var url = '/appauth-choice-appuserlist';
    $.ajax({
        url: url,
        data: {
            'branch_code': branch_code
        },
        success: function (data) {
            $("#id_app_user_id").html(data);
        }
    });
    return false;
}

function refresh_group_list() {
    var url = '/sales-choice-productgrouplist';
    $.ajax({
        url: url,
        success: function (data) {
            $("#id_group_id").html(data);
        }
    });
    return false;
}

function refresh_brand_list() {
    var url = '/sales-choice-productbrandlist';
    $.ajax({
        url: url,
        success: function (data) {
            $("#id_brand_id").html(data);
        }
    });
    return false;
}


function refresh_appuser_list(branch_code) {
    var url = '/appauth-choice-appuserlist';
    $.ajax({
        url: url,
        data: {
            'branch_code': branch_code
        },
        success: function (data) {
            $("#id_app_user_id").html(data);
        }
    });
    return false;
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(function () {
    $('#btnSearch').click(function () {
        data_table_hide_show();
    });
});

function data_table_hide_show() {
    try {
        let div_id = document.querySelector("#data_table_extarnal");
        let div_classes = div_id.classList;
        if (div_classes.contains("deactivate_data_table")) {
            div_classes.toggle("deactivate_data_table", false);
            div_classes.toggle("activate", true);
        }
        else {
            div_classes.toggle("activate", false);
            div_classes.toggle("deactivate_data_table", true);
        }
    } catch (error) {
        return false;
    } finally {
    }
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