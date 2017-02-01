#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!-- Este widget requiere "input" "outuput" "action"--><div class="width-25"><form action="post.py">'''
if "action" in data:
  print '''	<input type="text" name="noticia-title" placeholder="Escribe el nombre de la noticia">	<textarea>'''  +str(data["noticia-descripcion"])  +'''</textarea>	<input type="text" class="hidden" name="noticia" value="'''  +str(data['noticia_id'])  +'''" >	'''
else:
  print '''	<input type="text" name="noticia-title" placeholder="Escribe el nombre de la noticia" value="'''  +str(data['noticia-title'])  +'''">	<textarea></textarea>'''
  pass
print ''''''
incluir(data,"previewImg")
print '''<input type="submit" name="" value="Publicar" class="btn"><input type="text" class="hidden" name="action" value="'''+str(data['action'])+'''" >		</form><script src="//cdn.tinymce.com/4/tinymce.min.js"></script><script>tinymce.init({ selector:'textarea' });</script></div>'''