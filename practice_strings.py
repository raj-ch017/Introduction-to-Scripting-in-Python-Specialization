"""
Practice Exercises for Strings - Course 2, Week 1
"""

from timeit import repeat


def two_chars(example_string):
    first_char = example_string[0]
    last_char = example_string[-1]
    out_string = first_char + last_char
    print(out_string)

#two_chars("It's just a flesh wound")

def all_but_two(example_string):
    if (len(example_string)>= 2):
        a = example_string[1:-1]
        print(a)

#all_but_two("It's a flesh wound")

def this_time_threes(example_string):
    if (len(example_string)>=3):
        first_chars = example_string[:3]
        last_chars = example_string[-3:]
        out_string = first_chars + last_chars
        print(out_string)

#this_time_threes("It's a flesh wound")

def echo(call,repeats):
    print ((call+"\n")*repeats)

#echo("The choice has already been made!",3)

def is_substring(example_string,test_string):
    if test_string in example_string:
        return True
    else:
        return False
    
#print(is_substring("The universe is reaching out.","demon"))

def make_nametag(name,topic):
    print("Hi! My name is {}. This lecture covers {}.".format(name,topic))

#make_nametag("Rajdeep","Python")

def make_int(int_string):
    if int_string.isdigit():
        if int(int_string)<0:
            return -1
        return int(int_string)
    else:
        return -1

#print(make_int("-123")) 

def name_swap(name_string):
    space_pos = name_string.find(" ")
    first1 = name_string[0].upper()
    first2 = name_string[1:space_pos]
    first_name = first1 + first2
    last1 = name_string[space_pos+1].upper()
    last2 = name_string[space_pos+2:]
    last_name = last1 + last2 
    print(last_name,first_name)

#name_swap("ratnopriya chatterjee")