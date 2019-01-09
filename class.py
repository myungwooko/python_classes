class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)


#
emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Kim', 'hoon', 40000)
emp_1.apply_raise()

print(emp_1)
print(emp_1.first)
print(emp_1.pay)
print(str(emp_1))
print(emp_1.__len__())
print(len(emp_1))
print(1, add(emp_1, emp_2))
print(2, emp_1.add(emp_2))
print(3, emp_1.__add__(emp_2))

print(f'Before fullname : {emp_1.fullname}')

emp_1.fullname = 'Corey Schafer'

print(f'After first    : {emp_1.first}')
print(f'After email    : {emp_1.email}')
print(f'After fullname : {emp_1.fullname}')

del emp_1.fullname

print(f'After delete first    : emp_1.first')
print(f'After delete email    : emp_1.email')
print(f'After delete fullname : emp_1.fullname')


# Inheritance1
class Developer(Employee):
    raise_amt = 1.9

    def __init__(self, prog_lang, **kwargs):
        super().__init__(**kwargs)
        self.prog_lang = prog_lang


dev_1 = Developer('Mw', 'Ko', 35000, 'Python')

print(dev_1.pay)

dev_1.apply_raise()

print(dev_1.pay)
print(dev_1)
print(dev_1.fullname)


# inheritance2
class Manager(Employee):
    raise_amt = 1.5

    def __init__(self, employees=None, **kwargs):
        super().__init__(**kwargs)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp)


#
mng_1 = Manager('Sw', 'J', 50000, ['a', 'b', 'c', 'd', 'k'])

print(mng_1)
print('These are before')
mng_1.print_emps()
mng_1.add_emp('z')
print('These are after')
mng_1.print_emps()


class Unknown(Developer, Manager):
    def __init__(self, first, last, pay, prog_lang, employees=None):
        super().__init__(first=first, last=last, pay=pay, prog_lang=prog_lang, employees=employees)
        print('I can be a manager or developer whatever I want to')


unk_1 = Unknown('Myungwoo', 'Ko', 40000, 'Python', ['a', 'b'])
print('Unknown raise_amt: ', unk_1.raise_amt)
unk_1.apply_raise()
print(unk_1.pay)
print(unk_1.prog_lang)
print('before emps: ')
unk_1.print_emps()
unk_1.add_emp('z')
print('after emps: ')
unk_1.print_emps()


class Animal:
    def __init__(self):
        print("I'm an animal")


class Human(Animal):
    def __init__(self):
        super().__init__()
        print("I'm a human")


class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("I'm a bird")


class Unknown(Human, Bird):
    def __init__(self):
        super().__init__()
        print("I'm Unknown. Please give me a name")


instance = Unknown()


# =>
# I'm an animal
# I'm a bird
# I'm a human
# I'm Unknown. Please give me a name


# Method bound checker
class Test:
    def ins(self):
        return 'instance method'

    @staticmethod
    def static():
        return 'static method'

    @classmethod
    def classM(cls):
        return 'class method'


a = Test()

print(
    '------------------------------------------------------------------------------------------------------------------------------------')
print('인스턴스를 통한 instance method 호출 : ', a.ins)
print('인스턴스를 통한 instance method 실행 : ', a.ins())
print(
    '------------------------------------------------------------------------------------------------------------------------------------')
print('인스턴스를 통한 staticmethod 접근 : ', a.static)
print('인스턴스를 통한 staticmethod 실행 : ', a.static())
print(
    '------------------------------------------------------------------------------------------------------------------------------------')
print('인스턴스를 통한 classmethod 접근 : ', a.classM)
print('인스턴스를 통한 classmethod 실행 : ', a.classM())
print(
    '------------------------------------------------------------------------------------------------------------------------------------')
print('클래스를 통한 instance method 접근 : ', Test.ins)
print('클래스를 통한 instance method 실행 by Test.ins()  : "TypeError: ins() missing 1 required positional argument"')
print('클래스를 통한 instance method 실행 by Test.ins(a) : ', Test.ins(a))
print(
    '------------------------------------------------------------------------------------------------------------------------------------')
print('클래스를 통한 staticmethod 접근 : ', Test.static)
print('클래스를 통한 staticmethod 실행 : ', Test.static())
print(
    '------------------------------------------------------------------------------------------------------------------------------------')
