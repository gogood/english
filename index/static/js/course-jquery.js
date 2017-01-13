/**
 * Created by Yangcaijiao on 2016/12/13 0013.
 */


/*****************************************公用代码*********************************/
var proposals = ['百度1', '百度2', '百度3', '百度4', '百度5', '百度6', '百度7', '17素材网', '百度', '新浪'];
var BASE_URL = "http://127.0.0.1:8000/index/";
var ajaxParams = {
    type: "get",
    url: BASE_URL + "api_course",
    dataType: 'json',
    jsonpCallback: 'myCall'
};
//用于重置selected
var SELECTED = {
    current_page: 1,
    num_per_page: 20,
    tag: {id_1: null, children: []},
    order: 'time',
    sort: '-',

};
var selected = {
    current_page: 1,
    num_per_page: 20,
    tag: {id_1: null, children: []},
    order: 'time',
    sort: '-',

};
var PARAMS;
/**
 * 获取数据函数
 * @param selected
 */
function getData(selected, url) {
    console.log({'fanwenqing': selected});
    $.ajax($.extend(ajaxParams, {
        type: "post",
        url: url || BASE_URL + "api_course_category/",
        data: JSON.stringify(selected),
        success: function (data) {
            console.log('i have gotten the data');
            //将数据回调到分类选卡插件的selected回调函数中，
            // 借用该回调函数进行每次获取数据库的数据来feed给课程列表，刷新课程列表
            PARAMS.selected(data);
        },
        error: function (xhr, status, error) {
            console.log('fail to get the data,this is the error back', error)
        }
    }))
}
/*****************************************公用代码*********************************/


$(document).ready(function () {
    console.log('keyibubuah', selected);
    /************************************页面开始加载时进行数据获取------begin--**********************************************/
    $.ajax($.extend(ajaxParams, {
        success: function (data) {
            var classifies = data.response_data.category;
            var courses = data.response_data.courses;
            console.log({data: data});
            console.log({courses: courses});
            //展示分类
            $('.course_select_container').course_select({
                dataClassify: {
                    classifyLabel: '已选择',
                    classifies: classifies
                }, selected: function (data) {//分类选卡点击后的回调函数
                    console.log('回调函数', data);
                    //展示产品列表
                    feedData(data.courses);
                    //展示分页
                    pagination(data);
                }
            });
            //展示产品列表
            feedData(courses.courses);
            //展示分页
            pagination(courses);

        }, error: function (xhr, status, error) {
            console.log({xhr: xhr, status: status, error: error});
        }
    }));
    /************************************页面开始加载时进行数据获取------end--**********************************************/

    /////////////////////////////    楚     河      汉     界     /////////////////////////////////////


    /************************************收搜------begin--**********************************************/
    $('#search-form').autocomplete({
        hints: proposals,
        buttonText: '搜索',
        width: 500,
        height: 18,
        onSubmit: function (text) {
            console.log('搜搜的关键字', text);
            selected = SELECTED;
            getData({keyword: text, current_page: 1, num_per_page: 20}, BASE_URL + "api_course_search/");
        },
        onBlur: function (text) {
            if (!text) {
                /*$('.classify .classify_0 .span0').siblings().removeClass('active');
                $('.classify .classify_0 .span0.span_0').addClass('active');*/
                getData(selected);
            }

        }
    });
    /************************************收搜------end--**********************************************/


    /////////////////////////////    楚     河      汉     界     /////////////////////////////////////

    /************************************列表布局------begin--**********************************************/
    $("div.switch_thumb").click(function () {
        if ($(this).hasClass("show")) {
            return;
        }
        $(this).siblings().removeClass('show');
        $(this).addClass('show');
        if ($(this).hasClass("left")) {//left是左边的按钮，为列表布局开关
            $("div.display").fadeOut("fast", function () {
                $(this).fadeIn("fast").removeClass("thumb_view row");
                $(this).parent().removeClass('container');
                $("div.content_block").removeClass("col-md-3 col-sm-4 col-xs-6");
            });
        } else {//是右边的按钮，为格子布局
            $("div.display").fadeOut("fast", function () {
                $(this).fadeIn("fast").addClass("thumb_view row");
                $(this).parent().addClass('container');
                $("div.content_block").addClass("col-md-3 col-sm-4 col-xs-6");
            });
        }
    });
    /************************************列表布局---end----**********************************************/

    /////////////////////////////    楚     河      汉     界     /////////////////////////////////////

    /************************************时间、价格、人气排序------begin--**********************************************/
    $('.list-nav span').click(function () {
        $(this).siblings().removeClass('active').attr('id', '0');
        $(this).addClass('active');
        switch ($(this).attr('id')) {
            case '+':
            case '0':
                selected.sort = '-';
                $(this).attr('id', selected.sort);
                break;
            case '-':
                selected.sort = '+';
                $(this).attr('id', selected.sort);
                break;
        }
        if ($(this).hasClass('population')) {
            selected.order = 'population';
        } else if ($(this).hasClass('price')) {
            selected.order = 'price';
        } else {
            selected.order = 'time';
        }
        console.log({'排序的结果': selected.order});
        //发送ajax请求获取数据
        getData(selected);
    });
    /************************************时间、价格、人气排序------end--**********************************************/

    /////////////////////////////    楚     河      汉     界     /////////////////////////////////////


    /************************************--课程详情-begin-**********************************************/
    $('.modal-header ul>li>a').click(function () {
        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
            return;
        }
        $(this).addClass('active');
    });
    $('.modal-body .descr ul>li').click(function () {
        if ($(this).hasClass('active')) {
            return;
        }
        $(this).siblings().removeClass('active');
        $(this).addClass('active');
        $('.modal-body .descr-content p').siblings().removeClass('active');
        $('.modal-body .descr-content p').eq($(this).index()).addClass('active');

    });
    /************************************--课程详情-end-**********************************************/

    /////////////////////////////    楚     河      汉     界     /////////////////////////////////////

    /***********************************函数调用************************************************************/
    /**
     * //feed data to productList
     * @param data
     */
    function feedData(data) {
        $('.list .display').productList({courses: data});
        //判断目前的列表布局状态是否为格子
        if ($('div.display').hasClass('thumb_view')) {
            $('div.display .content_block').addClass('col-md-3 col-sm-4 col-xs-6');
        }
    }

    /**
     * // pagination function
     * @param courses
     */
    function pagination(courses) {
        $('.pagination').jqPagination({
            current_page: courses.current_page,
            link_string: '/?page={page_number}',
            max_page: courses.total_page_count,
            page_string: '{current_page} / {max_page} 页',
            paged: function (page) {
                var _this = this;
                console.log({当前页页: page});
                $.jqPagination.defaultOptions = {
                    link_string: '/?page={page_number}',
                    max_page: courses.total_page_count,
                    page_string: '{current_page} / {max_page} 页',
                    paged: _this.paged
                };
                $.jqPagination($('.pagination'), page);

                selected.current_page = page;
                //获取数据
                console.log('分页时候', selected);
                //获取数据，注意getData该函数写在course-jquery文件中
                getData(selected);

            }
        });
    }

});

