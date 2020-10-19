# WORK IN PROGRESS :D
import math

col=25
row=25
grid=[]
openSet=[]
closedSet=[]
start=0
end=0
neighbours=[]
previous= None

def show(l):
    color(255) # Add color to know if the cell is visited or not
    rect(l[0]*w,l[1]*h,w-1,h-1) #To create a rectangular cell for each node

def addNeighbours(x,y):
    neighbours.append([])
    if x < (row-1):
        neighbours[x][y].append(grid[x+1][y])
    if x > 0:
        neighbours[x][y].append(grid[x-1][y])
    if y < (col-1):
        neighbours[x][y].append(grid[x][y+1])
    if y > 0:
        neighbours[x][y].append(grid[x][y-1])

def heuristic(a,b):
    dist = math.hypot(abs(a[0]-b[0]),abs(a[1]-b[1]))
    # or 
    # dist = abs(a[0]-b[0] + a[1]-b[1]
    return dist

for i in range(row):
    grid.append([])
    for j in range(col):
        grid[i].append([i,j,0,0,0])     # [x,y,f(n),g(n),h(n)]

start=grid[0][0]
end=grid[col-1][row-1]
w=width/col     #width is the width of the display area
h=height/row     #height is the height of the display area
openSet.append(start)

for i in range(row):
    for j in range(col):
        addNeighbours(i,j)

for i in range(row):
    for j in range(col):
        show(grid[i][j])


while len(openSet)>0:
    #keep going else there's no solution
    lowestIndex=0
    for i in openSet:
        if i[2]<openSet[lowestIndex][2]:
            lowestIndex=i
    
    current=openSet[lowestIndex]
    if current==end:
        path=[]
        temp=current
        path.append(temp)
        while previous in temp: # previous def is not used appropriately
            path.append(temp)
            temp=temp(previous) # error with previous

        print("Reached the end")

    openSet.remove(current)
    closedSet.append(current)
    neighbour=neighbours[current[0]][current[1]]

    for i in neighbour:
        x=i[0]
        y=i[1]
        if i not in closedSet:
            temp= current[3]+1
            if i in openSet:
                if temp<i[3]:
                    i[3]=temp
            else:
                i[3]=temp
                openSet.append(i)
        
        i[4]=heuristic(i,end)
        i[2]=i[3]+i[4]              # formula: f(n) = g(n) + h(n)   
        i[previous]=current # error


for i in openSet:
    openSet[i]

for i in closedSet:
    closedSet[i]

for i in path:
    show(i)