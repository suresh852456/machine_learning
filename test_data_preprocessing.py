import unittest
from data_preprocessing import convert_datatype as cd
import numpy as np
import pandas as pd
from pandas import Series

class test_processing(unittest.TestCase):

    def test_lists(self):
        assert isinstance(cd([1,2,3],"list"),list)
        assert isinstance(cd((1,2,3),"list"),list)
        assert isinstance(cd(pd.Series([1,2,3]),"list"),list)
        assert isinstance(cd({'0':1,'1':2,'2':3},"list"),list)
        assert isinstance(cd(pd.DataFrame([1,2,3]),"list"),list)
        assert isinstance(cd(pd.DataFrame([[1,2,3],[3,4,5]]),"list"),list)
        assert isinstance(cd(np.array([1,2,3]),"list"),list)
        assert isinstance(cd(np.array([[1,2,3],[3,4,5]]),"list"),list)

    def test_tuples(self):
        assert isinstance(cd([1,2,3],"tuple"),tuple)
        assert isinstance(cd((1,2,3),"tuple"),tuple)
        assert isinstance(cd(Series([1,2,3]),"tuple"),tuple)
        assert isinstance(cd({'0':1,'1':2,'2':3},"tuple"),tuple)
        assert isinstance(cd(pd.DataFrame([1,2,3]),"tuple"),tuple)
        assert isinstance(cd(pd.DataFrame([[1,2,3],[3,4,5]]),"tuple"),tuple)
        assert isinstance(cd(np.array([1,2,3]),"tuple"),tuple)
        assert isinstance(cd(np.array([[1,2,3],[3,4,5]]),"tuple"),tuple)

    def test_series(self):
        assert isinstance(cd([1,2,3],"Series"),Series)
        assert isinstance(cd((1,2,3),"Series"),Series)
        assert isinstance(cd(Series([1,2,3]),"Series"),Series)
        assert isinstance(cd({'0':1,'1':2,'2':3},"Series"),Series)
        assert isinstance(cd(pd.DataFrame([1,2,3]),"Series"),Series)
        assert isinstance(cd(np.array([1,2,3]),"Series"),Series)

    def test_dicts(self):
        assert isinstance(cd([1,2,3],"dict"),dict)
        assert isinstance(cd((1,2,3),"dict"),dict)
        assert isinstance(cd(Series([1,2,3]),"dict"),dict)
        assert isinstance(cd({'0':1,'1':2,'2':3},"dict"),dict)
        assert isinstance(cd(pd.DataFrame([1,2,3]),"dict"),dict)
        assert isinstance(cd(pd.DataFrame([[1,2,3],[3,4,5]]),"dict"),dict)
        assert isinstance(cd(np.array([1,2,3]),"dict"),dict)
        assert isinstance(cd(np.array([[1,2,3],[3,4,5]]),"dict"),dict)
    def test_dataframe(self):
        assert isinstance(cd([1,2,3],"DataFrame"),pd.core.frame.DataFrame)
        assert isinstance(cd((1,2,3),"DataFrame"),pd.core.frame.DataFrame)
        assert isinstance(cd(Series([1,2,3]),"DataFrame"),pd.core.frame.DataFrame)
        assert isinstance(cd({'0':1,'1':2,'2':3},"DataFrame"),pd.core.frame.DataFrame)
        assert isinstance(cd(pd.DataFrame([1,2,3]),"DataFrame"),pd.core.frame.DataFrame)
        assert isinstance(cd(pd.DataFrame([[1,2,3],[3,4,5]]),"DataFrame"),pd.core.frame.DataFrame)
        assert isinstance(cd(np.array([1,2,3]),"DataFrame"),pd.core.frame.DataFrame)
        assert isinstance(cd(np.array([[1,2,3],[3,4,5]]),"DataFrame"),pd.core.frame.DataFrame)

    def test_ndarray(self):
        assert isinstance(cd([1,2,3],"array"),np.ndarray)
        assert isinstance(cd((1,2,3),"array"),np.ndarray)
        assert isinstance(cd(Series([1,2,3]),"array"),np.ndarray)
        assert isinstance(cd({'0':1,'1':2,'2':3},"array"),np.ndarray)
        assert isinstance(cd(pd.DataFrame([1,2,3]),"array"),np.ndarray)
        assert isinstance(cd(pd.DataFrame([[1,2,3],[3,4,5]]),"array"),np.ndarray)
        assert isinstance(cd(np.array([1,2,3]),"array"),np.ndarray)
        assert isinstance(cd(np.array([[1,2,3],[3,4,5]]),"array"),np.ndarray)


if __name__ == "__main__":
    unittest.main()
