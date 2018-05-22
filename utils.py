'''
Module used to define the utilities required
'''
import math
import pandas
import numpy


def euclidean_distance(vector_1,vector_2):
    '''
    calculates the euclidean distance between two vectors
    '''
    result=0.0
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
         for v1,v2 in zip(vector_1,vector_2):
            result+=(v1-v2)**2
    else:
       raise ValueError
    return math.sqrt(result)




def test_case():
    vec1=[1,2,3,5,6]
    vec2=[3,12,3,4,5]
    expected_answer="10.29563"
    #print euclidean_distance(vec1,vec2)
    vec1=tuple(vec1)
    vec2=tuple(vec2)
    #print euclidean_distance(vec1,vec2)
    import numpy
    vec1=numpy.array(vec1)
    vec2=numpy.array(vec2)
    #print euclidean_distance(vec1,vec2)
    import pandas
    vec1=pandas.DataFrame(vec1)
    vec2=pandas.DataFrame(vec2)
    #print vec1.shape
    #print euclidean_distance(vec1,vec2)
    

test_case()   
