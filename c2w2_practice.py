"""
Practice assignments for course 2 - week 2
"""

def first_last_list(example_list):
    out_list = []
    out_list.append(example_list[0])
    out_list.append(example_list[-1])
    print(out_list)

#first_last_list([2,3,5,7,11,13])

def create_true_false():
    out_string = []
    for index in range(16):
        if index > 7:
            out_string.append("False")
        else:
            out_string.append("True")
    print(out_string)

#create_true_false()

def word_count(text,word):
    count = 0
    word_list = text.split(" ")
    for words in word_list:
        if words == word:
            count = count + 1
    print(count)

#word_count()

def list_max(num_list):
    max_ele = num_list[0]
    for element in num_list:
        if element > max_ele:
            max_ele = element
    return max_ele

#print(list_max([4]))
#print(list_max([-3, 4]))
#print(list_max([5, 3, 1, 7, -3, -4]))
#print(list_max([1, 2, 3, 4, 5]))

def concatenate_ints(int_list):
    x = " "
    for element in int_list:
        x = x + str(element)
    return int(x)

#print(concatenate_ints([4]))
#print(concatenate_ints([4, 0, 4]))
#print(concatenate_ints([123, 456, 789]))
#print(concatenate_ints([32, 796, 1000]))

def strange_sum(numbers):
    sum = 0
    for number in numbers:
        if (number % 3 != 0):
            sum = sum + number
    return sum

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))