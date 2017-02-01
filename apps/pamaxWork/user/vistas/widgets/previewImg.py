print '''<!--Parametros requeridos: input , output , detalle --><div><style>  .thumb {    height: 75px;    border: 1px solid #000;    margin: 10px 5px 0 0;  }</style><input type="file" id="''',data['input'],'''" name="''',data['input'],'''[]" multiple /><output id="''',data['output'],'''"></output><script type="text/javascript">''',
importar(data,"previewImg")
print '''</script></div>''',