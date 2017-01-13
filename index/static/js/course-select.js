/**
 * Created by Yangcaijiao on 2016/12/14 0014.
 */
(function ($) {
    $.fn.course_select = function (params) {
        params = $.extend({
            dataClassify: {
                classifyLabel: '选择',
                classifies: [{
                    id: 1,
                    title: '46级',
                    children: [{
                        title: '考试目标',
                        id: 11,
                        children: [{id: 12, title: '四级'}, {id: 13, title: '六级'}]
                    }, {title: '当前水平', id: 12, children: [{id: 121, title: '零基础'}, {id: 122, title: '0基础'}]}]
                }, {
                    id: 2,
                    title: 'BEC商务英语',
                    children: [{
                        title: '当前水平',
                        id: 21,
                        children: [{id: 211, title: '高中水平'}, {id: 212, title: '其它'}]
                    }, {title: '授课模式', id: 22, children: [{id: 221, title: '课件课'}, {id: 222, title: '混合课'}]}]
                }, {
                    id: 3,
                    title: '口译翻译',
                    children: [{
                        title: '考试目标',
                        id: 31,
                        children: [{id: 311, title: '基础口译'}, {id: 312, title: '中级口译'}, {
                            id: 313,
                            title: '高级口译'
                        }, {id: 314, title: 'CATTI二级'}, {id: 315, title: 'CATTI三级'}, {
                            id: 316,
                            title: 'CATTI三级'
                        }, {id: 317, title: '同声传译'}, {id: 318, title: '专四'}, {id: 319, title: '专八'}, {
                            id: 31191,
                            title: '基础笔译'
                        }, {id: 31192, title: '中级笔译'}, {id: 3193, title: '高级笔译'}]
                    },
                        {
                            title: '当前水平',
                            id: 32,
                            children: [{id: 321, title: '零基础'}, {id: 322, title: '有基础'}]
                        }, {
                            title: '开班时间',
                            id: 323,
                            children: [{id: 324, title: '12月开班'}, {id: 325, title: '1月开班'}, {id: 326, title: '2月开班'}]
                        }
                    ]
                }
                ]
            },
            selected: function (data) {
            }
        }, params);
        PARAMS = params;
        var dataClassify = params.dataClassify;
        var classifies = dataClassify.classifies;
        /*----------------------将所有的分类进行分类---开始-------------------------------------------*/
        var all = {title: '全部', id: 'all', children: []};//[{title, id,children:[string]}]
        for (var i in classifies) {//[{title,id,children:[{title, id,children:[string]}]
            var children = classifies[i].children;
            for (var j in children) {//[{title, id,children:[string]
                if (i == 0) {
                    //如果是第一个大分类，则直接将它的内容复制给新对象o,然后将o作为所有分类的下一级分类的新分类
                    //处理的时候注意不要直接将一个对象赋给另一个变量
                    var o = {title: children[j].title, id: children[j].id, children: [].concat(children[j].children)};
                    all.children.push(o);
                } else {//如果是第二大分类开始，则要判断该分类下一级分类是否已经出现在all.children
                    var index = findTitleByIndex(all.children, children[j].title);
                    if (index > -1) {//如果该下级的分类已经存在，则将存储其分类内容的数组跟all.children对应的分类的数组进行无重复合并
                        all.children[index].children = combineArr(all.children[index].children, children[j].children);
                    }
                    else {//如果该下级的分类不存在存在，将其作为一个新的下级分类添到oll.children中
                        var o = {
                            title: children[j].title,
                            id: children[j].id,
                            children: [].concat(children[j].children)
                        };
                        all.children.push(o);
                    }
                }
            }
        }
        //将全部分类插入前面
        classifies.unshift(all);
        /*----------------------将所有的分类进行分类---结束-------------------------------------------*/
        this.each(function () {
            var classify_head = $('<div></div>').addClass('classify_head');
            var headLabel = $('<span></span>').addClass('classify_head_label');
            headLabel.text(dataClassify.classifyLabel + ':');
            classify_head.append(headLabel);
            classify_head.appendTo(this);
            //分类的开始
            var classify_body = $('<div></div>').addClass('classify_body');
            classify_body.appendTo(this);
            //一级分类
            var classify0 = $('<div></div>').addClass('classify_0');
            classify0.appendTo(classify_body);
            //给每个可点击的二级选项添加一个属性，存储放置在头顶已经选择的对应项
            //获取总分类
            for (var i in dataClassify.classifies) {
                var c = dataClassify.classifies[i];
                //处理总分类title
                var span = $('<span></span>').addClass('span0 span_' + i).attr('id', c.id).html(c.title).click(function () {
                    if ($(this).hasClass('active')) {
                        return;
                    }
                    clickTopLevel($(this), dataClassify, classify_head, classify_body, createSpan);
                    //获取该分类的数据
                    loadData(selected);
                });
                classify0.append(span);//填入一级分类
                if (i == 0) {//默认将‘全部’分类展开
                    console.log('点击总分类时', selected);
                    clickTopLevel(span, dataClassify, classify_head, classify_body, createSpan);
                }
            }

            //点击选项卡时，将选择的项放置分类选卡的头部，并且实现可以取消的功能
            dataClassify.click2select = function (span, class_name) {
                var div = $('<div></div>').addClass(class_name).attr('id', span.attr('id')).css({
                    'margin-left': '20px',
                    'border': '1px dashed #00b4ec',
                    'font-size': '16px',
                    'padding-top': '2px',
                    'padding-bottom': '2px',
                    'padding-left': '10px',
                    'padding-right': '10px',
                    'color': '#00b4ec',
                    'background-color': 'rgba(0,204,255,0.09)'
                }).data('ids', span.data('ids'));
                var span1 = $('<span></span>').text(span.text()).addClass(class_name);
                var span2 = $('<span></span>').text('×').css({
                    /* 'float': 'right',*/
                    'margin-left': '2px',
                    'font-size': '18px',
                    'cursor': 'pointer'
                }).click(function () {
                    span.css({'color': 'black'});
                    div.remove();
                    //删除selected的记录
                    selected.tag.children = selected.tag.children.filter(function (item) {
                        if (item.id_3 !== span.attr('id')) {
                            return item;
                        }
                    });
                    console.log({'sahnchu': selected});
                    //删除所选的内容，需要重新取值
                    loadData(selected);
                });
                span.selectedItem = div;
                div.append(span1);
                div.append(span2);
                classify_head.append(div);
            };

            //创建span
            function createSpan(child, class_name, ids, isSelect) {
                var span = $('<span></span>').html(child.title).attr('id', child.id);
                if (class_name) {
                    span.addClass(class_name);
                }
                if (isSelect) {
                    ids.id_3 = span.attr('id');
                    span.data('ids', ids);
                    span.click(function () {
                        //删除数组selected里相关的记录
                        selected.tag.children = selected.tag.children.filter(function (item) {
                            if (item.id_2 != ids.id_2) {
                                return item;
                            }
                        });
                        console.log({'shan': selected});
                        classify_head.find('div.' + class_name).remove();
                        //判断该选项是否已经选上，选上后进行删除
                        var re = /active/;
                        var isSelected = re.exec(span.attr('class'));
                        if (isSelected) {
                            $(this).css({'color': 'black'}).removeClass('active');
                        } else {//否则，与span同类的元素的样式进行复原，为该span进行样式的修改，使其识别与未被选上的元素
                            $(this).siblings('.active').css({'color': 'black'}).removeClass('active'); //改变样式 siblings:同胞元素
                            $(this).addClass('active').css({'color': '#00b4ec'});
                            //记录到数组selected里
                            selected.tag.children.push({id_2: ids.id_2, id_3: span.attr('id')});
                            console.log({'tianjia': selected});
                            //将选中的项放置头部
                            dataClassify.click2select($(this), class_name, class_name);
                        }
                        //但该选项卡的点击事件发生后，需要重新获取数据，进行列表的刷新
                        loadData(selected);

                    }).hover(function () {
                        var re = /active/;
                        var isSelected = re.exec(span.attr('class'));
                        if (!isSelected) {
                            $(this).css({'color': '#00b4ec'});
                        }
                    }, function () {
                        var re = /active/;
                        var isSelected = re.exec(span.attr('class'));
                        if (!isSelected) {
                            $(this).css({'color': 'black'});
                        }
                    });
                }
                return span;
            }
        });
        return this;

        //点击总分时进行展开
        function clickTopLevel(_this, dataClassify, classify_head, classify_body, createSpan) {//点击总分类时
            selected.tag = {id_1: _this.attr('id'), children: []};
            console.log({'zongfeigaibian': selected});
            //将之前的被激活的span样式进行修改
            $('div.classify_0').find('.active').removeClass('active');
            _this.addClass('active');
            var re = /span_(\d+)/g;
            var classN = _this.attr('class');
            var or = re.exec(classN);
            var order = or[1];
            var cc = dataClassify.classifies[order];
            //清空下面的选项和已经选上的内容
            $('div.classify_1').remove();
            classify_head.find('div').remove();
            var classify = $('<div></div>').addClass('classify_1').css({'width': '100%', 'height': 'auto'});
            classify.appendTo(classify_body);
            //获取分类1
            var children = cc.children;//每个元素{title,id, []}
            for (var i_1 in children) {
                var div = $('<div></div>').addClass('_classify_1 classify_1_' + i_1).css({
                    'width': '100%',
                    'height': 'auto',
                    'border-bottom': '1px dashed #ddd',
                    'padding-top': '2px',
                    'padding-bottom': '2px',

                });

                var div_right = $('<div></div>').addClass('div_right _' + i_1).css({
                    'width': '90%',
                    'height': 'auto',

                });
                var ids = {id_1: _this.attr('id'), id_2: children[i_1].id}
                var spans = children[i_1].children.map(function (child) {
                    return createSpan(child, 'right_' + i_1, ids, true);
                });
                div_right.append(spans);
                var div_left = $('<div></div>').addClass('div_left').css({
                    'width': '9%',
                    'word-break': 'keep-all'
                });
                //console.log({总分类:{id:_this.attr('id'),title:_this.html()},二级分类:{id:children[i_1].id,title:children[i_1].title}})
                var child = {
                    title: children[i_1].title + ':',
                    id: children[i_1].id,
                    children: [].concat(children[i_1].children),
                    f_id: _this.attr('id')
                }
                div_left.append(createSpan(child, 'noPointer'));
                div.append(div_left);
                div.append(div_right);
                div.appendTo(classify);
            }
            moreDiv();
        }


        //合并数组并实现数组元素的唯一性
        function combineArr(arr_1, arr_2) {
            arr_1 = arr_1.map(function (item) {
                return {title: item.title.trim(), id: item.id};
            });
            var arr_3 = arr_2.filter(function (item) {
                var existed = false;
                for (var i in arr_1) {
                    if (arr_1[i].title == item.title.trim()) {
                        existed = true;
                    }
                }
                if (!existed) {
                    return item;
                }

            });
            return arr_1.concat(arr_3);
        }

        //查找相同的title，返回index
        function findTitleByIndex(arr, title) {
            for (var i in arr) {
                if (arr[i].title == title)return i;
            }
            return -1;
        }

        //查看是否过多显示
        function moreDiv() {
            var div_p = $('div.classify_1');
            if (div_p.height() > 150) {
                var div_s = div_p.children();
                var h = 0;
                var isHide = false;
                for (var i in div_s) {
                    var son = div_p.find('.classify_1_' + i);
                    h = h + son.height();
                    if (h > 150) {
                        isHide = true;
                        son.addClass('hided').hide();
                    }
                }
                var more_div = $('<div></div>').addClass('more').css({
                    'width': '100%',
                    'text-align': 'center',
                    'color': 'gray',
                });
                if (isHide) {
                    console.log('isHide');
                    var more_span = $('<span></span>').addClass('more').css({
                        'width': '100%',
                        'cursor': 'pointer',
                        'font-size': '13px'
                    }).text('更多选项 ↓').click(function () {
                        if (div_p.find('.hided').hasClass('toShow')) {
                            $(this).text('更多选项 ↓');
                            div_p.find('.hided').removeClass('toShow').hide();
                        } else {
                            console.log('放下来');
                            $(this).text('收起  ↑');
                            div_p.find('.hided').addClass('toShow').show();
                        }
                    }).hover(function () {
                        $(this).css({'color': '#00b4ec'});
                    }, function () {
                        $(this).css({'color': 'gray'});
                    }).click(function () {
                        console.log('dile');
                    });
                    more_div.append(more_span);
                    div_p.append(more_div);
                }
            }
        }

        //获取数据
        function loadData(selected) {
            selected.current_page = 1;
            getData(selected);

        }
    };
})(jQuery);
