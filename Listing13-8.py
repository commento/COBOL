
l = []

for i in range(10):
    inp = input("Enter a number")
    l.append(inp)


oddNumBtwZeros = False
evenNumBtwZeros = False
noneBtwZeros = False
oneZero = False
noZeros = False

for i, elem in enumerate(l):
    if elem == '0':
        oneZero = True
    for j, elem2 in enumerate(l):
        if elem2 == '0' and elem == '0' and j > i+1:
            if (j-i+1)%2==0: 
                evenNumBtwZeros = True
                break
            else: 
                oddNumBtwZeros = True
                break
        elif elem2 == '0' and elem == '0' and j == i+1:
            noneBtwZeros = True
    if evenNumBtwZeros or oddNumBtwZeros:
        break

if oneZero == False:
    noZeros = True

if oddNumBtwZeros:
    print("oddNumBtwZeros")
elif evenNumBtwZeros:
    print("evenNumBtwZeros")
elif noneBtwZeros:
    print("noneBtwZeros")
elif oneZero:
    print("one zero")
elif noZeros:
    print("no zeros")
