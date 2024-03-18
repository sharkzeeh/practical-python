# Reading: 7.5 Decorated Methods

# @staticmethod is used to define a so-called static class methods
# (from C++/Java). A static method is a function that is part of the
# class, but which does not operate on instances.

# @classmethod is used to define class methods. A class method is a
# method that receives the class object as the first parameter instead
# of the instance.

class Foo:
    @staticmethod
    def foo(x):
        print('x =', x)

    def bar(self):
        print(self)

    @classmethod
    def spam(cls):
        print(cls)


if __name__ == '__main__':
    # @staticmethod
    Foo.foo(2)

    # @classmethod
    f = Foo()
    f.bar()     # instance `f` <__main__.Foo object at 0x000001E255C0ECD0>
    Foo.spam()  # class  `Foo` <class '__main__.Foo'>
