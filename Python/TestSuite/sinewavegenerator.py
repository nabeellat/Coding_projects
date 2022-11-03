
"""function to create a sin wave based on a give sampling rate, frequency.."""
import numpy as np
def sinewave(sampling_rate,frequncy,n,inputs):
    epsilon = 1/sampling_rate
    sinewave = []
    for i in range(0, inputs):
    for i in range(0,frequncy):
        sinewave.append(np.sin(2*np.pi*frequncy*n*epsilon))
    return sinewave
main
