from abc import ABC, abstractmethod
class base_ml(ABC):

    def confusion_matrix(self, *args):
        pass

    def precision(self, *args):
        pass

    def recall(self, *args):
        pass

    def logarithmic_loss(self, *args):
        pass

    def cross_validation_score(self, *args):
        pass

    def ROC_area(self, *args):
        pass

    def classification_report(self, *args):
        pass

    def mean_abs_error(self, *args):
        pass

    def mse(self, *args):
        pass

    def abs_error(self, *args):
        pass

    def r_squared(self, *args):
        pass

    @abstractmethod
    def train(self, *args):
        pass

    @abstractmethod
    def test(self, *args):
        pass
