import numpy as np
from SALib.sample import sobol_sequence
import math

def Column_shift(N, k, R, skip_value = None):
    '''
    Parameters
    ----------
    N : Int
        Number of samples
    k : Int
        Number of parameters
    R : Int
        Number of replicates
    skip_value : Int, optional
        Number of samples to skip. The default is N.

    Returns
    -------
    sequence_dict : Dict
        Dictionary that contains shifted samples

    '''
    if R > math.factorial(2 * k) - 1:
        print('The number of replicates exceeds the limit. Possible number of replicates should be less than ' + str (math.factorial(2 * k)))
        
        return
    
    if skip_value == None:
        skip_value = N
        
    sequence = sobol_sequence.sample(N + skip_value, 2 * k)[skip_value:, :] #generate base sample
    sequence_dict = {} #dict for saving shifted samples
    
    D = np.arange(0, 2 * k)
    D_arr = np.zeros((R, 2 * k))
    
    for i in range(R):
        D_temp = D.copy()
        np.random.shuffle(D_temp)
        
        while np.any([np.array_equal(D_temp, row) for row in D_arr]):
            np.random.shuffle(D_temp)
        
        D_arr[i, :] = D_temp
        
        sequence_dict[i] = sequence.T[D_temp].T

    return sequence_dict