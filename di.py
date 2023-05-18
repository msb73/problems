from dataclasses import dataclass


@dataclass
class Cafe:
    regno : int
    name : str
    cost : int
    loc : str
    demand : list
    status : str

@dataclass
class Party:
    cafe : list
    loc_per : dict

    def final_cost(self, regno):
        return (lambda x , y: i.cost + (i.cost * (self.loc_per[i.loc] / 100)) if i.regno == y for i in x )(self.care, regno)
        for i in self.cafe:
            if i.regno == regno:
                return i.cost + (i.cost * (self.loc_per[i.loc] / 100))
    def available_cafe(self, loc, budget):
        dic = {i.name : i.cost for i in self.cafe if i.loc == loc and i.status == 'Available'}
        if len(dic)  == 1:  return list(dic.keys())
        if len(dic) == 0:   return []

        minvalue = min(dic, key= lambda x : dic[x])
        return  sorted(filter(lambda x : dic[x] == minvalue, dic.keys()))


ls = []
for i in range(int(input())):
    regno = int(input())
    ls.append(Cafe(
        regno,  #reg_no
        input(),    # name
        int(input()), #cost
        input(),        #loc
        [int(input()) for _ in range(7)], # list
        input()) # status)
    )
dic = {}
print('for is starting')
for _ in range(4):
    location = input()
    percentage = int(input())
    dic[location] = int(percentage)


party1 = Party(ls, dic)
finalcost = party1.final_cost(int(input()))
ava_cafe = party1.available_cafe(input(), int(input()))
print(finalcost)
if len(ava_cafe) == 0:
    print('No cafe is Available')
else:
    print(*ava_cafe)