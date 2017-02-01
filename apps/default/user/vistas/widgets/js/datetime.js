/*
Requiere en el heder:

<link rel="stylesheet" type="text/css" href="{{print config.base_url}}static/js/dhtmlgoodies_calendar/dhtmlgoodies_calendar/dhtmlgoodies_calendar.css?random=20051112"
<script src="{{print config.base_url}}static/js/dhtmlgoodies_calendar/dhtmlgoodies_calendar/dhtmlgoodies_calendar.js?random=20060118"></ script>
*/
	
function mostrarCalendar(obj,formato='yyyy/mm/dd hh:ii',booleando=false){
		if (navigator.appName=="Netscape"){
			displayCalendar(obj,formato,obj,booleando);		
		}
	}
