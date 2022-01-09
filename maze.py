import random
import math

board = [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
target=[]

def h(pos1,pos2):
     x1,y1=pos1
     x2,y2=pos2
     return math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))

def print_board():
    i=0
    while i < 5:
        j=0
        while j < 5:
            print(board[i][j], end="  ")
            j=j+1
        print("\n")
        i=i+1

def generate_blocks():
    i=1
    while i<= 10:
        x=random.randint(0,4)
        y=random.randint(0,4)
        board[x][y] = 1
        i=i+1
    board[0][0]=0
    

def set_goal():
    flag=True
    while flag:
        x=random.randint(0,4)
        y=random.randint(0,4)
        if not(board[x][y]):
            target.append(x)
            target.append(y)
            print(target)
            flag=False

def possible_moves(pos,visited):
    pos_moves=[]
    i,j=pos 
    for l in [i-1,i,i+1]:
        for m in [j-1,j,j+1]:
            if  l>=0 and m>=0 and l<len(board) and m<len(board[0]) and not((l,m)==(i,j)) and board[l][m]!=1:
                 if (l,m) not in visited: pos_moves.append((l,m))
    print(pos)
    print(pos_moves)
    return pos_moves

def solve(src,target,visited,d):
    visited.append(src)
    print(src)
    print(target)
    src=list(src)
    if src==target: return visited
    pos_moves=possible_moves(src,visited)
    if(pos_moves==[]): return False
    scores=[h(x,target)+d for x in pos_moves]
    min_score=min(scores)
    selected_moves=[]
    for i in range(len(pos_moves)):
        if scores[i]==min_score: selected_moves.append(pos_moves[i])
    for move in selected_moves:
        if solve(move,target,visited,d+1)!=False: return visited
    return False

def maze():
    visited=[]
    res=solve([0,0],target,visited,0)
    print(res)
    if not res: print("No result exists")
    else: 
        print('Path :',res) 
        display(res)
        
def display(moves):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i,j) in moves: print('+',end=' ')
            else: print(board[i][j],end=' ')
        print()
    print()

generate_blocks()
set_goal()
print_board()
maze()
