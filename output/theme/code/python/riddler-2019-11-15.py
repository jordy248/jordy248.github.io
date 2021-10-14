# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:37:54 2019

@author: NelsonJ
"""

from random import seed, choice
from statistics import mean

##### ------ #####
##### ------ #####
##### config #####
##### ------ #####
##### ------ #####
seed(42)

def roll_die(sides=10):
    result = choice(range(0, sides))
    
    return(result)
    
def update_score(score=None):    
    if score is None:
        score = 0.
    
    # roll and get results
    new_roll = roll_die(sides=10)
    
    # end the game if new_roll = 0
    if new_roll in [0, 9]:
        return(float(repr(score) + repr(new_roll)))
    else:
        # get last digit of current score
        score_last_digit = int(repr(score)[-1])
        
        # if new_roll is greater than last digit of current score, update it
        if score_last_digit == 0:
            return(update_score(score = new_roll / 10))
        elif new_roll > score_last_digit:
            return(update_score(score = float(repr(score) + repr(new_roll))))
        else:
            return(update_score(score = score))

test_results = [update_score() for _ in range(int(1e6))]
mean(test_results)

    
(0 * .1) + \
 (.9 * .1) + \
 ((.80 * .5 + .89 * .5) * .1) + \
 ((.70 * (1/3) + .78 * (1/3) + .79 * (1/3)) * .1) + \
 ((.60 * .25 + .67 * .25 + .68 * .25 + .69 * .25) * .1) + \
 ((.50 * .2 + .56 * .2 + .57 * .2 + .58 * .2 + .59 * .2) * .1) + \
 ((.40 * (1/6) + .45 * (1/6) + .46 * (1/6) + .47 * .2 + .48 * .2 + .49 * .2) * .1) + \



sides = 10
running_total = 0

for i in range(0, sides):
    curr_total = 0
    
    for j in range(i, sides):
        print(j)
    print('\n')

total = 0

for i in reversed(range(0 + 1, sides)):
    curr_tot = ['0' + '.' + str(i)]
    curr_opts = [opt for opt in range(i + 1, sides)]
    
    
    for j in range(len(curr_opts)):
        curr_tot = curr_total
        curr_tots.append(str(curr_tot) + str(curr_opts[j]))
        
        curr_js = curr_opts[j:]
        
        for k in 
        
        for k in curr_opts[j:]:
            curr_tots.append(str(curr_tot) + str(k))
        print('\n')
    

    for tot in curr_tots:
        total += float(tot) * (1 / len(curr_tots))
    
        
        
        
        
        
        
    print('\n')






    
    
    
    
    
    
    
    
    
    
    
    
    
