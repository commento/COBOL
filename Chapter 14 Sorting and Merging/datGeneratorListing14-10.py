
f = open("Listing14-10.dat", "w")


guestNames = ["ciao", "come", "va", "oggi", "tutto", "bene", "grazie", "mille", "buona", "sera", "tante", "cose"]

countryNames = ["Italy", "Germany", "France", "UK", "Ireland", "Italy", "Germany", "France", "UK", "Italy", "Germany", "France"]

guestComments = ["ciao", "come", "va", "oggi", "tutto", "bene", "grazie", "mille", "buona", "sera", "tante", "cose"]

for i in range(len(guestNames)):
    string = guestNames[i].ljust(20) + countryNames[i].ljust(20) + guestComments[i].ljust(40) + "\n"
    f.write(string)

f.close()