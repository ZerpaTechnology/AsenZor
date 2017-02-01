# -*- coding: utf-8 -*-
print '''<!DOCTYPE html><html><head><link rel="stylesheet" href="'''
print config.base_url
print '''static/css/ff.css">	<title></title></head><body><form action="post.py">	user<input type="text" name="user">	password<input type="password" name="password">	email<input type="email" name="email">	name<input type="text" name="name">	lastname<input type="text" name="lastname">	rank<input type="number" name="rank">	avatar<input type="text" name="avatar">	department<input type="number" name="department_id">	position<input type="number" name="position_id">	<input type="submit" name="">	<input type="text" class="hidden" name="action" value="sing_up">	</form></body></html>'''
