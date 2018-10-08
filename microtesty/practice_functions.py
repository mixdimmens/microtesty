# practice functions from codeacademy python course, saved here for posterity and because we don't know git

#factorials any integer or float you parse through it, y'all

def factorial(x):
  total= 1
  while x>0:
    total*=x
    x-=1
  return total
    
print (factorial(22))


#looks for word in text and replacees it with asterisks for as many characters as word happens to be

def censor(text, word):
  #while word in text:
  new_text=text
  new_word = '*'*len(word) 
  i=0
  while i<len(text)-len(word)+1:#cycle through program for as many cycles as
    # text is long minus the lenght of word(which would be uneseccary as the 
    # remaining range in text would be shorter than word anyway)

    #print (len(word)) #prints the length of word
    print (text[i:i+len(word)]) #print a range from text that's as long as 
    #word is, starting from i, so the cycle number we're on within text. 
    # this allows us to pull any sting out of text that then may be compaired
    #  to word
    if text[i:i+len(word)]==word: #puts the above into action, compairing a 
      #range from text starting at i and ending at i plus the length of word 
      # to word itself in an if statement 

      #new_word = '*'*len(word) 
    #print (i)
    #print (text[i:i+len(word)])
      new_text=new_text[:i]+new_word+new_text[i+len(word):len(text)] #assembles 
      #the ranges of text that we want from before the replaced segment, 
      # followed by the asterisks the length of word, followed by the range of 
      # text that comes after the word found by our above if statement

    #print
      
      #text[i:len(word)].append(new_word)
      #text[i:len(word)]'*'*len(word)
    print (new_word)#test
    print (new_text)#test
    i+=1
  return new_text #shoot

print(censor('testy test test. this is just a test', 'test'))

# same as function above, but without the explanations /(

def censor2(text, word):
  new_text=text
  new_word = '*'*len(word) 
  i=0
  while i<len(text)-len(word)+1:
    print (text[i:i+len(word)])
    if text[i:i+len(word)]==word:
      new_text=new_text[:i]+new_word+new_text[i+len(word):len(text)] #assembles 
    i+=1
  return new_text #shoot



def count(sequence, item):
  i=0
  increment=0
  sequence_length=sequence
  if type(sequence)==int:
    sequence=str(sequence)
    item=str(item)
    for n in range(len(sequence)):
      if sequence[n:n+len(item)]==item:
        increment+=1
  elif type(sequence)==str:
    for i in range(len(sequence)):
      if sequence[i:i+len(item)]==item:
          increment+=1
  elif type(sequence)==list:
    sequence_length=str(sequence_length)
    item=str(item)
    for n in range(len(sequence_length)):
      if sequence_length[n:n+len(item)]== item:
        increment+=1
      else:
        continue
  return increment
    
def county(sequence, item):
  i=0
  increment=0
  sequence_length=sequence
  item_length=item
  if type(sequence)==int:
    print('int!')
    sequence=str(sequence)
    item=str(item)
    #item=str(item)
    for n in range(len(sequence)):
      if sequence[n:n+len(item)]==item:
        increment+=1
        print ('count: '),
        print (increment)
  elif type(sequence)==str:
    print('str!')
    for i in range(len(sequence)):
#      print(sequence[i:i+len(item)])
#      print (i)
      if sequence[i:i+len(item)]==item:
          increment+=1
          print('count: '),
          print (increment)
  elif type(sequence)==list:
    print('list!')
    sequence_length=str(sequence_length)
    item_length=str(item_length)
#    item=str(item)
    for n in range(len(sequence)):
#      while len(sequence[n:])<len(item_length):
      if type(sequence[n])!=type(item):
        pass
      elif type(sequence[n])==type(item) and sequence[n]==item:
        increment+=1
      else:
        pass
#    else:
#      ss 
#    for n in range(len(sequence_length)):
#      while len(sequence_length[n+len(item)])<len(sequence_length): 
#      if sequence_length[n:n+len(item)]== item:
#        increment+=1
#        print('increment: ')
#        print(increment)
#      else:
#        print (n)
  return increment


def median(x):
  y=x
  y.sort()
  print (y)
  avg=0
  lgth=float(len(x))#/2.0
  print ('lgth: '),
  print (lgth)
  if lgth/2.0 ==lgth//2: #even list length handling
    print ('even!')
    lgth2=len(x)//2
    print (x[lgth2-1])
    print (x[lgth2])
    avg=float((y[lgth2-1]+y[lgth2]))
    avg=avg/2.0
  else:# odd list length handling, needs to be flusehd out
    print ('odd!')
    lgth2=len(x)//2
    print ('median index value: ',)
    print (lgth2)
    avg=y[lgth2]
  return avg
    
    

    
    
    
    
    