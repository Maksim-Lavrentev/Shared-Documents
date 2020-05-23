# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10

@author: Maksim Lavrentev

---------------------------------------------------------

Interactive Rajesh's descendant's gender determination
in console.

"""

import rajesh

def get_int(s):
    userdata = input(s)
    if userdata == 'q':
        return None
    try:
        user_num = int(userdata)
        return user_num
    except ValueError:
        print()
        print("I need an integer to continue.")
        print(s)
        return(get_int(s))

def call_console():
    r = rajesh.rajesh_tree()

    print("Start determination of the gender of Rajesh's K-th descendant in N-th generation.")
    print()
    n = get_int("Enter int number of generation N or q to quit: ")
    if n!=None:
        k = get_int("Enter int number of descendant K or q to quit: ")
        if k!=None:
            print()
            try:
                print("The gender of {k}-th descendant in {n}-th generation is:".format(k=k,n=n),
                  r.c_search(n,k))
            except (ValueError, TypeError) as err:
                print(err)
                print()
                call_console()

call_console()
