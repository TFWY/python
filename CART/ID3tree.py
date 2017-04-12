# -*- coding:utf-8 -*-

from  numpy import  *
import  math
import  copy
import  cPickle as pickle

class ID3tree(object):
    def __init__(self):
        self.tree={}
        self.dataSet=[]
        self.labels=[]

    def loadDataSet(self,path,labels):
        recordlist=[]
        fp=open(path,"rb")
        content=fp.read()
        fp.close()
        rowlist=content.splitlines()
        recordlist=[row.split("\t") for  row in rowlist if row.strip()]
        self.dataSet=recordlist
        self.labels=labels

    def train(self):
        labels=copy.deepcopy(self.labels)
        self.tree=self.buildTree(self.dataSet,labels)

    def buildTree(self,dataset,labels):
        catelist=[data[-1] for data in dataset]

        if catelist.count(catelist[0])==len(catelist):
            return  catelist[0]

        if len(dataset[0])==1:
            return  self.maxcate(catelist)

        bestfeat=self.getbestfeat(dataset)
        bestfeatlabel=labels[bestfeat]
        tree ={bestfeatlabel:{}}
        del(labels[bestfeat])

        uniquevals=set([data[bestfeat] for data in dataset])
        for value in uniquevals:
            sublabels =labels[:]
            splitdataset =self.splitdataset(dataset,bestfeat,value)
            subtree=self.buildTree(splitdataset,sublabels)
            tree[bestfeatlabel][value]=subtree
        return  tree

    def maxcate(self,catelist):
        items=dict([(catelist.count(i),i)for i in catelist])
        return  items[max(items.keys())]

    def getbestfeat(self,dataset):
        numfeatures=len(dataset[0])-1
        baseentropy=self.computeentropy(dataset)
        bestinfogain=0.0
        bestfeature=-1

        for i in xrange(numfeatures):
            uniquevals=set([data[i] for data in dataset])
            newentropy=0.0
            for value in uniquevals:
                subdataset=self.splitdataset(dataset,i,value)
                prob=len(subdataset)/float(len(dataset))
                newentropy+=prob*self.computeentropy(subdataset)
            infogain =baseentropy-newentropy
            if (infogain>bestinfogain):
                bestinfogain=infogain
                bestfeature=i
        return  bestfeature
    def computeentropy(self,dataset):
        datalen=float(len(dataset))
        catelist=[data[-1] for data in dataset]

        items=dict([(i,catelist.count(i))for i in catelist])
        infoentropy=0.0
        for key in items:
            prob=float(items[key])/datalen
            infoentropy-=prob*math.log(prob,2)
        return  infoentropy

    def splitdataset(self,dataset,axis ,value):
        rtnlist=[]
        for featvec in dataset:
            if featvec[axis]==value:
                rfeatvec=featvec[:axis]
                rfeatvec.extend(featvec[axis+1:])
                rtnlist.append(rfeatvec)
        return  rtnlist

    def predict(self,inputtree,featlabels,testvec):
        root=inputtree.keys()[0]
        seconddict=inputtree[root]
        featindex=featlabels.index(root)
        key=testvec[featindex]
        valueoffeat=seconddict[key]
        if isinstance(valueoffeat,dict):
            classlabel=self.predict(valueoffeat,featlabels,testvec)
        else:classlabel=valueoffeat
        return  classlabel
