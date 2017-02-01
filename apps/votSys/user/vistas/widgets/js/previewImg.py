#!/usr/bin/python
# -*- coding: utf-8 -*-
print '''  function handleFileSelect(evt) {    var files = evt.target.files; /* FileList object*/     /* Loop through the FileList and render image files as thumbnails.*/    for (var i = 0, f; f = files[i]; i++) {       /* Only process image files.*/      if (!f.type.match('image.*')) {        continue;      }       var reader = new FileReader();       /* Closure to capture the file information.*/      reader.onload = (function(theFile) {        return function(e) {          /* Render thumbnail.*/          var span = document.createElement('span');          '''
if data["detalle"]==True:
  print '''            span.innerHTML = ['Nombre: ', escape(theFile.name), ' || Tamanio: ', escape(theFile.size), ' bytes || type: ', escape(theFile.type), '<br /><img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/><br />'].join('');          '''
else:
  print '''             span.innerHTML = ['<br /><img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/><br />'].join('');          '''
  pass
print """            document.getElementById('"""+str(data["output"])+"""').insertBefore(span, null);        };      })(f);       /* Read in the image file as a data URL.*/      reader.readAsDataURL(f);    }  }   document.getElementById('"""+str(data["input"])+"""').addEventListener('change', handleFileSelect, false);"""