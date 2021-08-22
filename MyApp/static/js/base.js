function submit_delete(id) {
    $.ajax({
        type: 'GET',
        url: "delete/"+id+'/',
        dataType: "html",
        complete: function (data) {
            $('#project_'+id).remove();
        }
    });
}
function popu_form() {
    console.log('{{ project.name }}');
}