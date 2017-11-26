function showMask() {
    $(".mask").css("height", $(document).height());
    $(".mask").css("width", $(document).width());
    $(".mask").show();
}

function hideMask() {
    $(".mask").hide();
    $(".login").css('display', 'none');
    $(".register").css('display', 'none');
}

//function show_login() {
//    showMask();
//    $(".register").css('display', 'none');
//    $(".login").css('display', 'block');
//}





