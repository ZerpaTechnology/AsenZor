#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-type: text/html\n\n"
print '<meta charset="utf-8">'
print "<html>controlador: vista!</html>"
import os
import sys
sys.path.append("../../../config")
import config
newRoot=os.environ['REDIRECT_URL'].split("/")
print newRoot
def index():
	return dict()
def pagina2():
	return dict()