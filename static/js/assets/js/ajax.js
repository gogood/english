/**
 * Created by Administrator on 2017/1/8.
 */
function ajax_fun(type, data, url){
    var fun_data = $.ajax({
        type: type,
        dataType: 'json',
        data: data,
        url:url,
        success:function(data){
            return data;
        },
        error:function(status, error){
            console.log({'stauts':status, 'error': error});
        }
    });

    return fun_data;
}