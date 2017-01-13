/**
 * Created by Administrator on 2017/1/4.
 */

jQuery(document).ready(function() {
    	 //手机号栏失去焦点
	$(".f1-first-name").blur(function(){
		var component = '.f1-first-name';
		var error = '.error-mobile-number';
		var text = '请输入您的手机号';
		if(is_void_field(component, error, text)){
			if(is_mobile_phone(component, error)){
				mobile = $(component).val();
               ajax_mobile_is_exist(mobile);
			}

		}

		//reg=/^1[3|4|5|7|8][0-9]\d{4,8}$/i;//验证手机正则(输入前7位至11位)
		//
		//if( $(this).val()=="")
		//{
		//
		//    $(this).next().html("请输入您的手机号");
		//    $(this).next().css("display","block");
		//}
		//else if($(this).val().length<11)
		//{
		//
		//    $(this).next().html("手机号长度有误！");
		//    $(this).next().css("display","block");
		//}
		//else if(!reg.test($(".f1-first-name").val()))
		//{
		//
		//    $(this).next().html("手机号不存在!");
		//    $(this).next().css("display","block");
		//}
		//else
		//{
		//    $(this).next().empty();
		//}
	});
    	$('#change-validate-time').click(function(){
		ajax_meassage();

	});

    	  /*验证码输入框失去焦点*/
	$(".photokey").blur(function(){
		var component1 = '.photokey';
		var component2 = '.phoKey';
		var error = '.error-validate';
		var text = "验证码输入错误！";
		is_equal(component1, component2, error, text, false);

		//var code1=$('input.photokey').val();
		//var code2=$(".phoKey").text();
		//if(code1!=code2)
		//{
		//	$(this).next().next().html("验证码输入错误！");
		//	$(this).next().next().css("display","block");
		//}
		//else
		//{
		//	$(this).next().next().empty();
        //
		//}
	});
	//{#           when you get mobile-phone message validate,you should input it#}
    	$('.message_validate').blur(function(){
		var component = '.message_validate';
		var error = '.error_message_validate';
		var text = '请输入验证码';
		$('.error_message_validate').css("color","#ff0000");
		is_void_field(component, error, text);
	});

    	$('.f1-password').blur(function(){
		var error = '.error-f1-password';
		var component = '.f1-password';
		var text = "密码不能为空";
		if(is_void_field(component, error, text)){
			is_password(component, $('.f1-password').val(), error);
		}
	});


        /*
        Fullscreen background
    */
    //$.backstretch("/static/images/img/backgrounds/2.jpg");

    //$('#top-navbar-1').on('shown.bs.collapse', function(){
    //	$.backstretch("resize");
    //});
    //$('#top-navbar-1').on('hidden.bs.collapse', function(){
    //	$.backstretch("resize");
    //});

    /*
        Form
    */
    $('.f1 fieldset:first').fadeIn('slow');

    $('.f1 input[type="text"], .f1 input[type="password"]').on('focus', function() {
    	$(this).removeClass('input-error');
    });

    	/*生成验证码*/
	//function shuffle(){
	//	var arr=['1','r','Q','4','S','6','w','u','D','I','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
	//		'q','2','s','t','8','v','7','x','y','z','A','B','C','9','E','F','G','H','0','J','K','L','M','N','O','P','3','R',
	//		'5','T','U','V','W','X','Y','Z'];
	//	return arr.sort(function(){
	//		return (Math.random()-.5);
	//	});
	//}
	//shuffle();
	//function show_code(){
	//	var ar1='';
	//	var code=shuffle();
	//	for(var i=0;i<6;i++){
	//		ar1+=code[i];
	//	}
	//	//var ar=ar1.join('');
	//	$(".phoKey").text(ar1);
	//}
	show_code();
	$(" .phoKey").click(function(){
		show_code();
	});

});

function scroll_to_class(element_class, removed_height) {
	var scroll_to = $(element_class).offset().top - removed_height;
	if($(window).scrollTop() != scroll_to) {
		$('html, body').stop().animate({scrollTop: scroll_to}, 0);
	}
}

function bar_progress(progress_line_object, direction) {
	var number_of_steps = progress_line_object.data('number-of-steps');
	var now_value = progress_line_object.data('now-value');
	var new_value = 0;
	if(direction == 'right') {
		new_value = now_value + ( 100 / number_of_steps );
	}
	else if(direction == 'left') {
		new_value = now_value - ( 100 / number_of_steps );
	}
	progress_line_object.attr('style', 'width: ' + new_value + '%;').data('now-value', new_value);
}

function is_mobile_phone(component, error){
	reg=/^1[3|4|5|7|8][0-9]\d{4,8}$/i;//判断输入的手机号是否符合规范

	if($(component).val().length<11)
	{
        $(component).addClass('input-error');
		$(error).html("手机号长度有误！");
		$(error).css("display","block");
		return false;
	}
	else if(!reg.test($(".f1-first-name").val()))
	{

		$(error).html("手机号不存在！");
		$(error).css("display","block");
		$(component).addClass('input-error');
		return false;
	}
	else
	{
		$(error).empty();
		$(component).removeClass('input-error');
		return true;
	}
}

function is_void_field(component, error, text){
	if( $(component).val()== ''){
		console.log('45678');
		$(error).html(text);
		$(error).css("display","block");
		$(component).addClass('input-error');
		return false;
	}else{
		$(error).empty();
		$(component).removeClass('input-error');
		return true;
	}
}

