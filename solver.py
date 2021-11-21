import numpy as np
import copy


grid = [
        [62, 33, 36, 0, 60, 0, 0, 15, 0, 0],
        [0, 0, 0, 76, 37, 0, 0, 84, 0, 0],
        [32, 0, 0, 0, 78, 89, 0, 0, 82, 19],
        [0, 58, 0, 90, 93, 0, 0, 0, 13, 0],
        [64, 0, 0, 0, 86, 0, 98, 0, 0, 71],
        [0, 4, 67, 0, 0, 96, 0, 0, 41, 0],
        [0, 65, 0, 0, 0, 73, 48, 0, 0, 21],
        [0, 54, 0, 0, 0, 100, 0, 44, 0, 0],
        [0, 0, 0, 7, 24, 0, 0, 0, 0, 0],
        [53, 0, 25, 28, 51, 8, 0, 46, 0, 10]
]

gridOriginal = copy.deepcopy(grid)

stack = []

def numIndex(num):
  global grid
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if (grid[i][j] == num):
        col = grid[i].index(num)
        row = i
        return [row, col]

def inGrid(num):
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if (grid[i][j] == num):
        return True
  return False

def process(grid, stack):
  num = 100
  # finding the index of num
  index = numIndex(num)
  # adding 100 to the stack to start off
  stack.append([num])

  while num > 0:
    
    # exists = False initially
    exists = False

    # check each index in stack, if one of the numbers equals num, skip the next conditional
    for i in stack:
      if i[0] == num:
        exists = True
    # if none of the numbers equal num, we can add it to the stack
    if (not exists):
      stack.append([num])

    
    # run possible() with index, num, and stack
    if (possible(gridOriginal, grid, index, num, stack)):
      
      index = numIndex(num-1)
      
      # if possible returns True (either a number was already in the grid, and it was in the range of movement from the index that we were at, or there was an empty space)
      # we will add the index where the move was made to, to the number we are currently at 
      stack[100-num].append(index)
      num-=1

      # then subtract 1 from num, and officially set the index to the new index (weird interaction with the possible method)
      
    else:
      # if it returns false, we will remove the last index of the stack, and add one to the number and find the index of num-1
      stack.pop()
      num += 1
      index = numIndex(num)
    
    if (num == 1):
      print(np.matrix(grid))
      print("YOU win!")
      return
    elif (num > 100):
      # if no more moves are possible, then eventually the stack will fill up and num will be greater than 100
      print("sorry, the puzzle is not possible")
      return

