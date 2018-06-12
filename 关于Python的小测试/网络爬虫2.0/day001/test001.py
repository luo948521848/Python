from urllib import request

#访问的网页ַ
req = request.Request("http://www.baidu.com")
#伪装成正常的用户
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
#开始访问
resp = request.urlopen(req)
#打印访问的结果
print(resp.read().decode("utf-8"))