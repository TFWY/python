#-*- coding: utf-8 -*-

import  cPickle as pickle#持久化类

def readbunchobj(path):#读取bunch对象
    file_obj=open(path,"rb")
    bunch=pickle.load(file_obj)
    file_obj.close()
    return  bunch
def writebunchobj(path,bunchobj):#写入bunch对象
    file_obj=open(path,"wb")
    pickle.dump(bunchobj,file_obj)
    file_obj.close()