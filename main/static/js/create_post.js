$(document).ready(function () {

    //Set page subtitle
    $('#blog-span').text("Блог / Добавить статью");

    //Init rich text editor
    tinymce.init({
        selector: '#post-text'
    });

    //Preview image before adding
    function readURL(input) {

        if (input.files && input.files[0]) {

            $('#image-preview-p').html("<div class='image'>" +
                "<div class='overlay'>" +
                "<i id='delete-icon' class='material-icons'>cancel</i> " +
                "</div>" +
                "   <img style='max-width: 100%;' id=\"post-image-preview\" alt=\"your image\">" +
                "</div>");

            var reader = new FileReader();

            reader.onload = function (e) {
                $('#post-image-preview').attr('src', e.target.result);
            };

            reader.readAsDataURL(input.files[0]); // Convert to base64 string

            //Remove image btn
            $('#delete-icon').click(function () {
                $('.image').remove()
            })

        }
    }

    //Set listener on hidden input
    $("#post-image").change(function () {
        readURL(this);
    });

});