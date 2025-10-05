x = int('42') #можно преобразовать
print(x)

y = int(-12.12) #можно преобразовать
print(y)

#s = int('123e')
#print(s) нельзя(Ошибка:ValueError: invalid literal for int() with base 10: '123e')
#Содержит кириллическую букву 'е'

#a = int('91.4')
#print(s) нельзя(Ошибка:ValueError: invalid literal for int() with base 10: '91.4')
#Строка содержит десятичную точку

#z = int(524.345 ** 435345345311145345)
#print(z) нельзя(Ошибка:OverflowError: (34, 'Result too large')
#Настолько большое число что не вмещаеться в строку

#f = int('7.1 + 4')
#print(f) нельзя(Ошибка:ValueError: invalid literal for int() with base 10: '7.1 + 4'
#Это строка с арифметическим выражением, а не числовое значение

#g = int('4' - 2)
#print(g) нельзя(Ошибка:TypeError: unsupported operand type(s) for -: 'str' and 'int')
#Это выражение пытается вычесть число из строки, что вызывает ошибку

#h = int('4 - 2')
#print(h) нельзя(Ошибка:ValueError: invalid literal for int() with base 10: '4 - 2')
#Это строка с арифметическим выражением
