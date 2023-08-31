#!/usr/bin/python
'''Given a pile of coins of different values, 
  determine the fewest number of coins needed to meet
  a given amount total.
'''
import sys

def makeChange(coins, total):
    '''
    Return fewest number of coins to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    '''
    if total <= 0:
      return 0
    else:
      from math import trunc

coins = sorted(coins, reverse=True)
coin_dict = {}
while total is not None:
  for c in coins:
    if total % c == o:
        coin_dict[c] = total / c
      return(int(sum(coins_dict.values())))
    else:
        coin_dict[c] = trunc(total / float(c))
        total -= (c * coin_dict[c])
return -1
