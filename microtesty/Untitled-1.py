def tax_calc():
    tax= 1.08875
    subtotal = input('subtotal?')
    subtotal= float(subtotal)
    with_tax = subtotal*tax
    return  'with_tax: %f' % with_tax
    #return with_tax

#def tip_calc(with_tax):
 #   tip_percentage = input('tip percentage?')
 #   total = tip_percentage*with_tax
 #   return 'with tip: %d' % total

print (tax_calc())
