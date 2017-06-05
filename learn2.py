import re
import urllib.request
import time
import urllib.error

headers = ("User-Agent","")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
listurl=[]

def use_proxy(proxy_addr,url):
	try:
		import urllib.request
		proxy = urllib.request.ProxyHandle({'http':proxy_addr})
		opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
		urllib.request.install_opener(opener)
		data = urllib.request.urlopen(url).read().decode('utf-8')
		return data
	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)
		time.sleep(10)
	except Exception as e:
		print("Exception:"+str(e))
		time.sleep(1)


def getllisturl(key,pagestart,pageend,proxy):
	try:
		page = pagestart
		keycode = urllib.request.quote(key)
		pagecpde = urllib.request.quote("&page")
		for page in range(pagestart,pageend+1):
			url = " "
			data1 = use_proxy(proxy,url)
			listurlpat = ''
			listurl.append(re.compile(listurlpat,re.S).findall(data1))
		print("共获取到" + str(len(listurl)) + "页")
		return listurl
	except urllib.error.URLError as e:
		if hasattr(e,"code"):
			print(e.code)
		if hasattr(e,"reason"):
			print(e.reason)
		time.sleep(10)
	except Exception as e:
		print("Exception:"+str(e))
		time.sleep(1)

def getcontent(listurl,proxy):
	pass

key = "物联网"
proxy = " "
proxy2 = " "
pagestart = 1
pageend = 2
listurl = getlisturl(key,pagestart,pageend,proxy)
getcontent(listurl,proxy)


