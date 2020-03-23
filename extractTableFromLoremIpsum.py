file = open("loremipsum.txt", "r")
w    = open("Listing13-7.dat", "w")

s = file.readline()
l = []

while (s != ''):
    s = s.replace(",", "")
    s = s.replace(".", "")
    s = s.replace("\n", "")
    l = s.split(" ")
    for elem in l:
        w.write(elem + "\n")
    s = file.readline()

w.close()
file.close()