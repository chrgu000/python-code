#-*- coding: utf-8 -*-
# 请求格式如下，用于服务器业务警告通知
# curl -i -H "Content-Type: application/json" -X POST -d '{"mobile" : "19994411399", "content" : "Geth-test02$$1.2.4.8$$erc20API$$09-21 16:08 出错重启了一次"}' http://localhost:5000/foo
from flask import Flask, abort, request 
import json
from send_sms import SMS

app = Flask(__name__)

@app.route('/foo', methods=['POST']) 
def foo():
    if not request.json:
        abort(400)
    # print("type: ", type(request.json))
    # print(request.json['mobile'])
    # print(request.json['content'])
    sms = SMS()
    # 获取参数
    result = request.json
    # 手机号
    sms.mobile = result['mobile'] or '19994411399'
    # 发送模板变量内容
    sms.content = result['content']
    # 发送警告
    send = sms.send()
    # return json.dumps(request.json)
    # 返回发送结果
    return send


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)