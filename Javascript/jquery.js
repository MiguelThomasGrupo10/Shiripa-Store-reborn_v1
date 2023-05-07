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


//INTEGRACIÓN DE API RESCATANDO INFORMACIÓN
//INTEGRACIÓN DE API RESCATANDO INFORMACIÓN
//NOTA: este jquery fue sacado de apiComidas ejercicio YARAVI
$(document).ready(function(){
    $("#enviar").click(function(){
        $.get("https://nosotros-ce6c2-default-rtdb.firebaseio.com/Empresas.json",
        function(data){
            $.each(data.Empresas, function(i,item){
                $("#categorias").append("<tr><td>"+item.idCategory+"</td><td>"+
                item.strCategory + "</td><td><img src='" + item.strCategoryThumb + "'></td><td>" +
                item.strCategoryDescription + "</td></tr>");
            });
        });
    });
});
