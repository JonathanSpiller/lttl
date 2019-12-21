$( document ).ready(function() {
    
    $('#url-input').click(function () {
        $('#url-output').removeClass('red-glow').removeClass(' yellow-glow');
    })

    $('#daytime').click(function () {
        window.location.href = $(this).attr('rel');
    })

    $('#make-little').click(function () {
        var url = $('#url-input').val();
       
        if (url.trim() == ""){
            return;
        }
        if (!url.includes('http://') && !url.includes('https://') && !url.includes('www') && !url.includes('.')){
            $('#url-output').val("That url is a little broken!").addClass('red-text red-glow');
            $('#url-output-holder').css('visibility', 'visible');
            return;
        }

        var csrftoken = getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url: $(this).attr('rel'),
            type: 'post',
            data: {url: url},
            success: function(response) {
                $('#url-output').val(response).addClass(' yellow-glow');
                $('#url-output-holder').css('visibility', 'visible')
            },
            failure: function(response) {
                alert('Got an error dude');
            }
        });
    });  

})