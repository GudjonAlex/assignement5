#1. Sequencið byggir á að x(n)=x(n-1)+x(n-2)+x(n-3)
#2. Ef n=1,2,3 er ekki hægt að bæta við fyrri 3 breytum svo þau tilfelli
#   þurfa að vera sér
#3. Prenta út viðeigandi tölu þangað til að n-skiptum hefur verið náð

n = int(input("Enter the length of the sequence: ")) # Do not change this line

#Einfaldast að hafa fyrstu þrjár áður en lykkjan byrjar

x_1 = 1
x_2 = 2
x_3 = 3

if n == 1:
    print(x_1)
elif n == 2:
    print(x_1)
    print(x_2)
elif n == 3:
    print(x_1)
    print(x_2)
    print(x_3)
elif n > 3:
    print(x_1)
    print(x_2)
    print(x_3)
    for i in range(3,n):
        number = x_1 + x_2 + x_3
        x_1 = x_2
        x_2 = x_3
        x_3 = number
        print(number)