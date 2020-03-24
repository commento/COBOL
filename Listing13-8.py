
l = []

for i in range(10):
    inp = input("Enter a number")
    l.append(inp)


oddNumBtwZeros = False

numBtwTheFirstTwoZeros = 0

oneZero = False
twoZeros = False
noZeros = True


# only valid for the first two zeros, other zeros interval are not evaluated
for i, elem in enumerate(l):
    if oneZero is False and elem == '0':
        oneZero = True
        noZeros = False
    elif oneZero and elem != '0':
        numBtwTheFirstTwoZeros += 1
    elif oneZero and elem == '0':
        oneZero = False
        twoZeros = True
        break

if twoZeros:
    if numBtwTheFirstTwoZeros == 0:
        print("noneBtwZeros")
    elif numBtwTheFirstTwoZeros % 2 == 0:
        print("evenNumBtwZeros")
    else:
        print("oddNumBtwZeros")
elif oneZero:
    print("one zero")
elif noZeros:
    print("no zeros")
