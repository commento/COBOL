import random

f = open("CensusFile.dat", "w")
recordId = 0
while recordId < 50000:
    string    = str(recordId).zfill(7)
    string   += str(random.randrange(1, 51, 1)).zfill(2) # UpperLimit not included
    string   += str(random.randrange(1, 4, 1))
    string   += str(random.randrange(1, 3, 1))
    string   += random.choice("YN")
    string += "\n"
    f.write(string)
    recordId += 1


f.close()