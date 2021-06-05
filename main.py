# def find_largest_element(num_1, num_2, num_3):
#   """Given three numbers, return the largest."""
#   #jupiter
#   if(num_1 > num_2 and num_1 > num_3):
#     return num_1
#   elif(num_2 >num_1 and num_2>num_3):
#     return num_2
#   elif(num_3>num_1 and num_3>num_2):
#     return num_3

# print(find_largest_element(6,8,9))   
def factorial(num):
  """Given a number, calculate the factorial. All numbers >= 0
  
  The factorial of 4 is 4 * 3 * 2 * 1 == 24
  """
  fact=1
  for i in range(1,num+1):
      fact *= i
  return fact 
  
   

var = factorial(4)
print(var)  