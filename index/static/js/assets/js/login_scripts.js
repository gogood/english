/**
 * Created by Administrator on 2017/1/6.
 */
//document.write("<script language='javascript' src='/static/assets/js/common.js'></script>");
document.write("<script language='javascript' src='/static/js/assets/js/ajax.js'></script>");
jQuery(document).ready(function(){


    $('#parentPhone').blur(function(){
         reg=/^1[3|4|5|7|8][0-9]\d{4,8}$/i;//判断输入的手机号是否符合规范
        var phone = $('#parentPhone').val();
        if(phone != '' && phone.length == 11 && reg.test(phone)){
            ajax_apply_mobile_is_exist(phone);
        }
    });

    $('#apply-btn').on('click', function(){
        reg=/^1[3|4|5|7|8][0-9]\d{4,8}$/i;//判断输入的手机号是否符合规范
        patrn = /^(\w){6,20}$/;
        submit = true;
        if($('#childName').val() == ''){
            submit = false;
            alert('请填入孩子的姓名');
        }
        if($('#parentPhone').val() == ''){
            submit = false;
            alert('请填入手机号');
        }else {
            if($('#parentPhone').val().length < 11){
            submit  = false;
            alert('手机号长度不对！');
        }else if(!reg.test($('#parentPhone').val())){
                submit = false;
                alert('手机号无效！');
            }
        }
        if($('#applyPass').val() == ''){
            submit = false;
            alert('密码不能空');
        }else if(!patrn.exec($('#applyPass').val())){
                 submit = false;
                 alert('密码请输入6-20位字母，数字，或者下划线！');
        }
        if($('#recommandPhone').val() != ''){
             if($('#recommandPhone').val().length < 11){
            submit  = false;
            alert('推荐人手机号长度不对！');
        }else if(!reg.test($('#recommandPhone').val())){
                submit = false;
                alert('推荐人手机号无效！');
            }
        }
        if( submit ){
            console.log('apply success');
            var stu_name = $('#childName').val();
            var mobile_phone = $('#parentPhone').val();
            var password = $('#applyPass').val();
            var recom_mobile = $('#recommandPhone').val();
            ajax_apply(stu_name, mobile_phone, password, recom_mobile)
        }
    });

    // if($.cookie('loreUser') == "true"  && $.session.get('key')){
    //     console.log('zidongdenglu');
    //    $('#login-remember').attr("checked", true);
    //     var mobile = $.cookie("mobile");
    //     var password =$.cookie('password');
    //    $('#login-username').val($.cookie("mobile"));
    //    $('#login-password').val($.cookie('password'));
    //     ajax_login(mobile, password);
    //}


    $('#user_center').on('click', function(){
                 ajax_is_login();
    });


    $('#login-remember').on('click', function(e){
        if(e.target.checked){
            console.log({'checked': e.target.checked});
            $('#change-validate-time').attr("checked", true);
        }else{
            $("#change-validate-time").removeAttr("checked");

        }
    });

    $(".f1-first-name").blur(function(){
		var component = '.f1-first-name';
		var error = '#error_mobile';
		var text = '请输入您的手机号';
		if(is_void_field(component, error, text)){
			is_mobile_phone(component, error)
		}
    });

     $('.btn-success').on('click',function(){
        var component = '.f1-first-name';
        var error ='#error_mobile';
        var text = '请输入您的手机号';
        var submit = true;
        if(!is_void_field(component, error,text)){
             submit = false;
        }else{
            if(!is_mobile_phone(component,error)){
                submit = false;
            }
        }

         if( submit ){
             var mobile = $('.f1-first-name').val();
             var password =$('#login-password').val();
             console.log({mobile: mobile, password:password});
             is_login_remember();
             ajax_login(mobile, password);
         }
    })
});

function ajax_apply_mobile_is_exist(mobile_numbe){
	var send_data = {mobile: mobile_numbe};
    var result ;
	 $.ajax({
		type:'POST',
		dataType:'json',
		data: send_data,
		url:'/index/api_mobile_is_exist/',
		success:function(data){
            //result = this;
            //console.log({'data': data});
            if(data.result == 'true'){
                alert('手机号已经被注册了！');
                $('#apply-btn').attr('disabled', 'true');
            }else{
               $('#apply-btn').removeAttr('disabled');
            }

		},
		error:function(status, error){
			  return false;
		}

	});

}

function ajax_apply(stu_name, mobile_phone, password, recom_mobile){
    console.log('ajax_apply');
    var data = {englisth_name: stu_name, mobile: mobile_phone, password: password, recom_mobile: recom_mobile};
    var send_data = JSON.stringify(data);
    $.ajax({
         type: 'POST',
         dataTye: 'json',
         data: send_data,
         url: '/index/api_apply/',
         success: function(data){
             console.log({'return_apply_data': data});
             if(data.result == 'true'){
                 window.location.href = '/index/apply';
             }else{
                 alert('申请失败！');
             }

         },
        error: function(status, error){

        }

    });
}

function ajax_is_login(){
    console.log('ajax_is_login');
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: '/index/api_login/',
        success: function(data){
            if(data.result == 'false'){
                $('#myRegisterModal').modal('show');
            }else{
            window.location.href = '/index/user_center';
            }
        },
        error: function(status, error){
            console.log({status: status, error: error});
        }
    });
}

function ajax_login(mobile, password){
    var send_data = {mobile: mobile, password: password};
    //data = ajax_fun('POST', send_data, '/index/api_login/');
    //console.log({'data':data});
    //if(data.result == 'false'){
    //    console.log('falsefalse');
    //    $('#error_message').html('用户名或者密码错误');
    //    $('#error_message').css('display', 'block');
    //}else{
    //    $('#login_success').removeClass('hidden');
    //    $('.greet').html('Hi,'+ data.student);
    //    $('#change_after_login').addClass('hidden');
    //    $('#myRegisterModal').modal('hide');
    //    //ajax_login_index(data);
    //}
    $.ajax({
        type:'POST',
        dataType:'json',
        data:send_data,
        url:'/index/api_login/',
        success: function(data){
            console.log(data);
            if(data.result == 'false'){
                console.log('falsefalse');
                $('#error_message').html('用户名或者密码错误');
                $('#error_message').css('display', 'block');
            }else{
                $('#login_success').removeClass('hidden');
                $('.greet').html('Hi,'+ data.student);
                $('#change_after_login').addClass('hidden');
                $('#myRegisterModal').modal('hide');
                //ajax_login_index(data);
            }

        },
        error: function(status, error){
            console.log({status: status, error: error});
        }
    })
}


//# login-remember
function is_login_remember(){
    console.log({'checked': $('#login-remember').is(":checked")});
    if($('#login-remember').is(":checked")){
        var mobile = $('#login-username').val();
        var password = $('#login-password').val();
        $.cookie("loreUser", 'true',{expires: 7}); //存储一个带7天期限的cookie
        $.cookie('mobile', mobile, {expires: 7});
        $.cookie('password', password, {expires: 7});
    }else{
        $.cookie("loreUser", 'false',{expires: -1});
        $.cookie('mobile', "", {expires: -1});
        $.cookie('password', "", {expires: -1});
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