#for j in [1, 2, 3]:
  #  print(j)
 
 
 
#for i in range(1,4):
#    print(i)



##for i in range(1,11):
##    print (i)



#a = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#for k in range(len(a)):
#    print(a[k])
    
    
    
    
#for i in range(0,10,2):
#        print(i)



##for star in range(0,4):
##    print(4 * "*")
  
  
##for star in range(0,4):
##    print(star * '*')



##def pyramid():
##    for star in range(0,4):
##        print(star * '*')
##    for star in range(4,0,-1):
##        print(star * '*')
##pyramid()
    
    
    

##def letterSearch(string): 
##  for letter in string:
##     if letter == 'a':
##        return True
##
##data = 'this is papa erbynn'
##print(letterSearch(data))




##def anyLetterSearch(string,alphabet):
##    for letter in string:
##        if letter == alphabet:
##            return True
##
##data = 'this is papa erbynn'
##print(anyLetterSearch(data,'r'))





def anyLetterSearch2(string):
    let1=False
    let2=False
    for letter in string:
        if letter == 's':
            let1 = True
        elif letter == 'm':
            let2 = True
    if let1 and let2:
        return True
    else:
        return False
    
data = 'this is papa erbynn'
print(anyLetterSearch2(data))