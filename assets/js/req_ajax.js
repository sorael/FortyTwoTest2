$(document).ready(function () {
    var defaultTitle = "Requests";
    var isActive;

    window.onfocus = function () {
      isActive = true;
    };
    window.onblur = function () {
      isActive = false;
    };

    function isHover(){
        $.ajax({
            url: "/requests/",
            success: function(data) {
                $("title").text(defaultTitle);
                var tbody = $('tbody').html('');
                data.requests.forEach(function (request, i) {
                    var row = $('<tr id="'+ request.id +'">');
                    row.append($('<td>').text(i + 1));
                    row.append($('<td>').text(request.date_time));
                    row.append($('<td>').text(request.method));
                    row.append($('<td>').text(request.file_path));
                    row.append($('<td>').text(request.ver_protocol));
                    row.append($('<td>').text(request.status));
                    row.append($('<td>').text(request.content));
                    tbody.append(row);
                });
            }
        });
    }

    function loadCount(){
        $.ajax({
            url: "/requests_count/",
            data: {'id': $('tr:eq(1)').attr('id')},
            success: function(data) {
                $("title").text(data.len + " " + defaultTitle);
            }
        });
    }

    setInterval(function (){(isActive) ? isHover() : loadCount();}, 2000);
});