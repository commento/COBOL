def steady(num):
    tot = 0
    tot += num
    print ("total is", tot)

class Dynamic:
    def __init__(self):
        self.tot = 0
    def call(self, num):
        self.tot += num
        print("total is", self.tot)

inpt = input("Enter a number ")
d = Dynamic()
while inpt != "":
    num = int(inpt)
    steady(num)
    d.call(num)
    inpt = input("Enter a number ")
