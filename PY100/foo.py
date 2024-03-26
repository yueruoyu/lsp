foo = ['a', 'b', 'c', 'd']
print(id(foo))

def set_foo():
    foo = ['A', 'B', 'C']
    foo.pop()
    print (foo)

set_foo()
print(foo)
print(id(foo))

