<?php

class roots
{
	function __construct(){
	$libs_folder="libs/";
	$models_folder="modelos/";
	$ajax_file="ajax.json";
	}

}




class config
{
	public function __construct(){
		$_config = json_decode(file_get_contents("../../../../config/config.json"),true);
		
		foreach ($_config as $key => $value) {
			if (is_array($value)==true){
				if ($value !=[]){
					eval('$'."this->".$key."="."['".implode(",",$value)."']".";\n");
					
				}
				else{
					eval('$'."this->".$key."="."[]".";\n");
				}
			}
			else{
				if (is_string($value)==true){
					eval('$'."this->".$key."='".$value."';\n");
				}
				else{
					eval('$'."this->".$key."=".$value.";\n");
				}
			}
		}
		$_file=fopen("../../../../config/config.json","w");
		fwrite($_file,"");
		fclose($_flise);

	}

}









?>