/**
 * Created by Administrator on 2017/1/9.
 */
jQuery(document).ready(function(){
            /*
        Fullscreen background
    */
    $.backstretch("/static/assets/img/backgrounds/2.jpg");

    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });
});