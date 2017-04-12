#-*- coding:  utf-8 -*-

import  numpy as np
from  numpy import  *

def  loadDataSet():
    postingList=[['my','dog','has','flea','prolems','help','please'],
                 ['maybe','not','take','him','to','dog','park','stupid'],
                 ['my','dalmation','is','so','cute','I','love','him','my'],
                 ['stop','posting','stupid','worthless','garbage'],
                 ['mr','licks','ate','my','steak','how','to','stop','him'],
                 ['quit','buying','worthless','dog','food','stupid']]
    classVec=['b', 'a', 'b', 'a', 'b', 'a']
    return  postingList,classVec

class NBayes(object):
    def _init_(self):
        self.vocabulary=[]
        self.idf=0
        self.tf=0
        self.tdm=0
        self.labels=[]
        self.doclength = 0
        self.lableltemps=0
        self.vocablen=0
        self.testset=0
        self.pyi

    def train_set(self,trainset,classVec):
        self.cate_prob(classVec)
        self.doclength=len(trainset)
        tempset =set()
        [tempset.add(word) for doc in trainset for word in doc]
        self.vocabulary=list(tempset)
        self.vocablen=len(self.vocabulary)
        self.calc_tfidf(trainset)
        #self.calc_wordfreq(trainset)
        self.build_tdm()

    def cate_prob(self,classVec):
        self.labels=classVec
        self.lableltemps=list(set(self.labels))
        self.pyi=[0.0]*len(self.lableltemps)
        for lableltemp in self.lableltemps:
            #lab=self.lableltemps.index(lableltemp)
            #fl=float(self.labels.count(lableltemp))/float(len(self.labels))
            self.pyi[self.lableltemps.index(lableltemp)] = float(self.labels.count(lableltemp))/float(len(self.labels))

    #def calc_wordfreq(self,trainset):
     #   self.idf=np.zeros([1,self.vocablen])
      #  self.tf =np.zeros([self.doclength,self.vocablen])
       # for indx in xrange(self.doclength):
        #    for word in trainset[indx]:
         #       self.tf[indx,self.vocabulary.index(word)]+=1
          #  for signleword in set(trainset[indx]):
           #     self.idf[0,self.vocabulary.index(signleword)]+=1

    def calc_tfidf(self,trainset):
        self.idf=np.zeros([1,self.vocablen])
        self.tf=np.zeros([self.doclength,self.vocablen])
        for indx in xrange(self.doclength):
            for word in trainset[indx]:
                self.tf[indx,self.vocabulary.index(word)]+=1
            self.tf[indx]=self.tf[indx]/float(len(trainset[indx]))
            for signleword in set(trainset[indx]):
                self.idf[0,self.vocabulary.index(signleword)]+=1
        self.idf=np.log(float(self.doclength)/self.idf)
        self.tf =np.multiply(self.tf,self.idf)

    def build_tdm(self):
        self.tdm=np.zeros([len(self.lableltemps),self.vocablen])
        sumlist=np.zeros([len(self.lableltemps),1])
        for indx in xrange(self.doclength):
            self.tdm[self.lableltemps.index(self.labels[indx])]+=self.tf[indx]
            sumlist[self.lableltemps.index(self.labels[indx])]=np.sum(self.tdm[self.lableltemps.index(self.labels[indx])])
        self.tdm=self.tdm/sumlist

    def  map2vocab(self,testdata):
        self.testset=np.zeros([1,self.vocablen])
        for word in testdata:
            self.testset[0,self.vocabulary.index(word)]+=1

    def predict(self,testset):
        if np.shape(testset)[1]!=self.vocablen:
            print ("print error")
            exit(0)
        predvalue =0
        predclass =""
        for tdm_vect,keyclass in zip(self.tdm,self.lableltemps):
            temp =np.sum(testset*tdm_vect*self.pyi[self.lableltemps.index(keyclass)])
            if temp>predvalue:
                predvalue=temp
                predclass=keyclass
        return  predclass
