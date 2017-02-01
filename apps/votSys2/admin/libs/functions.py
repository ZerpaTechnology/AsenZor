def ajax(url,parameros):
	f=open(url,"w")
	f.write(str(parameros))
	f.close()
def phpload(url,script,browser=False):
	import os
	if browser==False:
		os.system("php "+script)
	else:
		print '<iframe src="'+url+script+'" style="border:none;width:100%;">'+'</iframe>'