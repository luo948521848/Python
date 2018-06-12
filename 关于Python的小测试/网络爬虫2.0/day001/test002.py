from urllib.request import Request
from urllib.request import urlopen
from urllib import parse
#post注入表单信息

#输入的是目标网页
#在进入目标网页可能需要传入一些值
req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")
#表单输入的类容
postData = parse.urlencode(
    [
       ("StartStation" , "2f940836-cedc-41ef-8e28-c2336ac8fe68"), 
       ("EndStation" , "977abb69-413a-4ccf-a109-0272c24fd490"), 
       ("SearchDate" , "2018/01/06"), 
       ("SearchTime" , "23:30"), 
       ("SearchWay" , "DepartureInMandarin")    
        ])

#伪装成从上一个网页进入的
req.add_header("Origin" ,"http://www.thsrc.com.tw" )
#伪装成正常的主机访问
req.add_header("User-Agent" ,"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36")
#注入表值进入目标网页
resp = urlopen(req, data=postData.encode("utf-8"))
#打印输出的结果
print(resp.read().decode("utf-8"))