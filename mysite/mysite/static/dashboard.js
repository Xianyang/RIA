$(function () {
    $.ajax({
        type: 'GET',
        url: '/api/model_list',
        dataType: 'json',
        success: function (data) {
            strategy_list = data["model_list"];
            $("#strategy_list_info").html("");
            for (var i = 0; i < strategy_list.length; i++) {
                strategy_list[i].risk_value = parseFloat(strategy_list[i].risk);
                strategy_list[i].return = (parseFloat(strategy_list[i].return) * 100).toFixed(1) + '%';
                strategy_list[i].risk = (parseFloat(strategy_list[i].risk_value) * 100).toFixed(1) + '%'
                strategy_list[i].value_at_risk = (parseFloat(strategy_list[i].value_at_risk) * 100).toFixed(1) + '%'

                var htmlStr = "<tr stock_id='" + strategy_list[i].id + "'>";
                htmlStr += "<td>" + strategy_list[i].code + "</td>"
                htmlStr += "<td>" + strategy_list[i].objective + "</td>"
                htmlStr += "<td>" + strategy_list[i].return + "</td>"
                htmlStr += "<td>" + strategy_list[i].risk + "</td>"
                htmlStr += "<td>" + strategy_list[i].value_at_risk + "</td>"
                htmlStr += "</tr>"
                $("#strategy_list_info").append(htmlStr)
            }
            $("#strategy_list_info tr").on('click', function () {
                window.location = "/model/" + $(this).attr("stock_id");
            });
        }
    });


    //var strategy_list = [{
    //    "id": 123,
    //    "code": "1,001",
    //    "objective": "Lorem",
    //    "return": "ipsum",
    //    "risk": "dolor",
    //    "value_at_risk": "sit"
    //}, {
    //    "id": 456,
    //    "code": "1,001",
    //    "objective": "Lorem",
    //    "return": "ipsum",
    //    "risk": "dolor",
    //    "value_at_risk": "sit"
    //}];
    //for (var i = 0; i < strategy_list.length; i++) {
    //    strategy_list[i].return = (parseFloat(strategy_list[i].return) * 100).toFixed(1) + '%';
    //    strategy_list[i].risk = (parseFloat(strategy_list[i].risk) * 100).toFixed(1) + '%'
    //    strategy_list[i].value_at_risk = (parseFloat(strategy_list[i].value_at_risk) * 100).toFixed(1) + '%'
    //    var htmlStr = "<tr stock_id='" + strategy_list[i].id + "'>";
    //    htmlStr += "<td>" + strategy_list[i].code + "</td>"
    //    htmlStr += "<td>" + strategy_list[i].objective + "</td>"
    //    htmlStr += "<td>" + strategy_list[i].return + "</td>"
    //    htmlStr += "<td>" + strategy_list[i].risk + "</td>"
    //    htmlStr += "<td>" + strategy_list[i].value_at_risk + "</td>"
    //    htmlStr += "</tr>"
    //    $("#strategy_list_info").append(htmlStr)
    //}
    $("#strategy_list_info tr").on('click', function () {
        window.location = "/model?id=" + $(this).attr("stock_id");
    });

    for (var i = 20; i <= 85; i++) {
        $("#user_age_select").append("<option value='" + i + "'>" + i + "</option>")
    }
    for (var i = 20; i <= 85; i++) {
        $("#retire_age_select").append("<option value='" + i + "'>" + i + "</option>")
    }
    $("#user_profile_form select,#user_profile_form input").change(function () {
        $.ajax({
            type: "POST",
            url: "/save_user_profile/",
            data: $("#user_profile_form").serialize(), // serializes the form's elements.
            success: function (data) {
                strategy_list[i]
                var reference = $("#user_profile_form [name='risk_preference']").val();
                var min = 0;
                var max = 1;
                if(reference=="High"){
                    min = 0.28
                    max = 0.4
                }
                if(reference=="Above Average"){
                    min = 0.20
                    max = 0.28
                }
                if(reference=="Above Average"){
                    min = 0.12
                    max = 0.20
                }
                if(reference=="Below Average"){
                    min=0.06
                    max=0.12
                }
                if(reference=="Low"){
                    min = 0
                    max = 0.06
                }
                updateTable(min,max)

                console.log(data)
            }
        });
    });

    function compare(a, b) {
        if (a.risk_value < b.risk_value)
            return -1;
        if (a.risk_value > b.risk_value)
            return 1;
        return 0;
    }

    function updateTable(min_risk,max_risk) {
        $("#strategy_list_info").html("");
        for (var i = 0; i < strategy_list.length; i++) {
            if(strategy_list[i].risk_value<min_risk || strategy_list[i].risk_value>max_risk){
                continue
            }

            var htmlStr = "<tr stock_id='" + strategy_list[i].id + "'>";
            htmlStr += "<td>" + strategy_list[i].code + "</td>"
            htmlStr += "<td>" + strategy_list[i].objective + "</td>"
            htmlStr += "<td>" + strategy_list[i].return + "</td>"
            htmlStr += "<td>" + strategy_list[i].risk + "</td>"
            htmlStr += "<td>" + strategy_list[i].value_at_risk + "</td>"
            htmlStr += "</tr>"
            $("#strategy_list_info").append(htmlStr)
        }

        $("#strategy_list_info tr").on('click', function () {
            window.location = "/model/" + $(this).attr("stock_id");
        });
    }
})