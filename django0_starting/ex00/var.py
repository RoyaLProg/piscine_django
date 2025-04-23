def my_var():
    var1 = 42
    var2 = "42"
    var3 = "quanrante-deux"
    var4 = 42.0
    var5 = True
    var6 = [42]
    var7 = {42: 42}
    var8 = (42,)
    var9 = set()

    print(f'{var1} has type {type(var1)}')
    print(f'{var2} has type {type(var2)}')
    print(f'{var3} has type {type(var3)}')
    print(f'{var4} has type {type(var4)}')
    print(f'{var5} has type {type(var5)}')
    print(f'{var6} has type {type(var6)}')
    print(f'{var7} has type {type(var7)}')
    print(f'{var8} has type {type(var8)}')
    print(f'{var9} has type {type(var9)}')


if __name__ == '__main__':
    my_var()
