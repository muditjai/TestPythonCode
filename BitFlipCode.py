'''
Created on Jun 26, 2016

@author: muditj
'''

import numpy as np
import matplotlib.pyplot as plt
import os
import random

if __name__ == '__main__':
    if not os.path.isfile("Binary.txt") or True:
        num_size = 20
        random.choice()
        a = np.random.choice(['0', '1'], num_size)
        print(a)
        f = open("Binary.txt", 'w')
        '::type f: file'
        f.write(str(a))
        f.close()
    
    
    with open("Binary.txt", 'r') as f:
        a = f.read();
        a = a.strip('[]').replace("'", '').split(' ')
    

    h = np.asarray([0 if x == '0' else 1 for x in a])
    c = ['g' if x == 0 else 'b' for x in h]
    print(h)

    max_count = 0
    max_i = 0
    cur_i = 0
    prev_zero_i = 0
    prevprev_zero_i = 0
    
    for i in range(len(h)):  
        cur_i += 1
        if h[i] == 0:
            if max_count < cur_i - prevprev_zero_i - 1:
                max_count = cur_i - prevprev_zero_i - 1
                max_i = prev_zero_i
                
            prevprev_zero_i = prev_zero_i
            prev_zero_i = cur_i
            
    if max_count < cur_i - prevprev_zero_i - 1:
        max_count = cur_i - prevprev_zero_i - 1
        max_i = prev_zero_i
        
    c[max_i-1] = 'r'
    plt.bar(np.arange(len(h)), h+0.5, color=c)
    
    plt.show()
    
    