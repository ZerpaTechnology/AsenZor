#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''$(document).ready(function () {'''
a=["hola mundo"]
print '''	'''
for elem in ["a","b","c"]:
  print '''		'''
  if elem =="a":
    print '''			alert("'''    +str(elem)    +'''");		'''
  else:
    print '''			'''
    pass
  print '''	'''
  pass
print '''	console.log('javascript');})'''