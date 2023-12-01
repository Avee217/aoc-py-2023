from utils import *

@answer_part_a(year=2023, day=1)
def part_1(lines):
    # print(lines)
    part_a = 0
    part_b = 0

    for each in lines:
        part_a_digits = []
        part_b_digits = []
        for i,x in enumerate(each):
            if x.isdigit():
                part_a_digits.append(x)
                part_b_digits.append(x)
            for j,val in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
                if each[i:].startswith(val):
                    part_b_digits.append(str(j+1))
        part_a += int(part_a_digits[0]+part_a_digits[-1])
        #print(part_a)
        part_b += int(part_b_digits[0]+part_b_digits[-1])
        #print (part_b)
    #return (part_a)
    return (part_b)