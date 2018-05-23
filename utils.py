'''
Module used to define the utilities required
'''
from __future__ import division
import math
from itertools import izip
import pandas
import numpy
from scipy.spatial.distance import minkowski,cosine

def prepare_data(vector_1,vector_2):
    '''
    checking and adhering to rules
    '''
    if type(vector_1) is type(vector_2) and len(list(vector_1))== len(list(vector_2)):
         if isinstance(vector_1,pandas.core.frame.DataFrame):
             if vector_1.shape[1]!=1 and vector_1.shape[0]==1:
                 vector_1=vector_1.values.tolist()[0]
             elif vector_1.shape[1]==1:
                 vector_1=vector_1.iloc[:,0].values.tolist()
         if isinstance(vector_2,pandas.core.frame.DataFrame): 
             if vector_2.shape[1]!=1 and vector_2.shape[0]==1:
                 vector_2=vector_2.values.tolist()[0]
             elif vector_2.shape[1]==1:
                 vector_2=vector_2.iloc[:,0].values.tolist()
         return vector_1,vector_2
    else:
       raise ValueError("Length or type different")
    

def euclidean_distance(vector_1,vector_2):
    '''
    calculates the euclidean distance between two vectors
    '''
    vector_1,vector_2=prepare_data(vector_1,vector_2)
    return math.sqrt(sum(math.pow(v1-v2,2) for v1,v2 in zip(vector_1,vector_2)))

def manhattan_distance(vector_1,vector_2):
    '''
    calculates manhattan similarity
    '''
    vector_1,vector_2=prepare_data(vector_1,vector_2)
    return sum(abs(v1-v2) for v1,v2 in zip(vector_1,vector_2))

def minkowski_distance(vector_1,vector_2,n_root):
    '''
    calculates minkowski distance
    '''
    vector_1,vector_2=prepare_data(vector_1,vector_2)
    if isinstance(n_root,int) and n_root>=1:
        return sum(math.pow(abs(v1-v2),n_root) for v1,v2 in zip(vector_1,vector_2))**(1/n_root)
    elif isinstance(n_root,str):
       try:
           n_root=int(n_root)
           return minkowski_distance(vector_1,vector_2,n_root)
       except ValueError:
           raise ValueError("nth root should be integer and greater than 0")
    else:
       raise ArithmeticError("nth root can not be Zero")

def cosine_similarity(vector_1,vector_2):
    '''
    calculates the cosine similarity
    '''
    vector_1,vector_2=prepare_data(vector_1,vector_2)
    numerator=sum(v1*v2 for v1,v2 in zip(vector_1,vector_2))
    denominator=reduce(lambda x,y:math.sqrt(x)*math.sqrt(y),map(lambda x: sum([i if x==0 else j for i,j in [ (v1**2,v2**2) for v1,v2 in zip(vector_1,vector_2)]]),(0,1)))
    dot_product = numpy.dot(vector_1, vector_2)
    norm_a = numpy.linalg.norm(vector_1)
    norm_b = numpy.linalg.norm(vector_2)
    return 1-(numerator/denominator)
    

def test_case():
    vec1=[1,2,3,5,6]
    vec2=[3,12,3,4,5]
    expected_eucliden=10.29563
    expected_manhattan=14
    
    print euclidean_distance(vec1,vec2)
    print manhattan_distance(vec1,vec2)
    print minkowski_distance(vec1,vec2,2)
    print minkowski_distance(vec1,vec2,1)
    vec1=tuple(vec1)
    vec2=tuple(vec2)
    print euclidean_distance(vec1,vec2)
    print manhattan_distance(vec1,vec2)
    print minkowski_distance(vec1,vec2,2)
    print minkowski_distance(vec1,vec2,1)
    vec1=numpy.array(vec1)
    vec2=numpy.array(vec2)
    print euclidean_distance(vec1,vec2)
    print manhattan_distance(vec1,vec2)
    print minkowski_distance(vec1,vec2,2)
    print minkowski_distance(vec1,vec2,1)
    vec1=pandas.DataFrame(vec1)
    vec2=pandas.DataFrame(vec2)
    print euclidean_distance(vec1,vec2)
    print manhattan_distance(vec1,vec2)
    print minkowski_distance(vec1,vec2,2)
    print minkowski_distance(vec1,vec2,1)
    print minkowski_distance(vec1,vec2,3)
    print minkowski_distance(vec1,vec2,4)
    print minkowski(vec1,vec2,3)
    print minkowski(vec1,vec2,4)
    print cosine_similarity(vec1,vec2)
    print cosine(vec1,vec2)


test_case()   
