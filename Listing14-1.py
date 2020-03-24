
with open("Listing14-1.dat", "r") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
content.sort()

totPartial = 0
prevId = content[0][:10]

print("UNIVERSAL TELECOMS MONTHLY REPORT")
print("SUBSCRIBERID     BILLABLEVALUE")

for elem in content:
    if elem[:10] == prevId:
        totPartial += float(elem[11:15]+"."+elem[15:17])
    else:
        print(prevId, "     ", "${:,.2f}".format(round(totPartial,2)))
        prevId = elem[:10]
        totPartial = float(elem[11:15]+"."+elem[15:17])

print(prevId, "     ", "${:,.2f}".format(round(totPartial,2)))



