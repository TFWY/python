#-*- coding: utf-8 -*-


def savefile(savepath,content): #保存文件
    fp=open(savepath,"wb")
    fp.write(content)
    fp.close()

def readfile(path): #读取文件
    fp=open(path,"rb")
    content=fp.read()
    fp.close()
    return  content