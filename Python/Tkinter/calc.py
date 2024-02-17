a = float(input("enter the first operand"))
op = input("enter the operation")
b = float(input("enter the second operand")) 

result = 0.0

if op == '+':
	result = a+b
	print(f'result = {result}')
elif op == '-':
	result = a-b
	print(f'result = {result}')

elif op == '*':
	result = a*b
	print(f'result = {result}')

elif op == '/':
	result = a/b
	print(f'result = {result}')

else:
	print(f"Simple calculators dont support {op}")
	
	