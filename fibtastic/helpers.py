"""
Author: Rick James
Date: 3-16-2015
Purpose: Rubicon ISE Interview
"""

def gen_fib(n):
    ret_list = [0]
    a, b = 0, 1
    for i in xrange(n):
        temp = a
        a = b
        b = temp + b
        ret_list.append(a)
    return ret_list
