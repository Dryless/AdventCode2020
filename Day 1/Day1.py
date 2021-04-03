
  
  
h = open('Input1.txt', 'r') 
  
content = list(h) 

for i in range(0, len(content)): 
    content[i] = int(content[i]) 

for a in range(0, len(content)):
    for b in range(0, len(content)):
        for c in range(0, len(content)):
                    sum = content[a]+ content[b] +content[c]
                    if(sum == 2020):
                        print(str(content[a])+" + "+ str(content[b])+ " + " + str(content[c]) )
                        ans = content[a]*content[b]*content[c]


print(ans)

h.close()