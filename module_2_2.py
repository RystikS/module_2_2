#Первый вариант
first = int(input('Введите первое число', ))
second = int(input('Введите второе число', ))
third = int(input('Введите третье число'))
if first==second and second==third and first==third:
  print('3')
elif first==second or second==third or first==third:
  print('2')
else:
  print('0')
  
#Второй вариант
first = int(input('Введите первое число', ))
second = int(input('Введите второе число', ))
third = int(input('Введите третье число'))
a = first/second
b = first/third
c = second/third
sum = (a+b+c)
sum_1 = (a+b)
if sum==3:
  print('3')
elif sum_1>1:
  print('2')
else:
  print('0')

