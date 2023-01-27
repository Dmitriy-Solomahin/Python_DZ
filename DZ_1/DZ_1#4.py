# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no
def checking_area(x, y, summa):
    n =1
    result = False 
    while n <= x:
        if (n*y) == summa:
            result = True
            break
        elif (n*y) > summa:
            break
        n+=1
    return result

length = int(input("длина шоколадки: "))
width = int(input("ширина шоколадки: "))
required_area = int(input("сколько нужно долек: "))

if required_area > (length*width):
    result = False
else:
    result = checking_area(length, width, required_area)
    if result == False:
        result = checking_area(width, length, required_area)

if result == True:
    print("можно получить за один разлом: ")
else:
    print("за один разлом столько кусочков получить нельзя")

