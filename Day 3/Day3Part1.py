h = open("Day 3\Day3Input1.txt", 'r') 

Forest = list(h)
count = 0
col = 0 
hz = 1
state = 0 # this is for part 2

for row in range(0,len(Forest)):    
    if(state == 0):
        if(Forest[row][col].find('#') != -1): # checking if there is a tree
            count = count + 1 
        

        col = col + hz      # col increase by horizantal slope
        size = len(Forest[row])

        if (col >= 31): # checks if the col is at the end 
            col= col - 31                   # Resets to col - col.size

        state = 1 #this is a hard coded solution for part 2 
    else: 
        state = 0
print(count)


    
        

