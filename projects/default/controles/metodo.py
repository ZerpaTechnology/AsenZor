#! /usr/bin/python
#-*- coding:utf-8-*-
print "Content-type: text/html\n\n"
print "<html>Hello world!"
newRoot=os.environ['REDIRECT_URL'].split("/")
print [newRoot]
def imp():
	print "hola"

