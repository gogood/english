/**
 * Created by Yangcaijiao on 2016/12/26 0026.
 */

(function ($) {
    $.fn.productList = function (params) {
        params = $.extend({}, params);
        var courses = params.courses;
        console.log({param: params});
        this.each(function () {
            var _this = this;
            //先删除所有的子节点，以实现重新建立子孩子。
            $(this).children().remove();
            //产品列表的头一个产品格，不用于展示产品，用于占位置
            var listHead = $("<div></div>").addClass("content_block head");
            $(this).append(listHead);
            if (courses.length < 1) {
                noContent(_this);
            } else {
                //产品列表
                for (var i in courses) {
                    $(this).append(listItem(courses[i]));
                }
            }
            //产品列表的最后一个产品格，不用于展示产品，用于占位置
            var listHead = $("<div></div>").addClass("content_block foot");
            $(this).append(listHead);
        });
        return this;

    }

    /**
     * 显示产品item布局
     * */
    function listItem(data) {
        //父容器
        var content_block = $('<div></div>').addClass("content_block");
        //放置图片的子容器
        var photo_block = $('<div></div>').addClass("photo");
        //放置产品信息的子容器
        var info_block = $('<div></div>').addClass("info");
        //详情按钮的子容器
        var detailBtn = $('<a></a>').addClass('button button-glow button-border button-rounded button-primary').text('查看详情').click(function () {
            showMyModal(data);
        });

        //设置放置图片的子容器的组件
        var img = $('<img/>').attr('src', data.image);
        var _img = $('<p></p>').addClass('watch Hui-iconfont Hui-iconfont-bofang').text('免费试听');
        photo_block.append([img, _img]);

        //设置放置产品信息的子容器的组件
        var nameContainer = $('<h2></h2>');
        var name = $('<a></a>').text(data.course_name);
        nameContainer.append(name);
        var target = $('<p></p>').addClass('target').text(data.target);
        var cost = $('<p></p>').addClass('cost').text('¥ ' + data.pay);
        var other = $('<p></p>').addClass('other').html("适合" + data.student_lv + "级别&nbsp;&nbsp;&nbsp;&nbsp;▏&nbsp;总共" + data.number_course);
        info_block.append([nameContainer, target, cost, other]);

        //将各个子容器放进父容器中
        content_block.append([photo_block, info_block, detailBtn]);
        //返回父容器
        return content_block;
    }

    /**
     * 显示产品详情的函数
     * @param data
     */
    function showMyModal(data) {
        //在显示模态框之前进行数据加载
        $('#myModal').on('show.bs.modal', function () {
            //找到课程标题
            $(this).find('a.navbar-brand').text(data.course_name);
            //找到课程图片
            $(this).find('img').attr({'src': data.image});
            //找到课程费用
            $(this).find('.info_1 p.cost').text(data.pay);
            //找到课程适合水平
            $(this).find('.info_1 p.course_level').text(data.student_lv);
            //找到课时数
            $(this).find('.info_1 p.course_number').text(data.number_course);
            //找到课程简介
            $(this).find('.descr-content p._1').html(data.description);
            //找到课程目标
            $(this).find('.descr-content p._2').text(data.target);
        });
        //打开模态框
        $('#myModal').modal('show');
    }

    /**
     * 列表没有内容的布局
     */
    function noContent(_this){
        var no_content = $('<div></div>').addClass('no-content Hui-iconfont').text('暂无相关课程');
                $(_this).append(no_content);
                //乌鸦图片
                var bird = $('<div class="bird"></div>');
                $(_this).append(bird);
                var i = 10;
                var toRight = true;
                setInterval(a, 500);
                function a() {
                    if (bird.hasClass('active')) {
                        bird.removeClass('active');
                    } else {
                        bird.addClass('active');
                    }
                    bird.css({left: i + 'px'});
                    if (i + bird.width() < $(_this).width() && toRight) {
                        i += 20;
                    } else {
                        toRight = false;
                    }
                    if (!toRight && i > 10) {
                        i -= 20;
                    } else {
                        toRight = true;
                    }
                }
    }
})(jQuery);