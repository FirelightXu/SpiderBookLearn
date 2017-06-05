import queue
import threading
import re
import urllib.request
import time
import urllib.error


urlqueue = queue.Queue()




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


class getllisturl(threading.Thread):

	def __init__(self,key,pagestart,pageend,proxy,urlqueue):
		threading.Thread.__init__(self)
		self.pagestart = pagestart
		self.pageend = pageend
		self.proxy=proxy
		self.urlqueue=uelqueue
		self.key = key

	def run(self):
		page = self.pagestart
		keycode = urllib.request.quote(key)
		pagecpde = urllib.request.quote("&page")
		for page in range(self.pagestart,self.pageend+1):
			url = " "
			data1 = use_proxy(proxy,url)
			listurlpat = ''
			listurl.append(re.compile(listurlpat,re.S).findall(data1))
		print("共获取到" + str(len(listurl)) + "页")

		for i in range(0,len(listurl)):
			time.sleep(7)
			for j in range(0,len(listurl[i])):
				try:
					url = listurl[i][j]
					url = url.replace("amp;","")
					self.urlqueue.put(url)
					self.urlqueue.task_done
				except urllib.error.URLError as e:
					if hasattr(e,"code"):
						print(e.code)
					if hasattr(e,"reason"):
						print(e.reason)
					time.sleep(10)
				except Exception as e:
					print("Exception:"+str(e))
					time.sleep(1)

class getcontent(threading.Thread):

	def __init__(self,urlqueue,proxy):
		threading.Thread.__init__(self)
		self.urlqueue = urlqueue
		self.proxy = proxy

	def run(self):
		url = self.urlqueue.get()

#并行控制程序
class contrl(threading.Thread):
	def __init__(self,urlqueue):
		threading.Thread.__init__(self)
		self.urlqueue=urlqueue
	def run(self):
		while(True):
			print ("程序执行中")
			time.sleep(60)
			if (self.urlqueue.empty()):
				print ("程序执行完毕")
				exit()





key = "物联网"
proxy = " "
proxy2 = " "
pagestart = 1
pageend = 2

t1 = getllisturl(key,pagestart,pageend,proxy,uelqueue)
t1.start()

t2 = getcontent(urlqueue,proxy)
t2.start()

t3 = contrl(urlqueue)
t3.start()



