$('.collapse').on('show.bs.collapse', function () {
    $(this).parent().removeClass("zeroPadding");
});

$('.collapse').on('hide.bs.collapse', function () {
    $(this).parent().addClass("zeroPadding");
});

$("document").ready(function(){
    $('.table-drop-button').click(function(){
        $(this).toggleClass('glyphicon-triangle-right glyphicon-triangle-bottom');
    });

    $('.table-sort-button').click(function(){
        $(this).toggleClass('glyphicon-triangle-bottom glyphicon-triangle-top');
    });

    $('.selectable-table').on('click', '.clickable-row', function (event) {
        if($(this).hasClass('active')){
            $(this).removeClass('active')
        }else{
            $(this).addClass('active')
        }
    });
});

