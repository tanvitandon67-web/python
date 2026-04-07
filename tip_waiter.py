def total_bill(bill_amount,tip_precentage) :
    total = bill_amount + (tip_precentage / 100)* bill_amount
    total = round(total,2) 
    print("total amount that you have to pay ",total)

total_bill(150,20)
