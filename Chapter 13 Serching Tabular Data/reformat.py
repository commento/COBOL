file = open("reformat.txt", "r")
w    = open("datastructure.txt", "w")

l = file.readline()

while (l != ''):
    if "VALUE" in l:
        w.write("{\"code\" : " + l[21:24] + "\", \"name\" : \"" + l[24:].split(" ")[0] + "\", \"capital\" : \"" + l[38:].split(" ")[0] + "\"},\n" )
        w.write("{\"code\" : \"" + l[52:54] + "\", \"name\" : \"" + l[54:].split(" ")[0] + "\", \"capital\" : \"" + l[68:].split(".")[0] + "},\n" )
    l = file.readline()

w.close()
file.close()