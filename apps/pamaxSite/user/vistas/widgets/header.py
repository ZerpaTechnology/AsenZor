#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''		<header id="header row">			<div class="ed-container container-header">				<div class="ed-item web-25 web-main-start azul">					<div class="logo">						<img class="logo__img" src="'''+str(data['base_url'])+'''static/img/logopamax2.png" alt="logo">					</div>				</div>'''+str(data["logueado"])+''''''
if data["logueado"]==True:
  print '''				<div class="ed-item web-75 web-main-end web-cross-center">					<ul class="menu">						<li class="menu__item" id="hamburguer"><a class="menu__link bt-menu"><span class="flaticon-list-1 close"></span></a></li>						<li class="menu__item"><a class="menu__link" href="#"><span class="flaticon-envelope"></span></a></li>						<li class="menu__item"><a class="menu__link" href="#"><img class="imagen-perfil" src="'''  +str(data['base_url'])  +'''static/img/yohangel.svg" alt=""> Yohangel Ramos</a></li>					</ul>				</div>'''
else:
  print ''''''
  pass
print '''			</div>		</header>'''