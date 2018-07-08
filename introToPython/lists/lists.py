#list = [] #just like the array
#list.append('a') #pushes 'a' into the array
#print list 

#printing even numbers between min and max number
def evenBtn(): #if u pass in arguments u cannot take user input
    min1 = int(input('> min: '))
    max1 = int(input('> max: '))

    numStorage = []
    for number in range(min1,max1):
               if number % 2 == 0:
                   numStorage.append(number)
                   
    return numStorage

print(evenBtn())
    
