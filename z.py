class Request:
    def __init__(self, id, oid, sla) -> None:
        self.id = id
        self.oid = oid
        self.sla = sla
        self.rs = 'Open'
        self.rp = 'NA'

class Helpdesk:
    dic = {'High' : 1, 'Medium' : 2, 'Low' : 3}
    def __init__(self, ls) -> None:
        self.ls = ls

    def sm(self):
        for i in self.ls:
            if i.sla >= 5:
                i.rp = 'low'
            elif i.sla >= 3 and i.sla < 5:
                i.rp = 'Medium'
            elif i.sla < 3 :
                i.rp = 'High'

    def tm(self, eoid, n):
        cl = []
        counter = 0
        self.ls = sorted(self.ls, key = lambda x : Helpdesk.dic[x.rp])
        (lambda l: i for i in l(self.ls))
        for i in self.ls:
            if i.oid == eoid:
                if counter >= n:
                    break
                counter += 1
                i.rs = 'Closed'
        self.ls = sorted(self.ls, key= lambda x : x.id)
        if counter == 0:
            print('No records found!')
        else:
            print('No of records closed: '+ str(counter))
        for i in self.ls:
            print(f'{i.id} {i.rs}')
ls = []
# for _ in range(int(input())):
#     ls.append(
#         Request(int(input()),
#         input(),
#         int(input())
#         )
#     )
# print('sdf')
# oid = str(input())
# n = int(input())
# hd1 = Helpdesk(ls)
# hd1.sm()
# hd1.tm(oid, n)

