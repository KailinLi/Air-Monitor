# -*- coding: utf-8 -*-

import time
import threading
import requests
import json
from alidayu import api, appinfo
 
def sendMessage (aqi, quality, location, action):
    appkey = "appkey"
    secret = "secret"
    # 输入阿里大于上提供的appkey和secret，发送短信
    req = api.AlibabaAliqinFcSmsNumSendRequest()
    req.set_app_info(appinfo(appkey, secret))
 
    req.extend = ""
    req.sms_type = "normal"
    req.sms_free_sign_name = "name"
    req.sms_param = "{location:'"+location.encode('UTF-8')+"',aqi:'"+str(aqi)+"',quality:'"+quality.encode('UTF-8')+"',action:'"+action+"'}"
    req.rec_num = "phone number"
    req.sms_template_code = "number"
    # 自行在阿里大于申请获取用户名和短信模版编码，并输入发送对象的手机号
    try :
        resp = req.getResponse()
        #print (resp)
    except Exception,e:
        print (e)

def netWork():
    r = requests.get('http://apicloud.mob.com/environment/query?key=keynumber&city=北京')
    # 以北京为例，请使用http://api.mob.com/#/apiwiki/environment 上的信息，替换上面的keynumber，该服务免费，但要注册
    json_data = json.loads(r.text)
    return json_data[u'result'][0][u'quality'], json_data[u'result'][0][u'aqi'], json_data[u'result'][0][u'city']

def action (aqi):
    if aqi > 320:
        return "不要外出"
    elif aqi > 220:
        return "减少外出"
    else:
        return "佩戴口罩"

def loop():  
    getQuality, getAqi, getCity = netWork()
    print getAqi
    if getAqi > 150:
        sendMessage(getAqi, getQuality, getCity, action(getAqi))
    threading.Timer(3600 * 6, loop).start()
    # 每隔6小时循环，因为python运行占用CPU很少，这里采用了比较dirty的方法
  
  
threading.Timer(1, loop).start() 