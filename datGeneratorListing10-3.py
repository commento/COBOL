import random

gn= ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

f = open("Listing10-3Master.dat", "w")
recordId = 0
while recordId < 50:
    string    = str(recordId).zfill(6)
    string   += str(gn[recordId] + " Gadget").ljust(30)
    string   += str(random.randrange(1, 9999, 1)).zfill(4)
    string   += str(random.randrange(1, 99, 1)).zfill(4)
    string   += "99"
    string += "\n"
    f.write(string)
    recordId += 1

f.close()