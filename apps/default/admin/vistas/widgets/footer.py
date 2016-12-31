print """<footer class="text-center bg-ubuntu_jet white pad-t1 pad-b1">
	zerpatechnlogy@2016
</footer>
<script type="text/javascript">
	$(document).ready(function() {
	$.ajax({
        type: 'POST',
        url: "post.py",
        data: {param: "prueba"}, //passing some input here
        dataType: "text",
        success: function(response){
           output = response;
           alert(output);
        }
}).done(function(data){
    console.log(data);
    alert(data);
});
	alert("hola");
	});
</script>"""