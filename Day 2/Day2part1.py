
Valid=0
k=0
t=0
h = open("Day 2\Day2Input1.txt", 'r') 

content = list(h)

for a in range(0,len(content)):
    
    hyphen = content[a].find('-')
    space = content[a].find(' ')
    end = content[a].find('\n')
    Min = int(content[a][0:hyphen])
    Max = int(content[a][hyphen+1:space+1])
    Key = content[a][space+1]
    Password = content[a][space+4:end]


    for b in range(0, len(Password)):
        if(Password[b].find(Key) != -1):
            k=k+1

    if(Min<=k<=Max):
        Valid=Valid+1
    
    k=0
    
    t = t+1

print (str(Valid) + " "+ str(t))