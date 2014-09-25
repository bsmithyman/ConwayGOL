import numpy as np

DEFAULT_SHAPE   = (5, 5)
DEFAULT_NONZERO = [[1,  2], [2, 2], [3, 2]]

class Conway (object):

    def __init__ (self, initcond = None):

        if initcond is None:
            initcond = np.zeros(DEFAULT_SHAPE)
            for loc in DEFAULT_NONZERO:
                initcond[loc[0], loc[1]] = 1

        self.initcond = initcond.copy()
        self.dims = initcond.shape
        self.state = initcond.copy()

    def _evolve (self):

        neighbours = -self.state

        for i in xrange(self.dims[0]):
            for j in xrange(self.dims[1]):
                neighbours[i,j] += self.state[i-1:i+2, j-1:j+2].sum()

        self.state = 1 * (((neighbours > 1) * (neighbours < 4) * self.state + (neighbours == 3)) > 0)

    def __call__ (self):

        self._evolve()
        return self.state