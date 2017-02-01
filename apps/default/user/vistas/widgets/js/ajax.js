//este script necesita el parametro ajax-data
function ajax({{data["ajax-data"]}}){
    var respuesta =null;
    $.ajax({
            data:data,
            type:"POST",
            dataType:"text",
            url:"ajax.py",
            success:function(response){respuesta=response;},
            async: false

     });
}