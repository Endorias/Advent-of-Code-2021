#BINGO game Advent of code day number 4
import random as r

#variables
grid_sz = 5
drawnNums = []

#class for numbers in grid
class Gvalues:
    def __init__(self, value, seen):
        self.value = value
        self.seen = seen
    
    def getValue(self):
        return self.value
    
    def getSeen(self):
        return self.seen

#method for creating randomized board
#input: NULL
#output: Array of Gvalues objects that contain numbers and states 
def createRandomBoard():
    grid_vals = []
    for i in range(grid_sz * grid_sz):
        tmp = r.randrange(25)#generates a random number from 0-24
        while grid_vals.count(tmp) > 0:
            tmp = r.randrange(25)
        grid_vals.append(Gvalues(tmp, False))
    return grid_vals

#method for printing board
#input: board of choice
#output: void
def printGrid(grid):
    print("Grid:")
    count = 0
    for x in grid:
        if count == 5:
            print("")
            count = 0
        
        print(x.getValue(), end= "  ")
        count += 1

    print("\n")

# method for cheking whether or not a board has gotten bingo
# input: board to check
# output: boolean. If Bingo return True, if not return False
def bingoCheck(grid):
    #check rows
    seens = 0
    count = 0
    for x in grid:
        if count == 5:
            count = 0
            seens = 0
        if x.getSeen() == True:
            seens += 1
        count += 1
        if seens == 5:
            return True
    
    #check Columns
    for y in range(5):
        seens = 0
        for i in range(0, 21, 5):
            if grid[y+i].getSeen() == True:
                seens += 1
            if seens == 5:
                return True
        seens = 0
    return False
            
#method for drawing numbers for bingo
#input: List of all drawn numbers to check for duplicates
#output: touple ({updated drawn numbers list}, {last drawn number})
def drawNum(numList):
    tmp = r.randrange(25)
    while numList.count(tmp) > 0:
        tmp = r.randrange(25)
    numList.append(tmp)
    return (numList, tmp)

#Creates all three boards
b1 = createRandomBoard()
b2 = createRandomBoard()
b3 = createRandomBoard()

print("boards created") #debugging

while len(drawnNums) < (grid_sz*grid_sz + 1):
    
    #draws a number and updates the drawn numbers list
    toup = drawNum(drawnNums)
    drawnNums = toup[0]
    num = toup[1]

    print("number drawn: ", num) #Prints drawn number into console

    #Marks the Bingo numbers on the boards as seen
    for x in b1:
        if x.getValue() == num:
            x.seen = True
    for x in b2:
        if x.getValue() == num:
            x.seen = True
    for x in b3:
        if x.getValue() == num:
            x.seen = True
    

    #Assigns values for checking if a board won
    b1win = bingoCheck(b1)
    b2win = bingoCheck(b2)
    b3win = bingoCheck(b3)

    print("\n")

    #Checks whether board 1 has gotten Bingo on the turn
    if b1win:
        sum = 0
        for x in b1:
            if x.getSeen() == False:
                sum += x.getValue()
        score = sum * num
        print("B1 score: " , score)#prints out the board name and score for this round
        printGrid(b1)

    #Checks whether board 2 has gotten Bingo on the turn
    if b2win:
        sum = 0
        for x in b2:
            if x.getSeen() == False:
                sum += x.getValue()
        score = sum * num
        print("B2 score: " , score) #prints out the board name and score for this round
        printGrid(b2)

    #Checks whether board 3 has gotten Bingo on the turn
    if b3win:
        sum = 0
        for x in b3:
            if x.getSeen() == False:
                sum += x.getValue()
        score = sum * num
        print("B3 score: " , score)#prints out the board name and score for this round
        printGrid(b3)
    

    #Exits program of one or more boards have gotten BINGO
    if b1win or b2win or b3win:
        exit()
    else:
        print("No Bingo")

