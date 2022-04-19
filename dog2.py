# задаём переменные, которые будут в теле while
count = 0
distance = 100 # километров, например
firstfriendsp = 5 # км/ч
secondfriensp = 4 # км/ч
dogspeed = 7 # км/ч
friend = 2

# while = loop (C++,C#) задаём условие, которое надо проверять постоянно, 
# непрогнозируемое количество раз
while distance > 10:
    if friend == 1: # == это проверка на соответсвие, сравниение, равно ли?
        time = distance / (firstfriendsp + dogspeed)
        friend = 2
    else: 
        time = distance / (secondfriensp + dogspeed)
        friend = 1
# if-else должны покрывать все возможные значения, если-то
    distance = distance - (firstfriendsp - secondfriensp) * time
# пишем эту дистанс на уровное вайла, потому что это внутри одного цикла
# теперь мы вычитаем скорости, так как теперь они идут в одном направлении, 
# разница будет считаться только, если скорость первого будет меньше второго
    count +=1
# или count +=1 значит увиличиваем (но можно и делить /=, умножать *=, вычитать -=)
print(count)