def possible(gridOriginal, grid, index, num, stack):

  if (inGrid(num-1)):
    try:
      if (grid[index[0] + 2][index[1] + 1] == num-1 and [index[0]+2, index[1]+1] not in stack[100-num] and index[0] + 2 >= 0 and index[1] + 1 >= 0): # [+2, +1]

        return True
    except Exception:
      pass
    try:
      if (grid[index[0] + 2][index[1] - 1] == num-1 and [index[0]+2, index[1]-1] not in stack[100-num] and index[0] + 2 >= 0 and index[1] - 1 >= 0): # [+2, -1]
        
        return True
    except Exception:
      pass
    try:
      if (grid[index[0] + 1][index[1] + 2] == num-1 and [index[0]+1, index[1]+2] not in stack[100-num] and index[0] + 1 >= 0 and index[1] + 2 >= 0): # [+1, +2]
        
        return True
    except Exception:
      pass
    try:
      if (grid[index[0] + 1][index[1] - 2] == num-1 and [index[0]+1, index[1]-2] not in stack[100-num] and index[0] +1 >= 0 and index[1] - 2 >= 0): # [+1, -2]
        
        return True
    except Exception:
      pass
    try:
      if (grid[index[0] - 1][index[1] - 2] == num-1 and [index[0]-1, index[1]-2] not in stack[100-num] and index[0] - 1 >= 0 and index[1] - 2 >= 0): # [-1, -2]
        
        return True
    except Exception:
      pass
    try:
      if (grid[index[0] - 1][index[1] + 2] == num-1 and [index[0]-1, index[1]+2] not in stack[100-num] and index[0] - 1 >= 0 and index[1] + 2 >= 0): # [-1, +2]
        
        return True
    except Exception:
      pass
    try: 
      if (grid[index[0] - 2][index[1] - 1] == num-1 and [index[0]-2, index[1]-1] not in stack[100-num] and index[0] - 2 >= 0 and index[1] - 1 >= 0): # [-2, -1]
        
        return True
    except Exception:
      pass
    try: 
      if (grid[index[0] - 2][index[1] + 1] == num-1 and [index[0]-2, index[1]+1] not in stack[100-num] and index[0] - 2 >= 0 and index[1] + 1 >= 0): # [-2, +1]
        return True
    except Exception:
      pass
    if grid[index[0]][index[1]] != gridOriginal[index[0]][index[1]]:
      grid[index[0]][index[1]] = 0
    return False
  else:
    try:
      if (grid[index[0] + 2][index[1] + 1] == 0 and [index[0]+2, index[1]+1] not in stack[100-num] and index[0] + 2 >= 0 and index[1] + 1 >= 0): # [+2, +1]
        
        grid[index[0]+2][index[1]+1] = num-1
        return True
    except Exception:
      pass
    try: 
      if (grid[index[0] + 2][index[1] - 1] == 0 and [index[0]+2, index[1]-1] not in stack[100-num] and index[0] + 2 >= 0 and index[1] - 1 >= 0): # [+2, -1]
        
        grid[index[0]+2][index[1]-1] = num-1
        return True
    except Exception:
      pass
    try: 
      if (grid[index[0] + 1][index[1] + 2] == 0 and [index[0]+1, index[1]+2] not in stack[100-num] and index[0] + 1 >= 0 and index[1] + 2 >= 0): # [+1, +2]
        
        grid[index[0]+1][index[1]+2] = num-1
        return True
    except Exception:
      pass
    try: 
      if (grid[index[0] + 1][index[1] - 2] == 0 and [index[0]+1, index[1]-2] not in stack[100-num] and index[0] + 1 >= 0 and index[1] - 2 >= 0): # [+1, -2]
        
        grid[index[0] + 1][index[1] - 2] = num-1
        return True
    except Exception:
      pass
    try: 
      if (grid[index[0] - 1][index[1] - 2] == 0 and [index[0]-1, index[1]-2] not in stack[100-num] and index[0] - 1 >= 0 and index[1] - 2 >= 0): # [-1, -2]
        
        grid[index[0]-1][index[1]-2] = num-1
        return True
        
    except Exception:
      pass
    try: 
      if (grid[index[0] - 1][index[1] + 2] == 0 and [index[0]-1, index[1]+2] not in stack[100-num] and index[0] - 1 >= 0 and index[1] + 2 >= 0): # [-1, +2]
  
        grid[index[0]-1][index[1]+2] = num-1
        return True
    except Exception:
      pass
    try: 
      if (grid[index[0] - 2][index[1] - 1] == 0 and [index[0]-2, index[1]-1] not in stack[100-num] and index[0] - 2 >= 0 and index[1] - 1 >= 0): # [-2, -1]
        
        grid[index[0]-2][index[1]-1] = num-1
        return True
    except Exception:
      pass
    try: 
      if (grid[index[0] - 2][index[1] + 1] == 0 and [index[0]-2, index[1]+1] not in stack[100-num] and index[0] - 2 >= 0 and index[1] + 1 >= 0): # [-2, +1]
        grid[index[0]-2][index[1]+1] = num-1
        return True
    except Exception:
      pass
    if grid[index[0]][index[1]] != gridOriginal[index[0]][index[1]]:
      grid[index[0]][index[1]] = 0
    return False

process(grid, stack)
