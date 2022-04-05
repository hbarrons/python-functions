# def sum_to(num):
#   sum = 0
#   for n in range(1, num + 1):
#    sum += n
#   return sum

# print(sum_to(6))
# print(sum_to(10))



# def largest(list):
#   list.sort()
#   print(list[-1])

# largest([1, 2, 3, 4, 0]) 
# largest([10, 4, 2, 231, 91, 54])  


# def occurrences(str1, str2):
#   print(str1.count(str2))

# occurrences('fleep floop', 'e')
# occurrences('fleep floop', 'p')
# occurrences('fleep floop', 'ee')
# occurrences('fleep floop', 'fe')

def product (*args):
  num = 1
  for i in args:
    num *= i
  print(num)


product(-1, 4) 
product(2, 5, 5)
product(4, 0.5, 5)