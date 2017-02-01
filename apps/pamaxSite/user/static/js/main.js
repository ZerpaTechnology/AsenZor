$(document).ready(function(){


	$('.submenu').click(function(){
		$(this).next().slideToggle();

		if($('.up-down').hasClass('flaticon-chevron-arrow-down')){
			$('.up-down').removeClass('flaticon-chevron-arrow-down');
			$('.up-down').addClass('flaticon-chevron-arrow-up');
		}else if($('.up-down').hasClass('flaticon-chevron-arrow-up')){
			$('.up-down').removeClass('flaticon-chevron-arrow-up');
			$('.up-down').addClass('flaticon-chevron-arrow-down');
		}
	});

	$('.bt-menu').click(function(){
			main();	
		if($('.close').hasClass('flaticon-list-1')){
			$('.up-down').removeClass('flaticon-list-1');
			$('.up-down').addClass('flaticon-cancel');
		}else if($('.close').hasClass('flaticon-cancel')){
			$('.up-down').removeClass('flaticon-cancel');
			$('.up-down').addClass('flaticon-list-1');
		}
	});

	$('.department__empleado').on('click','h4',function(){
		var t = $(this);
		var tp = t.next();
		var p = t.parent().siblings().find('.department__empleado--content');
		tp.slideToggle();
		p.slideUp()
	});


	$('a.cronometro__conteo').click(function(){
		$('#modal').show();
		$('#modal').addClass("animated fadeInDown");
	})

	
});

var contador = 1;
function main(){
	if(contador == 1){
		$('.menu-lateral').animate({
			left:'0'
	});
		contador = 0;
	}else{
		contador = 1;
		$('.menu-lateral').animate({
		left:'-100%'
		});
	}
};