'''
Created on Jun 17, 2016

@author: muditj
'''
import numpy as np
import string

def genDNA(length):
    '::type length: list(np.ndarray)'
    return np.random.choice(['A', 'T', 'C', 'G'], length)

if __name__ == '__main__':

    a = np.arange(6).reshape(2,3)
    a = genDNA(10)
    b = genDNA(30000000)
    '::type a: np.ndarray'
    '::type b: np.ndarray'
    c = np.lib.stride_tricks.as_strided(b, (len(b) - len(a) + 1, len(a)), (b.dtype.itemsize, )*2)

    d = c == a

    e = np.all(d, axis=1)
    f = [i for i in range(len(e)) if e[i] == True]
    print(f)

    print(''.join(a));
    print(b)

    print([b[f[i]:f[i] + len(a)] for i in range(len(f))])