<<<<<<< HEAD
print '''<div class="text-center width-40 height-50 bg-ubuntu_jet white inline-block">	<form class="width-40 height-50">	''',
incluir(data,"previewImg")
print '''		<input type="text" name="titulo">	<textarea name="noticia"></textarea>	<input type="submit" name="" value="Guardar" class="pad-1 bg-ubuntu_blue white">	<input type="text" name="action" value="crearNoticia">	<a href="" class="pad-1 bg-ubuntu_red white">Cancelar</a>		</form></div>''',
=======
print '''<div class="text-center width-40 height-50 bg-ubuntu_jet white d-inline-block marg-1">	<form class="width-40 height-50">	<label>Titulo de la noticia</label><br>	<input type="text" name="titulo" class="d-inline-block width-95p"><br>	''',
incluir(data,"previewImg-marco")
print '''	''',
incluir(data,"previewImg-boton")
print '''		<label>Texto de la noticia</label><br>	<textarea name="noticia" class="d-inine-block width-95p height-20"></textarea><br>	<input type="submit" name="" value="Guardar" class="pad-1 bg-ubuntu_blue white marg-t1 d-inline-block"><br>		<a onclick="''',data['funCerrar'],'''()" class="pad-1 marg-t1 bg-ubuntu_red white d-inline-block width-10" >Cancelar</a>	<input type="text" name="action" value="crearNoticia" class="hidden">	</form></div>''',
>>>>>>> ef41972007de3cb6b5a635ee0e0d501b6ceeae02
