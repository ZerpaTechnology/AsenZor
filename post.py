#!/usr/bin/python
# -*- coding: utf-8 -*-
print "Content-type: text/html\n\n"

# Import modules for CGI handling 
import cgi, cgitb

# Create instance of FieldStorage 
data= cgi.FieldStorage()

# Get data from fields
output = data["param"]

# This will print to stdout for testing
print("Hello World!!!")
print(output)