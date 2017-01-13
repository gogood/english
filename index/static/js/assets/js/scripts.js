document.write("<script language='javascript' src='/static/js/assets/js/common.js'></script>");

jQuery(document).ready(function () {
    //creat birthday calendar
    create_calendar();

    //孩子生日失去焦点
    $(".child-birthday").blur(function () {
        var component = '.child-birthday';
        var error = '.error-child-birthday';
        var text = "请输入孩子生日";
        is_void_field(component, error, text);
    });

    //{#           recommand-mobile-phone-validate#}
    $(".f1-recommand-mobile").blur(function () {
        var component = '. f1-recommand-mobile';
        var error = '.error-recommand-mobile';
        is_mobile_phone(component, error);
        //reg=/^1[3|4|5|7|8][0-9]\d{4,8}$/i;//验证手机正则(输入前7位至11位)
        //if($(this).val() != ''){
        //	if($(this).val().length < 11){
        //		$('.error-recommand-mobile').html('手机号长度有误！');
        //		$('.error-recommand-mobile').css('display', 'block');
        //	}
        //	else if(!reg.test($('#click-recommend').val())){
        //		$('.error-recommand-mobile').html('手机号不存在！');
        //		$('.error-recommand-mobile').css('display', 'block');
        //	}
        //	else{
        //		$('.error-recommand-mobile').empty();
        //	}
        //}
    });


    $('.f1-repeat-password').blur(function () {
        console.log('123pas');
        var component1 = '.f1-repeat-password';
        var component2 = '.f1-password';
        var error = '.error-f1-repeat-password';
        var text = "密码不一致！";
        if (is_void_field(component1, error, '请输入密码！')) {
            is_equal(component1, component2, error, text, true);
        }

        //var password = $('.f1-password').val();
        //var repeat_password = $('.f1-repeat-password').text();
        //if(password != repeat_password)
        //{
        //    $('.error-f1-repeat-password').html("密码不一致！");
        //    $('.error-f1-repeat-password').css("display","block");
        //}
        //else
        //{
        //    $('.error-f1-repeat-password').empty();
        //
        //}
    });


    // click recommend will show recommenc things
    $("#click-recommend").click(function () {
        $("#click-recommend").addClass("hidden");
        $("#click-recommend-show").removeClass("hidden");
    });


    // next step
    $('.f1 .middle-next').on('click', function () {
        console.log('11111');
        var parent_fieldset = $(this).parents('fieldset');
        var next_step = true;
        // navigation steps / progress steps
        var current_active_step = $(this).parents('.f1').find('.f1-step.active');
        var progress_line = $(this).parents('.f1').find('.f1-progress-line');

        // fields validation
        if ($('input').hasClass('f1-first-name')) {
            var component = '.f1-first-name';
            var error = '.error-mobile-number';
            var text = '请输入您的手机号';
            if (is_void_field(component, error, text)) {  // when you add something in mobile
                if (!is_mobile_phone(component, error)) {
                    next_step = false;
                }
            } else {
                next_step = false;
            }
            if ($('input').hasClass('child-birthday')) {
                var component = '.child-birthday';
                var error = '.error-child-birthday';
                var text = '请输入孩子生日';
                if (!is_void_field(component, error, text)) {
                    next_step = false;
                }
                //$('input.child-birthday').addClass('input-error');
                //$(".error-child-birthday").html("请输入孩子生日");
                //$(".error-child-birthday").css("display","block");

                if ($('input').hasClass('f1-about-yourself')) {
                    var component1 = '.photokey';
                    var component2 = '.phoKey';
                    var error = '.error-validate';
                    var text = '验证码输入错误！';
                    if (!is_equal(component1, component2, error, text, false)) {
                        next_step = false;
                    }

                    //if($('input.f1-about-yourself').val() == '' ){
                    //	$('input.f1-about-yourself').addClass('input-error');
                    //	$('input.f1-about-yourself').next().next().html("验证码输入错误！");
                    //	next_step = false;
                    //}
                    //else if($('input.f1-about-yourself').val() != ''){
                    //	var code1=$('input.photokey').val();
                    //	var code2=$(".phoKey").text();
                    //	if(code1!=code2)
                    //	{
                    //		$('input.f1-about-yourself').next().next().html("验证码输入错误！");
                    //		$('input.f1-about-yourself').next().next().css("display","block");
                    //		next_step = false;
                    //	}
                    //}else{
                    //	$('input.f1-about-yourself').next().next().empty();
                    //	$('input.f1-about-yourself').removeClass('input-error');
                    //}

                    if ($('input').hasClass('f1-recommand-mobile')) {
                        var component = '.f1-recommand-mobile';
                        var error = '.error-recommand-mobile';
                        if ($(component).val() != '') {
                            if (!is_mobile_phone(component, error)) {
                                next_step = false;
                            }
                        }


                    }
                }

            }
        }

        //if($('input.f1-first-name').val() == ""){
        //	$('input.f1-first-name').addClass('input-error');
        //
        //$('input.f1-first-name').next().html('请输入你的手机号');
        //$('input.f1-first-name').next().css("display","block");
        ////$(".error1").html("请输入你的手机号");
        ////$(".error1").css("display","block");
        //next_step = false;
        //}
        //else if($('input.f1-first-name').val() != ""){
        //	reg=/^1[3|4|5|7|8][0-9]\d{4,8}$/i;
        //	if($('input.f1-first-name').val().length < 11){
        //		$('input.f1-first-name').addClass('input-error');
        //      $('input.f1-first-name').next().html('手机号长度有误！');
        //      $('input.f1-first-name').next().css('display', 'block');
        //		next_step = false;
        //  }
        //  else if(!reg.test($('input.f1-first-name').val())){
        //		$('input.f1-first-name').addClass('input-error');
        //      $('input.f1-first-name').next().html('手机号不存在！');
        //      $('input.f1-first-name').next().css('display', 'block');
        //		next_step = false;
        //  }
        //}else{
        //	$('input.f1-first-name').next().empty();
        //   $('input.f1-first-name').removeClass('input-error');
        //}

        // fields validation
        if (next_step) {
            console.log('22222');
            parent_fieldset.fadeOut(400, function () {
                // change icons
                current_active_step.removeClass('active').addClass('activated').next().addClass('active');
                // progress bar
                bar_progress(progress_line, 'right');
                // show next step
                $(this).next().fadeIn();
                console.log({'show_next_step': this});
                console.log('test-next');
                $('h3.mobile-phone').html($('input.f1-first-name').val());
                //ajax request message validate
                ajax_meassage();

                // scroll window to beginning of the form
                scroll_to_class($('.f1'), 20);
            });
        }

    });


    $('.f1 .btn-next-submit').on('click', function () {
        //var parent_fieldset = $(this).parents('fieldset');
        var submit = true;
        var time = true;
        //var next_step = true;
        // navigation steps / progress steps
        //var current_active_step = $(this).parents('.f1').find('.f1-step.active');
        //var progress_line = $(this).parents('.f1').find('.f1-progress-line');
        console.log('333333');
        //$('.error_message_validate').empty();
        //$('.message_validate').removeClass('input-error');
        if ($('input').hasClass('message_validate')) {

            //$('.error_message_validate').css("color","#ff0000");
            //is_void_field(component, error, text);
            //	var component = '.message_validate';
            //	var error = '.error_message_validate';
            //	var text = "请输入验证码！";
            console.log({'hello_hello': $('input.message_validate').val()});
            //console.log({'validate_message_value': validate_message_value});
            if ($('input.message_validate').val() == "") {
                console.log('empty1');
                var component = '.message_validate';
                var error = '.error_message_validate';
                var text = '请输入验证码';
                $('.error_message_validate').css("color", "#ff0000");
               // is_void_field(component, error, text);
                 $('.error_message_validate').text(text);
                    $('.error_message_validate').css("color", "#ff0000");
                    $('.error_message_validat').css('display', 'block');
                 console.log($('.error_message_validate').attr('class'),$('.error_message_validate').text());
                submit = false;
            } else {
                if ($('input.message_validate').val() != validate_message_value) {
                    $('.message_validate').addClass('input-error');
                    $('.error_message_validate').html("验证码输入错误！");
                    $('.error_message_validate').css("color", "#ff0000");
                    $('.error_message_validat').css('display', 'block');
                    submit = false;
                    console.log({'different': submit});

                } else {
                    $('.message_validate').removeClass('input-error');
                    $('.error_message_validate').empty();
                    console.log({'same': submit})
                }
            }

            //if(!is_void_field(component, error, text)){
            //	submit = false;
            //	console.log({'void':submit});
            //}
            //if($('.message_validate').val() == ''){
            //	$('.error_message_validate').html("请输入验证码！");
            //
            //	next_step = false;
            //}else{
            //	$('.error_message_validate').empty();
            //
            //}

            if ($('input').hasClass('f1-password')) {

                var passsword_component = '.f1-password';
                var password_error = '.error-f1-password';
                var text = "密码不能为空！";
                if (!is_void_field(passsword_component, password_error, text)) {

                    submit = false;
                    console.log({'password is void': submit});

                } else {
                    if (!is_password(passsword_component, $(passsword_component).val(), password_error)) {

                        submit = false;
                        console.log({'password is no-corrent': submit});
                    }
                }

                if ($('input').hasClass('f1-repeat-password')) {
                    var repeat_pas_com = '.f1-repeat-password';
                    var repeat_pas_error = '.error-f1-repeat-password';
                    var text = "密码不能为空！";
                    if (!is_void_field(repeat_pas_com, repeat_pas_error, text)) {
                        console.log('confirm password is void ');
                        submit = false;
                        console.log({'confirm password is void ': submit});
                    } else {
                        var error_text = "密码不一致！";
                        if (!is_equal(repeat_pas_com, passsword_component, repeat_pas_error, error_text, true)) {

                            submit = false;
                            console.log({'confirm password is no-corrent ': submit});
                        }
                    }
                }
            }
        }

        //if($('.f1-password').val() == ''){
        //	$('.error-f1-password').html("密码不能为空！");
        //	next_step = false;
        //
        //}else{
        //	$('.error-f1-password').empty();
        //
        //}
        //if($('.f1-password').val() != ''){
        //	if(!is_password($('.f1-password').val())){
        //		$('.error-f1-password').html("只能输入6-20个字母、数字、下划线");
        //
        //		next_step = false;
        //
        //	}else{
        //		$('.error-f1-password').empty();
        //
        //	}
        //}

        //if($('.f1-repeat-password').val() == ''){
        //	$('.error-f1-repeat-password').html('密码不能为空！');
        //
        //	next_step = false;
        //
        //}else{
        //	$('.error-f1-repeat-password').empty();
        //
        //}
        //if($('.f1-repeat-password').val() != ''){
        //	var password = $('.f1-password').val();
        //	var repeat_password = $('.f1-repeat-password').text();
        //	if(password != repeat_password)
        //	{
        //		$('.error-f1-repeat-password').html("密码不一致！");
        //		$('.error-f1-repeat-password').css("display","block");
        //		next_step = false;
        //
        //	}
        //	else
        //	{
        //		$('.error-f1-repeat-password').empty();
        //
        //	}
        //}
        if (SetTime()) {
            time = false;
            $('.error_message_validate').html("验证码无效,请重新获取！");
            $('.message_validate').addClass('input-error');
        }


        // fields validation
        if (submit && time) {
            var mobile = $('.f1-first-name').val();
            var birthday = $('.child-birthday').val();
            var password = $('.f1-password').val();
            var recomment_mobile = $('.f1-recommand-mobile').val();
            console.log({'mobile': mobile}, {'birthday': birthday}, {'password': password});
            ajax_register(mobile, password, birthday, recomment_mobile);

        }

        //if(next_step){
        //		parent_fieldset.fadeOut(400, function() {
        //	// change icons
        //	current_active_step.removeClass('active').addClass('activated').next().addClass('active');
        //	// progress bar
        //	bar_progress(progress_line, 'right');
        //	// show next step
        //	$(this).next().fadeIn();
        //
        //		// ajax request message validate
        //		//ajax_meassage();
        //
        //	// scroll window to beginning of the form
        //	scroll_to_class( $('.f1'), 20 );
        //});
        //}


    });

    // previous step
    //$('.f1 .btn-previous').on('click', function() {
    //	// navigation steps / progress steps
    //	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    //	var progress_line = $(this).parents('.f1').find('.f1-progress-line');
    //
    //	$(this).parents('fieldset').fadeOut(400, function() {
    //		// change icons
    //		current_active_step.removeClass('active').prev().removeClass('activated').addClass('active');
    //		// progress bar
    //		bar_progress(progress_line, 'left');
    //		// show previous step
    //		$(this).prev().fadeIn();
    //		// scroll window to beginning of the form
    //	scroll_to_class( $('.f1'), 20 );
    //	});
    //});

    // submit
    //$('.f1').on('submit', function(e) {
    //
    //
    //	// fields validation
    //	$(this).find('input[type="text"], input[type="password"], textarea').each(function() {
    //		if( $(this).val() == "" ) {
    //			e.preventDefault();
    //			$(this).addClass('input-error');
    //		}
    //		else {
    //			$(this).removeClass('input-error');
    //		}
    //	});
    //	// fields validation
    //
    //});
});

