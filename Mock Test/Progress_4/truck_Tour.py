  #!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    
    n = len(petrolpumps)  #Size of matrix (double array)
    petrolRemain = 0      #variable to store remaining of petrol 
    stat = 0
        
    for i in range(n):
        petrol = petrolpumps[i][0];     # get petrol value from matrix
        distance = petrolpumps[i][1];   # get distance value from matrix
        petrolRemain += petrol - distance
            
    #check if remaining petrol is empty, reset the counter, and start from the next pumpstation
        if petrolRemain < 0:
            stat = i+1;
            petrolRemain = 0;
    return stat;

if __name__ == '__main__':
