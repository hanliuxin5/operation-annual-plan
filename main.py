# coding:utf-8
from flask import Flask, request, make_response
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.replies import TextReply
from wechatpy import parse_message
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/wechat", methods=["GET", "POST"])
def wechat_auth():
    # print(request.args)
    if request.method == 'GET':
        if len(request.args) > 3:
            token = 'lizhiwodage'
            query = request.args
            signature = query['signature']
            timestamp = query['timestamp']
            nonce = query['nonce']
            echostr = query['echostr']
            try:
                check_signature(token, signature, timestamp, nonce)
                make_response(echostr)
            except InvalidSignatureException:
                print("sinature认证失败")
                return make_response("sinature认证失败")
        else:
            print("args认证失败")
            return make_response("args认证失败")
    elif request.method == 'POST':
        rec = request.stream.read()
        msg = parse_message(rec)
        print("id=%s,source=%s,target=%s,type=%s" % (msg.id, msg.source, msg.target, msg.type))
        content = "empty"

        if msg.type == "event":
            if msg.event == "pic_photo_or_album":
                if msg.key == "sign":
                    content = "sign"
                    process_sign(msg.count, msg.pictures)
            if msg.event == "click":
                if msg.key == "items":
                    content = "items"
                    process_items()

        if msg.type == "image":
            get_user_uploadpics(msg.source, msg.image)

        reply = TextReply(content=content, message=msg)
        xml = reply.render()
        response = make_response(xml)
        response.content_type = 'application/xml'
        return response


def process_sign(count=0, pics={}):
    print("process_sign>>>start")
    print("count=%s" % count)
    print(pics)
    print("process_sign>>>end")


def process_items():
    print("process_items")


def get_user_uploadpics(userid="", url=""):
    print("get_user_uploadpics>>>start")
    print("userid=%s,pics=%s" % (userid, url))
    print("get_user_uploadpics>>>end")


if __name__ == "__main__":
    app.run(host="172.31.30.163", port=80, debug=True)