//using jQuery
//function getCookie(name) {
//    var cookieValue = null;
//    if (document.cookie && document.cookie != '') {
//        var cookies = document.cookie.split(';');
//        for (var i = 0; i < cookies.length; i++) {
//            var cookie = jQuery.trim(cookies[i]);
//            // Does this cookie string begin with the name we want?
//            if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                break;
//            }
//        }
//    }
//    return cookieValue;
//}
//var csrftoken = getCookie('csrftoken');
//function csrfSafeMethod(method) {
//    // these HTTP methods do not require CSRF protection
//    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//}
//$.ajaxSetup({
//    beforeSend: function(xhr, settings) {
//        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//            xhr.setRequestHeader("X-CSRFToken", csrftoken);
//        }
//    }
//});


function ajax_register(mobile_number, password, birthday, recomment_mobile) {
    var send_data = {mobile: mobile_number, password: password, birthday: birthday, recomment_mobile: recomment_mobile};
    $.ajax({
        type: 'POST',
        dataType: 'json',
        data: send_data,
        url: '/index/api_register/',
        success: function (data) {
            console.log({'success_return': data});
            var parent_fieldset = $('.f1 .btn-next-submit').parents('fieldset');
            var current_active_step = $('.f1 .btn-next-submit').parents('.f1').find('.f1-step.active');
            var progress_line = $('.f1 .btn-next-submit').parents('.f1').find('.f1-progress-line');
            parent_fieldset.fadeOut(400, function () {
                // change icons
                current_active_step.removeClass('active').addClass('activated').next().addClass('active');
                // progress bar
                bar_progress(progress_line, 'right');
                // show next step
                $('#success').fadeIn();

                // ajax request message validate
                //ajax_meassage();

                // scroll window to beginning of the form
                scroll_to_class($('.f1'), 20);
            });
            return true;
        },
        error: function (status, error) {
            return false;
        }
    })
}


function create_calendar() {
    $('.form_date').datetimepicker({
        language: 'zh-CN',
        format: 'yyyy-mm-dd',
        pickerPosition: "bottom-left",
        weekStart: 1,
        todayBtn: true,
        autoclose: true,
        todayHighlight: 1,
        startView: 2,
        minView: 2,
        forceParse: 0,
        showMeridian: true

    }).on("click", function (ev) {
        $(".error-child-birthday").empty();
        $('input.child-birthday').removeClass('input-error');

    }).on('changeDate', function (ev) {
        $(".error-child-birthday").empty();
        $('input.child-birthday').removeClass('input-error');
    });
}




