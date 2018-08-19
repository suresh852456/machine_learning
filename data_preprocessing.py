import pandas
import numpy
from numpy import ndarray
from pandas import Series,DataFrame


def convert_datatype(data, conversion_type = "array"):

    available_types = [list, tuple, dict, DataFrame, Series, ndarray]
    string_types = ["list", "tuple", "dict", "DataFrame", "Series", "array"]
    val=available_types[string_types.index(conversion_type)]
    if isinstance(data,val):
        return data
    elif isinstance(data,dict):
        if conversion_type == "list" or conversion_type == "tuple":
            return val(data.values())
        elif conversion_type == "DataFrame" or conversion_type == "array" :
            if conversion_type == "array":
                return val(list(data.values()))
            for key in data.keys():
                temp = data[key]
                data[key] = [temp]
    elif isinstance(data,DataFrame):
        if conversion_type == "array":
            return data.values
    if conversion_type == "dict":
        keys=range(len(data))
        if isinstance(data,(list,tuple)):
            return {key:value for key,value in zip(keys,data)}
        else:
            return convert_datatype(convert_datatype(data,"list"),"dict")
    elif conversion_type == "Series" and isinstance(data,DataFrame):
        return data.iloc[0,:]
    if isinstance(data,tuple):
        data = list(data)
    return val(data)
