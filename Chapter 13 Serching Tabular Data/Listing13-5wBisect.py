from bisect import bisect_left 

def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

l1 = []
l2 = []

file   = open("Listing13-5.dat", "r")
for line in file:
    l1.append(line[0:2])
    l2.append(line[2:].split("\n")[0])

i = input("enter a country code: ")

while (i != ""):
    ret = BinarySearch(l1, i.upper())
    if ret == -1:
        print("country code not valid")
    else:
        print(l2[ret])
    i = input("enter a country code: ")