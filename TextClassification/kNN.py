#-*- coding: utf-8 -*-

from  numpy import  *
import  operator
from  Nbyayes_lib import  *


def cosdist(vectors1,vectors2):
    return  dot(vectors1,vectors2)/(linalg.norm(vectors1)*linalg.norm(vectors2))

def classify(testdata,trainSet,listClasses,k):
    dataSetSize=trainSet.shape[0]
    distances=array(zeros(dataSetSize))
    for indx in xrange(dataSetSize):
        distances[indx]=cosdist(testdata,trainSet[indx])
    sortedDistIndicies=argsort(-distances)
    classCount={}
    for i in range(k):
        voteIlabel=listClasses[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1

    sortedClassCount=sorted(classCount.iteritems(),
                            key=operator.itemgetter(1),reverse=True)
    return  sortedClassCount[0][0]

