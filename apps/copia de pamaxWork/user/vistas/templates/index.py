# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html lang="en"><head>	<meta charset="UTF-8">	<title>Administrador</title>	<meta http-equiv="X-UA-Compatible" content="IE=edge">	<meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">	<link rel="stylesheet" href="'''
print data['base_url']
print '''static/css/font/flaticon.css">	<link rel="stylesheet" href="'''
print data['base_url']
print '''static/css/admin.css">	<link rel="stylesheet" href="'''
print data['base_url']
print '''static/css/normalize.css">	<link rel="stylesheet" href="'''
print config.base_url
print '''static/css/ff.css"></head><body id="login">	<section class="log">		<div class="ed-container">			<div class="ed-item">				<div class="login">					<img class="login__logo" src="img/logopamax2.png" alt="logo">				</div>				<div class="login__contenedor">					<form action="post.py" class="sing" method="post" >						<input class="sing__campo using__usuario" type="text" placeholder="Usuario" name="user">						<input class="sing__campo sing__password" type="password" placeholder="Contraseña" name="password">						<input class="hidden" name="action" value="sing_in">						<input type="submit" name="" value="Entrar" class="sing__entrar">											</form>				</div>				<p class="login__footer">Panel de Personal</p>			</div>		</div>			</section></body></html>'''
