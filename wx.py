# coding:utf-8
from flask import Flask, request, make_response
import time
import hashlib
import xml.etree.ElementTree as ET

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
            s = [timestamp, nonce, token]
            s.sort()
            s = ''.join(s)
            sha1str = hashlib.sha1(s.encode('utf-8')).hexdigest()
            if sha1str == signature:
                return make_response(echostr)
            else:
                return make_response("认证失败")
        else:
            return make_response("认证失败")
    else:
        rec = request.stream.read()
        xml_rec = ET.fromstring(rec)
        tou = xml_rec.find('ToUserName').text
        fromu = xml_rec.find('FromUserName').text
        try:
            content = xml_rec.find('Content').text
        except AttributeError:
            print('this is not a message!')
        xml_rep = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
        response = make_response(xml_rep % (fromu, tou, str(int(time.time())), "hello"))
        response.content_type = 'application/xml'
        return response
