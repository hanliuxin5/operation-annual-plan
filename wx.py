# coding:utf-8
from flask import Flask, request, make_response
import time
import hashlib
import xml.etree.ElementTree as ET
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.replies import TextReply
from wechatpy import parse_message

app = Flask(__name__)


@app.route("/wechat", methods=["GET", "POST"])
def wechat_auth():
    print(request.args)
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
                print("认证失败")
                return make_response("认证失败")
        else:
            print("认证失败")
            return make_response("认证失败")
    else:
        rec = request.stream.read()
        msg = parse_message(rec)
        reply = TextReply(content='text reply', message=msg)
        xml = reply.render()
        response = make_response(xml)
        response.content_type = 'application/xml'
        return response