print('클래스를 통한 classmethod 접근 : ', Test.classM)
print('클래스를 통한 classmethod 실행 : ', Test.classM())

print(
    '------------------------------------------------------------------------------------------------------------------------------------')


# An example of inheritance connection
class A:
    def __init__(self):
        print('Initializing: class A')

    def sub_method(self, b):
        print('Printing from class A:', b)


class B(A):
    def __init__(self):
        print('Initializing: class B')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class B:', b)
        super().sub_method(b + 1)


class C(B):
    def __init__(self):
        print('Initializing: class C')
        super().__init__()

    def sub_method(self, b):
        print('Printing from class C:', b)
        super().sub_method(b + 1)


if __name__ == '__main__':
    c = C()
    c.sub_method(1)

    To
    understand
    decorator


def do_twice(func):
    def wrapper(*args):
        func(*args)
        return func(*args)

    return wrapper


@do_twice
def say_whee():
    print("Whee!")


@do_twice
def greet(name):
    print(f"Hello {name}")


say_whee()
greet("World!")


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


a = return_greeting("Adam")
print(a)

print(id(2))
a = 2
b = 2
print(id(a))
print(id(b))


class AbstractClass(object):

    def __new__(cls, a, b):
        instance = super().__new__(cls)
        instance.__init__(a, b)
        return 3

    def __init__(self, a, b):
        print("Initializing Instance", a, b)


a = AbstractClass(2, 3)
print(a)


class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)


#
emp_1 = Employee('John', 'Smith', 50000)
emp_2 = Employee('Kim', 'hoon', 40000)
emp_1.apply_raise()

print(emp_1)
print(emp_1.first)
print(emp_1.pay)
print(str(emp_1))
print(emp_1.__len__())
print(len(emp_1))
print(1, add(emp_1, emp_2))
print(2, emp_1.add(emp_2))
print(3, emp_1.__add__(emp_2))

print(f'Before fullname : {emp_1.fullname}')

emp_1.fullname = 'Corey Schafer'

print(f'After first    : {emp_1.first}')
print(f'After email    : {emp_1.email}')
print(f'After fullname : {emp_1.fullname}')

del emp_1.fullname

print(f'After delete first    : emp_1.first')
print(f'After delete email    : emp_1.email')
print(f'After delete fullname : emp_1.fullname')


# Inheritance1
class Developer(Employee):
    raise_amt = 1.9

    def __init__(self, prog_lang, **kwargs):
        super().__init__(**kwargs)
        self.prog_lang = prog_lang


dev_1 = Developer('Mw', 'Ko', 35000, 'Python')

print(dev_1.pay)

dev_1.apply_raise()

print(dev_1.pay)
print(dev_1)
print(dev_1.fullname)


# inheritance2
class Manager(Employee):
    raise_amt = 1.5

    def __init__(self, employees=None, **kwargs):
        super().__init__(**kwargs)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp)


#
mng_1 = Manager('Sw', 'J', 50000, ['a', 'b', 'c', 'd', 'k'])

print(mng_1)
print('These are before')
mng_1.print_emps()
mng_1.add_emp('z')
print('These are after')
mng_1.print_emps()


class Unknown(Developer, Manager):
    def __init__(self, first, last, pay, prog_lang, employees=None):
        super().__init__(first=first, last=last, pay=pay, prog_lang=prog_lang, employees=employees)
        print('I can be a manager or developer whatever I want to')


unk_1 = Unknown('Myungwoo', 'Ko', 40000, 'Python', ['a', 'b'])
print('Unknown raise_amt: ', unk_1.raise_amt)
unk_1.apply_raise()
print(unk_1.pay)
print(unk_1.prog_lang)
print('before emps: ')
unk_1.print_emps()
unk_1.add_emp('z')
print('after emps: ')
unk_1.print_emps()


# interface and **kwargs

class A(object):
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, b, **kw):
        self.b = b
        super(B, self).__init__(**kw)


class C(A):
    def __init__(self, c, **kw):
        self.c = c
        super(C, self).__init__(**kw)


class D(B, C):
    def __init__(self, a, b, c, d):
        super(D, self).__init__(a=a, b=b, c=c)
        self.d = d


d = D('ay', 'bee', 'cla', 'dra')
print(d.d)
