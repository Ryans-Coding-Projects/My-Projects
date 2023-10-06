#This program is used to determine an items amount during a sale.

cost = float(input("Enter cost of item before sale: "))

sale_amount = float(input("Enter sale percentage: "))

sale = cost - (sale_amount * cost)

print(f"The price of this item on sale is {sale}")
