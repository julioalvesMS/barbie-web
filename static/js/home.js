var cFiles = [];
var hFiles = [];

function main(){
    // Check if all submission conditions are satisfied
    $('form').submit(function(event){
        if(checkClassInfo() && checkFiles()){
            loading();
            return;
        }
        event.preventDefault();
    });
    $('#add-code-file').on('click', addCFile);
}

function addCFile(){
    var nFiles = $('#code-files-table >tbody >tr').length + 1;
    $('#code-files-table').find('tbody').append('<tr><td><a class="rem-file"><img src="close.svg" width=20></a></td><td><input type="file" accept=".c, .h" class="code-file" name="cfile_'+nFiles+'" size="45"></td></tr>');
    $('.rem-file').on('click', function(){
        $(this).parent().parent().remove();
        $('input[type=file]').each(function( index ){
                $(this).attr('name', 'cfile_'+(index+1));
        });

    });
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
        notification('Informe o número do laboratório');
        ok = false;
    }
    return ok;
}

function checkFiles(){
    var files = [];
    $('input[type=file]').each(function(){
            files.push($(this).val());
    });
    for(var i=0; i<files.length; i++){
        if(!(files[i])){
            notification('É necessário que todos os negócios contenham arquivos');
            return false;
        }
    }
    if(!files){
        notification('Fornceça ao menos um arquivo de código');
        return false;
    }
    return true;
}

// Notifica o usuario de uma mensagem de erro
function notification(msg) {
    alert(msg);
}

addCFile();
$(document).ready(main);
