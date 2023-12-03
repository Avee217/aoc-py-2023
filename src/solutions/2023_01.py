from utils import *

#@answer_part_a(year=2023, day=1)
def part_1(lines):
    # print(lines)
    part_a = 0
    for each in lines:
        part_a_digits = []
        for i,x in enumerate(each):
            if x.isdigit():
                part_a_digits.append(x)         
        part_a += int(part_a_digits[0]+part_a_digits[-1])
        #print(part_a)
    return (part_a) 

@answer_part_b(year=2023, day=1)
def part_2(lines):
    part_b = 0
    for each in lines:
            part_b_digits = []
            for i,x in enumerate(each):
                if x.isdigit():
                    part_b_digits.append(x)
                for j,val in enumerate(["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                    if each[i:].startswith(val):
                        part_b_digits.append(str(j))
            part_b += int(part_b_digits[0]+part_b_digits[-1])
            #print (part_b)
    return (part_b)