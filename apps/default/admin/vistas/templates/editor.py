# -*- coding: utf-8 -*-
print '<!DOCTYPE html><html>'
print '<head>	<meta charset="utf-8">		<title>Administrador</title>	<link rel="stylesheet" type="text/css" href="'
print config.base_url
print 'static/css/estilos.css">	<link rel="stylesheet" type="text/css" href="'
print config.base_url
print 'static/css/bootstrap.css">	<link rel="stylesheet" type="text/css" href="'
print config.base_url
print 'static/css/ff.css"></head>'



print '<body class="AsenZor-admin ff"><div class="container-fluid">	<div class="row">		<div class="col-md-12">			'
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


print '		</div>		</div class="container">		<div class="row">		<div>			<div class="col-md-6">			<h1><b>Aplicaciones Instaladas</b></h1>			<h2><b>Producción</b></h2>			'
import os
print '			'
l=os.listdir(data["base_root"]+"../../")
print '			'
for elem in l:
  print '			<h3 class="marg-l2">'
  print elem
  print '</h3>			'
  pass
print '			<h2><b>Desarollo</b></h2>			'
l=os.listdir(config.base_root+config.projects_url)
print '			'
for elem in l:
  print '			<h3 class="marg-l2"><a href="'
  print config.base_url+'vista='+elem+'-edit&admin=True'
  print '">'
  print elem
  print '</a></h3>			'
  pass
print '			</div>			'
print """<div class="col-md-6">
				<div class="cpanel">
					<ul style="list-style:none; padding-left:0px;">
						<li><button class="btn1" style="margin-left:60%;margin-right:10%;margin-top:10px;">Cambiar Contraseña</button></li>
						<li><hr class="h"></li>
						<li>
							<ul st	yle="list-style:none;">
								<li><b>Versión:</b> 0.1</li>
								<li><b>Original author:</b> Jesús Zerpa</li>
								<li><b>Email:</b> jesus26abraham1996@gmail.com</li>
								<li><b>Website:</b> https:zerpatechnology.com.ve</li>
								<li>AsenZor esta actualizado</li>
							</ul>
						</li>
						<li><hr class="h"></li>
						<li>
							<ul class="interLine " style="list-style:none;">
								<li><b>Nuevo Proyecto</b></li>
								<li>Nombre del Proyecto</li>
								<li><input type="text" name="nombreProyecto"></li>
								<li><input type="submit" name="nProyecto" value="Crear" class="btn2"></li>
							</ul>
						</li>
						<li><hr class="h"></li>
						<li class="margin-left"><b>Subir un proyecto empaquetado</b></li>
						<li class="margin-left">
							<ul class="interLine" style="list-style:none;">
								
								<li>Renombre del proyecto</li>
								<li><input type="text" name="rProyecto"></li>
								
								<li>
								<div class="lineal">
									<ul style="list-style:none;" class="lineal">
										<li>
											<input type="submit" name="" value="aplicar" class="btn2">
										</li>
										<li>
											<bottom class="btn3">Subir</bottom>
										</li>
									</ul>
									</div>
								</li>
							</ul>
						</li>
						<li class="maring-left">
						<li class="margin-left"><b>Importe un proyecto de la comunidad</b></li>
							<div class="margin-left">
							<ul>
								
								<li>Renombre del proyecto</li>
								<li><input type="text" name="rProyecto"></li>
								<li><input type="checkbox" name="">Sobreescribir la aplicación ya instalada</li>
								<li>
								<div class="lineal">
									<ul style="list-style:none;" class="lineal">
										<li>
											<input type="submit" name="" value="aplicar" class="btn2">
										</li>
										<li>
											<button class="btn3">Explorar</button>
										</li>
										
									</ul>
									</div>
								</li>
							</ul>
							</div>
						</li>
						<li><hr class="h"></li>
						<li class="margin-left"><b>Deploy</b></li>
						<li class="margin-left">
						<div class="lineal-block margin-left">
						<ul>
							

							<li><button class="btn3">Instale en Google App Engine</button></li>
							<li><button class="btn3">Instale en OpenShift</button></li>
							<li><button class="btn3">Deploy a PythonAnywhere</button></li>
						</ul>
						</div>
						</li>
						<li><hr class="h"></li>
						
						<ul>
							
							<li><b>Asistente para una nueva aplicación</b></li>
							<li><button class="btn3">Asistente</button></li>
						</ul>
						
						<li><hr class="h"></li>
						
						<li>
						<div class="lineal">
						<ul><li><b>Comunidad </b></li><li><button class="btn3">Foro</button></li><li><button class="btn3">Chat</button></li></ul>
						</div>
						</li>
						
						<li>
							<div class="widget-commit">
								<div class="commit">
									<div class="commit-image">
									<ul>
										<li><div class="commit-name">Nombre apellido</div></li>
										<li><img src="../../../static/imgs/icono_perfil.jpg"></li>
									</div>
									<div class="commit-content">
									<ul>
										<li><div class="commit-date">Fecha</div></li>
										<li><p class="commit-message">
											Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatum quibusdam, pariatur accusantium nemo quo veniam, aspernatur consequuntur perspiciatis culpa facere, magni modi sint, praesentium expedita ullam nobis perferendis laudantium sit.
										</p></li>
									</ul>
									</div>
										
								</div>
							</div>
						</li>

					</ul>
				</div>
			</div>"""


print '		</div>		</div>	</div></div>'
print """<footer class="text-center bg-ubuntu_jet white pad-t1 pad-b1 row">
	zerpatechnlogy@2016
</footer>"""


print '</body></html>'


