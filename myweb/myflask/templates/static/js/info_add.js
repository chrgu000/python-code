var max_line_num = {};
//添加新记录
function add_line(index) {
    // 获取当前div的id
    var id = $(index).parents(".tab-pane").get(0).id;
    // alert(id);
    // 行数加1
    if ($("#" + id + " #content").children("tr").length <= 0) {
        max_line_num[id] = parseInt(0);
    }
    max_line_num[id] += 1;
    // 插入行
    var new_line_html = "<tr id='line" + max_line_num + "'>"
    var title_num = $('#' + id + ' thead tr').children("td").length;
    for (var i = 1; i <= title_num - 1; i++) { //n个标题n个输入框，最后一格是操作格子
        new_line_html += ("<td><input type='text' class='form-control' placeholder='value" + max_line_num[id] + "'></input></td>")
    }
    new_line_html += ( //加上一个操作格子
        "<td>" +
        "<button type='button' class='btn btn-info btn-xs' onclick='up_exchange_line(this);'>上移</button> " +
        "<button type='button' class='btn btn-info btn-xs' onclick='down_exchange_line(this);'>下移</button> " +
        "<button type='button' class='btn btn-danger btn-xs' onclick='remove_line(this);'>删除</button> " +
        "</td>" +
        "</tr>"
    )
    $("#" + id).find('#content').append(new_line_html); // 添加新行
}
//显示模态框时的操作
// $('#info').on('show.bs.modal', function () {
//添加一行
// add_line();
// 没有内容隐藏
// $("#info").find('.modal-footer').each(function () {
//     var info = $(this).find("#content").find("tr");
//     if ( info.length == 0) {
//         $(this).attr("style","display:none;");
//     }else{
//         $(this).attr("style","display:block;");
//     }
// });
// })
//关闭模态框后刷新页面
// $('#info').on('hidden.bs.modal', function () {
//     location.reload(); /* 刷新页面 */
// })
//删除选择记录
function remove_line(index) {
    // 获取当前div的id
    var id = $(index).parents(".tab-pane").get(0).id;
    // 获取当前的tr 
    var $tr = $(index).parents("tr");

    if (confirm("确定要删除改记录吗？")) {
        $tr.remove();
        max_line_num[id] -= 1;
    }
}
//上移
function up_exchange_line(index) {
    // 获取当前的tr 
    var $tr = $(index).parents("tr");

    if ($tr.index() < 1) {
        alert('已经是最顶项了!');
        return false;
    }
    $tr.prev().before($tr); //在每个匹配的元素之前插入内容。
    $tr.css("background-color", "yellow"); //移动项添加背景色
    event.stopPropagation(); //阻止事件冒泡
}
//下移
function down_exchange_line(index) {
    // 获取当前div的id
    var id = $(index).parents(".tab-pane").get(0).id;
    // 获取当前的tr 
    var $tr = $(index).parents("tr");
    if ($tr.index() == max_line_num[id] - 1) {
        alert('已经是最底项了!')
        return false;
    }
    $tr.next().after($tr); //在每个匹配的元素之后插入内容。
    //移动项添加背景色
    $tr.css("background-color", "yellow");
    event.stopPropagation(); //阻止事件冒泡
}
//提交数据

function SubData() {
    var errord = false; // 中途出错不提交数据
    var jsonData = {}; //需要提交的数据
    // 获取信息区的div列表
    var info_div = $(".modal-body .tab-content").children("div").get();
    for (var $d in info_div) { //遍历要提交的数据
        var div_id = info_div[$d].id; //div的id值
        if (div_id != 'infoOther') {
            jsonData[div_id] = [];
        } else { //other项用字典
            jsonData[div_id] = {};
        }
        //取值
        if (div_id == 'infoOther') {  //other标签页用字典
            $("#" + div_id).find('#content tr').each(function () { //每一行input框一次执行
                var dict = [];
                console.log($(this).children('td').length);
                for (var i = 1; i <= $(this).children('td').length - 2; i++) { //数组下标从0开始-1；最后一个操作格子-1
                    dict.push($(this).find("td:eq(" + i + ")").find("input").val())
                }
                jsonData['infoOther'][$(this).find("td:eq(0)").find("input").val()] = dict;
            });
        } else {
            $("#" + div_id).find('#content tr input').each(function () { //每一个input框一次执行
                jsonData[div_id].push($(this).val())
            });
        }
    }
    // if (errord) {
    console.log("=======>>>>>>>" + JSON.stringify(jsonData));

    // $.ajax({
    //     url: 'http://127.0.0.1:5000/post',
    //     data: data,
    //     type: 'post',
    //     dataType: 'json',
    //     headers: {
    //         Accept: "application/json",
    //         "Content-Type": "application/json;charset=utf-8"
    //     },
    //     processData: false,
    //     cache: false,
    // success:function (msg) {
    //     alert("提交成功"+JSON.stringify(msg));
    // },
    // error:function (msg) {
    //     alert("提交失败"+JSON.stringify(msg));
    // }
    // });

    // location.reload(); /* 刷新页面 */
}