# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10

@author: Maksim Lavrentev

---------------------------------------------------------

Use rajesh_tree().c_search(n, k) for *cyclical* search of
a k-th child's gender in n-th genration

Use rajesh_tree().r_search(n, k) for *recursive* search of
a k-th child's gender in n-th genration

Recursive search might not finish due to recursion limit
if n is too high.

"""

#increase limit for recursion loop
import sys
sys.setrecursionlimit(10000)

class rajesh_tree:
    
    def __init__(self, r_gender = "M"):
        #check gender correctness in input
        if r_gender not in ["M","F"]:
            raise TypeError("Input Error: r_gender must be str: 'M' or 'F'")
        
        self.r_gender = r_gender

    def check_input(self, n, k):
        #check inputs on errors
        
        if type(k) != int or type(n) != int:
            raise TypeError("Input Error: n and k must be int")
        if n < 1 or n > 10**4:
            raise ValueError("Input Error: n must be between 1 and 10^4")
        if k < 1 or k > min(10**15,2**(n-1)):
            raise ValueError("Input Error: k must be between 1 and min(10^15,2^(n-1))")

    def c_search(self, n, k):
        #cyclical child's gender search
        #returns gender of the k-th descendant of n-th genetration
        #after input check done by srch_gen_n_k function
        
        #n - num of generation to search
        #nn - num of current generation in loop (is altered in cycle)
        #k - num of descendant in the generation (is altered in cycle)
        #p_gender - parent's gender (Rajesh's line) (is altered in cycle)
        
        #c_gender - children's gender
        #c_k - alteration of k
        
        #check input on errors
        self.check_input(n, k)
        
        #start search 
        nn = 1
        p_gender = self.r_gender
        
        while nn < n:
            if p_gender == "M":
                c_genders = ("M","F")
            else:
                c_genders = ("F","M")
            
            #key is used to split the gender sequence of the generation in 2
            key = 2**(n-1-nn)
            
            if k <= key:
                c_gender = c_genders[0]
                c_k = k
            else:
                c_gender = c_genders[1]
                c_k = k - key
            
            p_gender = c_gender
            k = c_k
            nn += 1
        
        return p_gender

    def r_search(self, n, k):
        #recursive search
        #returns gender of the k-th descendant of n-th genetration
        
        #might not work with n>=2950 due to recursion limit
        
        #check input on errors
        self.check_input(n, k)
        
        #call search 
        return self._r_search(n, 1, k, self.r_gender)

    def _r_search(self, n, nn, k, p_gender):
        #recursive child's gender search
        #returns gender of the k-th descendant of n-th genetration
        #after input check done by srch_gen_n_k function
        
        #n - num of generation to search
        #nn - num of current generation in loop (is altered in recursion)
        #k - num of descendant in the generation (is altered in recursion)
        #p_gender - parent's gender (Rajesh's line) (is altered in recursion)

        #c_gender - children's gender
        #c_k - alteration of k
        #c_nn - alteration of nn
        
        if nn == n:
            return p_gender
        
        if p_gender == "M":
            c_genders = ("M","F")
        else:
            c_genders = ("F","M")
        
        #key is used to split the gender sequence of the generation in 2
        key = 2**(n-1-nn)
        
        if k <= key:
            c_gender = c_genders[0]
            c_k = k
        else:
            c_gender = c_genders[1]
            c_k = k - key
        
        c_nn = nn + 1
        return self._r_search(n, c_nn, c_k, c_gender)