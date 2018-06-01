
import numpy as np
import argparse

'''
HW03
My Name : Tingbin Huang 
Partner: Perez Joseph

'''


def getPrime(a,b):

    '''  
    Description : this function find all prime number beteen input parameter a and b 

    >>> getPrime(2,3) == [2]
    False
    
    >>> getPrime(1,10) == [2, 3, 5, 7]
    True
    
    '''  
    newList = []
    if a > b:                       # Testing if a > b 
        temp = a 
        a = b
        b = temp
    
    if b > 2:                       # any number that is less than 2 is NOT a prime number, so it starts testing for b > 2 
        if a < 0:                   # Testing if 'a' is a negative number
            a = 1       
        a = a + 1
        arr = np.array(range(a,b))  # make an np.array

        set_arr = set(arr)                # convert array to a set 
        newSet = set()                    # create new set naming 'newSet' 
        for p in range(a,b):
            for i in range(2,p):
                if p % i == 0 :                  
                    newSet.add(p)         # add non-prime number to 'newSet' 
        newList = list(set_arr - newSet)  # use the original set, set_arr, to minize 'newSet' to get all prime number, and put all prime number in a list       
        newList = sorted(newList)         # sort this list 
    return newList           


if __name__ == "__main__":
   
    import doctest
  
    #------------------------------------
    # creating parser

    parser = argparse.ArgumentParser()

    parser.add_argument('-x', type = int)
    parser.add_argument('-y', type = int)


    args = parser.parse_args()  


    x = args.x
    y = args.y

    #------------------------------------
    # calculate getPrime(x,y) and print answer

    answer = getPrime(x,y)

    if answer == []:
        print("\n\nPrime number between", x, " and ", y, ": None\n\n")
    else:

        print("\n\nPrime number between", x, " and ", y, ": ", answer,"\n\n")







