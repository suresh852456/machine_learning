'''
Module used to define the utilities required
'''
from __future__ import division,print_function
import math
try:
    from itertools import izip
except ImportError:
    from functools import reduce

import numpy
import pandas
from scipy.spatial.distance import minkowski,cosine

from data_preprocessing import prepare_data


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

def cosine_similarity(vector_1,vector_2,distance=False):
    '''
    calculates the cosine similarity
    '''
    vector_1,vector_2=prepare_data(vector_1,vector_2)
    numerator=sum(v1*v2 for v1,v2 in zip(vector_1,vector_2))
    denominator=reduce(lambda x,y:math.sqrt(x)*math.sqrt(y),map(lambda x: sum([i if x==0 else j for i,j in [ (v1**2,v2**2) for v1,v2 in zip(vector_1,vector_2)]]),(0,1)))
    if distance:
        return 1-(numerator/denominator)
    else:
        return numerator/denominator
