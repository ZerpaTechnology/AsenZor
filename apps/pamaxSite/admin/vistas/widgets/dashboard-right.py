print '<div class="col-md-6">				<div class="cpanel height-50-xs">											<button class="btn1" style="margin-left:60%;margin-right:10%;margin-top:10px;">Cambiar Contraseña</button>						<hr class="h">																				'
for elem in data["AsenZor:Detalles"]:
  print '							<h5 class="marg-l2"><b>'
  print elem
  print '</b>'
  print data["AsenZor:Detalles"][elem]
  print '</h5>							'
  pass
print '																			<hr class="h">													<div class="marg-l2">								<h5><b>Nuevo Proyecto</b></h5>								<h5>Nombre del Proyecto</h5>								<h5><input type="text" name="nombreProyecto"></h5>								<h5><input type="submit" name="nProyecto" value="Crear" class="btn2"></h5>															</div>																			<hr class="h">						<div class="marg-l2">							<h5 class="margin-left"><b>Subir un proyecto empaquetado</b></h5>																<h5>Renombre del proyecto</h5>								<input type="text" name="rProyecto">								<div class="lineal">											<input type="submit" name="" value="aplicar" class="btn2">												<bottom class="btn3">Subir</bottom>								</div>															<h5>Renombre del proyecto</h5>								<input type="text" name="rProyecto">								<input type="checkbox" name="">Sobreescribir la aplicación ya instalada								<div class="lineal">											<input type="submit" name="" value="aplicar" class="btn2">											<button class="btn3">Explorar</button>									</div>														</div>												<hr class="h">						<div class="marg-l2">							<h5><b>Deploy</b></h5>							<div class="lineal-block">								<button class="btn3">Instale en Google App Engine</button>								<button class="btn3">Instale en OpenShift</button>								<button class="btn3">Deploy a PythonAnywhere</button>														</div>							</div>												<hr class="h">						<div class="marg-l2">							<b>Asistente para una nueva aplicación</b>						<button class="btn3">Asistente</button>						</div>						<hr class="h">						<div class="marg-l2"> 						<div class="lineal">						<b>Comunidad </b><button class="btn3">Foro</button>						<button class="btn3">Chat</button>						</div>						</div>												'
incluir(data,"chat-box")
print '										</div>			</div>'
