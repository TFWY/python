#-*- coding: utf-8 -*-

import  sys

import bunchtest
import  segcorpus

reload(sys)
sys.setdefaultencoding('utf-8')

corpus_path="pycorpusfile/test_corpus_small/" #未分类分词语料库路径
wordbag_path="pycorpusfile/test_word_bag/test_set.dat"#分词语料Bunch对象持久化路径
seg_path="pycorpusfile/test_corpus_seg/"#分词后分类语料库路径

segcorpus.seg(corpus_path, seg_path)
bunchtest.pickobj(seg_path,wordbag_path)