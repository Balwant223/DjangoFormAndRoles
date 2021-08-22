function submit_delete(id) {
    $.ajax({
        type: $('#delete_form_'+id).attr('method'),
        url: $('#delete_form_'+id).attr('action'),
        data: $('#delete_form_'+id).serialize(),
        success: function (data) {
            $('#project_'+id).remove();
            $("#all_cards_table").load("home.html #all_projects_list") 
        }
    });
}