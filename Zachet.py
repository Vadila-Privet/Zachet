# 3 числа - упорядочивание в порядке неубывания
value4=0
value1 = input()
value2 = input()
value3 = input()
if value1 >= value2:
    value4=value1
    value1=value2
    value2=value4
if value2 >= value3:
    value4=value2
    value2=value3
    value3=value4
if value1 >= value2:
    value4=value1
    value1=value2
    value2=value4
print(value1, value2, value3)