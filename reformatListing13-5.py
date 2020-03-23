file = open("textraw.txt", "r")
w    = open("Listing13-5.dat", "w")

l = file.readline()

while (l != ''):
    w.write(l.split("\t")[1] + l.split("\t")[0] + "\n" )
    l = file.readline()

w.close()
file.close()