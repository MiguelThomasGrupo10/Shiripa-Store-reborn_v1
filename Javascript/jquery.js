$(document).ready(function(){
    $("#form-contacto").validate({
        rules:{
            email:{required: true, email: true},
            seleccion:{required: true},
            textcontact:{required: true, minlenght: 10, maxlenght:500},
        },
        messages:{
            email: "El campo es obligatorio.",
            textcontact: "Debe contener menos de 500 letras.",
            seleccion: "Debes elegir una opcion."
        }
    });
    $('#enviarform').on('click',function(){
        $("#form-contacto").valid()
    });
});