import operator
file = open("Listing13-7.dat", "r")


d = {}
s = file.readline()
while (s != ''):
    s = s.split("\n")[0]
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
    s = file.readline()


print("1", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]
print("2", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]
print("3", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]
print("4", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]
print("5", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]
print("6", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]
print("7", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]
print("8", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]
print("9", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]
print("10", max(d.items(), key=operator.itemgetter(1))[0], max(d.items(), key=operator.itemgetter(1))[1])
del d[max(d.items(), key=operator.itemgetter(1))[0]]

