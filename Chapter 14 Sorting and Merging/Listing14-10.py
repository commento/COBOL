
with open("Listing14-10.dat", "r") as f:
    content = f.readlines()

content = [x.strip() for x in content] 
content = [x[20:40]+x[:20] for x in content if x[20:40] != "Ireland".ljust(20)]
content.sort()

w = open("Listing14-10_2.rpt", "w")

w.write("       FOREIGN GUESTS REPORT" + "\n")
w.write("COUNTRY           VISITORS" + "\n")

for elem in content:
    w.write(elem + "\n")

w.write("       *****ENDOFREPORT*****" + "\n")

w.close()