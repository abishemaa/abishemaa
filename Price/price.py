# input section
# prompt the price excluding the tax
price_excl_tax = float(input("enter the price of the item (excluding the tax):"))
while price_excl_tax <= 0:
    price_excl_tax = float(input("enter the valid price:"))
# prompt the number of the items for that price
num_items = int(input("enter the number of items:"))
while num_items <= 0:
    num_items = int(input("enter the number of items:"))
# prompt for vat rate
vat_rate = int(input("enter the vat rate:"))
while vat_rate < 0 or vat_rate > 100:
    vat_rate = int(input("enter the vat rate(0-100):"))
# calculation section
# calculate the total amount of the items
total_price_excl_tax = price_excl_tax * num_items
# calculate the vat rate for the total price
vat_amount = total_price_excl_tax * (vat_rate / 100)
# add total price of the items and the vat amount to gain total price including tax
total_price_incl_tax = total_price_excl_tax + vat_amount

# output section
print("total price including tax: ", total_price_incl_tax)
