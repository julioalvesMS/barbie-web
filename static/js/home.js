var cFiles = [];
var hFiles = [];

function main(){
    // Check if all submission conditions are satisfied
    $('form').submit(function(event){
        if(checkClassInfo()){
            loading();
            return;
        }
        event.preventDefault();
    });
    $('#add-code-file').on('click', addCFile);
}

function addCFile(){
    var nFiles = $('#code-files-table >tbody >tr').length + 1;
    $('#code-files-table').find('tbody').append('<tr><td><input type="file" accept=".c, .h" class="code-file" name="cfile_'+nFiles+'" size="45"></td></tr>');
}

function loading(){
    $(".loading").show();
    $(".content").hide();
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

// Notifica o usuario de uma mensagem de erro
function notification(msg) {
    alert(msg);
}

addCFile();
$(document).ready(main);
