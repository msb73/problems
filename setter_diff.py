class Geeks:
     def __init__(self):
          self._age : int
       
     # using property decorator
     # a getter function
     def age(self):
         print("getter method called")
         return self._age
     def __setattr__(self, __name: str, __value: any) -> None:
        print('__value = ' + str(__value))
        if(__value < 18):
           raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self.__dict__[__name] = __value
mark = Geeks()
  
mark.age = 20
  
print(mark.age)
[[72.85043152431703,18.667656401984026],[72.853156635447,18.667676752664697],[72.85639675716615,18.669160727095218],[72.8582635494424,18.672535216349708],[72.85892876247621,18.675909697119614],[72.85498055080629,18.67058372505297],[72.85043152431703,18.667656401984026]]