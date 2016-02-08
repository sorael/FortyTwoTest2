$(document).ready(function() {
    function block_form() {
        $("#loading").show();
        $('textarea').attr('disabled', true);
        $('input').attr('disabled', true);
    }

    function unblock_form() {
        $('#loading').hide();
        $('textarea').removeAttr('disabled');
        $('input').removeAttr('disabled');
        $('.errorlist').remove();
    }

    var options = {
        beforeSubmit: function() {
            block_form();
            $("#form_ajax").hide();
        },
        success: function(data) {
            if (data['success'] == 'true') {
                    unblock_form();
                    $('#contact_photo_id').attr('src', '/uploads/'+ data.photo);
                    $("#form_ajax").show();
                    setTimeout(function() {
                        $("#form_ajax").hide();
                    }, 3000);
                }
            else if (data['success'] == 'false') {
                unblock_form();
                $("#form_ajax_error").show();
                var errors = data.errors;
                for (err in errors) {
                    var id = '#id_' + err;
                    $(id).before(errors[err]);
                }
                setTimeout(function() {
                    $("#form_ajax_error").hide();
                }, 3000);
            }
        }
    };

    $('#editform').ajaxForm(options);
});