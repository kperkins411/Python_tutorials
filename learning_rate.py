'''
calculates triangular learning rates
'''
import math
import matplotlib.pyplot as plt
import numpy as np

stepsize = 250
maxLR=2
minLR=1

def getTriangularLRs(*,return_half_step):
    return



def getTriangularLRs(numb_iterations, max_lr, min_lr, return_half_step=False):
    '''
    returns a single tooth /\ of a sawtooth wave that varies from min_lr to max_lr
   :param numb_iterations:  total learning_rates to generate, make an even number so stepsize will be 1/2 of it
    :param max_lr:
    :param min_lr:
    :param  step_size =None  used for learning rate finder do several epochs, with increasing LRs
            to determine appropriate range
    :return: list of learning rates
    '''
    data = []
    # set stepsize == numb_iterations (1/2 sawtooth) for calculating appropriate Learning rate range
    stepsize = numb_iterations
    if return_half_step == False:
        stepsize = numb_iterations // 2

    for itr in range(numb_iterations):
        cycle = math.floor(1 + itr / (2 * stepsize))
        x = abs(itr / stepsize - 2 * cycle + 1)
        lr = max_lr + (max_lr - min_lr) * max(0, (1 - x))
        data.append(lr)
    return data


def getCosignLRs(numb_iterations, max_lr, min_lr):
    '''
    generates a list of max_iter_per_cycle learning rates that starts at max_lr and descends
    to base_lr in a cosign wave
    max_iter_per_cycle changes according to schedule in epochs_per_cycle_schedule
    :param numb_iterations:  total learning_rates to generate, make an even number so stepsize will be 1/2 of it
    :param max_lr:
    :param min_lr:
     :return: list of learning rates
    '''
    # cosign varies between 1 and -1 (sweep of 2), factor to scale between lowlr and high_lr
    scale = 2 / (max_lr - min_lr)

    # then translate so ranges between low_lr and high_lr
    data = (np.cos(np.linspace(0, np.pi, numb_iterations)) / scale) + (max_lr - min_lr) / 2 + min_lr
    return data

class TestObj(object):

    RESTART_CYCLE = 0
    def __init__(self,  base_lr=1e-3, max_lr=6e-3,
                 batch_size = 64, numb_images= 5011,
                 epochs_per_cycle_schedule = [1,1,2,2,3], make_last_cycle_base_lr = True,*, lr_fun = getCosignLRs, calculate_LR = False ):
        '''
        :param optimizer:  optimizer, used primarily for applying learning rate to params
        :param base_lr:  the minimum learning rate
        :param max_lr:  the maximum learning rate
        :param batch_size:
        :param numb_images:
        :param epochs_per_cycle_schedule: this should sum to total number of epochs or your last epoch has lr somewhere
         between max_lr and base_lr
        :param make_last_cycle_base_lr if last cycle should have all learning rates = base_lr
        '''

        self.lr_fun = lr_fun

        #how many iterations per epoch
        self.max_iter_per_cycle = numb_images // batch_size

        # if [1,2,3] then first cosign descent occurs over 1 epoch,
        # second over 2 epochs, 3rd over 3 epochs for a total of 6 epochs
        #any after that are over 3 epochs
        self.epochs_per_cycle_schedule = epochs_per_cycle_schedule
        self.epochs_per_cycle_schedule_loc = 0

        self.base_lr = base_lr
        self.max_lr = max_lr

        #gradually reduce max_lr
        numb_cycles = len(self.epochs_per_cycle_schedule)

        if (make_last_cycle_base_lr == True):
            numb_cycles -=1    #will make the last cycle equal to the base learning rate

        self.max_lr_reducer = (self.max_lr - self.base_lr) /numb_cycles

        self.batch_size = batch_size
        self.numb_images = numb_images

        # covers the last partial batch
        self.pad = 1 if numb_images % self.batch_size > 0 else 0

        #start at 0
        self.current_iteration = TestObj.RESTART_CYCLE
        self.loc = TestObj.RESTART_CYCLE
        self._calculate_learning_rate=calculate_LR

    def _getNumberIterations(self):
        '''
        how many batches for this cycle
        if 1 epochs per cycle, then LRs contains numb batches   values from max_lr to base LR
        if 2 epochs per cycle, then LRs contains numb batches*2 values from max_lr to base LR
        :return:
        '''

        #how many epochs per cosign cycle
        multiplier = self.epochs_per_cycle_schedule[self.epochs_per_cycle_schedule_loc]
        self.epochs_per_cycle_schedule_loc+=1   #go to the next one

        return (self.numb_images//self.batch_size)*multiplier + self.pad

    def _getMaxLearningRate(self):
        '''
        reduce the max learning rate after each complete cosign cycle
        :return:
        '''
        return self.max_lr- self.epochs_per_cycle_schedule_loc* self.max_lr_reducer

    def _calculate_learning_rate_range(self):
        '''
        generates a list of max_iter_per_cycle learning rates that starts at max_lr and descends
        to base_lr in a cosign wave
        max_iter_per_cycle changes according to schedule in epochs_per_cycle_schedule
        '''

        #gradually reduce the learning rate
        maxlr = self._getMaxLearningRate()

        # then translate so ranges between low_lr and high_lr

        self.vals = self.lr_fun(self.max_iter_per_cycle,self.max_lr, self.base_lr, return_half_step = self._calculate_learning_rate)

    def _get_lr(self):
        # time to go to the next cycle length?
        if (self.loc == TestObj.RESTART_CYCLE):
            if (self.epochs_per_cycle_schedule_loc < len(self.epochs_per_cycle_schedule)):
                self._calculate_learning_rate_range()
                print(f"   number vals {len(self.vals)}")
            else:
                #just return the lowest learning rate
                self.loc=len(self.epochs_per_cycle_schedule)-1
                # raise (IndexError,"finished all epochs_per_cycle_schedule entries")

        lrs=[]
        lrs.append(self.vals[self.loc])

        self.writer('cosann', lrs[0])

        #set up for next time, either the next learning rate or restart
        self.loc +=1
        if (self.loc ==len(self.vals)):
            self.loc = TestObj.RESTART_CYCLE

        return lrs

    def batch_step(self):
         for param_group, lr in zip(self.optimizer.param_groups, self._get_lr()):
            param_group['lr'] = lr

    def setWriter(self, writer):
         '''
         for tensorboard1
         :param writer:
         :return:
         '''
         self.writer.setWriter(writer)
myObj = TestObj(lr_fun = getTriangularLRs)
myObj._calculate_learning_rate=True
myObj._calculate_learning_rate_range()
lrs = myObj.vals




# lrs = getTriangularLRs(stepsize, stepsize, 2,1)
# lrs1 = [(i,j)for i,j in enumerate(lrs)]
# give plot a title
plt.title("triangular learning rate")

# make axis labels
plt.xlabel("cycle")
plt.ylabel("lr")

# data = zip(*data)
# x,y = zip(*lrs)

# lrs = [1,2,4,8]
plt.plot(lrs)

plt.show()