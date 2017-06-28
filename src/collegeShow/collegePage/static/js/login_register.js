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

function show_login() {
    showMask();
    $(".register").css('display', 'none');
    $(".login").css('display', 'block');
}

function show_register() {
    showMask();
    $(".login").css('display', 'none');
    $(".register").css('display', 'block');
}

function login() {
    var username = $("#login_username").val();
    var password = $("#login_password").val();
    $.ajax({
        type: "POST",
        data: {
            "username": username,
            "password": password,
        },
        url: "/login/",
        dataType: "html",
        success: function(data, status, xml) {
            data = JSON.parse(data);
            //alert(data.Msg);
            hideMask();
            window.location.href =window.document.location.pathname;
            //location.reload()
        }
    })
}

function register() {
    var username = $("#register_username").val();
    var password = $("#register_password").val();
    var stuprovince = $("#register_stuprovince").val();
    var stutype = $("#register_stutype").val();
    var score = $("#registet_score").val();
    $.ajax({
        type: "POST",
        data: {
            "username": username,
            "password": password,
            "stuProvince": stuprovince,
            "stuType": stutype,
            "score": score,
        },
        url: "/register/",
        cache: false,
        dataType: "html",
        success: function(data, status, xml) {
            data = JSON.parse(data);
            alert(data.Msg);
            location.reload();
        }
    })
}

