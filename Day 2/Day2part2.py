
Valid=0
t=0
h = open("Day 2\Day2Input1.txt", 'r') 

content = list(h)

for a in range(0,len(content)):
    
    hyphen = content[a].find('-')
    space = content[a].find(' ')
    end = content[a].find('\n')
    First = int(content[a][0:hyphen])-1
    Second = int(content[a][hyphen+1:space+1])-1
    Key = content[a][space+1]
    Password = content[a][space+4:end]


    if(Password[First] == Key): 
        if(Password[Second] != Key):
            Valid = Valid +1
    if(Password[Second] == Key): 
        if(Password[First] != Key):
            Valid = Valid +1


    
    t = t+1

print (str(Valid) + " "+ str(t))