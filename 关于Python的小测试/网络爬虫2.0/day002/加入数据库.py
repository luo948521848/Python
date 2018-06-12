from urllib.request import  urlopen
from bs4 import BeautifulSoup
import re
import pymysql
#get的访问方法减少了很多需要伪装的地方
#这里直接进行访问   后面的read.decode("utf-8")防止输出结果乱码
resp = urlopen("http://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
#将获取的内容解析
soup = BeautifulSoup(resp , "html.parser")
#获取所有以/wiki/开头的a标签的herf属性
listUrls = soup.findAll("a" , href = re.compile(r"^/wiki/"))
for url in listUrls:
    if not re.search("\.(jpg|JPG)$",url["href"]):
        print(url.get_text(),"<---->" ,"http://en.wikipedia.org/"+url["href"])
        conn = pymysql.connect(
                    host = '127.0.0.1',
                    port = 3306, #注意这里不是字符串
                    user = 'root',
                    passwd = '092248',
                    db = 'python',
                    charset = 'utf8'                                   
              )

        try:
            #获取会话对象
            cursor = conn.cursor()
            #可以用纯粹的sql的语句 不用加单引号
            sql = "insert into urls(urlname ,urlhref)values(%s,%s)"
            #在这里注入参数  注意括号
            cursor.execute(sql,(url.get_text(), "http://en.wikipedia.org/"+url["href"]))
            #提交事件
            conn.commit()
        finally:
            conn.close()