import random

# this is not needed, I added a file that is the expected output, not the expected input
f = open("Listing14-5.dat", "w")
l = []
recordId = 0
count = 0
while recordId < 200:
    string    = str(recordId).zfill(10)
    string   += str(random.randrange(0, 10000, 1)).zfill(4)
    string   += str(random.randrange(10, 100, 1)).zfill(2)
    string   += str(random.randrange(0, 1000000, 1)).zfill(6)
    string   += str(random.randrange(10, 100, 1)).zfill(2)
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