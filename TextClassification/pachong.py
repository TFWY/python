#-*- coding: gbk -*-
import urllib2
import  sys
import  cPickle as pickle

path="pycorpusfile/htmfile/test.html"

#reload(sys)
#sys.setdefaultencoding('utf-8  ')

url="http://news.163.com/rank/"

response= urllib2.urlopen(url)
content=response.read()
file_obj=open(path,"wb")
pickle.dump(content,file_obj)
file_obj.close()
#print content.decode("gbk")#.encode("utf-8")
