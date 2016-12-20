def phpload(url,script,browser=False):
	import os
	if browser==False:
		os.system("php "+script)
	else:
		print '<iframe src="'+url+script+'">'+'</iframe>'