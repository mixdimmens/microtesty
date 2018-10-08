#attempting to create a tax calculator. wish me luck!

#tax = 2
#subtotal = 1.0



def tax_calc():
    #tax = .08875
    #print('subtotal?')
    subtotal = input('subtotal ammount?')
    subtotal = float(subtotal)
    tax = subtotal*.08875
    print ('tax: %f') % tax
    return (tax)
    #total = subtotal*(tax*.001)
    #print("$")
#rint(atmpt)

#atmpt()
#atmpt(subtotal)

def tip_calc():
    #tax_calc()
    #subtotal = input('subtotal ammount?')
    #subtotal = float(subtotal)
    #subtotal = tax_calc()
    tip_percentage = input ("tip percent?")
    tip_percentage = float(tip_percentage)
    tip_percentage = tip_percentage/100
    tip = tip_percentage*(tax_calc()/.08875)
    print('tip: %f') % tip
    return (tip)

#print(tax_calc + tip_calc)

def bill_total_calc():
    #tip_calc()
    total = tip_calc()+tax_calc()+(tax_calc()/.08875)
    print('bill total is: %f') % total
    
#tax_calc()

bill_total_calc()

