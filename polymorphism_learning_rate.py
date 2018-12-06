import math
import numpy as np

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
    def getStepSize(self,numb_iterations):
        return numb_iterations // 2

    def getLRs(self, numb_iterations, max_lr, min_lr):
        # determines the halfway point
        step_size = self.getStepSize(numb_iterations)
        data = []
        for itr in range(numb_iterations):
            cycle = math.floor(1 + itr / (2 * step_size))
            x = abs(itr / step_size - 2 * cycle + 1)
            lr = max_lr + (max_lr - min_lr) * max(0, (1 - x))
            data.append(lr)
        return data

class TriangularLR_LRFinder(TriangularLR):
    def getStepSize(self,numb_iterations):
        return numb_iterations #makes stepsize and numb_iterations equal, you get first half of triangular wave

class CosignLR(LR):
    def getLRs(self, numb_iterations, max_lr, min_lr):
        '''
        Cosign that starts at max_lr and decreases to min_lr
        '''
        scale = 2 / (max_lr - min_lr)

        # then translate so ranges between low_lr and high_lr
        data = (np.cos(np.linspace(0, np.pi, numb_iterations)) /
                scale) + (max_lr - min_lr) / 2 + min_lr
        return data
#-----------------------------------------
#visual test
import matplotlib.pyplot as plt

numb_iterations=250
max_lr=2
min_lr=1

class DisplayLR(object):
    def __init__(self, LR):
        self.LR = LR

    def __call__(self):
        self.print()

    def print(self, mult=1):
        lrs = self.LR.getLRs(numb_iterations*mult,max_lr, min_lr)
        plt.plot(lrs)
        plt.show()

tlr = TriangularLR()
ob1 = DisplayLR(tlr)
ob1.print()
tlr.numb_iterations = numb_iterations*2
ob1.print(2)

tlr = TriangularLR_LRFinder()
ob1 = DisplayLR(tlr)
ob1.print()
tlr.numb_iterations = numb_iterations*2
ob1.print(2)

tlr = CosignLR()
ob1 = DisplayLR(tlr)
ob1.print()
tlr.numb_iterations = numb_iterations*2
ob1.print(2)

ob3 = DisplayLR(CosignLR())
ob3.print()