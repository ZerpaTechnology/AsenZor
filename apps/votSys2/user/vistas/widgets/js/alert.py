print '''$(document).ready(function () {''',
a=["hola mundo"]
print '''	''',
for elem in ["a","b","c"]:
  print '''		''',
  if elem =="a":
    print '''			alert("''',    print elem    print '''");		''',
  else:
    print '''			''',
    pass
  print '''	''',
  pass
print '''	console.log('javascript');})''',