# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 02:15:28 2020

@author: Ferdi
"""

import numpy as np

'''grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]'''

grid = [[0, 0, 3, 8, 0, 0, 0, 0, 4], 
        [0, 6, 0, 0, 3, 0, 0, 7, 0],
        [9, 0, 0, 0, 0, 2, 1, 0, 0],
        [4, 0, 0, 0, 0, 9, 3, 0, 0],
        [0, 8, 0, 0, 4, 0, 0, 6, 0],
        [0, 0, 5, 2, 0, 0, 0, 0, 8],
        [0, 0, 9, 3, 0, 0, 0, 0, 1],
        [0, 3, 0, 0, 6, 0, 0, 9, 0],
        [1, 0, 0, 0, 0, 5, 2, 0, 0]]

print(np.matrix(grid))
print('-'*82)

#%%

def possible(x, y, n):
    for i in range(9):
        if grid[x][i] == n:
            return False
    for i in range(9):
        if grid[i][y] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x0 + i][y0 + j] == n:
                return False
    return True


#%%

def solve():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1,10):
                    if possible(i, j, n):
                        grid[i][j] = n
                        solve()
                        grid[i][j] = 0
                return
    print(np.matrix(grid))
    
solve()
   


            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
