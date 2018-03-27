from numpy import *
import operator
def createDataset():
     group=array([1.0,1.1],[1.0,1.0],[0,0],[0,0.1])
     labels=['A','A','B','B']
     return group,labels
def classify0(inx,dataSet,lables,k):
     dataSetSiz=dataSet.shape[0]
     diffMat=tile(inx,(dataSetSiz),1) -dataSet
     sqDiffMat=diffMat**2
     sqDistance=sqDiffMat.sum(axis=1)
     distance=sqDistance**0.5
     sortedDistIndicies=distance.argsort()
     classCount={}
     for i in range(k):
          votelabel=lables[sorted(sortedDistIndicies[i])]
          classCount[votelabel]=classCount.get((votelabel,0)+1)
     sortedClassCount=sorted((classCount.iteritems),key=operator.itemgetter(1),reverse=True)
     return sortedClassCount


