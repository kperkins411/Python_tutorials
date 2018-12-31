import math
class LR(object):
    '''
    Base class, returns a single cycle of learning rates
    '''
    def __call__(self, *args, **kwargs):
        return self.getLRs()

    def getLRs(self,numb_iterations,max_lr, min_lr):
        '''
        :param numb_iterations: number total samples
        :param max_lr: upper
        :param min_lr: lower
        :return: list of learning rates, numb_iterations long
        '''
        raise NotImplementedError

class TriangularLR(LR):
    def _getStepSize(self,numb_iterations):
        '''
        step size is defined as 1/2 of the total cycle
        :param numb_iterations:
        :return:
        '''
        return numb_iterations // 2

    def getLRs(self, numb_iterations, max_lr, min_lr):
        # determines the halfway point
        step_size = self._getStepSize(numb_iterations)
        data = []
        for itr in range(numb_iterations):
            cycle = math.floor(1 + itr / (2 * step_size))
            x = abs(itr / step_size - 2 * cycle + 1)
            lr = min_lr + (max_lr - min_lr) * max(0, (1 - x))
            data.append(lr)
        return data

class Linear_Increase(TriangularLR):
    def getStepSize(self, numb_iterations):
        return numb_iterations  # makes stepsize and numb_iterations equal, you get first half of triangular wave

class Linear_Decrease(TriangularLR):
    def getStepSize(self, numb_iterations):
        return numb_iterations  # makes stepsize and numb_iterations equal, you get first half of triangular wave

import matplotlib.pyplot as plt
def plot(lrs):
    # give plot a title
    plt.title("learning rates")

    # make axis labels
    plt.xlabel("sample")
    plt.ylabel("learning rate")

    plt.scatter(range(len(lrs)), lrs)
    plt.show()

if __name__ == '__main__':
    li = Linear_Increase()
    # ld = Linear_Decrease()

    lrs = ld.getLRs(100, 1.0, 0.1)
    plot(lrs)