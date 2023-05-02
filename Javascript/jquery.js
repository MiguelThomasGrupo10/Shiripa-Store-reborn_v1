$(document).ready(function(){
    $("#form-contacto").validate({
        ignore:[],
        debug:false,
        rules:{
            email:{required: true, email: true},
            seleccion:{required: true},
            textoarea:{required: true},
        },
        messages:{
            email: "Se requiere completar este campo.",
            textoarea:{
                required:"Se requiere completar este campo.",
            },
            seleccion: "Debes elegir una opcion."
        }
    });
    $('#enviarform').on('click',function(){
        $("#form-contacto").valid()
    });
});