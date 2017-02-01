$(document).ready(function () {
{{a=["hola mundo"]}}
	{{for elem in ["a","b","c"]:}}
		{{if elem =="a":}}
			alert("{{print elem}}");
		{{else:}}
			{{pass}}
	{{pass}}
	
console.log('javascript');
})