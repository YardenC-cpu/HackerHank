'''
Sherlock and the Beast, taken from HackerRank. See the harder version of it in the 3sum question) 
Source: https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem

Description:
We are given a number and a set of rules and we need to determine rather the given
number is a "decent" one. 
A Decent Number has the following properties:
    Its digits can only be 3's and/or 5's.
    The number of 3's it contains is divisible by 5.
    The number of 5's it contains is divisible by 3.
    It is the largest such number for its length.


Explanation:
If we think about it, it is a math problem! we see the usage in the modulo 
and the prompt for the problem indicate that the solution will be computed 
and that the solution shouldn't be complicated. 
My approach:
    If we divide any number by 3, the modulo that we can get must be smaller then 
    the divisioner -> that means that we can get either 0, 1, 2
    *if we get 0: the number is divisiable 
    *if we get 1: then we need to subtract 5 from it twice 
        13%3=1, 13-5=8, 8-5=3
    *if we get 2: then we need to subtract 5 from it once
        14%3=2, 15-5=9
    So, we know that each time that our %3!=0 we need to subtract 5 from it.
    Since this number will eventuall give me the number that is divisiable by 3, 
    we can subtract it from the number given to get the number that is divisiable by 5
    (unless it is smaller then 0 and then we need to return -1)
'''


def sherlockBeast(n):

    three_division = n 

    while three_division%3 !=0:
        three_division -= 5
    
    if three_division <0:
        print(-1)
    else:
        print('5'*(three_division)+'3'*(n-three_division))

print(sherlockBeast(11))