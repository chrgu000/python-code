var currentStep = 0;
var max_line_num = 0;
//添加新记录
function add_line(that) {
    // 获取当前div的id
    var id = $(that).parents(".modal-footer").get(0).id;
    // alert(id);

    max_line_num = $("#" + id + " #content tr:last-child").children("td").html();
    if (max_line_num == null) {
        max_line_num = 1;
    } else {
        max_line_num = parseInt(max_line_num);
        max_line_num += 1;
    }
    $("#" + id).find('#content').append(
        "<tr id='line" + max_line_num + "'>" +
        "<td style='display:none'>" + max_line_num + "</td>" +
        "<td><input type='text' class='form-control' placeholder='步骤名称" + max_line_num +
        "'></input></td>" +
        "<td><input type='text' class='form-control' placeholder='步骤名称" + max_line_num +
        "'></input></td>" +
        "<td class='td_Item'><input type='text' class='form-control' placeholder='步骤描述" + max_line_num +
        "'></td>" +
        "<td>" +
        "<button type='button' class='btn btn-info btn-xs' onclick='up_exchange_line(this);'>上移</button> " +
        "<button type='button' class='btn btn-info btn-xs' onclick='down_exchange_line(this);'>下移</button> " +
        "<button type='button' class='btn btn-danger btn-xs' onclick='remove_line(this);'>删除</button> " +
        "</td>" +
        "</tr>");
}
//显示模态框时的操作
$('#info').on('show.bs.modal', function () {
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
})
//关闭模态框后刷新页面
// $('#info').on('hidden.bs.modal', function () {
//     location.reload(); /* 刷新页面 */
// })
//删除选择记录
function remove_line(index) {
    // 获取当前div的id
    var id = $(index).parents(".modal-footer").get(0).id;

    if (index != null) {
        currentStep = $(index).parent().parent().find("td:first-child").html();
    }
    if (currentStep == 0) {
        alert('请选择一项!');
        return false;
    }
    if (confirm("确定要删除改记录吗？")) {
        $("#" + id + " #content tr").each(function () {
            var seq = parseInt($(this).children("td").html());
            if (seq == currentStep) {
                $(this).remove();
            }
            if (seq > currentStep) {
                $(this).children("td").each(function (i) {
                    if (i == 0) $(this).html(seq - 1);
                });
            }
        });
    }
}
//上移
function up_exchange_line(index) {
    // 获取当前div的id
    var id = $(index).parents(".modal-footer").get(0).id;

    if (index != null) {
        currentStep = $(index).parent().parent().find("td:first-child").html();
    }
    if (currentStep == 0) {
        alert('请选择一项!');
        return false;
    }
    if (currentStep <= 1) {
        alert('已经是最顶项了!');
        return false;
    }
    var upStep = currentStep - 1;
    //修改序号, 第一列的序号值，已删除
    $('#' + id +' #line' + upStep + " td:first-child").html(currentStep);
    $('#' + id +' #line' + currentStep + " td:first-child").html(upStep);
    //取得两行的内容
    var upContent = $("#" + id).find('#line' + upStep).find("input").val();
    var currentContent = $('#line' + currentStep).html();
    alert(upContent + '++++++' + currentContent)
    $('#' + id +' #line' + upStep).html(currentContent);
    //交换当前行与上一行内容
    $('#' + id +' #line' + currentStep).html(upContent);
    $('#' + id +' #content tr').each(function () {
        $(this).css("background-color", "#ffffff");
    });
    $('#' + id +' #line' + upStep).css("background-color", "yellow");
    event.stopPropagation(); //阻止事件冒泡
}
//下移
function down_exchange_line(index) {
    // 获取当前div的id
    var id = $(index).parents(".modal-footer").get(0).id;

    if (index != null) {
        currentStep = $(index).parent().parent().find("td:first-child").html();
    }
    if (currentStep == 0) {
        alert('请选择一项!');
        return false;
    }
    if (currentStep >= max_line_num) {
        alert('已经是最后一项了!');
        return false;
    }
    var nextStep = parseInt(currentStep) + 1;
    //修改序号
    $('#' + id +' #line' + nextStep + " td:first-child").html(currentStep);
    $('#' + id +' #line' + currentStep + " td:first-child").html(nextStep);
    // alert('#line' + nextStep + '++++++' + '#line' + currentStep)
    //取得两行的内容
    var nextContent = $('#' + id).find('#line' + nextStep).html();
    var currentContent = $('#' + id).find('#line' + currentStep).html();
    //交换当前行与上一行内容
    $('#' + id +' #line' + nextStep).html(currentContent);
    $('#' + id +' #line' + currentStep).html(nextContent);
    $('#' + id +' #content tr').each(function () {
        $(this).css("background-color", "#ffffff");
    });
    $('#' + id +' #line' + nextStep).css("background-color", "yellow");
    event.stopPropagation(); //阻止事件冒泡
}
//提交数据

function SaveData() {

    var data = {};
    $('#content tr').each(function () {
        // data += "<item>";
        var proName = $(this).find("option:selected").text();
        // var stepNum = $(this).find("td:eq(0)").text();
        var stepName = $(this).find("td:eq(2)").find("input").val();
        var stepDescription = $(this).find("td:eq(3)").find("input").val();
        // alert(data[proName])
        if (data[proName] == undefined) {
            data[proName] = [stepName, stepDescription];
        } else {
            data[proName].push(stepName, stepDescription);
            // data[proName].push(stepDescription);
        }
    });
    data = JSON.stringify(data);
    // alert(data);

    $.ajax({
        url: 'http://127.0.0.1:5000/post',
        data: data,
        type: 'post',
        dataType: 'json',
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json;charset=utf-8"
        },
        processData: false,
        cache: false,
        // success:function (msg) {
        //     alert("提交成功"+JSON.stringify(msg));
        // },
        // error:function (msg) {
        //     alert("提交失败"+JSON.stringify(msg));
        // }
    });

    // location.reload(); /* 刷新页面 */
}