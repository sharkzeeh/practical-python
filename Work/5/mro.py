'''
Python uses cooperative multiple inheritance which obeys some rules about class ordering.

1. Children are always checked before parents
2. Parents (if multiple) are always checked in the order listed
'''

class A: pass
class B:
    attr = 'B'
class C(A, B): pass
class D(B):
    attr = 'D'
class E(C, D): pass


if __name__ == '__main__':
    e = E()
    print('E bases:', E.__bases__)
    print(f'E mro:', E.__mro__)
    for cls in e.__class__.__mro__:
        if 'attr' in cls.__dict__:
            print(f'attr was found in class {cls.__name__}!')
            print('E.attr ==', E.attr)
            break
