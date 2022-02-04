print("VAT Calculator")
print("")

inex = input("Please enter a 1 for including or a 2 for excluding: ")
vat = int(input("Please enter the VAT percentage: "))
print("")
if inex == '1':
    price = float(input("Please enter amount including VAT: R"))
    print("")
    print("VAT amount: R",price * (100/(100+vat)))
    print("Price excluding VAT: R",price - (price * (vat/100)))
elif inex == '2':
    price = float(input("Please enter amount excluding VAT: R"))
    print("")
    print("VAT amount: R",price * (100/(100+vat)))
    print("Price including VAT: R",price + (price * (vat/100)))
else:
    print("Incorrect value given")
