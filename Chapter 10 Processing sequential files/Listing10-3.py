fM = open("Listing10-3Master.dat", "r")
fT = open("Listing10-3Trans2.dat", "r")
fN = open("Listing10-3NewMast2.dat", "w")

readfM = fM.readline()
readfT = fT.readline()

# TODO: not complete, the handling for: readfM != '' OR readfT != '' should be added
while (readfM != '' and readfT != ''):
    gIdM = int(readfM[:6])
    gIdT = int(readfT[1:7])
    typeCode = int(readfT[0])

    if gIdT > gIdM:
        fN.write(readfM)
        readfM = fM.readline()
    elif gIdT == gIdM:
        if typeCode  == 1:
            print("Error Record already Exist")
        elif typeCode == 2:
            readfM = fM.readline()
        elif typeCode == 3:
            readfM = readfM[:40] + readfT[7:]
        readfT = fT.readline()
    elif gIdT < gIdM:
        if typeCode  == 1:
            fN.write(readfT[1:])
        elif typeCode == 2:
            print("Error Record not present")
        elif typeCode == 3:
            print("Error Record not present")
        readfT = fT.readline()


fM.close()
fT.close()
fN.close()
