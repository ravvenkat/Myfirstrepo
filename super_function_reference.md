Super() in a nutshell
Every Python instance has a class that created it.
Every class in Python has a chain of ancestor classes.
A method using super() delegates work to the next ancestor in the chain for the instance's class.
Example
This small example covers all the interesting cases:

class A:
    def m(self):
        print('A')

class B(A):
    def m(self):
        print('B start')
        super().m()
        print('B end')
        
class C(A):
    def m(self):
        print('C start')
        super().m()
        print('C end')

class D(B, C):
    def m(self):
        print('D start')
        super().m()
        print('D end')
The exact order of calls in determined by the instance the method is called from:

>>> a = A()
>>> b = B()
>>> c = C()
>>> d = D()
For instance a, there is no super call:

>>> a.m()
A
For instance b, the ancestor chain is B -> A -> object:

>>> type(b).__mro__   
(<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

>>> b.m()
B start
A
B end
For instance c, the ancestor chain is C -> A -> object:

>>> type(c).__mro__   
(<class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

>>> b.m()
C start
A
C end
For instance d, the ancestor chain is more interesting D -> B -> C -> A -> object:

>>> type(d).__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

>>> d.m()
D start
B start
C start
A
C end
B end
D end
