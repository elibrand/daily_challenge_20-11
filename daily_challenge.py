import string

code = [['7', ' ', '3'], ['T', 's', 'i'], ['h', '%', 'x'], ['i', ' ', '#'], ['s', 'M', ' '], ['$', 'a', ' '], ['#', 't', '%'], ['i', 'r', '!']]

first_third = []
second_third = []
third_third = []


for triplet in code:
    first_third.append(triplet[0][0])


for triplet in code:
    second_third.append(triplet[1][0])


for triplet in code:
    third_third.append(triplet[2][0])


final_string = ''.join(first_third + second_third + third_third)

actually_final_string = []


for symbol in final_string:
    if symbol in string.ascii_letters:
        actually_final_string.append(symbol)


print(''.join(actually_final_string))







