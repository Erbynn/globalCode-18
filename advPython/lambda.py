#def is_even():  num = input('>Enter a number: ')
#  if num % 2 == 0:
#    return 'True'
#print(is_even())



#items = [1,2,3,4]
#squares = list(map((lambda x: x ** 2), items)) #bring list for python3
#print(squares)


numbers = [1,56,234,87,4,76,42,69,90,135]

#using function
#def is_even2():
#   for number in numbers:
#      if number%2 == 0:
#         print(number)
#is_even2()

#using lambda
showList = list(map((lambda arg: arg), numbers)) #map ... used to print all elements
print(showList)

is_even = list(filter((lambda arg: arg%2 == 0), numbers)) #filer...to get a subset of elements
print(is_even)

is_odd = list(filter(lambda x: arg%2 != 0, number))

