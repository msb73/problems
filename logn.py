ls1 = [1,3,5,8,9,11]
ls2 = [2,4,6,7,10,12]
import time
timer = 0
while True:
    time.sleep(1)
    if len(ls1) and len(ls2):
        if ls1[len(ls1)//2 -1] < ls2[len(ls2)//2 -1]:
            for i in range((len(ls1)//2) -1):
                timer +=1 
                print(f'ls1 =   {ls1}           middle = {ls1[len(ls1)//2 -1 ]}', end= '	')
                print(f'timer = {timer}   drop = {ls1[i]}')
            ls1 = ls1[len(ls1)//2 -1 :]
            
            print(ls1)

        else:
            
            print(ls2)
            for i in range((len(ls2)//2) -1):
                timer +=1
                print(f'ls2 =   {ls2}           middle = {ls2[len(ls2)//2 -1 ]}',end= '		')
                print(f'timer = {timer}   drop = {ls2[i]}')
            ls2 = ls2[len(ls2)//2 -1:]
    # if len(ls2):
    #     ls21 , ls22 = ls2[:len(ls2)//2+1] , ls2[len(ls2)//2+1:]
