#通过http 来对账号进行验证
#利用urllib 进行http访问

import json
import tkinter #用以显示文本和图像
import urllib
class HttpPost():
    def login(name,password):
        print("进行登录操作")
        url = "http://localhost:8080/login"
        try:
            data = bytes(urllib.parse.urlencode({'name': str(name),'password':str(password)}), encoding=
            'utf8')
            response = urllib.request.urlopen(url,data=data)
            jsonDatas = json.load(response)
            sign =jsonDatas["sign"]   #如果是以类形式传输则通过2层结构进行解析
            return sign
        except (SyntaxError) as err:
            print("SyntaxError"+err.args)
        finally:
            None;