

print("Enter value of QuarterlyPurchases - ")
QP = input()
QP = int(QP)
	
print("Enter qty of books purchased - ")
Qty = input()
Qty = int(Qty)

print("club member enter Y or N - ")
Member = input()

if   Qty >= 1  and Qty < 5  and QP <  500: Discount = 0
elif Qty >= 1  and Qty < 5  and QP <  2000 and Member is "Y": Discount = 7
elif Qty >= 1  and Qty < 5  and QP <  2000 and Member is "N": Discount = 5
elif Qty >= 1  and Qty < 5  and QP >= 2000 and Member is "Y": Discount = 10
elif Qty >= 1  and Qty < 5  and QP >= 2000 and Member is "N": Discount = 8
 
elif Qty >= 6  and Qty < 20 and QP <   500 and Member is "Y": Discount = 3
elif Qty >= 6  and Qty < 20 and QP <   500 and Member is "N": Discount = 2
elif Qty >= 6  and Qty < 20 and QP <  2000 and Member is "Y": Discount = 12
elif Qty >= 6  and Qty < 20 and QP <  2000 and Member is "N": Discount = 10
elif Qty >= 6  and Qty < 20 and QP >= 2000 and Member is "Y": Discount = 25
elif Qty >= 6  and Qty < 20 and QP >= 2000 and Member is "N": Discount = 15

elif Qty >= 21 and Qty < 99 and QP <   500 and Member is "Y": Discount = 5
elif Qty >= 21 and Qty < 99 and QP <   500 and Member is "N": Discount = 3
elif Qty >= 21 and Qty < 99 and QP <  2000 and Member is "Y": Discount = 16
elif Qty >= 21 and Qty < 99 and QP <  2000 and Member is "N": Discount = 15
elif Qty >= 21 and Qty < 99 and QP >= 2000 and Member is "Y": Discount = 30
elif Qty >= 21 and Qty < 99 and QP >= 2000 and Member is "N": Discount = 20

print("Discount = ", Discount)