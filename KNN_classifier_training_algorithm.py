# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:08:00 2018

@author: sampr
"""

import pandas as pd

def predict(value) :
    
    data = pd.read_table("fruit_data_set.txt")
    
    k = int(input("\nEnter the value of n_neighbours : "))

    X = data['mass']
    Y = data['fruit_name']
    
    cache = []
    uniqueList = []
    
    for i in X:
        absval = abs(value-i)
        cache.append(absval)

    for i in range(1,k):
        mval = cache.index(min(cache))
        maxval = max(cache)
        cache[mval] = maxval
    
        tempX = X[mval]
       
        num = X.index[X == tempX]
    
        for j in num:
            uniqueList.append(Y[j])
        
    uset = set(uniqueList)
    ulist = list(uset)
    print(uset)
    number = []
    
    for item in uset:
        number.append(uniqueList.count(item))
        
    max_index = number.index(max(number))
    print(number)
    
    print("The Predicted fruit : " + ulist[max_index])
    

def main() :
    
    x = int(input("Enter a value to predict : "))
    
    predict(x)
                

if __name__ == "__main__": 
    main() 

