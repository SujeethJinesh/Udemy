import tensorflow as tf
import numpy as np

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x, *args, **kwargs):
        return x


#set a random seed to make it easier to get consistent runs
np.random.seed(0)

#want to load data from .npz file
data = np.load('data_with_labels.npz')
train = data['arr_0']/255. #contains pixel data normalized from 0 to 1
labels = data['arr_1'] #holds type of font it was

print(train[0])
print(labels[0])

import matplotlib.pyplot as plt
plt.ion() #automatically bring up figures when needed

#display a data from each font on graph
f, plts = plt.subplots(5, sharex=True)
c = 91
for i in range(5):
    plts[i].pcolor(train[c + i * 558],
                   cmap=plt.cm.gray_r)

def to_onehot(labels, nclasses=5):
    '''
    Convert labels to "one-hot" format.
    >>> a = [0,1,2,3]
    >>> to_onehot(a,5)
    array([[ 1.,  0.,  0.,  0.,  0.],
           [ 0.,  1.,  0.,  0.,  0.],
           [ 0.,  0.,  1.,  0.,  0.],
           [ 0.,  0.,  0.,  1.,  0.]])
    '''
    outlabels = np.zeros(len(labels), nclasses) #creates 2d array
    for i,l in enumerate(labels):
        outlabels[i,l] = 1
    return outlabels

onehot = to_onehot(labels)



