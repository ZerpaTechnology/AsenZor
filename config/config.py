#!/usr/bin/python
proyectos=["default","ej"]#lista de proyectos en el framework
proyectos_disp=["ej","default"]#lista de proyectos habilitados
base_url="http://localhost/webpyzer/"
apps=["default"]
libs_folder="modulos"
libs=["ztec"]#librerias cargadas en el framework
mod_debug=True;
apps_url="app/"
projects_url="projects/"

logs=base_url+"log.txt"
lengs=["es","en"]
leng_default=["es"]
host="https://localhost/"
fmk_url="webpyzer/"
base_url=host+fmk_url
base_url_absolute="/opt/lampp/htdocts/"+fmk_url
default_app="default"
default_controler="default"
controler_url="control/"+default_controler

vistas=["default"]#lista de todos la vistas html sin codigo python embebido
templates=[]#lista de todos los templates (vistas con codigo python embebido y widgets)
widgets=[]#lista con todos los widgets(templates minimalistas)
vistas_disp=["default"]#lista con las vistas disponibles para mostrar
templates_disp=[]#lista con los templates disponibles para mostrar
widgets_disp=[]#lista con los widgets disponibles para mostrar
custom_url=None

