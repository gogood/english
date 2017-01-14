/**
 * Created by Administrator on 2017/1/4.
 */
document.write("<script language='javascript' src='/static/js/assets/js/common.js'></script>");

jQuery(document).ready(function() {

    $('.f1 .middle-next').on('click', function(){
        var parent_fieldset = $(this).parents('fieldset');
    	var next_step = true;
    	// navigation steps / progress steps
    	var current_active_step = $(this).parents('.f1').find('.f1-step.active');
    	var progress_line = $(this).parents('.f1').find('.f1-progress-line');

        // fields validation
		if($('input').hasClass('f1-first-name')) {
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

            if($('input').hasClass('f1-about-yourself')) {
                var component1 = '.photokey';
                var component2 = '.phoKey';
                var error = '.error-validate';
                var text = '验证码输入错误';
                if (!is_equal(component1, component2, error, text, false)) {
                    next_step = false;
                }
            }

            	// fields validation
    	if( next_step ) {
			console.log('22222');
    		parent_fieldset.fadeOut(400, function() {
    			// change icons
    			current_active_step.removeClass('active').addClass('activated').next().addClass('active');
    			// progress bar
    			bar_progress(progress_line, 'right');
    			// show next step
	    		$(this).next().fadeIn();
				 //ajax request message validate
				ajax_meassage();

	    		// scroll window to beginning of the form
    			scroll_to_class( $('.f1'), 20 );
	    	});
    	}
        }

    });
    $('.f1 .btn-next-submit').on('click', function(){
        var submit = true;
        var time = true;
        console.log('333333');
        if($('input').hasClass('message_validate')) {
                var message_validate = '.message_validate';
        var message_error = '.error_message_validate';
        var message = "请输入验证码";
        if(is_void_field(message_validate, message_error, message)){
            console.log('123');
            if($('.message_validate').val() != validate_message_value){
            $('.message_validate').addClass('input-error');
            $('.error_message_validate').html("验证码输入错误");
            $('.error_message_validat').css('display','block');
            submit = false;
        }else {
                 console.log('456');
                $('.message_validate').removeClass('input-error');
                $('.error_message_validate').empty();
            }
        }else{
             console.log('789');
            $('.message_validate').addClass('input-error');
            $('.error_message_validate').html("验证码输入错误");
            $('.error_message_validat').css('display','block');
            submit = false;
        }

            if($('input').hasClass('f1-password')){

        var passsword_component = '.f1-password';
        var password_error = '.error-f1-password';
        var text = "密码不能为空";

        if(is_void_field(passsword_component,password_error,text)){
            if(!is_password(passsword_component, $(passsword_component).val(), password_error)){
                submit = false;
            }
        }else{
            submit = false;

        }
            }
        }

        //if(!is_void_field(message_validate, message_error, message)){
        //    submit = false;
        //}else{
        //       if($('.message_validate').val() != validate_message_value){
        //    $('.message_validate').addClass('input-error');
        //    $('.error_message_validate').html("验证码输入错误");
        //    $('.error_message_validat').css('display','block');
        //    submit = false;
        //}else{
        //    $('.message_validate').removeClass('input-error');
        //    $('.error_message_validate').empty();
        //}
        //
        //}



        if(SetTime()){
            time = false;
            $('.error_message_validate').html("验证码无效,请重新获取");
            $('.message_validate').addClass('input-error');

        }else{
            $('.error_message_validate').empty();
            $('.message_validate').removeClass('input-error');
        }

        // fields validation
        if( submit && time){
            console.log ({'submit': submit});
            var mobile = $('.f1-first-name').val();
            var password = $('.f1-password').val();
            console.log({'mobile': mobile}, {'password': password});
            ajax_forget_password(mobile, password);
        }

    });
});

function ajax_forget_password(mobile, password){
    var send_data = {mobile: mobile, password: password};
    $.ajax({
        type: 'POST',
        dataType: ' json',
        data: send_data,
        url:"/index/api_forget_password/",
        success: function(data){
            console.log({'success_return':data});
			var parent_fieldset = $('.f1 .btn-next-submit').parents('fieldset');
			var current_active_step = $('.f1 .btn-next-submit').parents('.f1').find('.f1-step.active');
			var progress_line = $('.f1 .btn-next-submit').parents('.f1').find('.f1-progress-line');
			parent_fieldset.fadeOut(400, function() {
    			// change icons
    			current_active_step.removeClass('active').addClass('activated').next().addClass('active');
    			// progress bar
    			bar_progress(progress_line, 'right');
    			// show next step
	    		$('#success').fadeIn();
    			scroll_to_class( $('.f1'), 20 );
	    	});
			return true;

        },
        error: function(status, error){
            console.log({'status': status, 'error': error});
            return false;
        }
    })
}
