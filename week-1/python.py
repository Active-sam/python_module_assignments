number1 = float(input('first number'))
oparator = input('oparater (+, -, /, x)')
number2 = float(input('second number'))

if oparator == '+':
  result = number1 + number2
elif oparator == '-':
  result = number1 - number2
elif oparator == '*':
  result = number1 * number2
elif oparator == '/':
  result = number1 / number2
else:
  print('inappropriete oparator')

print(f"{number1} {oparator} {number2} = {result}")