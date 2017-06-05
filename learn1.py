import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")

data = file.read()
dataline = file.readline()

'''
file.read()   读取的内容全部赋值给一个字符串变量
file.readlines()   读取的内容赋给一个列表变量
file.readline()    读取文件的一行内容

'''
fhandle = open('/Users/xuye/Documents/Deep_in_python_webcrawler/1.html',"wb")
fhandle.write(data)
fhandle.close()

# filename = urllib.request.urlretrieve("heep://edu.51cto.com",filename = "/Users/xuye/Documents/Deep_in_python_webcrawler/1.html")		
# 直接写入文件 urlretrieve 方法
# urlretrieve 会产生缓存，清除缓存的方法：
# urllib.request.urlclearnup()

file.info()
file.getcode()
file.geturl()
urllib.request.quote("http://www.sina.com.cn")
urllib.request.unquote(" ")

# build_opener() 来修改报头   （访问网站时添加user-agent的方法1）

url = " "
headers = ('User-Agent',".......")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()

# add_header() 来添加报头   （访问网站时添加user-agent的方法2）

url = ''
req = urllib.request.Request(url)
req.add_header('User-Agent','')
data = urllib.request.urlopen(req).read()

# 设置超时

for i in range(1,100):
	try:
		file = urllib.request.urlopen('http://....',timeout = 1)
		data = file.read()
		print (data)
	except Exception as e:
		print ("出现异常---》" + str(e))

# get()方法访问

url = "http://www.baidu.com/s?wd="
key = "中文"
key_code = urllib.request.quote(key)
url_all = url + key_code
req = urllib.request.Request(url_all) # 以对应的url为参数构建request对象
data = urllib.request.urlopen(req).read() # 通过urlopen打开构建的request对象
fh = open("path","wb") # 二进制方式写入
fh.write()
fh.close()

# post方法访问

import urllib.request
import urllib.parse

url = "http://...."
postdata = urllib.parse.urlencode({
	"name" : "clshinem",
	"pass" : "xuye123456"
	}).encode('utf-8') # 将数据使用urlopen编码处理后，使用encode（）设置为utf-8编码
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','....')
data = urllib.request.urlopen(req).read()
fhandle=open("path","wb")
fhandle.write()
fhandle.close()

# 代理ip

def use_proxy(proxy_addr,url):
	proxy = urllib.request.ProxyHandle({'http':proxy_addr})
	opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler) # 设置自己的opener对象
	urllib.request.install_opener(opener) # 创建全局默认的opener对象，创建后在使用urlopen时会使用我们安装的opener对象
	data = urllib.request.urlopen(url).read().decode('utf-8')
	return data
proxy_addr = "202.75.210.45:7777"
data = use_proxy(proxy_addr,"http://www.baidu.com")
print(len(data))

# urlError httpError
import urllib.request
import urllib.error

try:
	urllib.request.urlopen("http://blog....")
except urllib.error.URLError as e:
	print(e.code)
	print(e.reason)


try:
	urllib.request.urlopen("http:...")
except urllib.error.HTTPError as e:
	print (e.code)
	print (e.reason)
except urllib.error.URLError as e:
	print (e.reason)

# urlerror没有codema httperror就有 所以如果要整合这两个错误的话需要加一个判断
except urllib.error.URLError as e:
	if hasattr(e,"code"):
		print(e.code)
	if hasattr(e,"reason"):
		print(e.reason)


