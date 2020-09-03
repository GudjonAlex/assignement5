#1. Taka við int breytu frá notenda
#2. Safna hæstu tölu þangað til neikvæð tala er sett inn
#3. Eftir að neikvæð tala er sett inn, prenta hæstu tölu sem kom fram

num_int = int(input("Input a number: "))    # Do not change this line

temp_num_int = num_int
highest_num_int = temp_num_int
while num_int >= 0:
    temp_num_int = num_int
    if temp_num_int > highest_num_int:
        highest_num_int = temp_num_int
    else:
        temp_num_int = temp_num_int

    num_int = int(input("Input a number: "))

max_int = highest_num_int

print("The maximum is", max_int)    # Do not change this line
