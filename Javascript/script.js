//VALIDACION micuenta.html FORMULARIO HTML
//VALIDACION micuenta.html FORMULARIO HTML

function Ingreso(){
    var user,password,chk,txt;
    
    user = document.getElementById("username").value;
    password = document.getElementById("pwd").value;
    chk = document.getElementById("chkHtml").value;
    
    //USUARIO
    if (user.length == 0){
        txt = 'Usuario no debe estar vacío';
    }else{
        txt = "";
    }
    document.getElementById("valida_usuario").innerHTML = txt;

    //CONTRASEÑA
    if (password.length == 0){
        txt = "Escriba una contraseña"; 
    }else if (password.length > 1 && password.length < 6){
        txt = "Contraseña muy corta";
    }else{
        txt ="";
    }
    document.getElementById("valida_contraseña").innerHTML = txt;

    
    //CHECKBOX
   if (chk = true){
    txt = "sesión abierta";
   }else{
    txt = "";
   }
   document.getElementById("valida_checkbox").innerHTML = txt
}





