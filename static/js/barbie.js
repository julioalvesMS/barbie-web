
var cFiles = [];
var hFiles = [];

function main(){
    // Check if all submission conditions are satisfied
    $('form').submit(function(event){
        if(checkClassInfo()){
            return;
        }
        event.preventDefault();
    });
}

function checkClassInfo(){
    var ok = true;
    if($('input[name="disciplina"]').val()==='') {
        notification('Informe a disciplina');
        ok = false;
    }
    else if ($('input[name="turma"]').val()==='') {
        notification('Informe a turma');
        ok = false;
    }
    else if ($('input[name="lab"]').val()==='') {
        notification('Informe o numero do laboratório');
        ok = false;
    }
    return ok;
}

//
function submitLab(){
    var disciplina = $('input[name="disciplina"]').val();
    var turma = $('input[name="turma"]').val();
    var lab = $('input[name="lab"]').val();
}

// Notifica o usuario de uma mensagem de erro
function notification(msg) {
    alert(msg);
}

$(document).ready(main);
