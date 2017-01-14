/**
 * Created by Yangcaijiao on 2017/1/4 0004.
 */
$(function () {
    $('.item').parent().slideUp();
    /***************************侧导航 --begin--********************************************/
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
    /**************************侧导航 --end--********************************************/

    /***************************item 导航 --begin--********************************************/
    $('.item1>li').click(function (e) {
        if ($(this).hasClass('active')) {
            return;
        }
        $(this).siblings().removeClass('active');
        $(this).addClass('active');
        $('.item2').removeClass('active');
        $('.item2' + '.' + $(this).attr('id')).addClass('active');
    });
    /***************************item 导航 --end--********************************************/

    /***************************日历 --begin--********************************************/
    /*$('.info.time').click(function(e){
     $(this).animate({position:'absolute',top:'100px'},1,function(){
     $(this).fadeOut(function(){
     $('.info.detail').fadeIn();
     });
     })
     });*/
    /***************************日历  --end--********************************************/

    /***************************收藏 --begin--********************************************/
    /***************************收藏 --end--********************************************/

});