#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''<!-- Este widget requiere 'noticia-img' 'noticia-titulo' 'noticia-descripción' --><div class="pad-1">	<img src="'''+str(data['noticia-img'])+'''" class="whauto-5 d-inline-block widht-100p">	<div class="d-inline-block alg-top pad-1">		<a href="" class="right">Link</a>		<h5>'''+str(data['noticia-titulo'])+'''</h5>		<p>'''+str(data['noticia-descripción'])+'''</p>	</div></div>'''