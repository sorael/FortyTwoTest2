$(document).ready(function () {

    var defaultTitle = "Requests";
    var isActive = true;

    $('#sort').click(function () {
        if ($(this).attr('class') == "fa fa-angle-down") {
            $(this).removeClass("fa fa-angle-down");
            $(this).addClass("fa fa-angle-up");
            $(this).attr('title', '-date_time');
        } else {
            $(this).removeClass("fa fa-angle-up");
            $(this).addClass("fa fa-angle-down");
            $(this).attr('title', 'date_time');
        }
    });

    window.onfocus = function () {
      isActive = true;
    };
    window.onblur = function () {
      isActive = false;
    };

    function changePriority(el){
        var priority = $(el).val();
        var request_id = $(el).attr('id').slice(1);
        $.ajax({
            url: '/change_priority/',
            data: {'priority': priority, 'request_id': request_id},
            success: function(data) {
                if(data.success == 'true') {
                    alert("Request priority was changed.");
                } else if (data.success == 'false') {
                    alert("Request priority wasn't changed.");
                }
            }
        });
    }

    function isHover(){
        $.ajax({
            url: "/priority_requests/",
            data: {'priority': $('.active').attr('id'),
            'sort': $('#sort').attr('title')},
            success: function(data) {
                if (data.success == 'false') {
                    alert("Something happening. Please, reload the page.");
                } else if (data.success == 'true') {
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
                        row.append($('<td>').html('<input class="priority" type="number" min="1" max="3" id="p'
                            + request.id + '"' + ' value="' + request.priority + '" />'));
                        tbody.append(row);
                    });
                    $('.priority').change(function () {
                        changePriority(this);
                    });
                }
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

    setInterval(function (){(isActive) ? isHover() : loadCount();}, 1500);
});