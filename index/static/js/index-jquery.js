/**
 * Created by Yangcaijiao on 2016/12/12 0012.
 */
/*修改幻灯片的缩略图的位置*/
$(document).ready(function () {
    var controllers = $(".first-p #switcher");
    var w = controllers.width();
    controllers.css("margin-left", -w / 2);

    //设置幻灯片图片的高度
    var img = $("#featured .slides .myslide img");
    img.css("height", document.documentElement.clientHeight);
    window.onresize = function () {
        img.css("height", document.documentElement.clientHeight);
        //var section = $('div.section');
        img.css({"height": document.documentElement.clientHeight,"width":document.documentElement.clientWidth});
    }
});