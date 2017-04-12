#-*- coding: utf-8 -*-

from  numpy import *
from  ID3tree import *
import  bunchop as bo


path=""
treeaspath=""
labels=[]
vector=[]

dtree =ID3tree()
dtree.loadDataSet(path,labels)
dtree.train()
print  dtree.tree

bo.writebunchobj(dtree.tree,treeaspath)
mytree=bo.readbunchobj(treeaspath)
#print  mytree
print "truethprint:"," .......","->","id3treeprint:",dtree.predict(mytree,labels,vector)