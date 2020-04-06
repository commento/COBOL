import random

sl= ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

strings = []

f = open("Listing10-1.dat", "w")
recordId = 0
while recordId < 50:
    string    = random.choice(sl).ljust(14)
    string   += str(random.randrange(1, 99999, 1)).zfill(5)
    string   += str(random.randrange(1, 99999, 1)).zfill(5)
    string   += random.choice("MF")
    string   += str(random.randrange(1, 9999, 1)).zfill(4)
    string   += "99"
    string += "\n"
    strings.append(string)
    recordId += 1



for string in strings:
    strings.sort()
    f.write(string)
f.close()



# order in ascending order