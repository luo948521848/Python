from urllib.request import  urlopen
from bs4 import BeautifulSoup
import re
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