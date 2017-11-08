function infoFrame(userFrameStr) {
    // 头像自动截取用户名最后一个字符生成头像
    spstr = userFrameStr.split("");
    spstr = spstr[spstr.length - 1];
    $("#Userframe").html(spstr);
}

function editInfo() {
    // 编辑信息函数
    var userInfo_name = $("#userInfo_name");
    var inputHTML_name = "<input type='text' class='edit_input' id='Edited_name' value='" + userInfo_name.text() + "'>";
    userInfo_name.html(inputHTML_name);

    var userInfo_sex = $("#userInfo_sex");
    var inputHTML_sex = "<select id='Edited_sex'><option value='男'>男</option><option value='女'>女</option></select>";
    userInfo_sex.html(inputHTML_sex);

    var userInfo_stuProvince = $("#userInfo_stuProvince");
    var inputHTML_stuProvince = "<select id='Edited_stuProvince'><option value='江西'>江西</option><option value='山西'>山西</option><option value='四川'>四川</option><option value='湖南'>湖南</option></select>";
    userInfo_stuProvince.html(inputHTML_stuProvince);

    var userInfo_stuType = $("#userInfo_stuType");
    var inputHTML_stuType = "<select id='Edited_stuType'><option value='文科'>文科</option><option value='理科'>理科</option></select>";
    userInfo_stuType.html(inputHTML_stuType);


    var userInfo_schoolAddress = $("#userInfo_schoolAddress");
    var inputHTML_schoolAddress = "<input type='text' class='edit_input' id='Edited_schoolAddress' value='" + userInfo_schoolAddress.text() + "'>";
    userInfo_schoolAddress.html(inputHTML_schoolAddress);

    var userInfo_score = $("#userInfo_score");
    var inputHTML_score = "<input type='text' class='edit_input' id='Edited_score' value='" + userInfo_score.text() + "'>";
    userInfo_score.html(inputHTML_score);



    var userInfo_rank = $("#userInfo_rank");
    
    var inputHTML_rank = "<input type='text' class='edit_input' id='Edited_rank' value='" + userInfo_rank.text() + "'>";
    userInfo_rank.html(inputHTML_rank);

    var buttonHTML = "<a onclick='SaveInfo();'>保存信息</a>";
    var button = $("#userInfo_Edit");
    button.html(buttonHTML);
}

function SaveInfo() {
    // 保存信息函数
    var name = $("#Edited_name").val();
    var sex = $("#Edited_sex").val();
    var stuProvince = $("#Edited_stuProvince").val();
    var stuType = $("#Edited_stuType").val();
    var schoolAddress = $("#Edited_schoolAddress").val();
    var score = $("#Edited_score").val();
    var rank = $("#Edited_rank").val();
    //alert(rank)
    $.ajax({
        type: "POST",
        data: {
            "username": name,
            "sex": sex,
            "stuProvince": stuProvince,
            "stuType": stuType,
            "schoolAddress": schoolAddress,
            "score": score,
            "rank": rank,
        },
        url: "/edit_user/",
        cache: false,
        dataType: "html",
        success: function(data, status, xml) {
            data = JSON.parse(data);
            //alert(data.Msg);
            var userInfo_name = $("#userInfo_name");
            userInfo_name.html(name);
            var userInfo_sex = $("#userInfo_sex");
            userInfo_sex.html(sex);
            var userInfo_stuProvince = $("#userInfo_stuProvince");
            userInfo_stuProvince.html(stuProvince);
            var userInfo_stuType = $("#userInfo_stuType");
            userInfo_stuType.html(stuType);
            var userInfo_schoolAddress = $("#userInfo_schoolAddress");
            userInfo_schoolAddress.html(schoolAddress);
            var userInfo_score = $("#userInfo_score");
            userInfo_score.html(score);
            var userInfo_rank = $("#userInfo_rank");
            userInfo_rank.html(rank);

            var buttonHTML = "<a onclick='editInfo();'>编辑信息</a>";
            var button = $("#userInfo_Edit");
            button.html(buttonHTML);
            infoFrame(name);
        }
    })
}