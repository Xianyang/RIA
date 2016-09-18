$(function() {
    $.ajax({
        type: 'GET',
        url: '/api/model_list',
        dataType: 'json',
        success: function(data) {
            var strategy_list = data["model_list"];
            $("#strategy_list_info").html("");
            for (var i = 0; i < strategy_list.length; i++) {
                var htmlStr = "<tr stock_id='" + strategy_list[i].id + "'>";
                htmlStr += "<td>" + strategy_list[i].code + "</td>"
                htmlStr += "<td>" + strategy_list[i].objective + "</td>"
                htmlStr += "<td>" + strategy_list[i].return+"</td>"
                htmlStr += "<td>" + strategy_list[i].risk + "</td>"
                htmlStr += "<td>" + strategy_list[i].value_at_risk + "</td>"
                htmlStr += "</tr>"
                $("#strategy_list_info").append(htmlStr)
            }
            $("#strategy_list_info tr").on('click', function() {
                window.location = "/model/" + $(this).attr("stock_id");
            });
        }
    });


    var strategy_list = [{
        "id": 123,
        "code": "1,001",
        "objective": "Lorem",
        "return": "ipsum",
        "risk": "dolor",
        "value_at_risk": "sit"
    }, {
        "id": 456,
        "code": "1,001",
        "objective": "Lorem",
        "return": "ipsum",
        "risk": "dolor",
        "value_at_risk": "sit"
    }];
    for (var i = 0; i < strategy_list.length; i++) {
        strategy_list[i].return =  (parseFloat(strategy_list[i].return) * 100).toFixed(1) + '%';
        strategy_list[i].risk =  (parseFloat(strategy_list[i].risk) * 100).toFixed(1) + '%'
        strategy_list[i].value_at_risk =  (parseFloat(strategy_list[i].value_at_risk) * 100).toFixed(1) + '%'
        var htmlStr = "<tr stock_id='" + strategy_list[i].id + "'>";
        htmlStr += "<td>" + strategy_list[i].code + "</td>"
        htmlStr += "<td>" + strategy_list[i].objective + "</td>"
        htmlStr += "<td>" + strategy_list[i].return+"</td>"
        htmlStr += "<td>" + strategy_list[i].risk + "</td>"
        htmlStr += "<td>" + strategy_list[i].value_at_risk + "</td>"
        htmlStr += "</tr>"
        $("#strategy_list_info").append(htmlStr)
    }
    $("#strategy_list_info tr").on('click', function() {
        window.location = "/model?id=" + $(this).attr("stock_id");
    });

    for (var i = 20; i <= 85; i++) {
        $("#user_age_select").append("<option value='" + i + "'>" + i + "</option>")
    }
    for (var i = 20; i <= 85; i++) {
        $("#retire_age_select").append("<option value='" + i + "'>" + i + "</option>")
    }
    $("#user_profile_form select,#user_profile_form input").change(function(){
        $.ajax({
           type: "POST",
           url: "/save_user_profile/",
           data: $("#user_profile_form").serialize(), // serializes the form's elements.
           success: function(data)
           {
               console.log(data)
           }
         });
    });
})