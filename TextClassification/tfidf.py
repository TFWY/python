#-*- coding: utf-8 -*-

import  sys
import  os
import fileop
import bunchop
from  sklearn.datasets.base import  Bunch
from  sklearn import feature_extraction
from  sklearn.feature_extraction.text import TfidfTransformer#tf-idf向量转化类
from  sklearn.feature_extraction.text import TfidfVectorizer#tf-idf向量生成类

reload(sys)
sys.setdefaultencoding('utf-8')


#读取停用词表
stopword_path="pycorpusfile/train_word_bag/hlt_stop_words.txt"
stpwrdlst=fileop.readfile(stopword_path).splitlines()
#导入分词后词向量bunch
path="pycorpusfile/train_word_bag/train_set.dat"#词向量空间保存路径
bunch=bunchop.readbunchobj(path)
#构建tf-idf词向量空间对象
tfidfspace=Bunch(target_name=bunch.target_name,label=bunch.label,
                 filenames=bunch.filenames,tdm=[],vocabulary={})
#使用TfidfVectorizer初始化向量空间模型
vectorizer=TfidfVectorizer(stop_words=stpwrdlst,sublinear_tf=True,
                           max_df=0.5)
transformer=TfidfTransformer()#该类统计每个词语的tf-idf权值
#文本转为词频矩阵，单独保存字典文件
tfidfspace.tdm=vectorizer.fit_transform(bunch.contents)
tfidfspace.vocabulary=vectorizer.vocabulary_
#创建词袋的持久化
space_path="pycorpusfile/train_word_bag/tfidfspace.dat"#词向量词袋保存路径
bunchop.writebunchobj(space_path,tfidfspace)

