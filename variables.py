# Variables
#  • Variables allow you to store values 
# • A variable has a valid name (letters, digits, underscore, not a reserved keyword)
#  • Python is dynamically typed: variables can be redeclared
#  • We can use shortcut operators in order to cleanly redeclare a variable
#  • We can combine text and variables using the + operator in the print function


# this is how we comment in python just use #



amount_of_apple = 2
cost_of_apple = 5
print(amount_of_apple * cost_of_apple)

# Valid Variable Names
#  amount_of_apples
#  cost_of_apple
#  _total_cost
#  COST_OF_APPLE



#  Invalid Variable Names
#  am*unt_o%_app|es
#  c*st_o%_app|e
#  5apples_cos

# Reserved Keywords
#  False #  None #  True #  and #  as #  assert
#  break #  class #  continue #  def #  del
#  elif #  else #  except #  finally #  for
#  from #  global #  if #  import #  in
#  is #  lambda #  nonlocal #  not #  or #  pass
#  raise #  return #  try #  while #  with #  yield

# without short cut Operator

cost_of_apple = cost_of_apple + 2
print(cost_of_apple)
cost_of_apple = cost_of_apple - 2
print(cost_of_apple)
cost_of_apple = cost_of_apple * 2
print(cost_of_apple)
cost_of_apple = cost_of_apple ** 2
print(cost_of_apple)
cost_of_apple = cost_of_apple / 2
print(cost_of_apple)
cost_of_apple = cost_of_apple // 2
print(cost_of_apple)
cost_of_apple = cost_of_apple % 2
print(cost_of_apple)


# with short cut Operator (assignment operator)

cost_of_apple1 = 6
print("Cost of apple: ", cost_of_apple1)
cost_of_apple1 += 2
print("Cost of apple: ", cost_of_apple1)
cost_of_apple1 -= 2
print("Cost of apple: ", cost_of_apple1)
cost_of_apple1 *= 2
print("Cost of apple: ", cost_of_apple1)
cost_of_apple1 **= 2
print("Cost of apple: ", cost_of_apple1)
cost_of_apple1 /= 2
print("Cost of apple: ", cost_of_apple1)
cost_of_apple1 //= 2
print("Cosst of apple: ", cost_of_apple1)
cost_of_apple1%= 2  
print("Cost of apple: ", cost_of_apple1)


