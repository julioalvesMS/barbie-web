
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

// Pega a lista de todos os arquivos de codigo e header que devem ser upados
function getFiles(){
    // Esvazia o array, que pode possuir dados de tentativas anteriores de submissão
    cFiles = [];
    hFiles = [];

    // Pega os arquivos de codigo
    for(var i=0;i<$('code-file').length;i++){
        if ($('code-file')[i].val() !== '') {
            cFiles.append($('code-file')[i].val());
        }
    }
    // Pega os arquivos de header
    for(var i=0;i<$('header-file').length;i++){
        if ($('header-file')[i].val() !== '') {
            hFiles.append($('header-file')[i].val());
        }
    }

    console.log(hFiles);
    console.log(cFiles);

    // Necessario ao menos um arquivo de
    if(cFiles.length<1) {
        notification('Forneça ao menos 1 arquivo de código');
        return false;
    }
    else {
        return true;
    }
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
