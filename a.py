class Employee:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
    def __call__(self, *args: any, **kwds: any) -> any:
        print('HEllo')
    def fullname(self):
        print(type(self))
        return self.first + ' ' + self.last
    def __setattr__(self, __name: str, __value: any) -> None:
        if self.__dict__ == None:
            self.__dict__ = {}
        if self.__dict__.get(__name):
            print('Fuck Urself')
            return None
        self.__dict__[__name] = __value

        print(self.__dict__)
        return None
    def __getattribute__(self, name) -> any:
        return self.__dict__['e']
        
        
emp1 = Employee('Milind', 'Bharambe')
print(emp1.__setattr__('e', 'abcd'))
print(emp1.__setattr__('e', 'abd'))
# print(emp1)
# print(emp1.e)
