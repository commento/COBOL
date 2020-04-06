import random

f = open("Listing14-6.dat", "w")
l = []
recordId = 0
count = 0


import random
l = random.sample(range(100000), 600)

print(l)

while recordId < 600:
    cond = random.randrange(0, 2, 1)
    string = ""
    if cond == 0:
        string   += str(random.randrange(0, 20, 1)).zfill(2)
    else:
        string   += str(random.randrange(90, 100, 1)).zfill(2)
    string   += str(l[recordId]).zfill(5)
    string   += "LM" + str(random.randrange(0, 1000, 1)).zfill(3)
    string += "\n"
    f.write(string)
    recordId += 1

f.close()