function is_equal(component1, component2, error, text, is_password){
	var code1=$(component1).val();
	if(is_password){
		var code2 = $(component2).val();
	}else{
		var code2=$(component2).text();
	}
	console.log('1111is');
	console.log(code1);
	console.log(code2);
	if(code1 =='' || code1!=code2)
	{
		$(component1).addClass('input-error');
		$(error).html(text);
		$(error).css("display","block");
		return false;
	}
	else
	{
		$(error).empty();
		$(component1).removeClass('input-error');
		return true;
	}
}

function is_password(component, password, error){
	var patrn = /^(\w){6,20}$/;
	if(!patrn.exec(password)){
		$(error).html('只能输入6-20位的字母，数字，下划线！');
		$(error).css('display', 'block');
		$(component).addClass('input-error');
		return false;
	}else{
		$(component).removeClass('input-error');
		$(error).empty();
		return true;
	}
}

	/*生成随机数验证*/
//create random_data
function shuffle(){
	var arr=['1','r','Q','4','S','6','w','u','D','I','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
		'q','2','s','t','8','v','7','x','y','z','A','B','C','9','E','F','G','H','0','J','K','L','M','N','O','P','3','R',
		'5','T','U','V','W','X','Y','Z'];
	return arr.sort(function(){
		return (Math.random()-.5);
	});
}
function show_code(){
	var ar1='';
	var code=shuffle();
	for(var i=0;i<6;i++){
		ar1+=code[i];
	}
	//var ar=ar1.join('');
	$(".phoKey").text(ar1);
}

function ajax_meassage(){
	validate_time_count = 60;
		validate_message_value = creat_message_validate();
		var mobile = $('input.f1-first-name').val();
		var send_data = {mobile:mobile,validate_message:validate_message_value};
		//send = JSON.stringify(send_data);
		console.log('ajax go');
		$.ajax({
			type:"POST",
			dataType:'json',
			data:send_data,
			url:"/index/register_message_validate/",
			success:function(data){
				console.log('success123');
				//show message-validate-time,button is diabled,time maybe 60s,when time is 0s,will change to free-get
				$('#change-validate-time').attr("disabled", true);
				$('#change-validate-time').css("background-color", "#bbb");
				$('#change-validate-time').val( validate_time_count + "s后重新获取");
				InterValObj = window.setInterval(SetRemainTime, 1000); //启动计时器，1秒执行一次
				$('.error_message_validate').html("验证码已发至您的手机，30分钟内输入有效");
				$('.error_message_validate').css("color","#337ab7");
				//$('.error_message_validate').addClass('message_validate_tag');
			},
			error:function(status, error){
				console.log('123error');
				$("#change-validate-time").removeAttr("disabled");//启用按钮
				$("#change-validate-time").val("免费获取");
				$("#change-validate-time").css("background-color", "#337ab7");
				$('.error_message_validate').html("验证码发送失败，请重新获取");
				$('.error_message_validate').removeClass('message_validate_tag');
				$('.error_message_validate').css("color","#ff0000");
				console.log({"status": status, "error":error});
			}
		});
}

// 产生4位数的短信验证码
function creat_message_validate(){
	var charactors="1234567890";
	var value='',i;
	for(j=1;j<=4;j++){
		i = parseInt(10*Math.random());
		value = value + charactors.charAt(i);
	}
	return value;
}

//timer处理函数
function SetRemainTime() {
	if (validate_time_count == 0) {
		window.clearInterval(InterValObj);//停止计时器
		$("#change-validate-time").removeAttr("disabled");//启用按钮
		$("#change-validate-time").val("免费获取");
		$("#change-validate-time").css("background-color", "#337ab7");
		$('.error_message_validate').html("");
	}
	else {
		validate_time_count--;
		$("#change-validate-time").val(validate_time_count + "s后重新获取");
		$("#change-validate-time").css("background-color", "#bbb");
	}
}

function SetTime(){
    time = 30*60;
    if(time == 0){
        return true;
    }else{
        time--;
        return false;
    }
}

function ajax_mobile_is_exist(mobile_numbe){
	var send_data = {mobile: mobile_numbe};
	$.ajax({
		type:'POST',
		dataType:'json',
		data: send_data,
		url:'/index/api_mobile_is_exist/',
		success:function(data){
			console.log({'data': data});
            if($('.f1-first-name').hasClass('forget-mobile')){
                if(data.result == 'true'){
                    $('.f1-first-name').removeClass('input-error');
				$( '.error-mobile-number').empty();
				$('.middle-next').removeAttr("disabled");
                }else{
                      $('.f1-first-name').addClass('input-error');
			$( '.error-mobile-number').html('该手机号不存在！');
			$( '.error-mobile-number').css("display","block");
				$('.middle-next').attr("disabled", true);
                }
            }else{
                	if(data.result == 'true'){
                $('.f1-first-name').addClass('input-error');
			$( '.error-mobile-number').html('手机号已注册过了');
			$( '.error-mobile-number').css("display","block");
				$('.middle-next').attr("disabled", true);
			}else{
				$('.f1-first-name').removeClass('input-error');
				$( '.error-mobile-number').empty();
				$('.middle-next').removeAttr("disabled");
			}
            }
			return true;
		},
		error:function(status, error){
			  return false;
		}

	})

}

