def test(x, *args):
    print(x, args)
    print(args[0])
test(1, 2, 3, 4)