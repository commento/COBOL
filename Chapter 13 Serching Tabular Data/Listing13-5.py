# same problem in python does not require binary search
# from bisect import bisect_left 

# def BinarySearch(a, x): 
#     i = bisect_left(a, x) 
#     if i != len(a) and a[i] == x: 
#         return i 
#     else: 
#         return -1

dict = {}

file   = open("Listing13-5.dat", "r")
for line in file:
    dict[line[0:2]] = line[2:].split("\n")[0]

i = input("enter a country code: ")

while (i != ""):
    try:
        print(dict[i.upper()])
    except KeyError:
        print("country code not valid")
    i = input("enter a country code: ")



