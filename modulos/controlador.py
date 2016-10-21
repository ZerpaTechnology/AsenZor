#!/usr/bin/python
# -*- coding: utf-8 -*-
	import cgi
	import os
	import time
	sys.path.append("../../config")
	import config
	sys.path.append("../../"+config.libs_folder)
	import ztec
	archivo_act=sys.argv[0].split("/")[-1]
	
	for elem in config.libs:
		exec("import "+elem)
	
	request=cgi.FieldStorage()