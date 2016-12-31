# -*- coding: utf-8 -*-
print '<!DOCTYPE html><html>'
print '<head>	<meta charset="utf-8">		<title>Administrador</title>	<link rel="stylesheet" type="text/css" href="'
print config.base_url
print 'static/css/estilos.css">	<link rel="stylesheet" type="text/css" href="'
print config.base_url
print 'static/css/bootstrap.css">	<link rel="stylesheet" type="text/css" href="'
print config.base_url
print 'static/css/ff.css"></head>'



print '<body class="AsenZor-admin ff"><div class="container-fluid">	'
print """<header class="bg-ubuntu_jet row">
	<div class="col-md-12">
	<ul><li>
	<h1 class="analecta"><span style="color:rgb(0,102,255)">Asen</span><span style="color:#ff3300">Zor</span></h1></li>
	<li><h3 style="color:white;">Interfaz administrativa</h3></li>
	</ul>

	<nav id="AsenZor-menuPrincial"><ul><li><a><div>Sitio</div></a></li>
			 <li><a><div>Ayuda</div></a></li>
			 <li><a><div>Fin de sesión</div></a></li>
			 <li><a><div>Depurar</div></a></li>
		</ul>
	</nav>	
	</div>
	

</header>
"""


print '		<section class="row"><div class="col-md-12 bg-ubuntu_orange"><h1>Necesitas Loguearte para continuar</h1><label>Usuario</label>	<input type="text" name="nick"><label>Contraseña</label>	<input type="password" name="password">	<input type="submit" name="entar" value="Entrar"></div>	</section>	'
print """<footer class="text-center bg-ubuntu_jet white pad-t1 pad-b1 row">
	zerpatechnlogy@2016
</footer>"""


print '			</div></body></html>'


