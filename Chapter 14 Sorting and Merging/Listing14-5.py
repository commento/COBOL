
with open("Listing14-1.dat", "r") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
content.sort()

w = open("Listing14-5_2.srt", "w")

totCalls = 0
totTexts = 0
prevId = content[0][:10]


print("UNIVERSAL TELECOMS MONTHLY REPORT")
print("SUBSCRIBERID     CALLS    TEXTS")

for elem in content:
    if elem[:10] == prevId:
        if elem[-7] == "2":
            totCalls +=int(elem[-6:])
        else:
            totTexts +=int(elem[-6:])
    else:
        print(prevId, "     ",totCalls, "        ", totTexts)
        # truncation of the result in the cobol version, without errors. adjusted here with [-6:]
        w.write(prevId + str(totTexts).zfill(6)[-6:] + str(totCalls).zfill(8)[-8:] + "\n")
        prevId = elem[:10]
        totCalls = 0
        totTexts = 0
        if elem[-7] == "2":
            totCalls += int(elem[-6:])
        else:
            totTexts += int(elem[-6:])
        

print(prevId, "     ",totCalls, "        ", totTexts)
# truncation of the result in the cobol version, without errors. adjusted here with [-6:]
w.write(prevId + str(totTexts).zfill(6)[-6:] + str(totCalls).zfill(8)[-8:] + "\n")

w.close()