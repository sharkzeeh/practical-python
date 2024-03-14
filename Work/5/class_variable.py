class Foo:
     a = 13                  # Class variable
     def __init__(self, b):
         self.b = b          # Instance variable


if __name__ == '__main__':
    f = Foo(10)
    g = Foo(42)

    assert f.a == g.a

    assert f.b != g.b

    Foo.a = 42

    assert f.a == 42 and g.a == 42