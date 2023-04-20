//VALIDACION micuenta.html FORMULARIO HTML
//VALIDACION micuenta.html FORMULARIO HTML

function Ingreso(){
    var user,password,chk;
    user = document.getElementById("valida_usuario").value;
    password = document.getElementById("valida_contraseña").value;
    chk = document.getElementById("valida_checkbox").value;
    
    if (user){

    }
}





//FUNCION EJEMPLO

function validar(){
    var usu,pass,text;
    usu = document.getElementById("correo").value;
    pass = document.getElementById("password").value;

    if (usu.length == 0){
        text = "Usuario no debe estar vacío";   
    }else{
        text = "";
    }
    document.getElementById("valida_email").innerHTML = text;
    if (pass.length != 8){
        text = "Contraseña debe tener largo 8";
    }else{
        text = "";
    }
    document.getElementById("valida_password").innerHTML = text;
}