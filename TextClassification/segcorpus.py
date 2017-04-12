#-*- coding: utf-8 -*-

import  os
import  jieba
import fileop



def seg(corpus_path,seg_path):
    catelist=os.listdir(corpus_path) #获取corpus_path下的所有子目录
    for mydir in catelist:
        class_path=corpus_path+mydir+"/" #拼出分类子目录路径
        seg_dir=seg_path+mydir+"/" #拼出分词后分类运料库路径
        if not os.path.exists(seg_dir):#如果目录不存在则创建
            os.makedirs(seg_dir)
        file_list=os.listdir(class_path)#获取目录下的所有文件
        for file_path in file_list:#遍历目录下文件
            fullname=class_path+file_path#拼出文件名全路径
            content=fileop.readfile(fullname).strip()#读取文件内容
            content=content.replace("\r\n","").strip()#删除换行和多余空格
            content_seg=jieba.cut(content)
            fileop.savefile(seg_dir+file_path," ".join(content_seg))
    print "语料分词结束！"
