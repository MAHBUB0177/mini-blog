//Sidebar menu
$(function(){
    var current = location.pathname;
    $('#stacked-menu li a').each(function(){
        var $this = $(this);
        // if the current path is like this link, make it active
        if($this.attr('href').indexOf(current) !== -1){
            $this.addClass('has-active active-color');
            // this.parent().addClass('has-active');
            $this.parents('.has-child').addClass('has-open has-active')
        }
    })
    
})


let myPromise = new Promise(function(myResolve, myReject) {
// "Producing Code" (May take some time)

  myResolve(); // when successful
  myReject();  // when error
});

// "Consuming Code" (Must wait for a fulfilled Promise)
myPromise.then(
  function(value) { /* code if successful */ },
  function(error) { /* code if some error */ }
);
function print_div_data(divName) {
            var promise = new Promise(function (resolve,reject) {
            var divContents = document.getElementById(divName).innerHTML;
            // var title = document.getElementById('print_title').value;
            var css1=window.location.origin+"/static/assets/stylesheets/report-bootstrap.min.css" 
            var css2=window.location.origin+"/static/assets/stylesheets/report-page-pos-portrait.css" 
            console.log(css2)
            var a = window.open();
            a.document.write('<html><head>');
            // a.document.write('<title>'+title+'</title>');
            a.document.write('<link rel="stylesheet" href="'+css1+'">');
            a.document.write('<link rel="stylesheet" href='+css2+'>');
            a.document.write('</head><body>');
            a.document.write(divContents);
            a.document.write('</body></html>');
            a.document.close();
            if(a.document){
              resolve(a)
            }else{
              reject(("It is a failure lode print window."));
            }

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
 