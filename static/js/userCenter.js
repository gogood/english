/**
 * Created by Yangcaijiao on 2017/1/4 0004.
 */
$(function () {
    $('.item').parent().slideUp();
    /***************************�ർ�� --begin--********************************************/
    $('.main-navigation ul.navigation>li').click(function (e) {
        if ($(this).hasClass('active')) {
            return;
        }
        $(this).siblings().removeClass('active');
        $('.item').parent().slideUp();
        $(this).addClass('active');
        $("div[id='" + $(this).attr('id') + "']").slideDown();
        console.log({id: $("div[id='" + $(this).attr('id') + "']").attr('id')});

    });
    /**************************�ർ�� --end--********************************************/

    /***************************item ���� --begin--********************************************/
    $('.item1>li').click(function (e) {
        if ($(this).hasClass('active')) {
            return;
        }
        $(this).siblings().removeClass('active');
        $(this).addClass('active');
        $('.item2').removeClass('active');
        $('.item2' + '.' + $(this).attr('id')).addClass('active');
    });
    /***************************item ���� --end--********************************************/

    /***************************���� --begin--********************************************/
    /*$('.info.time').click(function(e){
     $(this).animate({position:'absolute',top:'100px'},1,function(){
     $(this).fadeOut(function(){
     $('.info.detail').fadeIn();
     });
     })
     });*/
    /***************************����  --end--********************************************/

    /***************************�ղ� --begin--********************************************/
    /***************************�ղ� --end--********************************************/

});