input = open('data.txt', 'r').read()

checksum = 0

for line in input.split("\n"):
    row = list( map(int, line.split("\t")) )
    checksum += max(row) - min(row)

print("Checksum: " + str(checksum))


#------------------------------#

s = 0

for line in input.split("\n"):
    row = list( map(int, line.split("\t")) )
    
    i = 0
    for i, a in enumerate(row):
        j = 0
        for j,b in enumerate(row):
            if i!=j and a%b==0:
                s += a/b

print("Sum of divided numbers: "+ str(s))