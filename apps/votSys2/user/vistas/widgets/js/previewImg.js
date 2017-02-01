
  function handleFileSelect(evt) {
    var files = evt.target.files; /* FileList object*/
 
    /* Loop through the FileList and render image files as thumbnails.*/
    for (var i = 0, f; f = files[i]; i++) {
 
      /* Only process image files.*/
      if (!f.type.match('image.*')) {
        continue;
      }
 
      var reader = new FileReader();
 
      /* Closure to capture the file information.*/
      reader.onload = (function(theFile) {
        return function(e) {
          /* Render thumbnail.*/
          var span = document.createElement('span');
          {{if data["detalle"]==True:}}
            span.innerHTML = ['Nombre: ', escape(theFile.name), ' || Tamanio: ', escape(theFile.size), ' bytes || type: ', escape(theFile.type), '<br /><img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/><br />'].join('');
          {{else:}}
             span.innerHTML = ['<br /><img class="thumb" src="', e.target.result,'" title="', escape(theFile.name), '"/><br />'].join('');
          {{pass}}  
          document.getElementById('{{print data["output"]}}').insertBefore(span, null);
        };
      })(f);
 
      /* Read in the image file as a data URL.*/
      reader.readAsDataURL(f);
    }
  }
 
  document.getElementById('{{print data["input"]}}').addEventListener('change', handleFileSelect, false);
