
with open("Listing14-1.dat", "r") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
content.sort()


totCalls = 0
totTexts = 0
prevId = content[0][:10]


print("UNIVERSAL TELECOMS MONTHLY REPORT")
print("SUBSCRIBERID     CALLS    TEXTS")

for elem in content:
    if elem[:10] == prevId:
        if elem[-7] == "2":
            totCalls +=1
        else:
            totTexts +=1
    else:
        print(prevId, "     ",totCalls, "        ", totTexts)
        prevId = elem[:10]
        totCalls = 0
        totTexts = 0
        if elem[-7] == "2":
            totCalls += 1
        else:
            totTexts += 1
        

print(prevId, "     ",totCalls, "        ", totTexts)


