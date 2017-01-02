#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("modulos")
from ztec.zred import serverSock,sendEmail
from ztec import zu
data=[""]
serverSock("localhost",9999,"",data)
while data[0]!=".salir":
	if data[0]!="":
		if data[0][:len("python zred.sendEmail(")]=="python zred.sendEmail(":
			args=data[0][len("python zred.sendEmail("):-1].split(",")
			sendEmail(args[0],args[1],args[2],args[3],args[4],debug=True)


		else:
			print data[0]
