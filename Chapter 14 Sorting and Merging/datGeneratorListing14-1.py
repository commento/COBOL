import random


f = open("Listing14-1.dat", "w")
l = []
recordId = 0
count = 0
while recordId < 200:
    string    = str(recordId).zfill(10)
    string   += str(random.randrange(1, 3, 1)).zfill(1)
    string   += str(random.randrange(0, 9999, 1)).zfill(4)
    string   += str(99)
    string += "\n"
    l.append(string)
    if count == 2:
        count = 0
        recordId += 1
    else:
        count += 1

randomizer = random.sample(range(600), 600)

for idx in randomizer:
    f.write(l[idx])

f.close()