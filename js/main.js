function main(){
    $('#add-c-file').on('click', addCFile);
    $('#add-h-file').on('click', addHFile);
}

function addCFile(){
    var nFiles = $('#c-files-table >tbody >tr').length + 1;
    $('#c-files-table').find('tbody').append('<tr><td><input type="file" accept=".c" class="code-file" name="cfile_'+nFiles+'" size="45"></td></tr>');
}

function addHFile(){
    var nFiles = $('#h-files-table >tbody >tr').length + 1;
    $('#h-files-table').find('tbody').append('<tr><td><input type="file" accept=".h" class="header-file" name="hfile_'+nFiles+'" size="45"></td></tr>');
}

addCFile();
addHFile();
$(document).ready(main);
