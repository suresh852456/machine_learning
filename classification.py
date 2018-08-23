

class tree(object):
    def __init__(self):
        self.children = []

    def __iterate_childrens(self):
        for children in self.children:
            children.__iterate_childrens()

    def create_tree(self):
        pass

    def train(self):
        pass

    def test(self):
        pass



class random_forest(tree)
def random_forest(x, y):
    pass

def c45(x,y):
    pass
