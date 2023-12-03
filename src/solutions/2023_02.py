from utils import *
from collections import defaultdict 

#@answer_part_a(year=2023, day=2)
def part_1(lines):
    part_a=0
    for line in lines:
        flag = True
        id , game = line.split(':')
        for turn in game.split(';'):
            for balls in turn.split(','):
                n, color = balls.split()
                if int(n)> {'red':12,'green':13, 'blue':14}.get(color,0):
                    flag = False
        if flag==True:
            part_a += int(id.split()[-1])
            #print(id)
    return(part_a)

@answer_part_b(year=2023, day=2)
def part_2(lines):
    part_b=0
    for line in lines:
        id , game = line.split(':')
        Val=defaultdict(int)
        for turn in game.split(';'):
            for balls in turn.split(','):
                n, color = balls.split()
                n = int(n)
                Val[color] = max(Val[color],n)
        score = 1
        for v in Val.values():
            score*=v
        part_b +=score
    return(part_b)