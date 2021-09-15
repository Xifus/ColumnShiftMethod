# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:00:48 2021

@author: Xifu Sun
"""

import numpy as np
from SALib.sample import sobol_sequence

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
    if skip_value == None:
        skip_value = N
    sequence = sobol_sequence.sample(N + skip_value, 2 * k)[skip_value:, :] #generate base sample
    sequence_dict = {} #dict for saving shifted samples
    
    D = np.arange(0, 2 * k)
    D_arr = np.zeros((R, 2 * k))
    
    for i in range(R):
        D_temp = D.copy()
        np.random.shuffle(D_temp)
        
        while check_dup(D_temp, D_arr, k):
            np.random.shuffle(D_temp)
        
        D_arr[i, :] = D_temp
        
        sequence_dict[i] = sequence.T[D_temp].T
        
    return sequence_dict
        
        
def check_dup(D_temp, D_arr, k):
    #Check if Matrix A or Matrix B was already used
    
    if np.any([np.array_equal(D_temp[:k], row) for row in D_arr[:, :k]]):
        return True
    elif np.any([np.array_equal(D_temp[k:], row) for row in D_arr[:, k:]]):
        return True
    
    return False