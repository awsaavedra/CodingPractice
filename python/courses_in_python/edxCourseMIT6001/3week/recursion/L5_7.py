'''
For this problem, write a recursive function, lenRecur, 
which computes the length of an input argument (a string), 
by counting up the number of characters in the string
'''

def lenRecur(aStr):
  if aStr == '':
    return 0
  else:
    return 1 + lenRecur(aStr[0:-1])

print lenRecur("abcd")
