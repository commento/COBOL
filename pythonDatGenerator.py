import random


monthSalesDetails = True

f = open("BranchSales3.dat", "w")
recordId = 0
while recordId < 60:
    string    = str(recordId).zfill(7)
    string   += str(random.randrange(1, 50, 1)).zfill(2)
    if monthSalesDetails:
        for i in range(12):
            string += str(random.randrange(0, 99999, 1)).zfill(5)
            string   += str(99)
    else:
        string   += str(random.randrange(0, 9999999, 1)).zfill(7)
        string   += str(99)
    string += "\n"
    f.write(string)
    recordId += 1


f.close()