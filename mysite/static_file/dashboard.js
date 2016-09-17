$(function() {
    $.ajax({
        type: 'GET',
        url: '/api/get_strategy_list',
        dataType: 'json',
        success: function(data) {
            var strategy_list = data["strategy_list"];
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
                window.location = "/strategy_list/" + $(this).attr("stock_id");
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
        window.location = "/stock_list/" + $(this).attr("stock_id");
    });
})