function main(){
    $('#add-code-file').on('click', addCFile);
}

function addCFile(){
    var nFiles = $('#code-files-table >tbody >tr').length + 1;
    $('#code-files-table').find('tbody').append('<tr><td><input type="file" accept=".c" class="code-file" name="cfile_'+nFiles+'" size="45"></td></tr>');
}


addCFile();
$(document).ready(main);
