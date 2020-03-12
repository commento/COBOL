import random

f = open("BranchSales2.dat", "w")
recordId = 0
while recordId < 60:
    string    = str(recordId).zfill(7)
    string   += str(random.randrange(1, 50, 1)).zfill(2)
    string   += str(random.randrange(0, 9999999, 1)).zfill(7)
    string   += str(99) + "\n"
    f.write(string)
    recordId += 1


f.close()