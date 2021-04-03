

NVletters = ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

h = open(r"Day 4\Day4Input1.txt", 'r') 

Cred = list(h)
valid = 0
passports = [] 

count = 0
Birth = -1
Issue = -1
Expiration = -1
Height = -1
Hair = -1
Eye = -1
PassID = -1
CoutryID = -1
byr = 0
iyr = 0
eyr = 0
hgt = 0
hcl = " "
elc = " "
pid = 0 
cid = 0
stand = " "

class plassport:
    def __init__ (self, byr, iyr, eyr, hgt, hcl, ecl, pid , cid, valid,stand):
        self.byr = byr # Birth year
        self.iyr = iyr  # Issue year
        self.eyr = eyr # Expiration
        self.hgt = hgt # Height
        self.hcl = hcl # Hair color
        self.ecl = ecl # Eye color 
        self.pid = pid # Passport ID
        self.cid = cid # country ID
        self.valid = valid # part 1 valid check 
        self.stand = stand # determines if the measurements are made in "in" or "cm"




for a in range(0,len(Cred)):
    if(Cred[a].find('\n') == 0):
        a = a + 1
        
        if((Birth != -1) and (Issue != -1) and (Expiration != -1) and (Height != -1) and (Hair != -1) and (Eye != -1) and (PassID != -1) ):
            valid = 1
        else:
            valid = -1

        
        passports.append(plassport(byr, iyr, eyr, hgt, hcl, elc, pid, cid, valid, stand)) # creates a new passport with the colleted info
        

        # resets the variables for input
        Birth = -1
        Issue = -1
        Expiration = -1
        Height = -1
        Hair = -1
        Eye = -1
        PassID = -1
        CoutryID = -1
        byr = 0
        iyr = 0
        eyr = 0
        hgt = 0
        hcl = " "
        elc = " "
        pid = 0 
        cid = 0
        stand = " "
    else:
        if(Birth == -1):      
            Birth = Cred[a].find('byr')
            if(Birth != -1):   
                byr = int(Cred[a][Birth+4:Birth+8])
        if(Issue == -1):
            Issue = Cred[a].find('iyr')
            if(Issue != -1):
                iyr = int(Cred[a][Issue+4:Issue+8])
        if(Expiration == -1):
            Expiration = int(Cred[a].find('eyr'))
            if(Expiration != -1):
                eyr = int(Cred[a][Expiration +4:Expiration+8])
        if(Height == -1):
            Height = Cred[a].find('hgt')
            if(Height != -1):
                if(Cred[a].find("in")!= -1):
                    stand = "in"
                    hgt = int(Cred[a][Height+4:Cred[a].find("in")])
                elif(Cred[a].find("cm")!= -1):
                    stand = "cm" 
                    hgt = int(Cred[a][Height+4:Cred[a].find("cm",Height+4 )])
        if(Hair == -1):
            Hair = Cred[a].find('hcl')
            if(Hair != -1):
                hcl = Cred[a][Hair+4:Hair+11]
        if(Eye == -1):
            Eye = Cred[a].find('ecl')
            if(Eye != -1):
                elc = Cred[a][Eye+4:Eye+7]
        if(PassID == -1):
            PassID = Cred[a].find('pid')
            if(PassID != -1):
                pid = Cred[a][PassID+4:Cred[a].find(" ", PassID+4)]
        if(CoutryID == -1):
            CoutryID = Cred[a].find('cid')
            if(CoutryID != -1): 
                cid = Cred[a][CoutryID+4:CoutryID]


if((Birth != -1) and (Issue != -1) and (Expiration != -1) and (Height != -1) and (Hair != -1) and (Eye != -1) and (PassID != -1) ):
    valid = 1
else:
    valid = -1
passports.append(plassport(byr, iyr, eyr, hgt, hcl, elc, pid, cid, valid,stand)) # creates the last passport with the colleted info

#valid checker
for b in range(0, len(passports)):
    if(passports[b].valid == 1):
        if((passports[b].byr >=  1920) and (passports[b].byr <=  2002) and (passports[b].iyr >=  2010) and (passports[b].iyr <=  2020) and (passports[b].eyr >=  2020) and (passports[b].eyr <=  2030)): # Year checks
            if(passports[b].stand == "cm"):
                if((passports[b].hgt >=  150) and (passports[b].hgt <=  193)): # Height cm
                    if(passports[b].hcl[0] == '#'):
                        for c in range(0,len(NVletters)): #checks for a bad letter in the hexadecimal value of hair color 
                            if(passports[b].hcl.find(NVletters[c])!= -1): #if found 
                                break
                        if(len(passports[b].pid) == 9):
                            if(passports[b].ecl == "amb" or "blu" or "brn" or "gry" or "grn" or "hzl" or "oth"):
                                count = count +1
            else:
                if((passports[b].hgt >=  59) and (passports[b].hgt <=  76)): # Height in 
                    if(passports[b].hcl[0] == '#'): # repeats line 130 
                        for c in range(0,len(NVletters)):
                            if(passports[b].hcl.find(NVletters[c])!= -1):
                                break
                        if(len(passports[b].pid) == 9):
                            if(passports[b].ecl == "amb" or "blu" or "brn" or "gry" or "grn" or "hzl" or "oth"):
                                count = count +1 


print(count)









