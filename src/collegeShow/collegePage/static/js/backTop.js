function a(x,y){
	l = $('#main').offset().left;
	w = $('#main').width();
	$('#tbox').css('left',(l + w + x) + 'px');
	$('#tbox').css('bottom',y + 'px');
}
function b(){
	h = $(window).height();
	t = $(document).scrollTop();
	if(t > h){
		$('#gotop').fadeIn('slow');
	}else{
		$('#gotop').fadeOut('slow');
	}
}
$(document).ready(function(e) {		
	a(10,10);//#tbox的div距浏览器底部和页面内容区域右侧的距离
	b();
	$('#gotop').click(function(){
		$(document).scrollTop(0);	
	})
});
$(window).resize(function(){
	a(10,10);//#tbox的div距浏览器底部和页面内容区域右侧的距离
});

$(window).scroll(function(e){
	b();		
})
/* 转载请保留版权信息：97站长网 www.97zzw.com */