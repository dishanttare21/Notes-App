console.log("Welcome to Notes");

$('.document-link').click(function(){
    $('#document-title').html($(this).data('title'));
    $('#document-content').html($(this).data('content'));
});